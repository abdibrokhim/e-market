import connections


class PersonDB:
    connection = connections.PersonDB().get_connection()
    cursor = connections.PersonDB().get_cursor()

    table_name = 'PERSON'

    def create_person_database(self):
        self.cursor.execute('''CREATE TABLE {}
            (NAME CHAR(25), 
            PASSWORD VARCHAR(25), 
            TYPE CHAR(25));'''.format(self.table_name))
        print("SUCCESS")
        self.cursor.close()


class ShopDB:
    connection = connections.ShopDB().get_connection()
    cursor = connections.ShopDB().get_cursor()

    table_name = 'FOOD'

    def create_shop_database(self):
        self.cursor.execute('''CREATE TABLE {}
            (NAME CHAR(25), 
            SUPPLY INTEGER, 
            PRICE INTEGER, 
            CATEGORY CHAR(25));'''.format(self.table_name))
        print("SUCCESS")
        self.cursor.close()