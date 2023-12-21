import sys

o = sys.argv[1:]


for i in range(1, len(o) + 1):
    print(sys.argv[i])


for i in sys.argv[1:]:
    print(i)