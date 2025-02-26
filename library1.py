# Sultan Nurfalah
# TI23H
class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You have successfully borrowed '{self.title}'")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"'{self.title}' has been returned successfully.")
        else:
            print(f"'{self.title}' is already available in the library.")


book1 = Book("Python Programming", "John Doe", "1234567890")
book1.borrow_book()
book1.borrow_book()  
book1.return_book()
book1.return_book() 
