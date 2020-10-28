from main_program.domain.ProgramInternalForm import ProgramInternalForm
from main_program.domain.Scanner import readFile, Scanner, reservedWords, separators, operators
from main_program.domain.SymbolTable import SymbolTable


def main():
    readFile()
    fileName = "data/p1.txt"
    st = SymbolTable(17)
    pif = ProgramInternalForm()
    scanner = Scanner()
    exceptionMessage = ""

    with open(fileName, 'r') as file:
        lineCounter = 0
        for line in file:
            lineCounter += 1
            for token in scanner.tokenizeFunction(line.strip()):
                if token in reservedWords+separators+operators:
                    if token == ' ':
                        continue
                    pif.addToken(token, (0, 0))
                elif scanner.checkIfIdentifier(token) or scanner.checkIfConstant(token):
                    id = st.add(token)
                    pif.addToken(token, id)
                else:
                    exceptionMessage += 'Lexical error at token ' + token + ', at line ' + str(lineCounter) + "\n"

    with open('data/st.out', 'w') as writer:
        writer.write(str(st))

    with open('data/pif.out', 'w') as writer:
        writer.write(str(pif))

    if exceptionMessage == '':
        print("No lexical errors")
    else:
        print(exceptionMessage)


main()