import pytest
from src.bibliotheque.library import Library
from src.bibliotheque.book import Book
from src.bibliotheque.user import User

class TestLibraryOperations:

    def setup_method(self):
        """Fixture complexe : bibliothèque avec livres et utilisateurs"""
        # TODO: Créez une bibliothèque
        self.library = Library(name="Bibliothèque Centrale")

        # TODO: Créez 2-3 livres avec différents ISBN
        self.book1 = Book(title="La Reine du Nil", author=" Christian Jacque", isbn="1234567890123")
        self.book2 = Book(title="Brave New World", author="Aldous Huxley", isbn="9876543210987")
        self.book3 = Book(title="Le craving", author="Judson Brewer", isbn="1111222233334")

        # TODO: Créez 2 utilisateurs
        self.user1 = User(name="Joe", email="joe@example.com")
        self.user2 = User(name="Amaury", email="amaury@example.com")

        # TODO: Ajoutez les livres à la bibliothèque
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

    def test_borrow_flow_success(self):
        """Test flux complet d'emprunt réussi"""
        # TODO: Empruntez un livre
        success = self.library.borrow_book(self.user1, self.book1.isbn)

        # TODO: Vérifiez tous les changements d'état
        assert success is True
        assert self.book1.is_available() is False
        assert self.book1 in self.user1.borrowed_books

    def test_user_cannot_borrow_more_than_limit(self):
        """Test limite d'emprunts par utilisateur"""
        # TODO: Faites emprunter 3 livres (limite)
        self.library.borrow_book(self.user2, self.book1.isbn)
        self.user2.add_borrowed_book(self.book1)

        self.library.borrow_book(self.user2, self.book2.isbn)
        self.user2.add_borrowed_book(self.book2)

        self.library.borrow_book(self.user2, self.book3.isbn)
        self.user2.add_borrowed_book(self.book3)

        # TODO: Tentez un 4ème emprunt
        extra_book = Book(title="La méthode Agora", author="Luc Bodin", isbn="5555666677778")
        self.library.add_book(extra_book)

        # TODO: Vérifiez que c'est refusé
        can_borrow_more = self.user2.can_borrow()
        assert can_borrow_more is False

        result = self.library.borrow_book(self.user2, extra_book.isbn)
        assert result is False
        assert extra_book.is_available() is True
        assert extra_book not in self.user2.borrowed_books
