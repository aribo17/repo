"""
Webshop
"""

from flask import Flask, request, render_template, g, session, redirect, url_for, flash, abort, \
    send_from_directory
import mysql.connector
import os
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "static/images"
ALLOWED_EXTENSIONS = ["txt", "pdf", "png", "jpg", "jpeg", "gif"]

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "TechAdmin111"
app.config["DATABASE_DB"] = "otakulife"
app.config["DATABASE_HOST"] = "localhost"


#############################################
@app.route('/addnewproduct', methods=['GET','POST'])
def addnewproduct():
    db = get_db()
    cur = db.cursor()
    product_name = request.form['name']
    description = request.form['description']
    regular_price = request.form['price']
    percentage = request.form['percentage']
    product_type = request.form['type']
    if "file" not in request.files:
        flash("No file part", "warning")
    file = request.files["file"]
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == "":
        flash("No selected file", "warning")
        return redirect(url_for("newproduct"))
    if file and allowed_file(file.filename):
        # "secure" the filename (form input may be forged and filenames can be dangerous)
        filename = secure_filename(file.filename)
        # save the file to the upload folder
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    else:
        flash("Not allowed file type", "danger")
        return render_template("newproduct.html", product_name=product_name,description=description,regular_price=regular_price,percentage=percentage,product_type=product_type)#redirect(url_for("newproduct"))
    sql = "INSERT INTO produkt(produktnavn, beskrivelse, standardpris, avslag, produktbilde, type_produkt) VALUES(%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,(product_name, description, regular_price, percentage, filename, product_type))
    db.commit()
    cur.close()
    return redirect(url_for("categories"))

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)





##############################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    error = None
    try:
        db = get_db()
        cur = db.cursor()
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            cur.execute("SELECT passord, admin FROM bruker WHERE brukernavn = %s;", (username,))
            user = cur.fetchone()

            if user and sha256_crypt.verify(password, user[0]):
                # YOU LOGGED IN!
                flash('You are logged in', "success")
                session['username'] = username
                if user[1] == True:
                    flash(' welcome admin', "success")
                    session['admin'] = True
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password', "danger")
                return render_template('login.html')

    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('admin', None)
    flash("You have been successfully logged out", "success")
    return redirect(url_for('login'))




@app.route('/categories')
def categories():
    if not "admin" in session:
        flash('Unauthorized access', "danger")
        return redirect(url_for("index"))
    db = get_db()
    cur = db.cursor()
    valid = 0
    try:
        sql = "SELECT * FROM produkt WHERE deleted=%s "
        cur.execute(sql, (valid,))
        produkt = cur.fetchall()

        return render_template("categories.html", produkt=produkt)
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()


@app.route('/editproduct/<int:produktid>', methods=['GET','POST'])
def editproduct(produktid):
    if not "admin" in session:
        flash('Unauthorized access', "danger")
        return redirect(url_for("index"))

    db = get_db()
    cur = db.cursor()
    valid = 0
    sql = "SELECT * FROM produkt WHERE deleted=%s AND produktid=%s"
    cur.execute(sql, (valid, produktid))
    produkt = cur.fetchone()
    if request.method == 'POST':
        try:
            product_name = request.form['name']
            description = request.form['description']
            regular_price = request.form['price']
            percentage = request.form['percentage']
            product_type = request.form['type']
            if "file" not in request.files:
                flash("No file part", "warning")
            file = request.files["file"]
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == "":
                flash("No selected file", "warning")
                return redirect(url_for("editproduct"))
            if file and allowed_file(file.filename):
                # "secure" the filename (form input may be forged and filenames can be dangerous)
                filename = secure_filename(file.filename)
                # save the file to the upload folder
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            else:
                flash("Not allowed file type", "warning")
                return render_template("editproduct.html", produkt=produkt)
            sql = "UPDATE produkt SET produktnavn=%s, beskrivelse=%s, standardpris=%s, avslag=%s, produktbilde=%s, type_produkt=%s WHERE produktid=%s"
            cur.execute(sql, (product_name, description, regular_price, percentage, filename, product_type, produktid))
            db.commit()

            return redirect(url_for('categories'))
        except mysql.connector.Error as err:
            return render_template("error.html", msg="Error querying data")
        finally:
            cur.close()
    return render_template("editproduct.html", produkt=produkt)

@app.route('/removeproduct/<int:produktid>', methods=['GET','POST'])
def removeproduct(produktid):
    if not "admin" in session:
        flash('Unauthorized access', "danger")
        return redirect(url_for("index"))
    db = get_db()
    cur = db.cursor()
    delete = 1
    try:
        sql = "UPDATE produkt SET deleted=%s WHERE produktid=%s"
        cur.execute(sql, (delete, produktid))
        db.commit()

        return redirect(url_for("categories"))
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()



