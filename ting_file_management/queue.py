from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)   
        return None

    def search(self, index):
        try:
            if self._data:
                return self._data[self.index]   
            return None
        except IndexError:
            raise IndexError(f"Índice inválido") 
