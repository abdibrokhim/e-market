import sqlite3

connection = sqlite3.connect('market.db')
cursor = connection.cursor()


class Cart:
    cart = []
    total = []
    cost = []

    def __init__(self, table_name):
        self.table_name = table_name

    def add_to_cart(self, item_name, item_total):
        # print("\n:: IN STOCK ::")
        # item_name = str(input("Input: "))
        # item_total = int(input("Input: "))

        item = cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if item_name == item[i][0]:
                self.cart.append(item_name)
                self.total.append(item_total)
                self.cost.append(item_total * item[i][2])
        print("ALL INFO\n", self.cart, self.total, self.cost)

    def get_cart(self,):
        print("\nCART\n", self.cart, self.total, self.cost)

    def delete_from_cart(self, item_name, item_total):
        item = cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for i in self.cart:
            if item_name == i:
                # self.cart.remove(item_name)
                self.total.insert(i, self.total[i] - item_total)
                if self.total.insert(i, self.total[i] - item_total) == 0:
                    self.cart.remove(item_name)
                self.cost.insert(i, self.cost[i] - item_total * item[2])
        print("ALL INFO\n", self.cart, self.total, self.cost)
