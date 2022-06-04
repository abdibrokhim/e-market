import sqlite3

connection = sqlite3.connect('market.db')
cursor = connection.cursor()


class Cart:
    cart = []
    total = {}
    cost = 0

    def __init__(self, table_name):
        self.table_name = table_name

    def add_to_cart(self, item_name, item_total, price=0):
        # print("\n:: IN STOCK ::")
        # item_name = str(input("Input: "))
        # item_total = int(input("Input: "))

        item = cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if item_name == item[i][0]:
                self.cart.append(item_name)
                self.total[item_name] = item_total
                price += item_total * item[i][2]
                self.cost += price
        print("ALL INFO\n", self.cart, self.total, self.cost)

    def get_cart(self,):
        print("CART\n", self.cart, self.cost)

    def delete_from_cart(self):
        pass
