library = []

def add_book():
    book = input("ENter you  book name: ")
    author = input("Enter author name: ")
    book = {"title": book, "author": author}
    library.append(book)
    return book

def search_book():
    query = input("Enter title or author to search: ").strip().lower()
    result = [book for book in library if query in book['title'].lower() or query in book['author'].lower()]

    if result:
        print("Books found:")
        for book in result:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books found matching your query.")

def display_inventory():
    if not library:
        print("No books in the library.")
    else:
        print("Current Library Inventory:")
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()