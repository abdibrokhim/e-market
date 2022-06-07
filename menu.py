from admin import Admin
from customer import Customer


class Menu:
    def main_menu(self):
        admin = Admin()
        customer = Customer()
        while True:
            print('\nCONTINUE AS ...\n')
            print('[1] -> ADMIN')
            print('[2] -> CUSTOMER')
            print('\n[0] -> EXIT\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                admin.main_menu()
            elif choice == 2:
                customer.main_menu()
            elif choice == 0:
                exit()
            else:
                print("\nINVALID")