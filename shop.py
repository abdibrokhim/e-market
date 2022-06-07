import connection


class Shop:
    connection = connection.ShopDB().get_connection()
    cursor = connection.ShopDB().get_cursor()

    table_name = 'FOOD'

    def add_item(self, ):
        item_name = str(input("INPUT ITEM NAME: ").upper())
        supply_number = int(input("INPUT ITEM QUANTITY: "))
        item_price = float(input("INPUT ITEM PRICE: "))
        item_category = str(input("INPUT ITEM CATEGORY: ").upper())

        self.connection.execute("INSERT INTO {} VALUES (?, ?, ?, ?)".format(self.table_name),
                           (item_name, supply_number, item_price, item_category))
        self.connection.commit()

    def delete_item(self, item_name):
        self.connection.execute("DELETE FROM {} WHERE NAME = ?".format(self.table_name), (item_name,))
        self.connection.commit()

    def update_item(self, item_name, item_total):
        self.connection.execute("UPDATE {} SET SUPPLY = ? WHERE NAME = ?".format(self.table_name), (item_total, item_name,))
        self.connection.commit()

    def get_item(self, ):
        items = self.cursor.execute("SELECT NAME FROM {}".format(self.table_name)).fetchall()
        print("\nAVAILABLE IN STOCKN\n")
        for i in range(0, len(items)):
            print(str(i + 1) + ':', items[i][0])

    def get_table(self, ):
        items = self.cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for item in items:
            print(item, end='\n')
