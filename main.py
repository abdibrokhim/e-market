from cart import Cart
from shop import Shop


def main():
    shop = Shop('FOOD')

    shopper = Cart('FOOD')

    shop.get_table()
    # shop.add_item()
    # shop.get_table()

    # shopper.add_to_cart()
    # shopper.add_to_cart()
    # print('\nTOTAL:', sum(shopper.cart_dict.values()))
    # print('FOR PAYMEMT:', sum(shopper.cost_dict.values()))

    # shopper.delete_from_cart()
    # print('\nTOTAL:', sum(shopper.cart_dict.values()))
    # print('FOR PAYMEMT:', sum(shopper.cost_dict.values()))


    print("\nSUCCESS\n")


if __name__ == '__main__':
    main()
