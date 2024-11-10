#   PYTHON CONSOLE BASED LIBRARY MANAGEMENT SYSTEM   #

#   Importing Library
import os
# import datetime

#   Variable Defining

##      Book Collection
# book_title
# author
# isbn
# status = ["Borrowed", "Available"]
book = [["book_id", "title", "author", "isbn", "status"], ["a001", "Atomic Habbit", "James Clear", "1847941834", 0], ["a002", "Rivals", "Jilly Cooper", "0593013689", 1] ]

##      Users
# user_id
# username
# borrowed_book
# book_id


#   Function Defining
def clear():
    os.system('cls')

def press():
    input("Press any key to continue..")
    os.system('cls')


def book_status(book_status_selected):
    if(book[book_status_selected][4] == 0):
        print("Sorry, this book is not available at the moment. Please choose another book.")
        press()
        main()
    elif(book[book_status_selected][4] == 1):
        print("This book is available to borrow. Do you want to borrow this book?")
        borrow = input("Yes/No : ")
        if(borrow == "n" or borrow == "N" or borrow == "no" or borrow == "No" or borrow == "NO"):
            clear()
            main()
        elif(borrow == "y" or borrow == "Y" or borrow == "yes" or borrow == "Yes" or borrow == "YES"):
            book[book_status_selected][4] == 0
            print("Book has been borrowed")
            press()
            main()
        else:
            print("Please enter a valid input")
            press()
            book_detail(book_status_selected)
        
def book_detail(book_selected):
    if(book_selected):
        print("Title : " + book[book_selected][1])
        print("Author : " + book[book_selected][2])
        print("ISBN : " + book[book_selected][3])
        if(book[book_selected][4] == 0):
            print("Status : Borrowed")
        elif(book[book_selected][4] == 1):
            print("Status : Available")

    print("Do you want to borrow this book?")
    borrow = str(input("Yes/No : "))
    if(borrow == "n" or borrow == "N" or borrow == "no" or borrow == "No" or borrow == "NO"):
        clear()
        main()
    elif(borrow == "y" or borrow == "Y" or borrow == "yes" or borrow == "Yes" or borrow == "YES"):
        book_status(book_selected)
    else:
        print("Please enter a valid input")
        press()
        book_detail(book_selected)

def get_book():
    clear()

    print("Availale Book")
    for i in range(1,3):
        print(i,". ", book[i][1])
        i=i+1
    print("0 .  Main Menu")
    get_book_menu = int(input("\nChoose available book : "))

    if(get_book_menu):
        clear()
        book_detail(get_book_menu)
    elif(get_book_menu == 0):
        main()
    elif(get_book_menu < 0):
        print("Please enter a valid number")
        press()
    else:
        print("Please enter a valid number")
        press()

def main():
    clear()
    print("LIBRARY MANAGEMENT SYSTEM")
    print("Menu")
    print("1. List Book")
    print("2. Borrow Book")
    print("\n0. Exit\n")

    get_menu = int(input("Enter menu : "))

    if(get_menu < 0):
        print("Menu does not exist")
        press()
        main()
    elif(get_menu == 1):
        get_book()
    elif(get_menu == 2):
        print("Function not available yet")
        press()
        main()
    elif(get_menu == 0):
        exit()
    else:
        print("Please enter a valid menu")
        press()
        main()


#   System Start
main()