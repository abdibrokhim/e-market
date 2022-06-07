import menu
# import database
# import database


def main():
    #------- UNCOMMENT CODE ABOVE/BELOW FOR THE FIRST TIME -------#
    #------- IT WILL CREATE TWO DATABASES -------#
    #------- ONE FOR [IN STOCK PRODUCTS], OTHER ONE FOR [USERS] -------#
    # database.PersonDB().create_person_database()
    # database.ShopDB().create_shop_database()

    menu.Menu().main_menu()

    print("\n\n!SUCCESS!\n\n")


if __name__ == '__main__':
    main()