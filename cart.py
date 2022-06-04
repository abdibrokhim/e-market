import sqlite3
connection = sqlite3.connect('market.db')
cursor = connection.cursor()


class Cart:
    cart = []
    total = 0
    cost = 0

    def __init__(self, table_name, item_name):
        self.table_name = table_name
        self.item_name = item_name

    def add_to_cart(self, cart, total, cost):
        item = cursor.execute("SELECT NAME, SUPPLY, PRICE FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if self.item_name == item[i][0]:
                cart.append(self.item_name)
                total += 1
                cost += total * item[i][3]
        print(cart, total, cost)

    def delete_from_cart(self):
        pass
