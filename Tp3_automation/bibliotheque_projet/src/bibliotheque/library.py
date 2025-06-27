from .book import Book
from .user import User

class Library:
	"""Gestionnaire de bibliothèque"""

	def __init__(self, name):
		# TODO: Initialisez nom et collections
		if not name:
			raise ValueError("Le nom de la bibliothèque ne peut pas être vide.")
		self.name = name
		self.books = {}  

	def add_book(self, book):
		# TODO: Ajoutez un livre à la collection
		if not isinstance(book, Book):
			raise TypeError("book doit être une instance de Book.")
		if book.isbn in self.books:
			raise ValueError(f"Un livre avec l'ISBN {book.isbn} existe déjà.")
		self.books[book.isbn] = book

	def find_book_by_isbn(self, isbn):
		# TODO: Trouvez un livre par ISBN
		return self.books.get(isbn, None)

	def borrow_book(self, user, isbn):
		# TODO: Gérez l'emprunt complet
		# 1. Trouvez le livre
		book = self.find_book_by_isbn(isbn)
		if book is None:
			return False

		# 2. Vérifiez que user peut emprunter
		# (TODO: implémenter logiquement si User a un quota, etc.)
		if not isinstance(user, User):
			raise TypeError("user doit être une instance de User.")

		# 3. Vérifiez que le livre est disponible
		if not book.is_available():
			return False

		# 4. Effectuez l'emprunt
		success = book.borrow()
		# (TODO: ajouter le livre aux emprunts de user si on gère cela)
		return success