@app.route('/order')
def order():
    if not "admin" in session:
        flash('Unauthorized access', "danger")
        return redirect(url_for("index"))
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT DISTINCT bestillingid, fornavn, etternavn FROM ((bruker br JOIN bestilling bs ON br.brukernavn = bs.brukernavn) NATURAL JOIN bestillingskurv bk)JOIN produkt p ON p.produktid = bk.produktid;"
        cur.execute(sql)
        bestilling = cur.fetchall()

        return render_template("order.html", bestilling=bestilling)
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()

def get_contactinfo(order_id):
    db = get_db()
    cur = db.cursor()
    sql = "SELECT DISTINCT br.fornavn, br.etternavn, br.email, br.addresse, bs.dato FROM bruker br JOIN bestilling bs ON br.brukernavn = bs.brukernavn WHERE bestillingid=%s;"
    cur.execute(sql, (order_id,))
    contact = cur.fetchone()
    cur.close()
    return contact


@app.route('/bestilling/<int:order_id>', methods=['GET', 'POST'])
def order_info(order_id):
    if not "admin" in session:
        flash('Unauthorized access', "danger")
        return redirect(url_for("index"))
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT bestillingid, produktnavn, produktbilde, tilbudpris, kvantitet, p.produktid FROM ((bruker br JOIN bestilling bs ON br.brukernavn = bs.brukernavn) NATURAL JOIN bestillingskurv bk) JOIN produkt p ON p.produktid = bk.produktid WHERE bestillingid=%s;"
        cur.execute(sql, (order_id,))
        data = cur.fetchall()
        info = get_contactinfo(order_id)
        sumList = []
        for liste in data:
            sumList.append(liste[3] * liste[4])
        newTotalSum = sum(sumList)

        return render_template("bestilling.html", orders=data, totalsum=newTotalSum, info=info)
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()


@app.route('/customer')
def customer():
    return render_template("customer.html")


@app.route('/addcustomer', methods=['GET', 'POST'])
def addcustomer():
    db = get_db()
    cur = db.cursor()
    try:
        username = request.form['username']
        password = sha256_crypt.hash(request.form['password'])
        email = request.form['email']
        fornavn = request.form['fornavn']
        etternavn = request.form['etternavn']
        addresse = request.form['addresse']
        sql = "INSERT INTO bruker (brukernavn, passord, email, fornavn, etternavn, addresse) VALUES(%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, (username, password, email, fornavn, etternavn, addresse))
        db.commit()
        return redirect(url_for("index"))
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()


@app.route('/newproduct')
def newproduct():
    if "admin" not in session:
        flash("Unauthorized access", "danger")
        return redirect(url_for("index"))
    return render_template("newproduct.html")




@app.route('/addneworder', methods=['GET', 'POST'])
def bestillingtabell():
    db = get_db()
    cur = db.cursor()
    try:
        username = request.form['brukernavn']
        print(username)
        delivery = request.form['leveringstid']
        print(delivery)
        status = request.form['bestillingstatus']
        print(status)
        id = request.form['bestillingid']
        print(id)
        produkt = request.form['produktid']
        print(produkt)
        kvantitet = request.form['kvantitet']
        print(kvantitet)
        sql = "INSERT INTO bestilling (brukernavn, dato, leveringstid, bestillingsstatus) VALUES(%s,now(),%s,%s);"
        cur.execute(sql, (username, delivery, status,))
        sql2 = "INSERT INTO bestillingskurv (bestillingid, produktid, kvantitet) VALUES(%s,%s,%s);"
        cur.execute(sql2, (id, produkt, kvantitet,))
        db.commit()
        return redirect(url_for("index"))
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()


@app.route('/neworder', methods=['GET', 'POST'])
def neworder():
    return render_template("neworder.html")


@app.route('/user')
def user():
    if 'username' in session:
        db = get_db()
        cur = db.cursor()
        try:
            sql = "SELECT DISTINCT bestillingid, fornavn, etternavn FROM ((bruker br JOIN bestilling bs ON br.brukernavn = bs.brukernavn) NATURAL JOIN bestillingskurv bk)JOIN produkt p ON p.produktid = bk.produktid WHERE br.brukernavn=%s;"
            cur.execute(sql, (session['username'],))
            bestilling = cur.fetchall()

            return render_template("profile.html", bestilling=bestilling)
        except mysql.connector.Error as err:
            return render_template("error.html", msg="Error querying data")
        finally:
            cur.close()
    else:
        return redirect('login')





