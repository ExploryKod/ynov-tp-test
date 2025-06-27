import pytest
from src.bibliotheque.book import Book

class TestBookCreation:
    """Tests de création de livre"""

    def test_create_book_when_valid_parameters_then_attributes_are_assigned(self):
        """Test création livre valide"""
        book = Book(title="1984", author="George Orwell", isbn="1234567890123")
        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.isbn == "1234567890123"
        assert book.is_available() is True

    def test_create_book_when_empty_title_then_raises_value_error(self):
        """Test titre vide lève une erreur"""
        with pytest.raises(ValueError, match="titre"):
            Book(title="", author="George Orwell", isbn="1234567890123")

    def test_create_book_when_invalid_isbn_too_short_then_raises_value_error(self):
        """Test ISBN trop court lève une erreur"""
        with pytest.raises(ValueError, match="ISBN"):
            Book(title="1984", author="George Orwell", isbn="12345")

    def test_create_book_when_invalid_isbn_too_long_then_raises_value_error(self):
        """Test ISBN trop long lève une erreur"""
        with pytest.raises(ValueError, match="ISBN"):
            Book(title="1984", author="George Orwell", isbn="1234567890123456789")

class TestBookBorrowing:
    """Tests d'emprunt de livre"""

    def setup_method(self):
        """Fixture : prépare un livre pour chaque test"""
        self.book = Book(title="1984", author="George Orwell", isbn="1234567890123")

    def test_is_available_when_new_book_then_returns_true(self):
        """Test livre neuf disponible"""
        assert self.book.is_available() is True

    def test_borrow_when_book_available_then_returns_true_and_book_unavailable(self):
        """Test emprunt livre disponible"""
        result = self.book.borrow()
        assert result is True
        assert self.book.is_available() is False

    def test_borrow_when_book_already_borrowed_then_returns_false(self):
        """Test emprunt livre déjà emprunté"""
        first_borrow = self.book.borrow()
        second_borrow = self.book.borrow()
        assert first_borrow is True
        assert second_borrow is False
        assert self.book.is_available() is False
