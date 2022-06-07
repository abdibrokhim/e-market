import shop


class Stock:
    def main_menu(self):
        while True:
            print('\n[1] -> ADD NEW PRODUCT TO DATABASE')
            print('[2] -> DELETE PRODUCT FROM DATABASE')
            print('[3] -> UPDATE PRODUCT DETAILS')
            print('[4] -> VIEW ALL AVAILABLE PRODUCTS')
            print('\n[0] -> EXIT\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                shop.Shop().add_item()
            elif choice == 2:
                item_name = str(input("\nINPUT PRODUCT NAME: "))
                shop.Shop().delete_item(item_name)
            elif choice == 3:
                item_name = str(input("\nINPUT PRODUCT NAME: ").upper())
                supply_number = int(input("INPUT PRODUCT QUANTITY: "))
                shop.Shop().update_item(item_name, supply_number)
            elif choice == 4:
                shop.Shop().get_table()
            elif choice == 0:
                exit()
            else:
                print("\nINVALID")