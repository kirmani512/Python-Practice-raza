library=[]

total=0

def add_book():
    global total

    title=input("title here: ")

    author=input("author here: ")

    book={"title": title, "author": author}

    library.append(book)

    total+=1

    print(f"book {title} by {author}")


def total_books():
    print(f"total books are {total}")

add_book()

total_books()


