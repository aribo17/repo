

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9 , 12, 34, 1)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers = (1,3,4,5)
player_two = LotteryPlayer("John")
# print(player_one.numbers == player_two.numbers)
#



class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # @classmethod
    # def go_to_school(cls):
    #     print("I'm going to school. ")
    #     print("I'm a {}".format(cls))

    @staticmethod
    def go_to_school():
        print("I'm going to school. ")

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
Student.go_to_school()
class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        return self.items.append({'name':name, 'price':price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item['price'] for item in self.items])


     @classmethod
     def franchise(cls, store):
         # Return another store, with the same name as the argument's name, plus " - franchise"
         return cls(store.name + ' - franchise')

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price))
