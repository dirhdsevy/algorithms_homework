"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
Розв’язання задачі за допомогою хеш-таблиці з відкритою адресацією.
"""

_SIZE = 130003  # Просте число, що значно більше за обсяг даних, щоб уникнути кластеризації
_table = [None] * _SIZE
_DELETED = ("DELETED", None)  # Маркер для видалених елементів

def _hash(key):
    return abs(hash(key)) % _SIZE

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global _table
    _table = [None] * _SIZE

def addBook(author, title):
    """ Додає книгу до бібліотеки. """
    global _table
    idx = _hash(author)
    start_idx = idx
    first_deleted_idx = None

    while _table[idx] is not None:
        if _table[idx] is _DELETED:
            if first_deleted_idx == None:
                first_deleted_idx = idx
        elif _table[idx][0] == author:
            _table[idx][1].add(title)
            return
        
        idx = (idx + 1) % _SIZE
        if idx == start_idx:
            break

    # Якщо автора не знайшли, вставляємо в першу доступну комірку
    target_idx = first_deleted_idx if first_deleted_idx is not None else idx
    if _table[target_idx] is None or _table[target_idx] is _DELETED:
        _table[target_idx] = (author, {title})
    else:
        raise MemoryError("Hash table is completely full!")

def find(author, title):
    """ Перевіряє чи міститься задана книга у бібліотеці. """
    idx = _hash(author)
    start_idx = idx

    while _table[idx] is not None:
        if _table[idx] is not _DELETED and _table[idx][0] == author:
            return title in _table[idx][1]
        
        idx = (idx + 1) % _SIZE
        if idx == start_idx:
            break
            
    return False

def delete(author, title):
    """ Видаляє книгу з бібліотеки. """
    global _table
    idx = _hash(author)
    start_idx = idx

    while _table[idx] is not None:
        if _table[idx] is not _DELETED and _table[idx][0] == author:
            if title in _table[idx][1]:
                _table[idx][1].remove(title)
            # Якщо у автора більше немає книг, звільняємо комірку через маркер
            if not _table[idx][1]:
                _table[idx] = _DELETED
            return
        
        idx = (idx + 1) % _SIZE
        if idx == start_idx:
            break

def findByAuthor(author):
    """ Повертає список книг заданого автора в алфавітному порядку. """
    idx = _hash(author)
    start_idx = idx

    while _table[idx] is not None:
        if _table[idx] is not _DELETED and _table[idx][0] == author:
            return sorted(list(_table[idx][1]))
        
        idx = (idx + 1) % _SIZE
        if idx == start_idx:
            break

    return []