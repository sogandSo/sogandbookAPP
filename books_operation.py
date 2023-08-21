books=[]
def add_book():
    global books             #optional code
    book = {}
    book["title"] = input("Enter title of the book:")
    book["auther"] = input("Enter auther of the book:")
    book["pages"] = int(input("Enter number of book pages:"))
    book["price"] = float(input("Enter price of the book:"))
    book["ISBN"] = input("Enter ISBN of the book:")
    books.append(book)

def list_book():
    for book in books :
        print("--------------------------------------------------------------")
        print(f"Title of book :{ book['title']}")
        print(f"Auther of book:{book['auther']}")
        print(f"Pages of book: {book['pages']}")
        print(f"Price of book: {book['price']}")
        print(f"ISBN of the book: {book['ISBN']}")
        print("--------------------------------------------------------------")

def find_book():
    isbn = input("Enter ISBN to find book: ")
    for book in books:
        if book['ISBN'] == isbn :
          print("--------------------------------------------------------------")
          print(f"Title of book :{ book['title']}")
          print(f"Auther of book:{book['auther']}")
          print(f"Pages of book: {book['pages']}")
          print(f"Price of book: {book['price']}")
          print(f"ISBN of the book: {book['ISBN']}")
          print("------------------------------------------------------------")
          break   #Return True
    else :
        print("--------------------------------------------------------------")
        print("This book IS NOT in books database!")
        print("--------------------------------------------------------------")


def find_by_auther():
    auther= input("Enter auther to find book: ")
    for book in books:
        if book['auther']==auther:
          print("--------------------------------------------------------------")
          print(f"Title of book :{ book['title']}")
          print(f"Auther of book:{book['auther']}")
          print(f"Pages of book: {book['pages']}")
          print(f"Price of book: {book['price']}")
          print(f"ISBN of the book: {book['ISBN']}")
          print("------------------------------------------------------------")
          break   #Return True
    else :
        print("--------------------------------------------------------------")
        print("This book IS NOT in books database!")
        print("--------------------------------------------------------------")

def find_by_title():
    title = input("Enter title to find book: ")
    for book in books:
        if book['title']==title:
          print("--------------------------------------------------------------")
          print(f"Title of book :{ book['title']}")
          print(f"Auther of book:{book['auther']}")
          print(f"Pages of book: {book['pages']}")
          print(f"Price of book: {book['price']}")
          print(f"ISBN of the book: {book['ISBN']}")
          print("------------------------------------------------------------")
          break   #Return True
    else :
        print("--------------------------------------------------------------")
        print("This book IS NOT in books database!")
        print("--------------------------------------------------------------")


def delete_book():
    isbn= input("Enter ISBN to delete book :")
    for book in books:
        if book["ISBN"] == isbn :
            books.remove(book)
            print("--------------------------------------------------------------")
            print("the book has been delete successfully ! ")
            print("--------------------------------------------------------------")
            break
    else:
        print("--------------------------------------------------------------")
        print("This book IS NOT in books database!")
        print("--------------------------------------------------------------")

  