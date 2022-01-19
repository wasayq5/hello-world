class Library:

    def __init__(self, available_books=["No Longer Human", "The Diary of a Young Girl", "The Hitchhiker's Guide To The Galaxy"]):
        self.availablebooks = available_books
    
    def display_available_books(self):
        print("The following is a list of all the books available: ")
        print(" ")
        for i in range(len(self.availablebooks)):
            print(self.availablebooks[i])
        main(None)

    def borrow_book(self):
        requested_book = input("Which book do you want to borrow?: ")
        while requested_book not in self.availablebooks:
            print("%s is currently not available in the library. Please pick one that is available" % (requested_book))
            self.display_available_books()
            print(" ")
            requested_book = input("Which book do you want to borrow?: ")
        else:
            self.availablebooks.remove(requested_book)
            print("You've borrowed %s" %(requested_book))
        main(None)

    def return_book(self):
        returned_book = input("Which book will you be returning?: ")
        self.availablebooks.append(returned_book)
        print("Thank you for returning %s." %(returned_book))
        main(None)
        
def main(msg="Welcome to Wasay's library program!"):
    """
    Inputs: A welcome message that is removed after being shown once
    This program presents the user with 4 different options for what they can do in the library.
    """
    
    print(" ")
    if msg == None:
        print("Here's what you can do in the library: ")
        print("(1) Display all available books in the library\n(2) Borrow a book\n(3) Return a book\n(4) Leave the library")
    else:
        print(msg)
        print(" ")
        print("Here's what you can do in the library: ")
        print("(1) Display all available books in the library\n(2) Borrow a book\n(3) Return a book\n(4) Leave the library")

    lib = Library()

    user_choice = input("Enter Choice: ")
    possible_choices = ['1', '2', '3', '4']

    if user_choice != '4':
        while user_choice not in possible_choices:
            print("invalid choice! Enter '1', '2', '3', or '4'")
            user_choice = input("Enter Choice: ")
            print(" ")
        if user_choice == '1':
            lib.display_available_books()
            print(" ")
        elif user_choice == '2':
            lib.borrow_book()
            print(" ")
        else:
            lib.return_book()

    else:
        print("Thank you for visiting the library!")

main()
    