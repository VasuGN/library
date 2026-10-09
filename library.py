import csv
import os

fileName = "books.csv"


def create_csv():
    if not os.path.exists(fileName):
        with open(fileName, "w", newline="") as file:
            writer = csv.writer(file) 
            writer.writerow(["Library", "Book Title", "Author"])
            print("header row added")


def add_book():
    library_name = input("Enter library name: ")
    book_title = input("Enter book title: ")
    author = input("Enter author name: ")

    with open(fileName, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([library_name, book_title, author])
    print("Books added")


def view_entries():
    with open(fileName, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
    if len(rows) <= 1:
        print("No entries found.")
        return
    for row in rows:
        print(" | ".join(row))


def main():
    create_csv()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a book")
        print("2. View entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
