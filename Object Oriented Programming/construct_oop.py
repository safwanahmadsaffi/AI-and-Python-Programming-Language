
class Book():                 #class = Data+Behaviour (method / function)
    def __init__(self,title,author,pages): #constructor
        self.title=title
        self.author=author
        self.pages=pages
        self.isbn=" "
    def add_isbn(self,isbn):
        self.isbn = isbn 
    
book1 = Book("Python Rocks!", "Jose Portilla", 159)
book1.add_isbn("987")
book2 = Book("Django Rocks!", "Jose Portilla", 159)
print(book1.isbn)
print(book2.isbn)