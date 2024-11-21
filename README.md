# Консольное приложение для управления библиотекой книг.

## Основные функции приложения:
  !1. Добавление книги в библиотеку (def add_book):
       Пользователь вводит название книги (title: str), автора книги (author: str), год написания книги (year: int).
     
  !2. Удаление книги из библиотеки (def del_book):
       Пользователь вводит id (id: int) книги:
         - Если в библиотеке нет книги под данным id, происходит обработка данного события и всплывает предупреждающее сообщение.
         - Если в библиотеке есть книга под данным id, происходит удаление данных об этой книге.
     
  !3. Поиск книги в библиотеке (def search_book):
       Пользователь вводит название книги (title: str | None) или автора книги (author: str | None), или год написания книги (year: int | None):
         - Если пользователь не ввёл ни одного аргумента, то программа выдаёт сообщение о том, что книга не найдена
         - Если пользователь ввёл 1 или 2 аргумента, программа выдаст книги, подлходящие под данные условия
         - Если пользователь ввёл все предложенные аргументы, то программа выдаст либо None, либо информацию о существующей в библиотеке книге.
     
  !5. Изменение статуса книги в библиотеке (def change_book_status):
       Пользователь вводит id (id: int) и статус (status: str) книги:
         - Если в библиотеке нет книги под данным id, происходит обработка данного события и всплывает предупреждающее сообщение.
         - Если указан валидный статус ("в наличии", "выдана") и валидный id, изменяется статус книги

  !6. Отображение всех книг в библиотеке (def get_books)


## При запуске программы НЕОБХОДИМО выбирать только те пункты, которые были предложены самой программой, иначе, в терминале будет высвечиваться сообщение: "Неверный номер пункта"

!!! БИБЛИОТЕКА КНИГ НЕ ПРЕДНАЗНАЧЕНА ДЛЯ ХРАНЕНИЯ ОДИНАКОВЫХ ЭКЗЕМПЛЯРОВ КНИГ !!!
!!! ДОБАВЛЕНИЕ ОДИНАКОВЫХ ЭКЗЕМПЛЯРОВ МОЖЕТ ПРИВЕСТИ К НЕОЖИДАННОМУ РЕЗУЛЬТАТУ !!!
