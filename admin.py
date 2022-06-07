import connection
import shopping


class Admin:
    connection = connection.PersonDB().get_connection()
    cursor = connection.PersonDB().get_cursor()

    table_name = 'PERSON'

    def main_menu(self):
        while True:
            print('\nCONTINUE ...\n')
            print('[1] -> SIGN IN')
            print('[2] -> SIGN UP')
            print('\n[0] -> BACK\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                self.sign_in()
            elif choice == 2:
                self.sign_up()
            elif choice == 0:
                return False
            else:
                print("\nINVALID")

    def sign_in(self):
        person_name = str(input("INPUT YOUR NAME: ").upper())
        person_password = int(input("INPUT YOUR PASSWORD: "))
        person_type = 'ADMIN'

        item = self.cursor.execute("SELECT NAME, PASSWORD, TYPE FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if person_name == item[i][0] and person_password == item[i][1] and person_type == item[i][2]:
                shopping.Shopping().main_menu()

    def sign_up(self):
        person_name = str(input("INPUT YOUR NAME: ").upper())
        person_password = str(input("INPUT YOUR PASSWORD: "))
        person_type = 'ADMIN'

        self.connection.execute("INSERT INTO {} VALUES (?, ?, ?)".format(self.table_name),
                                (person_name, person_password, person_type))
        self.connection.commit()