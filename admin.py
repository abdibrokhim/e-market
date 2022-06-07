from datetime import date
import connections
# import shopping


class Admin:
    connection = connections.PersonDB().get_connection()
    cursor = connections.PersonDB().get_cursor()

    table_name = 'PERSON'
    end = False

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
        person_password = str(input("INPUT YOUR PASSWORD: "))
        person_type = 'ADMIN'

        item = self.cursor.execute("SELECT NAME, PASSWORD, TYPE FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if person_name == item[i][0] and person_password == item[i][1] and person_type == item[i][2]:
                self.end = True
                self.get_person()
                break
            elif (person_name == item[i][0] or person_password == item[i][1]) and person_type == item[i][2]:
                print("\nWRONG ADMIN NAME OR PASSWORD\n")
                self.main_menu()
                break
        if not self.end:
            print("\nSIGN UP FIRSTLY\n")
            self.main_menu()

    def sign_up(self):
        admin = self.valid_admin()
        if admin:
            print("\nWELCOME!")
            person_name = str(input("\nINPUT YOUR NAME: ").upper())
            person_password = str(input("INPUT YOUR PASSWORD: "))
            person_type = 'ADMIN'

            self.connection.execute("INSERT INTO {} VALUES (?, ?, ?)".format(self.table_name),
                                    (person_name, person_password, person_type))
            self.connection.commit()

            print("\nNOW YOU CAN SIGN IN\n")
            self.main_menu()
        else:
            print("\nWRONG\n")
            self.main_menu()

    def valid_admin(self):
        secret_phrase = str(input("INPUT SECRET PHRASE TO SIGN UP AS ADMIN: "))
        if secret_phrase == str(date.today()):
            return True
        else:
            return False

    def get_person(self, ):
        items = self.cursor.execute("SELECT NAME, PASSWORD, TYPE FROM {}".format(self.table_name)).fetchall()
        print("\nPERSON\n")
        print("{:20} {:25}  {:20}".format('NAME', 'PASSWORD', 'TYPE'))
        print(56 * str("-"))
        for i in range(0, len(items)):
            print("{:20} {:25.25}  {:20}".format(items[i][0], items[i][1], items[i][2]))