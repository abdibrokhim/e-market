import sqlite3

connection = sqlite3.connect('market.db')
cursor = connection.cursor()


class Cart:
    cart_dict = {}
    cost_dict = {}

    def __init__(self, table_name):
        self.table_name = table_name

    def add_to_cart(self,):
        item_name = str(input("INPUT ITEM NAME: ").upper())
        item_total = int(input("INPUT ITEM QUANTITY: "))

        item = cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if item_name == item[i][0] and item_total <= item[i][1]:
                self.cart_dict.update({item_name: item_total})
                self.cost_dict.update({item_name: (item_total * item[i][2])})

        self.get_cart()

    def delete_from_cart(self,):
        item_name = str(input("INPUT ITEM NAME: ")).upper()
        item_total = int(input("INPUT ITEM QUANTITY: "))

        for i in self.cart_dict:
            if item_name == i and item_total <= self.cart_dict[i]:
                self.cart_dict.update({i: (self.cart_dict[i] - item_total)})
                self.cost_dict.update({i: self.cost_dict[i] - (item_total * (self.cost_dict[i] / self.cart_dict[i]))})

        self.get_cart()

    def get_cart(self,):
        print("\nCART:", self.cart_dict, self.cost_dict)