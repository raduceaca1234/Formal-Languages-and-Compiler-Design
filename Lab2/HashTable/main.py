from collections import deque


class HashTable:

    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    def hashFunction(self, value):
        sum = 0
        for chr in value:
            sum += ord(chr) - ord('0')
        return sum % self.__size

    def add(self, value):
        self.__items[self.hashFunction(value)].append(value)

    def contains(self, value):
        return value in self.__items[self.hashFunction(value)]

    def remove(self, value):
        self.__items[self.hashFunction(value)].remove(value)

    def __str__(self) -> str:
        result = ""
        for i in range(self.__size):
            result = result + str(i) + "->" + str(self.__items[i]) + "\n"
        return result

    def getPosition(self, value):
        listPosition = self.hashFunction(value)
        listIndex = 0
        for item in self.__items[listPosition]:
            if item != value:
                listIndex += 1
            else:
                break
        return (listPosition, listIndex)


class SymbolTable:

    def __init__(self, size) -> None:
        self.__ht = HashTable(size)

    def __str__(self) -> str:
        return str(self.__ht)

    def add(self, value):
        self.__ht.add(value)

    def contains(self, value):
        return self.__ht.contains(value)

    def remove(self, value):
        self.__ht.remove(value)

    def getPosition(self, value):
        return self.__ht.getPosition(value)


if __name__ == '__main__':
    identifiers = ['a', 'b', 'ab', 'ba']
    constants = ['1', '2', '3', '"123"']
    everything = identifiers + constants
    size = 17

    st = SymbolTable(size)

    for x in everything:
        st.add(x)

    print(st)

    assert (st.getPosition('ab') == (14, 0))
    assert (st.getPosition('ba') == (14, 1))
    assert (st.contains('"123"') is True)
    print("Tests passed")
