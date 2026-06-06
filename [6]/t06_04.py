"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
Розв’язання задачі за допомогою хеш-таблиці з методом ланцюжків.
"""

_SIZE = 11003  # Для ланцюжків розмір може бути меншим
_table = [[] for _ in range(_SIZE)]

def _hash(key):
    return abs(hash(key)) % _SIZE

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global _table
    _table = [[] for _ in range(_SIZE)]

def addBook(author, title):
    """ Додає книгу до бібліотеки. """
    idx = _hash(author)
    bucket = _table[idx]
    
    for pair in bucket:
        if pair[0] == author:
            pair[1].add(title)
            return
            
    bucket.append([author, {title}])

def find(author, title):
    """ Перевіряє чи міститься задана книга у бібліотеці. """
    idx = _hash(author)
    bucket = _table[idx]
    
    for pair in bucket:
        if pair[0] == author:
            return title in pair[1]
            
    return False

def delete(author, title):
    """ Видаляє книгу з бібліотеки. """
    idx = _hash(author)
    bucket = _table[idx]
    
    for i, pair in enumerate(bucket):
        if pair[0] == author:
            if title in pair[1]:
                pair[1].remove(title)
            if not pair[1]:
                bucket.pop(i)
            return

def findByAuthor(author):
    """ Повертає список книг заданого автора в алфавітному порядку. """
    idx = _hash(author)
    bucket = _table[idx]
    
    for pair in bucket:
        if pair[0] == author:
            return sorted(list(pair[1]))
            
    return []