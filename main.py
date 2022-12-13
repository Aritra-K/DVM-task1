from tabulate import tabulate
import uuid
import openpyxl


class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.is_borrowed = False
        self.genre = genre
        self.ubid = uuid.uuid4()

    @staticmethod
    def borrow_book():
        book_name = str(input("Enter name of book: "))
        for book_object in shelf_action.book_dict:
            if shelf_action.book_dict[book_object].name == book_name:
                if shelf_action.book_dict[book_object].is_borrowed:
                    print("Sorry that book isn't available for issuing right now: ")
                else:
                    print("Book borrowed")
                    shelf_action.book_dict[book_object].is_borrowed = True

    @staticmethod
    def return_book():
        book_name = str(input("Enter name of book: "))
        for book_object in shelf_action.book_dict:
            if shelf_action.book_dict[book_object].name == book_name:
                if shelf_action.book_dict[book_object].is_borrowed:
                    print("Book returned")
                    shelf_action.book_dict[book_object].is_borrowed = False
                else:
                    print("No such book was borrowed")

    def get_uuid(self):
        return self.ubid


class Shelf:
    def __init__(self, genre, book_dict):
        self.genre = genre
        self.book_dict = book_dict

    def show_catalog(self):
        headers = ["Name", 'Author', "Genre", 'Unique book id']
        book_list = []
        for i in self.book_dict:
            book = [self.book_dict[i].name, self.book_dict[i].author, self.book_dict[i].genre]
            book_list.append(book)
        print(tabulate(book_list, headers, tablefmt='orgtbl'))

    @staticmethod
    def add_book():
        name = str(input("Enter name of book: "))
        author = str(input("Enter author of book: "))
        genre = str(input("Enter genre of book: "))
        shelf_action.book_dict[uuid.uuid4()] = Book(name, author, genre)

    def remove_book(self):
        book_name = str(input("Enter name of book: "))
        for ubid in self.book_dict:
            if self.book_dict[ubid].name == book_name:
                return ubid
            else:
                return False

    def get_books_count(self):
        return len(self.book_dict)

    def populate_books(self):
        wb = openpyxl.load_workbook('books.xlsx')
        ws = wb['Sheet1']
        rows = ws.iter_rows(min_row=2, max_row=3, min_col=1, max_col=3)
        for name, author, genre in rows:
            self.book_dict[uuid.uuid4()] = Book(name.value, author.value, genre.value)



action = {uuid.uuid4(): Book('Alex Rider', 'Anthony Horowitz', 'action'),
          uuid.uuid4(): Book('Children of the Lamp Series', 'P.B. Kerr', 'action'),
          uuid.uuid4(): Book('The Bartimaeus trilogy', 'Jonathan Stroud', 'action'),
          uuid.uuid4(): Book('Hunger Games', 'Suzanne Collins', 'action')}

shelf_action = Shelf('action', action)


# CLI
while True:
    user = str(input("Enter user status (Basic/Lib): "))
    if user == "Basic":
        choice = str(input("Do you want to borrow or return a book (b/r) or see catalog (catalog): "))
        if choice == 'catalog':
            Shelf.show_catalog(shelf_action)
        elif choice == 'b':
            Book.borrow_book()
        elif choice == 'r':
            Book.return_book()
    elif user == 'Lib':
        print("1. Add a book")
        print("2. Remove a book")
        print("3. See catalog")
        print("4. Populate Books")
        choice = input("Enter choice: ")
        if int(choice) == 1:
            Shelf.add_book()
            print(shelf_action.book_dict)
        elif int(choice) == 2:
            ubid = Shelf.remove_book(shelf_action)
            if ubid:
                shelf_action.book_dict.pop(ubid)
        elif int(choice) == 3:
            Shelf.show_catalog(shelf_action)
    
        elif int(choice) == 4:
            Shelf.populate_books(shelf_action)





