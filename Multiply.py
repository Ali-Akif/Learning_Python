"""module Multiply contain table function"""

def table(nb, max=10):
    """
    Table show multiplication by nb from 1 * nb to max * nb
    """
    i = 0
    while i < max:
        i+=1
        print(i,"*",nb,"=", i * nb)

    
if __name__ == "__main__":
    table(4)
    input("push enter to exit")
