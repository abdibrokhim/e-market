import connections


class Cart:
    connection = connections.ShopDB().get_connection()
    cursor = connections.ShopDB().get_cursor()

    table_name = 'FOOD'
    cart_dict = {}
    for_payment = 0

    def add_to_cart(self,):
        item_name = str(input("INPUT ITEM NAME: ").upper())
        item_total = int(input("INPUT ITEM QUANTITY: "))

        item = self.cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if item_name == item[i][0] and item_total <= item[i][1]:
                self.cart_dict[item_name] = {'TOTAL': item_total, 'PRICE': (item_total * item[i][2])}
                # left_item = item[i][1] - item_total
                # shop.Shop().update_item(item_name, left_item)

    def delete_from_cart(self,):
        item_name = str(input("INPUT ITEM NAME: ")).upper()
        item_total = int(input("INPUT ITEM QUANTITY: "))

        for i in self.cart_dict:
            if item_name == i and item_total <= self.cart_dict[item_name]['TOTAL']:
                item_price = (self.cart_dict[item_name]['PRICE'] / self.cart_dict[item_name]['TOTAL'])
                self.cart_dict[item_name]['PRICE'] -= (item_total * item_price)
                self.cart_dict[item_name]['TOTAL'] -= item_total

    def get_cart(self,):
        print("\nCART\n")
        if not self.cart_dict:
            print("YOUR CART IS EMPTY")
        else:
            for item_id, item_info in self.cart_dict.items():
                print("\nNAME:", item_id)
                for val in item_info:
                    if val == 'PRICE':
                        print(val + ':', '$' + str(item_info[val]))
                        self.for_payment += item_info[val]
                    else:
                        print(val + ':', item_info[val])

        print("\nFOR PAYMENT:", '$' + str(self.for_payment))