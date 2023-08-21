# V 0major.*minor.*patch    -------> Beta version
# V 1.0.0 (23,5)
# V 2.0.0 (25,5)
#V 2.1.0  (28,5)
import books_operation as bop

# -----------Main-----------
books = []
while True:
    print("=============================================================")
    print("press A to add a book")
    print("press L to list all books")
    print("press F to find a book")
    print("press D to deleta a book")
    print("press Q to quit the APP")
    print("=============================================================")
    choice = input("enter here:").upper()

    if   choice == 'A':
        bop.add_book()
    elif choice == 'L' :
        bop.list_book()
    elif choice == 'F':
        print("------------------------------------------------------------")
        print("press A to find by auther")
        print("press T to find by title")
        print("press I to find by ISBN")
        print("------------------------------------------------------------")
        find = input("Find book by:").upper()
        if find== 'I':
            bop.find_book()
        elif find=='A':
            bop.find_by_auther()
        elif find== 'T':
            bop.find_by_title()
        else:
            continue
    elif choice == 'D' :
        bop.delete_book()
    elif choice == 'Q' :
        break
    else :
        print ("print one of the letter from above functions ")


