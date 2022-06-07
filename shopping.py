import shop
import cart


class Shopping:
    def main_menu(self):
        while True:
            print('\n[1] -> SHOP')
            print('[0] -> EXIT\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                shop.Shop().get_table()
                self.secondary_menu()
            elif choice == 0:
                exit()
            else:
                print("\nINVALID")

    def secondary_menu(self):
        while True:
            print('\n[1] -> ADD TO CART')
            print('[2] -> DELETE FROM CART')
            print('[3] -> VIEW CART')
            print('\n[0] -> BACK\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                cart.Cart().add_to_cart()
            elif choice == 2:
                cart.Cart().delete_from_cart()
            elif choice == 3:
                cart.Cart().get_cart()
            elif choice == 0:
                return False
            else:
                print("\nINVALID")

    def shopping(self):
        pass