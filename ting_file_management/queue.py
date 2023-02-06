from ting_file_management.abstract_queue import AbstractQueue
# python3 -m pytest tests/test_queue.py

class Queue(AbstractQueue):
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = [] # criar uma lista ou list()

    def __len__(self): # tamanho da fila
        return len(self._data)

    def enqueue(self, value): # acrescenta no final da fila
        self._data.append(value)

    def dequeue(self):
        try:
            if len(self._data) != 0: # se o len for maior q 0, entao retira o primeiro elemento
                return self._data.pop(self.FIRST_ELEMENT)   
        except:
            return None

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]   
        raise IndexError
