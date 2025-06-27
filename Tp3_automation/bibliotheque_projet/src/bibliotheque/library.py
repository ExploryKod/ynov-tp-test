from .book import Book
from .user import User

class Library:
	"""Gestionnaire de bibliothèque"""

	def __init__(self, name):
		# Initialisez nom et collections
		if not name:
			raise ValueError("Le nom de la bibliothèque ne peut pas être vide.")
		self.name = name
		self.books = {}

	def add_book(self, book):
		# Ajoutez un livre à la collection
		if not isinstance(book, Book):
			raise TypeError("book doit être une instance de Book.")
		if book.isbn in self.books:
			raise ValueError(f"Un livre avec l'ISBN {book.isbn} existe déjà.")
		self.books[book.isbn] = book

	def find_book_by_isbn(self, isbn):
		# Trouvez un livre par ISBN
		return self.books.get(isbn, None)

	def borrow_book(self, user, isbn):
		# Gérez l'emprunt complet
		# 1. Trouvez le livre
		book = self.find_book_by_isbn(isbn)
		if book is None:
			return False

		# 2. Vérifiez que user peut emprunter
		if not isinstance(user, User):
			raise TypeError("user doit être une instance de User.")
		if not user.can_borrow():
			return False

		# 3. Vérifiez que le livre est disponible
		if not book.is_available():
			return False

		# 4. Effectuez l'emprunt
		success = book.borrow()
		if success:
			user.add_borrowed_book(book)
			return True
		else:
			return False
