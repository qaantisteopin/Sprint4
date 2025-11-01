import pytest
from application import BooksCollector


@pytest.fixture(scope="function")
def collector():
    return BooksCollector()


@pytest.fixture(scope="function")
def collector_with_book():
    collector = BooksCollector()
    collector.books_genre = {"Автоматически добавленная книга": ""}
    return collector


@pytest.fixture(scope="function")
def collector_with_valid_books():
    collector = BooksCollector()
    collector.books_genre = {
        "Гарри Поттер и Философский камень": "Фантастика",
        "Властелин Колец": "Фантастика",
        "Капитал": "Ужасы",
    }
    return collector


@pytest.fixture(scope="function")
def collector_with_valid_adult_books():
    collector = BooksCollector()
    collector.books_genre = {
        "Капитал": "Ужасы",
        "Снеговик": "Детективы",
        "Некрономикон": "",
    }
    return collector


@pytest.fixture(scope="function")
def collector_with_valid_books_and_favorites():
    collector = BooksCollector()
    collector.books_genre = {
        "Гарри Поттер и Философский камень": "Фантастика",
        "Властелин Колец": "Фантастика",
        "Капитал": "Ужасы",
    }
    collector.favorites = ["Властелин Колец", "Капитал"]
    return collector
