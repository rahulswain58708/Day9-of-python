class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    def __str__(self):
        return f"{self.title} - {self.pages} pages"
b= Book("python",350)
print(b)