class Book:

    def __init__(self, isbn, título, autor, editorial, páginas, precio , ejemplares):
        self.isbn = isbn
        self.título = título
        self.autor = autor
        self.editorial = editorial
        self.páginas = páginas
        self.ejemplares = ejemplares 
        
        # Apartado 4
        if precio < 50 or precio > 1000:
            print("Precio no válido, debe estar entre 50 y 1000")
        else:
            self.precio = precio

    # Apartado 1
    def display(self):
        print("ISBN:" , self.isbn)
        print("Título:" , self.título)
        print("Precio:" , self.precio)
        print("Ejemplares:" , self.ejemplares)

    # Apartado 2
    def in_stock(self):
        if self.ejemplares > 0:
            return True
        else:
            return False

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

# Apartado 3
books = [book1, book2, book3, book4]

for book in books:
    book.display()
    print()


jack_books = []

for book in books: 
    if book.autor == "Jack": 
        jack_books.append(book.título)



print("Libros escritos por Jack:", jack_books)  
