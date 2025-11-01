class TestBookCollector:

    def test_add_new_book_valid_book_success(self, collector):
        collector.add_new_book("Новая книга")
        assert "Новая книга" in collector.books_genre
        assert collector.books_genre["Новая книга"] == ""
        assert len(collector.books_genre) == 1

    def test_add_new_book_empty_name_empty_dict(self, collector):
        collector.add_new_book("")
        assert "" not in collector.books_genre
        assert len(collector.books_genre) == 0

    def test_add_new_book_too_long_name_empty_dict(self, collector):
        long_name = "а" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre
        assert len(collector.books_genre) == 0

    def test_add_new_book_already_exists_one_book_in_dict(self, collector):
        collector.add_new_book("Повторяющаяся книга")
        collector.add_new_book("Повторяющаяся книга")
        assert "Повторяющаяся книга" in collector.books_genre
        assert len(collector.books_genre) == 1

    def test_set_genre_success_valid_book_valid_genre_one_el_in_dict(
        self, collector_with_book
    ):
        collector_with_book.set_book_genre("Автоматически добавленная книга", "Ужасы")
        assert (
            collector_with_book.books_genre["Автоматически добавленная книга"]
            == "Ужасы"
        )

    def test_set_genre_success_double_set_one_el_in_dict(self, collector_with_book):
        collector_with_book.set_book_genre("Автоматически добавленная книга", "Ужасы")
        collector_with_book.set_book_genre(
            "Автоматически добавленная книга", "Детективы"
        )
        assert (
            collector_with_book.books_genre["Автоматически добавленная книга"]
            == "Детективы"
        )

    def test_set_genre_nonexistent_book_one_el_in_dict(self, collector_with_book):
        collector_with_book.set_book_genre("Несуществующая книга", "Ужасы")
        assert "Несуществующая книга" not in collector_with_book.books_genre
        assert len(collector_with_book.books_genre) == 1

    def test_set_genre_invalid_genre_book_without_genre(self, collector_with_book):
        collector_with_book.set_book_genre(
            "Автоматически добавленная книга", "Философия"
        )
        assert collector_with_book.books_genre["Автоматически добавленная книга"] == ""

    def test_set_genre_empty_genre_book_without_genre(self, collector_with_book):
        collector_with_book.set_book_genre("Автоматически добавленная книга", "")
        assert collector_with_book.books_genre["Автоматически добавленная книга"] == ""

    def test_set_genre_empty_name_book_not_in_dict(self, collector_with_book):
        collector_with_book.set_book_genre("", "Ужасы")
        assert "" not in collector_with_book.books_genre

    def test_get_book_genre_valid_book_success(self, collector_with_valid_books):
        result = collector_with_valid_books.get_book_genre("Властелин Колец")
        assert result == "Фантастика"

    def test_get_book_genre_invalid_name_None(self, collector_with_valid_books):
        result = collector_with_valid_books.get_book_genre("Игра Эндера")
        assert result == None

    def test_get_book_genre_empty_name_None(self, collector_with_valid_books):
        result = collector_with_valid_books.get_book_genre("")
        assert result == None

    def test_get_books_with_specific_genre_valid_genre_list_with_two_books(
        self, collector_with_valid_books
    ):
        result = collector_with_valid_books.get_books_with_specific_genre("Фантастика")
        assert result == ["Гарри Поттер и Философский камень", "Властелин Колец"]

    def test_get_books_with_empty_dict_empty_list(self, collector):
        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == []

    def test_get_books_with_empty_genre_empty_list(self, collector_with_valid_books):
        result = collector_with_valid_books.get_books_with_specific_genre("")
        assert result == []

    def test_get_books_with_invalid_genre_empty_list(self, collector_with_valid_books):
        result = collector_with_valid_books.get_books_with_specific_genre("Фэнтези")
        assert result == []

    def test_get_books_genre_success(self, collector_with_valid_books):
        result = collector_with_valid_books.get_books_genre()
        assert result == {
            "Гарри Поттер и Философский камень": "Фантастика",
            "Властелин Колец": "Фантастика",
            "Капитал": "Ужасы",
        }

    def test_get_books_for_children_sucess(self, collector_with_valid_books):
        result = collector_with_valid_books.get_books_for_children()
        assert result == ["Гарри Поттер и Философский камень", "Властелин Колец"]

    def test_get_books_for_children_empty_dict_empty_list(self, collector):
        result = collector.get_books_for_children()
        assert result == []

    def test_get_books_for_children_adult_dict_empty_list(
        self, collector_with_valid_adult_books
    ):
        result = collector_with_valid_adult_books.get_books_for_children()
        assert result == []

    def test_add_book_in_favorites_valid_book_one_element_list(
        self, collector_with_valid_books
    ):
        collector_with_valid_books.add_book_in_favorites("Властелин Колец")
        assert collector_with_valid_books.favorites == ["Властелин Колец"]

    def test_add_book_in_favorites_already_exists_book_one_element_list(
        self, collector_with_valid_books
    ):
        collector_with_valid_books.add_book_in_favorites("Властелин Колец")
        collector_with_valid_books.add_book_in_favorites("Властелин Колец")
        assert collector_with_valid_books.favorites == ["Властелин Колец"]

    def test_add_book_in_favorites_invalid_book_empty_list(
        self, collector_with_valid_books
    ):
        collector_with_valid_books.add_book_in_favorites("Тихий Дон")
        assert collector_with_valid_books.favorites == []

    def test_add_book_in_favorites_empty_book_empty_list(
        self, collector_with_valid_books
    ):
        collector_with_valid_books.add_book_in_favorites("")
        assert collector_with_valid_books.favorites == []

    def test_delete_book_from_favorites_valid_book_one_element_list(
        self, collector_with_valid_books_and_favorites
    ):
        collector_with_valid_books_and_favorites.delete_book_from_favorites("Капитал")
        assert collector_with_valid_books_and_favorites.favorites == ["Властелин Колец"]

    def test_delete_book_from_favorites_already_deleted_book_one_element_list(
        self, collector_with_valid_books_and_favorites
    ):
        collector_with_valid_books_and_favorites.delete_book_from_favorites("Капитал")
        collector_with_valid_books_and_favorites.delete_book_from_favorites("Капитал")
        assert collector_with_valid_books_and_favorites.favorites == ["Властелин Колец"]

    def test_delete_book_from_favorites_invalid_book_two_elements_list(
        self, collector_with_valid_books_and_favorites
    ):
        collector_with_valid_books_and_favorites.delete_book_from_favorites("Тихий Дон")
        assert collector_with_valid_books_and_favorites.favorites == [
            "Властелин Колец",
            "Капитал",
        ]

    def test_delete_book_from_favorites_empty_book_two_elements_list(
        self, collector_with_valid_books_and_favorites
    ):
        collector_with_valid_books_and_favorites.delete_book_from_favorites("Т")
        assert collector_with_valid_books_and_favorites.favorites == [
            "Властелин Колец",
            "Капитал",
        ]

    def test_get_list_of_favorites_books_success(
        self, collector_with_valid_books_and_favorites
    ):
        result = collector_with_valid_books_and_favorites.get_list_of_favorites_books()
        assert result == ["Властелин Колец", "Капитал"]
