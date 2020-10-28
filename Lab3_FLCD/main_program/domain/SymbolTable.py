from collections import deque


class SymbolTable:

    def __init__(self, size):
        self.__ht = HashTable(size)

    def __str__(self) -> str:
        return str(self.__ht)

    def add(self, key):
        return self.__ht.add(key)

    def contains(self, key):
        return self.__ht.contains(key)

    def remove(self, key):
        self.__ht.remove(key)

    def getPosition(self, key):
        return self.__ht.getPosition(key)


class HashTable:

    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    def hash(self, key):
        sum = 0
        for chr in key:
            sum += ord(chr) - ord('0')
        return sum % self.__size

    def add(self, key):
        if self.contains(key):
            return self.getPosition(key)
        self.__items[self.hash(key)].append(key)
        return self.getPosition(key)

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    def __str__(self):
        result = ""
        for i in range(self.__size):
            result = result + str(i) + "->" + str(self.__items[i]) + "\n"
        return result

    def getPosition(self, key):
        listPosition = self.hash(key)
        listIndex = 0
        for item in self.__items[listPosition]:
            if item != key:
                listIndex += 1
            else:
                break
        return listPosition, listIndex
