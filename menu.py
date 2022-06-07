from shop import Shop
from cart import Cart


class Menu:
    def menu(self):
        shop = Shop()
        while True:
            print('\nBUY FOR HAPPINESS!\n')
            print('[1] -> SHOP')
            print('[0] -> EXIT\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                shop.get_item()
                self.shopping()
            elif choice == 0:
                exit()
            else:
                print("\nINVALID")

    def shopping(self):
        cart = Cart()
        while True:
            print('\nBUY FOR HAPPINESS!\n')
            print('[1] -> ADD TO CART')
            print('[2] -> DELETE FROM CART')
            print('[3] -> VIEW CART')
            print('[0] -> BACK\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                cart.add_to_cart()
            elif choice == 2:
                cart.delete_from_cart()
            if choice == 3:
                cart.get_cart()
            elif choice == 0:
                return False
            else:
                print("\nINVALID")