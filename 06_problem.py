#Q. Create a class Library to manage book borrowing and returning. Track available books.
class Library:
    def __init__(self,books):
        self.books=books
    
    def display_books(self):
        print("Available Books")
        for book in self.books:
            print(f"- {book}")
        
    def borrow_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"you borrowed '{book_name}' ")
        else:
            print("Book not available")
    
    def return_book(self,book_name):
        self.books.append(book_name)
        print(f"you return '{book_name}' ")

lib= Library(["python","c++","AI","ML"])
lib.display_books()
lib.borrow_book("python")
lib.display_books()
lib.return_book("python")
lib.display_books()