from cart import Cart
from shop import Shop


def main():
    item_1 = Shop('FOOD', 'RED BULL', 10, 1.99, 'ENERGY DRINKS')
    item_2 = Shop('FOOD', 'MONSTER', 10, 1.49, 'ENERGY DRINKS')
    item_3 = Shop('FOOD', 'BANG', 10, 2.29, 'ENERGY DRINKS')
    item_4 = Shop('FOOD', 'ROCKSTAR', 10, 1.79, 'ENERGY DRINKS')

    shop1 = Cart('FOOD')
    shop2 = Cart('FOOD')
    shop3 = Cart('FOOD')

    shop1.add_to_cart('MONSTER', 2)
    shop2.add_to_cart('RED BULL', 2)
    shop3.add_to_cart('RED BULL', 2)

    shop1.get_cart()
    shop2.get_cart()
    shop3.get_cart()

    # item_5.new_table('DRINK')

    # item_1.add_item()
    # item_2.add_item()
    # item_3.add_item()
    # item_4.add_item()

    # item_1.get_item()
    # item_1.get_table()

    # c = 0
    # while True:
    #     # shop = Market()
    #     if c < 1:
    #         print("\nWELCOME")
    #     print("\n:: CHOOSE AN OPTION ::\n")
    #     print("[1] -> SHOP")
    #     print("[2] -> EXIT\n")
    #
    #     choice = input("[?] -> ")
    #
    #     try:
    #         choice = int(choice)
    #     except ValueError:
    #         print("\nINVALID")
    #         continue
    #
    #     if choice == 1:
    #         item_1.get_item()
    #         c += 1
    #         return False
    #     elif choice == 2:
    #         exit()
    #     else:
    #         print("\nINVALID")
    #         c += 1

    print("\nSUCCESS\n")


if __name__ == '__main__':
    main()
