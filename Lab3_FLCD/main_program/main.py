from main_program.domain.ProgramInternalForm import PIF
from main_program.domain.Scanner import readFile, Scanner, reservedWords, separators, operators
from main_program.domain.SymbolTable import SymbolTable


def main():
    readFile()
    fileName = "p1.txt"
    st = SymbolTable(17)
    pif = PIF()
    scanner = Scanner()
    exceptionMessage = ""

    with open(fileName, 'r') as file:
        lineCounter = 0
        for line in file:
            lineCounter += 1
            for token in scanner.tokenize(line.strip()):
                if token in reservedWords+separators+operators:
                    if token == ' ':
                        continue
                    pif.add(token, (0, 0))
                elif scanner.isIdentifier(token) or scanner.isConstant(token):
                    id = st.add(token)
                    pif.add(token, id)
                else:
                    exceptionMessage += 'Lexical error at token ' + token + ', at line ' + str(lineCounter) + "\n"

    with open('st.out', 'w') as writer:
        writer.write(str(st))

    with open('pif.out', 'w') as writer:
        writer.write(str(pif))

    if exceptionMessage == '':
        print("Lexically correct")
    else:
        print(exceptionMessage)


main()