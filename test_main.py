import pytest

from main import BooksCollector


class TestBooksCollector:

        # (0) ТЕСТЫ МЕТОДА __INIT__
    # 1. По умолчанию значение словаря books_genre - {}
    def test_default_value_books_genre_empty_dictionary(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    # 2. self.favorites = []
    def test_default_value_favorites_empty_line(self):
        collector = BooksCollector()
        assert collector.favorites == []

    # 3. self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    def test_default_value_genre_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # 4. self.genre_age_rating = ['Ужасы', 'Детективы']
    def test_default_value_genre_age_rating_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

        # (1) ТЕСТЫ МЕТОДА add_new_book
    # 5. Книги добавились в словарь
    def test_add_new_book_add_two_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(list(collector.get_books_genre())) == 2

    # 6. Жанр добавленной книги - ''
    def test_add_new_book_without_specifying_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        assert collector.get_book_genre('Гордость и зомби') == ''

    # 7-11. Название книги может содержать 1,2,20,39 и 40 символов
    @pytest.mark.parametrize('book', ['Q', 'Qw', 'qwertyuiopasdfghjk20', 'qwertyuiopasdfghjk20qwertyuiopasdfghj39', 'qwertyuiopasdfghjk20qwertyuiopasdfghjk40',])
    def test_add_new_book_length_of_name_by_condition_true(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(list(collector.get_books_genre())) == 1

    # 12-14. Название книги не может содержать 0 символов, 41 символ и 100 символов
    @pytest.mark.parametrize('book', ['', 'qwertyuiopasdfghjk20qwertyuiopasdfghjkq41', 'qwertyuiopasdfghjk20qwertyuiopasdfghjk40qwertyuiopasdfghjk60qwertyuiopasdfghjk80qwertyuiopasdfghj100'])
    def test_add_new_book_length_of_name_not_by_condition_true(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(list(collector.get_books_genre())) == 0

    # 15. Попробовать добавить туже книгу
    def test_add_new_book_add_same_book_not_be_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        collector.add_new_book('Гордость и зомби')
        assert len(list(collector.get_books_genre())) == 1

        # (2) ТЕСТЫ МЕТОДА set_book_genre
    # 16. Можно устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre
    def test_set_book_genre_book_in_books_genre_and_genre_genre_be_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        collector.set_book_genre('Гордость и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и зомби') == 'Ужасы'

    # 17. Нельзя установить жанр книги, если книга есть в books_genre, но её жанр не входит в список genre
    def test_set_book_genre_book_in_books_genre_but_not_in_genre_genre_not_be_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        collector.set_book_genre('Гордость и зомби', 'Аниме')
        assert collector.get_book_genre('Гордость и зомби') == ''

    # 18. Нельзя установить жанр книги, если её жанр входит в список genre, но книги нет в books_genre
    def test_set_book_genre_book_in_genre_but_not_in_books_genre_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        collector.set_book_genre('Токийский гуль', 'Ужасы')
        assert collector.get_book_genre('Токийский гуль') == None

    # 19. Нельзя установить жанр книги, если книги нет в books_genre и её жанр не входит в список genre
    def test_set_book_genre_book_not_in_genre_and_books_genre_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        collector.set_book_genre('Токийский гуль', 'Аниме')
        assert collector.get_book_genre('Токийский гуль') == None

        # (3) ТЕСТЫ МЕТОДА get_book_genre
    # 20. Выводит жанр книги по её имени, когда жанр пуст
    def test_get_book_genre_new_book_with_empty_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        assert collector.get_book_genre('Гордость и зомби') == ''

    # 21. Выводит жанр книги по её имени, когда жанр не пуст
    def test_get_book_genre_new_book_with_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        collector.set_book_genre('Гордость и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и зомби') == 'Ужасы'

        # (4) ТЕСТЫ МЕТОДА get_books_with_specific_genre
    # 22. Выводит список книг с определённым жанром
    def test_get_books_with_specific_genre_fantasy_true(self):
        collector = BooksCollector()
        collector.add_new_book('Начало зомби')
        collector.set_book_genre('Начало зомби', 'Фантастика')
        collector.add_new_book('Назад в будущее зомби')
        collector.set_book_genre('Назад в будущее зомби', 'Фантастика')
        collector.add_new_book('Чужой зомби')
        collector.set_book_genre('Чужой зомби', 'Ужасы')
        collector.add_new_book('Достать ножи с зомби')
        collector.set_book_genre('Достать ножи с зомби', 'Детективы')
        collector.add_new_book('Зомби Клаус')
        collector.set_book_genre('Зомби Клаус', 'Мультфильмы')
        collector.add_new_book('Один дома с зомби')
        collector.set_book_genre('Один дома с зомби', 'Комедии')
        fantasy_list = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_list == ['Начало зомби', 'Назад в будущее зомби']

    # 23.Выведит пустой список, если у книг в books_genre не указан жанр
    def test_get_books_with_specific_genre_genre_of_books_is_not_specified_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Начало зомби')
        collector.add_new_book('Назад в будущее зомби')
        collector.add_new_book('Чужой зомби')
        collector.set_book_genre('Чужой зомби', 'Ужасы')
        collector.add_new_book('Достать ножи с зомби')
        collector.set_book_genre('Достать ножи с зомби', 'Детективы')
        collector.add_new_book('Зомби Клаус')
        collector.set_book_genre('Зомби Клаус', 'Мультфильмы')
        collector.add_new_book('Один дома с зомби')
        collector.set_book_genre('Один дома с зомби', 'Комедии')
        fantasy_list = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_list == []

    # 24. Выведит пустой список, если книг в books_genre нет
    def test_get_books_with_specific_genre_no_books_in_books_genre_empty_list(self):
        collector = BooksCollector()
        fantasy_list = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_list == []

        # (5) ТЕСТЫ МЕТОДА get_books_genre
    # 25. Выводит текущий словарь - с добавленной книгой
    def test_get_books_genre_new_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и зомби')
        assert collector.get_books_genre() == {'Гордость и зомби': ''}

        # (6) ТЕСТЫ МЕТОДА get_books_for_children
    # 26. Вернется список книг, жанр которых не в genre_age_rating и в genre
    def test_get_books_for_children_all_genres_from_genre_books_horror_and_detective_not_included(self):
        collector = BooksCollector()
        collector.add_new_book('Начало зомби')
        collector.set_book_genre('Начало зомби', 'Фантастика')
        collector.add_new_book('Чужой зомби')
        collector.set_book_genre('Чужой зомби', 'Ужасы')
        collector.add_new_book('Достать ножи с зомби')
        collector.set_book_genre('Достать ножи с зомби', 'Детективы')
        collector.add_new_book('Зомби Клаус')
        collector.set_book_genre('Зомби Клаус', 'Мультфильмы')
        collector.add_new_book('Один дома с зомби')
        collector.set_book_genre('Один дома с зомби', 'Комедии')
        books_for_children_list = collector.get_books_for_children()
        assert books_for_children_list == ['Начало зомби', 'Зомби Клаус', 'Один дома с зомби']

    # 27. Не вернет список книг, жанр которых не в genre_age_rating и не в genre
    def test_get_books_for_children_all_genres_not_from_genre_books_all_not_included(self):
        collector = BooksCollector()
        collector.add_new_book('Начало зомби')
        collector.set_book_genre('Начало зомби', 'Драма')
        collector.add_new_book('Чужой зомби')
        collector.set_book_genre('Чужой зомби', 'Хорор')
        collector.add_new_book('Достать ножи с зомби')
        collector.set_book_genre('Достать ножи с зомби', 'Пьеса')
        collector.add_new_book('Зомби Клаус')
        collector.set_book_genre('Зомби Клаус', 'Аниме')
        collector.add_new_book('Один дома с зомби')
        collector.set_book_genre('Один дома с зомби', 'Вестрн')
        books_for_children_list = collector.get_books_for_children()
        assert books_for_children_list == []

        # (7) ТЕСТЫ МЕТОДА add_book_in_favorites
    # 28. Можно добавить книгу в избранное, если книга находится в словаре books_genre и ее нет в списке favorites
    def test_add_book_in_favorites_book_in_books_genre_and_not_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Один дома с зомби')
        collector.add_book_in_favorites('Один дома с зомби')
        assert collector.get_list_of_favorites_books() == ['Один дома с зомби']

    # 29. Нельзя добавить книгу, если ее нет в словаре books_genre и списке favorites
    def test_add_book_in_favorites_book_not_in_books_genre_and_favorites_true(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Один дома с зомби')
        assert collector.get_list_of_favorites_books() == []

    # 30. Повторно добавить книгу в избранное нельзя
    def test_add_book_in_favorites_add_same_book_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Один дома с зомби')
        collector.add_book_in_favorites('Один дома с зомби')
        collector.add_book_in_favorites('Один дома с зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

        # (8) ТЕСТЫ МЕТОДА delete_book_from_favorites
    # 31. Можно удалить книгу из избранного, если она там есть
    def test_delete_book_from_favorites_book_in_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book('Один дома с зомби')
        collector.add_book_in_favorites('Один дома с зомби')
        collector.delete_book_from_favorites('Один дома с зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    # 32. Нельзя удалить книгу из избранного, если ее там нет
    def test_delete_book_from_favorites_book_not_in_favorites_book_has_not_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Один дома с зомби')
        collector.add_book_in_favorites('Один дома с зомби')
        collector.delete_book_from_favorites('Чужой зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

        # (9) ТЕСТЫ МЕТОДА get_list_of_favorites_books
    # 33. Выводит текущий список избранных книг - с добавленной книгой
    def test_get_list_of_favorites_books_new_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Один дома с зомби')
        collector.add_book_in_favorites('Один дома с зомби')
        assert collector.get_list_of_favorites_books() == ['Один дома с зомби']
