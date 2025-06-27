class User:
	"""Représente un utilisateur de la bibliothèque"""

	def __init__(self, name, email):
		# TODO: Validez email (doit contenir @)
		# TODO: Validez name (non vide)
		if not name:
			raise ValueError("Le nom de l'utilisateur ne peut pas être vide.")
		if "@" not in email:
			raise ValueError("L'email doit contenir un '@'.")
		self.name = name
		self.email = email
		self.borrowed_books = []

	def can_borrow(self, max_books=3):
		# TODO: Vérifiez si l'utilisateur peut emprunter
		# (limite de max_books livres)
		return len(self.borrowed_books) < max_books

	def add_borrowed_book(self, book):
		# TODO: Ajoutez un livre à la liste des emprunts
		self.borrowed_books.append(book)

	def remove_borrowed_book(self, book):
		# TODO: Retirez un livre de la liste des emprunts
		if book in self.borrowed_books:
			self.borrowed_books.remove(book)
