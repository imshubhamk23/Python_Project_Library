class Library:
    
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    
    def displayAvailableBooks(self):
        print("The available books are:- ")
        for book in self.books:
            print(" *",book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("This book is either Not Available or has been issued to someone else. Please wait till book is available.")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print('Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!')


class Student:
    
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow:- ")
        return self.book
        
    def returnBook(self):
        self.book = input("Enter the name of book you want to return:- ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    while True:
        welcomeMsg = """
=====Welcome to Central Library=====
    Please Choose an Option:- 
    Press 1:- List all books
    Press 2:- Request a book
    Press 3:- Add or Return a book
    Press 4:- Exit Library
        """
        print(welcomeMsg)
        a = int(input("Enter a Choice:- "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()


