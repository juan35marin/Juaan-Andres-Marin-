library = []

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    pages = input("Number of pages: ")
    try:
        pages = int(pages)
    except ValueError:
        print("Please enter a valid number for pages.")
        return
    book = {'title': title, 'author': author, 'pages': pages}
    library.append(book)
    print(f'Book "{title}" added.\n')

def search_by_title():
    title = input("Enter the title to search: ")
    found_books = [book for book in library if book['title'].lower() == title.lower()]
    if found_books:
        for book in found_books:
            print(f'Title: {book["title"]}, Author: {book["author"]}, Pages: {book["pages"]}')
    else:
        print("No books found with that title.")
    print()

def show_all_books():
    if library:
        print("Books in the library:")
        for book in library:
            print(f'Title: {book["title"]}, Author: {book["author"]}, Pages: {book["pages"]}')
    else:
        print("No books in the library.")
    print()

def menu():
    while True:
        print("----- Library Menu -----")
        print("1. Add book")
        print("2. Search book by title")
        print("3. Show all books")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_by_title()
        elif choice == '3':
            show_all_books()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

menu()