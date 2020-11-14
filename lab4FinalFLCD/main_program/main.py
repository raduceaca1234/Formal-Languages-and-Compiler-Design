import re

from main_program.domain.ProgramInternalForm import ProgramInternalForm
from main_program.domain.Scanner import readFile, Scanner, reservedWords, separators, operators
from main_program.domain.SymbolTable import SymbolTable
from main_program.domain.FiniteAutomata import FiniteAutomata


class Main:

    def __init__(self):
        self.st = SymbolTable(17)
        self.pif = ProgramInternalForm()
        self.scanner = Scanner()
        self.cases = ["=+", "<+", ">+", "<=+", ">=+", "!=+", "=-", "<-", ">-", "<=-", ">=-", "==-", "!=-"]

    def run(self):
        readFile()
        fileName = "data/p1.txt"
        exceptionMessage = ""
        faConstant = FiniteAutomata.readFromFile('data/constant.in')
        faIdentifier = FiniteAutomata.readFromFile('data/identifier.in')

        with open(fileName, 'r') as file:
            lineCounter = 0
            for line in file:
                lineCounter += 1
                tokens = self.scanner.tokenize(line.strip())
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reservedWords + separators + operators:
                        if tokens[i] == ' ':  # ignore adding spaces to the pif
                            continue
                        self.pif.addToken(tokens[i], (-1, -1))
                    elif tokens[i] in self.cases and i < len(tokens) - 1:
                        print(tokens[i])
                        if re.match("[1-9]", tokens[i + 1]):
                            print(tokens[i][:-1])
                            self.pif.addToken(tokens[i][:-1], (-1, -1))
                            extra = tokens[i][-1]
                            print(extra)
                            continue
                        else:
                            exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                                lineCounter) + "\n"
                    elif faIdentifier.isAccepted(tokens[i]):
                        id = self.st.add(tokens[i])
                        self.pif.addToken("identifier", id)
                    elif faConstant.isAccepted(tokens[i]):
                        print(tokens[i])
                        const = self.st.add(extra + tokens[i])
                        extra = ''
                        self.pif.addToken("constant", const)
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            lineCounter) + "\n"

        with open('data/st.out', 'w') as writer:
            writer.write(str(self.st))

        with open('data/pif.out', 'w') as writer:
            writer.write(str(self.pif))

        if exceptionMessage == '':
            print("Lexically correct")
        else:
            print(exceptionMessage)


main = Main()
main.run()
