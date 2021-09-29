from main.file_manager import manager
from main.user import user

def begin_test():
    x = manager.user_file()
    print("Test 1 passed")
    x.__set_path("test.txt")
    print("Test 2 passed")
    x.__init()
    print("Test 3 passed")

    z = user()
    print("Test 4 passed")
    z.__set_name("Denis")
    print("Test 5 passed")
    z.set_password("asd")
    print("Test 6 passed")
    z.__encrypt_password()
    print("Test 7 passed")

    x.__add_user(z)
    print("Test 8 passed")
    x.__check_file_integrity()
    print("Test 9 passed")

