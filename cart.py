import connections
import database
import shop


class Cart:
    connection = connections.ShopDB().get_connection()
    cursor = connections.ShopDB().get_cursor()

    table_name = database.ShopDB().table_name
    cart_dict = {}
    for_payment = 0
    # stock = False

    def add_to_cart(self,):
        stock = False
        item_name = str(input("\nINPUT PRODUCT NAME: ").upper())
        item_total = int(input("INPUT PRODUCT QUANTITY: "))

        item = self.cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if item_name == item[i][0] and item_total <= item[i][1]:
                self.cart_dict[item_name] = {'TOTAL': item_total, 'PRICE': (item_total * item[i][2])}
                stock = True
        if not stock:
            print("\nCURRENTLY NOT AVAILABLE\n")
            return False

    def delete_from_cart(self,):
        item_name = str(input("\nINPUT PRODUCT NAME: ")).upper()
        item_total = int(input("INPUT PRODUCT QUANTITY: "))

        if not self.cart_dict:
            print("\nYOUR CART IS EMPTY\n")
            return False
        for i in self.cart_dict:
            if item_name == i and item_total <= self.cart_dict[item_name]['TOTAL']:
                item_price = (self.cart_dict[item_name]['PRICE'] / self.cart_dict[item_name]['TOTAL'])
                self.cart_dict[item_name]['PRICE'] -= (item_total * item_price)
                self.cart_dict[item_name]['TOTAL'] -= item_total
            elif item_name != i or item_total > self.cart_dict[item_name]['TOTAL']:
                print("\nSOMETHING WENT WRONG\n")
                return False

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
            self.option()

    def option(self):
        while True:
            print("\n[1] -> CHECKOUT NOW")
            print("[2] -> CONTINUE SHOPPING\n")

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                self.checkout()
            elif choice == 2:
                return False
            else:
                print("\nINVALID")

    def checkout(self):
        print("\nCHECKOUT\n")
        for item_id, item_info in self.cart_dict.items():
            left_total = shop.Shop().get_total(item_id) - self.cart_dict[item_id]['TOTAL']
            shop.Shop().update_item(item_id, left_total)
        shop.Shop().get_table()
        print("\n\n!SUCCESS!\n\n")
        exit()