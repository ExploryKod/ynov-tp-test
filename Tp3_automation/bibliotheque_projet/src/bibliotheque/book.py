class Book:
	"""Représente un livre dans la bibliothèque"""

	def __init__(self, title, author, isbn):
		if not title:
			raise ValueError("Le titre ne peut pas être vide.")
		if not author:
			raise ValueError("L'auteur ne peut pas être vide.")
		if not isinstance(isbn, str) or len(isbn) != 13:
			raise ValueError("ISBN doit être une chaîne de 13 caractères.")

		self.title = title
		self.author = author
		self.isbn = isbn
		self.borrowed = False

	def is_available(self):
		"""Retourne True si le livre n'est pas emprunté."""
		return not self.borrowed

	def borrow(self):
		"""
		Marque le livre comme emprunté.
		Retourne True si l'opération réussit,
		False si le livre est déjà emprunté.
		"""
		if self.borrowed:
			return False
		self.borrowed = True
		return True

	def return_book(self):
		"""
		Marque le livre comme disponible.
		Retourne True si l'opération réussit,
		False si le livre n'était pas emprunté.
		"""
		if not self.borrowed:
			return False
		self.borrowed = False
		return True
