# from cart import Cart
from market import Market


def main():
    item_1 = Market('FOOD', 'RED BULL', 100, 1.99)
    item_2 = Market('FOOD', 'MONSTER', 100, 1.49)
    item_3 = Market('FOOD', 'BANG', 100, 2.29)
    item_4 = Market('FOOD', 'ROCKSTAR', 100, 1.79)

    # item_1.add_item()
    # item_2.add_item()
    # item_3.add_item()
    # item_4.add_item()

    item_1.get_item()
    # item_4.delete_item()
    # item_1.get_item()



    # c = 0
    # while True:
    #     if c < 1:
    #         print("\nWELCOME")
    #     print("\n:: CHOOSE AN OPTION ::\n")
    #     print("[1] -> GO TO SHOPPING")
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
    #         cart.buy()
    #         c += 1
    #     elif choice == 2:
    #         exit()
    #     else:
    #         print("\nINVALID")
    #         c += 1

    print("\nSUCCESS\n")


if __name__ == '__main__':
    main()