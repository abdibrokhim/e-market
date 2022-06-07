import sqlite3

from shop import Shop

connection = sqlite3.connect('market.db')
cursor = connection.cursor()


class Cart:
    table_name = 'FOOD'
    shop = Shop()
    cart_dict = {}
    order_dict = {}

    def add_to_cart(self,):
        item_name = str(input("INPUT ITEM NAME: ").upper())
        item_total = int(input("INPUT ITEM QUANTITY: "))

        item = cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if item_name == item[i][0] and item_total <= item[i][1]:
                self.cart_dict[item_name] = {'TOTAL': item_total, 'PRICE': (item_total * item[i][2])}
                # left_item = item[i][1] - item_total
                # Shop.update_item(item_name, left_item)

    def delete_from_cart(self,):
        item_name = str(input("INPUT ITEM NAME: ")).upper()
        item_total = int(input("INPUT ITEM QUANTITY: "))

        for i in self.cart_dict:
            if item_name == i and item_total <= self.cart_dict[item_name]['TOTAL']:
                item_price = (self.cart_dict[item_name]['PRICE'] / self.cart_dict[item_name]['TOTAL'])
                self.cart_dict[item_name]['PRICE'] -= (item_total * item_price)
                self.cart_dict[item_name]['TOTAL'] -= item_total

    def get_cart(self,):
        print("\nCART")
        for item_id, item_info in self.cart_dict.items():
            print("\nNAME:", item_id)
            for val in item_info:
                print(val + ':', item_info[val])