def get_bestsale():
    db = get_db()
    cur = db.cursor()
    limit = 5
    sql = "SELECT p.produktid, produktnavn, tilbudpris, SUM(kvantitet) FROM produkt AS p INNER JOIN bestillingskurv AS bk ON p.produktid=bk.produktid GROUP BY p.produktid ORDER BY SUM(kvantitet) DESC LIMIT %s;"
    cur.execute(sql,(limit,))
    result = cur.fetchall()
    cur.close()
    return result

@app.route('/dashboard')
def dashboard():
    if not "admin" in session:
        flash('Unauthorized access', "danger")
        return redirect(url_for("index"))
    db = get_db()
    cur = db.cursor()
    sql = "SELECT DATE_FORMAT(dato, '%Y-%m-%d') AS the_date, COUNT(*) AS count FROM bestilling GROUP BY the_date;"
    cur.execute(sql)
    graph_data = cur.fetchall()
    dates = []
    count = []
    for x in graph_data:
        dates.append(x[0])
        count.append(x[1])
    legend = 'Orders'
    labels = dates
    values = count
    sales_info = get_bestsale()
    cur.close()
    return render_template("dashboard.html", values=values, labels=labels, legend=legend, sales=sales_info)
########################################


def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"],
                                              database=app.config["DATABASE_DB"])
    return g._database


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


#############################################################################################



#######################################################################################
@app.route("/")
def index():
    """Index page that shows a list of products"""
    # TODO: fetch all products from database

    db = get_db()
    cur = db.cursor()
    valid = 0
    try:
        sql = "SELECT * FROM produkt WHERE deleted=%s"
        cur.execute(sql, (valid,))
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
    valid = 0
    try:
        sql = "SELECT * FROM produkt WHERE produktid=%s AND deleted=%s"
        cur.execute(sql, (product_id, valid))
        produkt = cur.fetchone()
        product_data = {
            "product_id": produkt[0],
            "product_name": produkt[1],
            "product_info": produkt[2],
            "product_price": produkt[3],
            "product_discount": produkt[4],
            "product_currentprice": produkt[5],
            "product_img": produkt[7],
            "product_type": produkt[8]
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
            sumList.append(cart_product[k]['product_discount'] * s_cart[k])
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
        flash("Product added to cart", "success")
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
            flash("Product removed cart", "info")
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
        flash("Quantity modified", "info")
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
    flash("Product added to cart", "success")
    msg = "{} piece(s) of product #{} have been added to the cart".format(request.form["qt"], product_id)
    return render_template("product.html", product=get_product(product_id), msg=msg)


@app.route("/checkout", methods=["POST"])
def checkout():
    """Checkout process"""
    action = request.form.get("action")
    if action == "do_1":
        # TODO: check order details, if all correct show confirmation form,
        # otherwise show order form again (with filled-in values remembered)
        cart_product = {}
        sumList = []
        totalsum = 0
        s_cart = session["cart"]
        for k, i in s_cart.items():
            cart_product[k] = get_product(k)
            sumList.append(cart_product[k]['product_discount'] * s_cart[k])
        newTotalSum = sum(sumList)

        return render_template("checkout_1.html")
    elif action == "do_2":
        if request.form.get("confirm") == "1":  # check if order is confirmed
            # TODO: save order in database and return order number
            db = get_db()
            cur = db.cursor()
            try:
                username = request.form['brukernavn']
                print(username)
                delivery = request.form['leveringstid']
                print(delivery)
                status = request.form['bestillingstatus']
                print(status)
                id = request.form['bestillingid']
                print(id)
                produkt = request.form['produktid']
                print(produkt)
                kvantitet = request.form['kvantitet']
                print(kvantitet)
                sql = "INSERT INTO bestilling (brukernavn, dato, leveringstid, bestillingsstatus) VALUES(%s,now(),%s,%s);"
                cur.execute(sql, (username, delivery, status,))
                sql2 = "INSERT INTO bestillingskurv (bestillingid, produktid, kvantitet) VALUES(%s,%s,%s);"
                cur.execute(sql2, (id, produkt, kvantitet,))
                db.commit()
            except mysql.connector.Error as err:
                return render_template("error.html", msg="Error querying data")
            finally:
                cur.close()

            return render_template("checkout_2.html", order_number="XXX")
        else:
            return render_template("checkout_1.html", err="You need to confirm the order.")
    else:
        # TODO: display form for order details
        return render_template("checkout_0.html")


if __name__ == "__main__":
    app.run()
