import sqlite3

connection = sqlite3.connect('market.db')
cursor = connection.cursor()


class Market:
    def __init__(self, table_name, item_name, supply_number, item_price):
        self.table_name = table_name
        self.item_name = item_name
        self.supply_number = supply_number
        self.item_price = item_price

    def new_table(self, ):
        cursor.execute("CREATE TABLE ? (NAME TEXT, SUPPLY INTEGER, PRICE INTEGER)", (self.table_name,))
        connection.commit()

    def add_item(self,):
        connection.execute("INSERT INTO {} VALUES (?, ?, ?)".format(self.table_name),
                           (self.item_name, self.supply_number, self.item_price,))
        connection.commit()

    def delete_item(self,):
        connection.execute("DELETE FROM {} WHERE NAME = ?".format(self.table_name), (self.item_name,))
        connection.commit()

    # @staticmethod
    def get_item(self, ):
        item = cursor.execute("SELECT NAME, SUPPLY, PRICE FROM {}".format(self.table_name)).fetchall()
        print(item)
