def is_prime(num):
    if num<=1:
        return False
    for i in range (2,num):
        if num%i==0:
            return False
    return True
def main():
    num=int(input("enter an number"))
    if is_prime(num):
        print("It is prime")
    else:
        print("It is not prime value")
main()
