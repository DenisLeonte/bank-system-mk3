import sys

sys.path.insert(0, 'C:\\Users\\denis\\PycharmProjects\\bank-systemV3\\main\\file_manager')
from file_manager import manager

sys.path.insert(0, 'C:\\Users\\denis\\PycharmProjects\\bank-systemV3\\main\\user')
from user import user

sys.path.insert(0, 'C:\\Users\\denis\\PycharmProjects\\bank-systemV3\\main\\transaction')
from transaction import transaction


class test:
    x = manager.user_file()

    def begin_test(self):
        print("Test 1 passed")
        self.x.set_path("database//database.txt")
        print("Test 2 passed")
        if self.x.check_file_integrity():
            print("Test 3 passed")
            print("Currently there are " + str(self.x.find_registered_users()) + " registered users")
            print("Test 4 passed")
            return True
        else:
            print("Problem with the database file")
            return False
