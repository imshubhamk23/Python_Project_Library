class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("The available books are:- ")
        for book in self.books:
            print(" *", book)

    def borrowBook(self,bookName):
        self.bookName = bookName
        if self.bookName in self.books:
            print(f"You have been issued {bookName}.")
            self.books.remove(bookName)
        else:
            print("The book is not available. Please borrow a different book!")

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book!")
        

class Student:

    def __init__(self,listOfStudents):
        self.studentslist = listOfStudents


    def borrow(self):
        self.book = input("Please Enter Name of book to borrow:- ")
        return self.book

    def returnbook(self):
        self.book = input("Please Enter Name of book to return:- ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["DSA", "Python Notes", "Jungle Book"])
    students = Student(["Rohan", "Shubham", "Mayur", "Mahesh"])
    while True:
        welcomeMsg = """=====Welcome to Library=====
        Please Choose an Option:- 
    Press 1:- List all books
    Press 2:- Request a book
    Press 3:- Add or Return a book
    Press 4:- Exit Library
        """
        name = input("Please enter your name:- ")
        if name in students.studentslist:
            print(welcomeMsg)
            try:
                a = int(input("Please Enter your choice:- "))
                if a <=4:
                    if a == 1:
                        centralLibrary.displayAvailableBooks()
                    elif a == 2:
                        centralLibrary.borrowBook(students.borrow())
                    elif a == 3:
                        centralLibrary.returnBook(students.returnbook())
                    elif a == 4:
                        print("Thanks for visiting the Library. Have a great day ahead!")
                        exit()
                else:
                    print("Please enter valid options!")
            except Exception:
                print("Invalid Input! Please try again")
        else:
            print('Your name does not exist in system. Please contact Librarian!')