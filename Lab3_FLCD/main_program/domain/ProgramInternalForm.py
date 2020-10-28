class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def addToken(self, token, pos):
        self.__content.append((token, pos))

    def __str__(self):
        result = ""
        for pair in self.__content:
            result += 'Token ' + pair[0] + " and Position: " + str(pair[1])  + "\n"
        return result
