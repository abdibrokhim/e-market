import connections
import database


class Shop:
    connection = connections.ShopDB().get_connection()
    cursor = connections.ShopDB().get_cursor()

    table_name = database.ShopDB().table_name

    def add_item(self, ):
        item_name = str(input("INPUT PRODUCT NAME: ").upper())
        supply_number = int(input("INPUT PRODUCT QUANTITY: "))
        item_price = float(input("INPUT PRODUCT PRICE: "))
        item_category = str(input("INPUT PRODUCT CATEGORY: ").upper())

        self.connection.execute("INSERT INTO {} VALUES (?, ?, ?, ?)".format(self.table_name),
                           (item_name, supply_number, item_price, item_category))
        self.connection.commit()

    def delete_item(self, item_name):
        self.connection.execute("DELETE FROM {} WHERE NAME = ?".format(self.table_name), (item_name))
        self.connection.commit()

    def update_item(self, item_name, item_total):
        self.connection.execute("UPDATE {} SET SUPPLY = ? WHERE NAME = ?".format(self.table_name), (item_total, item_name))
        self.connection.commit()

    def get_item(self, ):
        item_name = str(input("INPUT PRODUCT NAME: ").upper())
        items = self.cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {} WHERE NAME = ?".format(self.table_name), (item_name)).fetchall()
        print("\nPRODUCT INFO\n")
        print("{:18} {:8} {:10} {:10}".format('NAME', 'LEFT', 'PRICE', 'CATEGORY'))
        print(52 * str("-"))
        for i in range(0, len(items[0])):
            if i == 3:
                print("      {:10}".format(items[0][i]), end='')
            else:
                print("{:10} ".format(items[0][i]), end='')

    def get_table(self, ):
        items = self.cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        print("\nAVAILABLE IN STOCK\n")
        print("{:20} {:15} {:10} {:20}".format('NAME', 'LEFT', 'PRICE', 'CATEGORY'))
        print(61 * str("-"))
        for i in range(0, len(items)):
            print('{:20} {:4} {:16}      {:20}'.format(items[i][0], items[i][1], items[i][2], items[i][3]))