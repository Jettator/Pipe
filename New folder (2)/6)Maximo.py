import sys
array = []
y = 0
n = sys.stdin.readline()
for i in n:
    y += int(i)
    array.append(y)
    sys.stdout.write(str(y))
z = max (array)
sys.stdout.write("El maximo valor: " + format (str(b)))
sys.stdout.write(" ")
