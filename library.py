import os 

library_catalog={}

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear ")

def add_book():
    while True :
        clear_terminal()
        isbn=input("Enter ISBN :")
        title=input("Enter title:")
        author=input("Enter author:")

        library_catalog[isbn]={"title":title,
                               "author":author,"available":True}
        
        print(f"Book {title}by{author} added to the catalog with ISBN{isbn}")

        choice=input("Do you want to add another book? (y/n):")
        if choice.lower() != "y":
            break
        
def check_out_book():
    while True:
        clear_terminal()
        isbn=input("Enter ISBN to check out : ")
        if isbn in library_catalog:
            if library_catalog[isbn]["available"]:
                library_catalog[isbn]["available"]=False
                print(f"book '{[library_catalog][isbn]["title"]}' checked out successfully")
            else:
                print("Sorry,the book is currently checked out .")
        else:
            print("Book not found in the catalog")

        choice=input("Do you want to check out another book? (y/n)?")
        if choice.lower() != "y":
            break

def check_in_book():
    while True :

        clear_terminal()
        isbn=input("Enter ISBN to check in :")
        if isbn in library_catalog:
            if not library_catalog[isbn]["available"]:
             library_catalog[isbn]["available"]=True
             print(F"book '{library_catalog[isbn]['title']}' checked in successfully ")
            else:
             print("The book is already available")

        else:
            print("Book is not found in the catalog")

        choice=input("Do you want to check in author book?(y/n)")
        if choice.lower() !='y':
            break
    
def list_book():
    while True:

        clear_terminal()
        print("\n library Catalog")
        for isbn in library_catalog:
             book_info=library_catalog[isbn]
             print(f"ISBN: {isbn}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}")


        choice=input("Do you want to go back to the main list ?(y/n)")
        if choice.lower() =="y":
          break
      

while True:
    print("\n menu :")
    print("1.Add book ")
    print("2.check out book")
    print("3.check in book")
    print("4.List books")
    print("5.Exit")


    choice=input("Enter your choice (1-5):")

    if choice == "1":
            add_book()
    elif choice == "2":
            check_out_book()
    elif choice == "3":
            check_in_book()
    elif choice == "4":
            list_book()
    elif choice == "5":
        break
    else:
        print("Invild choice,Please enter a number between 1 and 5.")
    
