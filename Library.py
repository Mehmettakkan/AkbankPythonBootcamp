class Book:
    def __init__(self, book_name, author, release_date, number_of_pages):
        self.book_name = book_name
        self.author = author
        self.release_date = release_date
        self.number_of_pages = number_of_pages

class Library:

    def __init__(self, filename='Books.txt'):
        self.fileName = filename
        self.file = open(self.fileName, 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Dosyanın başına git
        lines = self.file.read().splitlines()  # Dosyayı oku ve satırlara ayır
        for line in lines:
            book_info = line.strip().split(', ')
            if len(book_info) == 4:
                book_name, author, release_date, number_of_pages = book_info
                print(f"Book: {book_name}, Author: {author}")
            else:
                print("Invalid format for a book entry:", line)

    def add_book(self):
        _book = Book(
            input("Enter the book name: "),
            input("Enter the book author: "),
            input("Enter the book release date: "),
            input("Enter the book number of pages: ")
        )

        book_info = f"{_book.book_name}, {_book.author}, {_book.release_date}, {_book.number_of_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def delete_book(self):
        _book_name = input("Enter the book name:")

        # Dosyadan tüm satırları oku
        self.file.seek(0)
        lines = self.file.readlines()

        # Her bir satırı kitap listesine ekle
        list_book = []
        for line in lines:
            list_book.append(line.strip())

        # Silinecek kitabı ara
        search_book = list(filter(lambda book: book.split(',')[0] == _book_name, list_book))

        # Eğer kitap bulunamazsa
        if len(search_book) == 0:
            print("No matching books found.")
        else:
            # İlk eşleşen kitabı listeden sil
            list_book.remove(search_book[0])
            print("Book deleted successfully.")

            # Dosyayı güncelle
            self.file.seek(0)
            self.file.truncate()
            for book in list_book:
                self.file.write(book + "\n")


def menu():
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")


# Main program
lib = Library()

while True:
    menu()
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.delete_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.") 