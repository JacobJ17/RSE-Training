class Book:
    def __init__(self, title: str, author: str):
        self.title = title.title()
        self.author = author.title()

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book('A Book', 'Me')

print(book)