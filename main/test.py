from file_manager import manager
from user import user
from transaction import transaction


def begin_test():
    x = manager.user_file()
    print("Test 1 passed")
    x.set_path("test10.txt")
    print("Test 2 passed")
    if x.check_file_integrity() :
        print("Test 3 passed")
        print("Currently there are " + str(x.find_registered_users()) + " registered users")
        print("Test 4 passed")
        us = x.find_user("Denis")
        print("Test 5 passed")
        z = manager.transaction_file()
        print("Test 6 passed")
        z.set_path(us)
        print("Test 7 passed")
        #z.init()

        tr = transaction()
        print("Test 8 passed")
        tr.set_sender("Denis")
        tr.set_destinatary("Denis")
        tr.set_ammount(700)
        z.add_transaction(tr)
        print("Test 9 passed")
    else:
        print("Problem with the database file")



begin_test()