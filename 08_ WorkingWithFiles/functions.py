def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('E:\\Education\\Acquaintance_Python\\08_ WorkingWithFiles\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник"""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('E:\\Education\\Acquaintance_Python\\08_ WorkingWithFiles\\book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')
    pass


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    pass


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    pass