import sys
a = 0
n = sys.stdin.readline()
for i in n:
    a+=int(i)
    sys.stdout.write(str(a))
    sys.stdout.write(" ")
