"""
Assignment 7: Webshop
"""

from flask import Flask, request, render_template, g, session, redirect, url_for, flash, abort
import mysql.connector
import os




app = Flask(__name__)
app.secret_key = os.urandom(24)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "TechAdmin111"
app.config["DATABASE_DB"] = "otakulife"
app.config["DATABASE_HOST"] = "localhost"
###############################################
#tester ut sqlalchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:TechAdmin111@localhost/otakulife'
# from models import dbAlc
# dbAlc.init_app(app)
#
# @app.route('/testdb')
# def testdb():
#     if dbAlc.session.query("1").from_statement("SELECT 1").all():
#         print('It works.')
#     else:
#         print('Something is broken.')
#
#
#


########################################


def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"], password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
    return g._database


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
#############################################################################################
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    if username is not None and email is not None and password is not None:
        pass
    else:
        return "Please fill all the fields"


#######################################################################################
@app.route("/")
def index():
    """Index page that shows a list of products"""
    # TODO: fetch all products from database
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM produkt"
        cur.execute(sql)
        produkter = cur.fetchall()
        return render_template("index.html", produkter=produkter)
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()

def get_product(product_id):
    """Loads a product from the database."""
    # TODO: look up product from database
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM produkt WHERE produktid=%s"
        cur.execute(sql, (product_id,))
        produkt = cur.fetchone()
        product_data = {
            "product_id":produkt[0],
            "product_name":produkt[1],
            "product_info":produkt[2],
            "product_price":produkt[3],
            "product_discount":produkt[4],
            "product_prosent":produkt[5],
            "product_img":produkt[6]
        }
        return product_data
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
            cur.close()



@app.route("/product/<int:product_id>", methods=['get', 'post'])
def product(product_id):
    """Product page"""

    return render_template("product.html", product=get_product(product_id))


@app.route("/cart")
def cart():
    """Shopping cart."""
    # TODO: fetch the contents of the cart from session
    cart_product = {}
    sumList = []
    totalsum = 0
    if "cart" not in session:
        return render_template("cart.html", productInCart=cart_product, totalsum=totalsum)
    else:
        s_cart = session["cart"]
        for k, i in s_cart.items():
            cart_product[k] = get_product(k)
            sumList.append(cart_product[k]['product_discount']*s_cart[k])
        newTotalSum = sum(sumList)
        return render_template("cart.html", qtIncart=s_cart, productInCart=cart_product, totalsum=newTotalSum)


class ShoppingCart:
    """Class representing a shopping cart."""

    def __init__(self, contents=dict()):
        """Initializes a shopping cart with content (if provided)."""
        self.__cart = contents

    def add(self, product_id, qt):
        """Adds a product to the shopping cart or increases its quantity if it's already there."""
        self.__cart[product_id] = self.__cart.get(product_id, 0) + qt

    def set(self, product_id, qt):
        """Sets a product quantity."""
        self.__cart[product_id] = qt

    def remove(self, product_id):
        """Removes a product from the shopping cart."""
        self.__cart.pop(product_id)

    def contains(self, product_id):
        """Checks if the cart contains a given product."""
        return product_id in self.__cart

    def contents(self):
        """Returns the contents of the cart as a dict."""
        return self.__cart



@app.route("/add", methods=["POST"])
def add():
    product_id = request.form.get("product_id", None)
    qt = int(request.form.get("qt", 0))

    if product_id and qt:
        cart = ShoppingCart(session.get("cart", dict()))
        cart.add(product_id, qt)
        session["cart"] = cart.contents()
        flash("Product added to cart")
    else:
        abort(400)

    return redirect(url_for("index"))


@app.route("/remove", methods=["GET"])
def remove():
    product_id = request.args.get("product_id", None)
    if product_id:
        cart = ShoppingCart(session.get("cart", dict()))
        if cart.contains(product_id):
            cart.remove(product_id)
            session["cart"] = cart.contents()
            flash("Product removed cart")
        else:  # trying to remove a product which is not in the cart
            abort(400)
    else:
        abort(400)
    return redirect(url_for("cart"))


@app.route("/mod", methods=["POST"])
def mod():
    product_id = request.form.get("product_id", None)
    qt = int(request.form.get("qt", 0))

    if product_id and qt:
        cart = ShoppingCart(session.get("cart", dict()))
        cart.set(product_id, qt)
        session["cart"] = cart.contents()
        flash("Quantity modified")
    else:
        abort(400)

    return redirect(url_for("cart"))


@app.errorhandler(400)
def bad_request(error):
    return render_template("400.html"), 400



@app.route("/addtocart", methods=["POST"])
def add_to_cart():
    """Add a given product to cart."""
    product_id = request.form["product_id"]
    # TODO: add product to cart
    add()
    flash("Product added to cart")
    msg = "{} piece(s) of product #{} have been added to the cart".format(request.form["qt"], product_id)
    return render_template("product.html", product=get_product(product_id), msg=msg)


@app.route("/checkout", methods=["POST"])
def checkout():
    """Checkout process"""
    action = request.form.get("action")
    if action == "do_1":
        # TODO: check order details, if all correct show confirmation form,
        # otherwise show order form again (with filled-in values remembered)

        return render_template("checkout_1.html")
    elif action == "do_2":
        if request.form.get("confirm") == "1":  # check if order is confirmed
            # TODO: save order in database and return order number
            return render_template("checkout_2.html", order_number="XXX")
        else:
            return render_template("checkout_1.html", err="You need to confirm the order.")
    else:
        # TODO: display form for order details
        return render_template("checkout_0.html")




if __name__ == "__main__":
    app.run()




