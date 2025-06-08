import sys
import operaciones as op


def writeFile(text:str, file:str):
    with open(file, 'a') as txt:
        txt.write(text)

if len(sys.argv)==3:
    n1, n2 = sys.argv[1], sys.argv[2]
    res = op.suma(n1, n2)
    writeFile(f'{n1} + {n2} = {res}\n', 'mi_test.txt')
else:
    sys.exit()