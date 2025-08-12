import json
from pathlib import Path

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title}, {self.author}, {self.isbn}"


class Library:
    def __init__(self, name: str, db_path: str = "/Users/aliyilmaz/Desktop/Python202/Proje/library.json"):
        self.name = name
        self._books = []
        self.db_path = Path(db_path)

    def _read_db(self) -> list:
        try:
            with self.db_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write_db(self, data: list) -> None:
        with self.db_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_book(self, book: Book):
        veriler = self._read_db()
        veriler.append({
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn
        })
        self._write_db(veriler)

        self._books.append(book)

    def check_book(self,book : Book):
        veriler = self._read_db()
        for veri in veriler:
            if veri.get("isbn") == book.isbn:
                print("var")
            else:
                print("yok")
    
    def delete_book(self,isbn : str):
        veriler = self._read_db()
        for veri in veriler:
            if veri.get("isbn") != isbn:
                yeni = veri.get()
        self._write_db(yeni)
                


b1 = Book("Sefiller", "Victor Hugo", "123")
library = Library("btü")
b2 = Book("dümen", "dümen", "234")
print(b1)

while True:
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitapları Listele")
    print("4. Kitap Ara")
    print("5. Çıkış")

    secim = int(input("Lütfen yapmak istediğiniz işlemi giriniz: "))

    if secim == 1:
        title = input ("Lütfen kitabın ismini giriniz: ")
        author = input ("Lütfen yazarın ismini giriniz: ")
        isbn = input ("Lütfen isbn numarasını giriniz: ")
        book = Book(title, author, isbn)
        library.add_book(book)
    
    elif secim == 2:
        isbn = input ("Lütfen silmek istediğiniz kitabın ISBN numarasını giriniz: ")
        library.delete_book(isbn)


    elif secim == 5:
        break