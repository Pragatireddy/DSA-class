def star_pattern(n):
    for i in range (1,n+1):
        for j in range(n): 
            print("*",end=" ")
        print()
def main():
    n=int(input("enter a number :"))
    star_pattern(n)
main()


def star_pattern(n):
    for i in range (1,n+1):
        for j in range(1,n+1):
            if j>=i:
                print(" ",end=" ")
            else:
                print("*", end=" ")
        print()
def main():
    n=int(input("enter a number :"))
    star_pattern(n)
main()

