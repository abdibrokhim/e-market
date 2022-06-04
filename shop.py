import sqlite3

connection = sqlite3.connect('market.db')
cursor = connection.cursor()


class Shop:
    def __init__(self, table_name, item_name, supply_number, item_price, item_category):
        self.table_name = table_name
        self.item_name = item_name
        self.supply_number = supply_number
        self.item_price = item_price
        self.item_category = item_category

    def new_table(self, table_name):
        cursor.execute("CREATE TABLE ? (NAME TEXT, SUPPLY INTEGER, PRICE INTEGER, CATEGORY TEXT)", (table_name,))
        connection.commit()

    def add_item(self, ):
        connection.execute("INSERT INTO {} VALUES (?, ?, ?, ?)".format(self.table_name),
                           (self.item_name, self.supply_number, self.item_price, self.item_category))
        connection.commit()

    def delete_item(self, ):
        connection.execute("DELETE FROM {} WHERE NAME = ?".format(self.table_name), (self.item_name,))
        connection.commit()

    # @staticmethod
    def get_item(self, ):
        items = cursor.execute("SELECT NAME FROM {}".format(self.table_name)).fetchall()
        for item in range(0, len(items)):
            print('[' + str(item + 1) + '] ', items[item][0])

    def get_table(self):
        items = cursor.execute("SELECT NAME, SUPPLY, PRICE, CATEGORY FROM {}".format(self.table_name)).fetchall()
        for item in items:
            print(item, end='\n')
