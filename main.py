class Book:
    amount = 0
    
    def __init__(self, title: str, author: str, year: int) -> None:
        self.id = Book.amount + 1
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'
        Book.amount += 1
      
        
    def set_new_status(self, status: str) -> None:
        self.status = status
        
    def to_dict(self) -> dict:
        return self.__dict__
    
    
class Library:
    def __init__(self):
        self.mas: list[Book] = []
    
    
    def add_book(self, title: str, author: str, year: int) -> dict:
        book = Book(title, author, year)
        self.mas.append(book)
        return {'Сообщение': 'Книга успешно добавлена в библиотеку'}
        
    def del_book(self, id: int) -> dict:
        has_id = False #Флаг для определения наличия id книги в библиотеке
        for book in self.mas:
            if book.id == id:
                has_id = True 
                self.mas.remove(book)
                return {'Сообщение': 'Книга успешно удалена из библиотеки'}
        if not has_id:
            raise IndexError
    
    def search_book(self, title: str | None = None, author: str | None = None, year: str | None = None) -> dict:
        result = ''
        if title or author or year:
            for book in self.mas:
                if book.title == title or book.author == author or book.year == year:
                    result += str(book.to_dict()) + '\n'
        if result:
            return result
        return {'Сообщение': 'Книга не найдена'}

    def change_book_status(self, id: int, status: str) -> dict:
        has_id = False #Флаг для определения наличия id книги в библиотеке
        for book in self.mas:
            if book.id == id:
                book.status = status
                return {'Сообщение': 'Статус книги успешно изменён'}
        if not has_id:
            raise IndexError
    
    def get_books(self) -> str | None:
        if self.mas:
            result = ''
            for book in self.mas:
                result += str(book.to_dict()) + '\n'
            return result
        return None
        

while(True):
    print('Выберите, что хотите сделать(номер пункта):\n1. Создать новую библиотеку\n2. Выйти\n')
    answer = int(input())
    
    if answer == 1:
        library = Library()
        while(True):
            print('\n\nВыберите, что хотите сделать(номер пункта):\n1. Добавить книгу\n2. Удалить книгу\n3. Искать книгу\n4. Отобразить все книги\n5. Изменить статус книги\n6. Выйти\n')
            answer = int(input())
            
            if answer == 1:
                try:
                    title = str(input('Введите название книги: '))
                    author = str(input('Введите автора книги: '))
                    year = int(input('Введите год написания книги: '))
                    print(library.add_book(title, author, year))
                except ValueError:
                    print('Введён неправильный тип аргументов. title: str, author: str, year: int\nПопробуйте ещё раз\n')   
            elif answer == 2:
                try:
                    id = int(input('Введите id книги: '))
                    print(library.del_book(id))
                except ValueError:
                    print('Введён неправильный тип аргумента. id: int\nПопробуйте ещё раз\n')
                except IndexError:
                    print('Попытка удалить несуществующую книгу')
            elif answer == 3:
                title = str(input('Введите название книги: '))
                author = str(input('Введите автора книги: '))
                year = input('Введите год написания книги: ')
                print(library.search_book(title, author, year))
            elif answer == 4:
                print(library.get_books(), end='')
            elif answer == 5:
                try:
                    id = int(input('Введите id книги: '))
                    status = str(input('Введите новый статус ("в наличии" или "выдана"): '))
                    if status in('в наличии', 'выдана'):
                        library.change_book_status(id, status)
                    else:
                        print('Введён неверный статус книги. Попробуйте снова\n')
                except ValueError:
                    print('Введён неправильный тип аргументов. id: int, status: str\nПопробуйте ещё раз\n')
                except IndexError:
                    print('Попытка изменить несуществующую книгу')      
            elif answer == 6:
                break
            else:
                print('Неверный номер пункта\n')
    elif answer == 2:
        print('Процесс завершён...')
        break
    else:
        print('Неверный номер пункта\n')