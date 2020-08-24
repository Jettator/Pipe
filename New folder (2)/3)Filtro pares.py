import sys
numero = sys.stdin.readline()
for i in numero:
    if int(i)%2 ==0:
        sys.stdout.write(str(i))
    else:
        sys.stdout.write("no es par")
