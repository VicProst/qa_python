# qa_python

ТЕСТЫ МЕТОДА __init__
1) test_default_value_books_genre_empty_dictionary : По умолчанию значение словаря books_genre - {}
2) test_default_value_favorites_empty_line : По умолчанию значение cписока favorites - []
3) test_default_value_genre_true : По умолчанию значение cписока genre - ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
4) test_default_value_genre_age_rating_true : По умолчанию значение cписока genre_age_rating - ['Ужасы', 'Детективы']

ТЕСТЫ МЕТОДА add_new_book (переменная name)
5) test_set_book_genre_book_in_books_genre_and_genre_genre_be_set : Книги добавились в словарь
6) test_add_new_book_without_specifying_genre_true : Жанр добавленной книги - ''
7-11) test_add_new_book_length_of_name_by_condition_true : Название книги может содержать 1,2,20,39 и 40 символов
12-14) test_add_new_book_length_of_name_not_by_condition_true : Название книги не может содержать 0 символов, 41 символ и 100 символов
15) test_add_new_book_add_same_book_not_be_added : Попробовать добавить туже книгу

ТЕСТЫ МЕТОДА set_book_genre (переменные name, genre)
16) test_set_book_genre_book_in_books_genre_and_genre_true : Можно устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre
17) test_set_book_genre_book_in_books_genre_but_not_in_genre_genre_not_be_set : Нельзя установить жанр книги, если книга есть в books_genre, но её жанр не входит в список genre
18) test_set_book_genre_book_in_genre_but_not_in_books_genre_no_genre : Нельзя установить жанр книги, если её жанр входит в список genre, но книги нет в books_genre
19) test_set_book_genre_book_not_in_genre_and_books_genre_no_genre : Нельзя установить жанр книги, если книги нет в books_genre и её жанр не входит в список genre

ТЕСТЫ МЕТОДА get_book_genre (переменная name)
20) test_get_book_genre_new_book_with_empty_genre_true : Выводит жанр книги по её имени, когда жанр пуст
21) test_get_book_genre_new_book_with_genre_true : Выводит жанр книги по её имени, когда жанр не пуст

ТЕСТЫ МЕТОДА get_books_with_specific_genre (переменная genre)
22) test_get_books_with_specific_genre_fantasy_true : Выводит список книг с определённым жанром
23) test_get_books_with_specific_genre_genre_of_books_is_not_specified_empty_list : Выведет пустой список если в books_genre у книг не указан жанр
24) test_get_books_with_specific_genre_no_books_in_books_genre_empty_list : Выведит пустой список если книг в books_genre нет

ТЕСТЫ МЕТОДА get_books_genre (переменной нет)
25) test_get_books_genre_new_book_true : Выводит текущий словарь - с добавленной книгой

ТЕСТЫ МЕТОДА get_books_for_children (переменной нет)
26) test_get_books_for_children_all_genres_from_genre_books_horror_and_detective_not_included : Вернется список книг, жанр которых не в genre_age_rating и в genre
27) test_get_books_for_children_all_genres_not_from_genre_books_all_not_included : Не вернет список книг, жанр которых не в genre_age_rating и не в genre

ТЕСТЫ МЕТОДА add_book_in_favorites (переменная name)
28) test_add_book_in_favorites_book_in_books_genre_and_not_in_favorites_true : Добавляет книгу в избранное, если книга находится в словаре books_genre и ее нет в favorites
29) test_add_book_in_favorites_book_not_in_books_genre_and_favorites_true : Нельзя добавить книгу, если она не находится в словаре и ее нет в favorites 
30) test_add_book_in_favorites_add_same_book_one_book : Повторно добавить книгу в избранное нельзя

ТЕСТЫ МЕТОДА delete_book_from_favorites (переменная name)
31) test_delete_book_from_favorites_book_in_favorites_delete_book : Можно удалить книгу из избранного, если она там есть
32) test_delete_book_from_favorites_book_not_in_favorites_book_has_not_deleted : Нельзя удалить книгу из избранного, если ее там нет

ТЕСТЫ МЕТОДА get_list_of_favorites_books (переменной нет)
33) test_get_list_of_favorites_books_new_favorites_books_true : Выводит текущий список избранных книг - с добавленной книгой
