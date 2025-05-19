# library=[]

# total=0

# def add_book():
#     global total

#     title=input("title here: ")

#     author=input("author here: ")

#     book={"title": title, "author": author}

#     library.append(book)

#     total+=1

#     print(f"book {title} by {author}")


# def total_books():
#     print(f"total books are {total}")

# add_book()

# add_book()

# total_books()


#another solution///////////////////////////////////
class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)

    def showinfo(self):
        print(f"the library has {self.noBooks} books. The Books are")
        for book in self.books:
            print(book)

l1=Library()
l1.addbook("python")
l1.addbook("Java")
l1.addbook("Php")

l1.showinfo()