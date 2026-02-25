#counting even numbers from 1 to n
def count_even(n):
    count=0
    for i in range(1,n+1):
        if i%2==0:
            count +=i
    return count

def main():
    n=int(input("enter a number"))
    print("even count:",count_even(n))
main()


#counting positive numbers
def count_pos(numbers):
    count=0
    for num in numbers:
        if num>0:
            count +=1
    return count
def main():
    numbers=[1,-2,-10,4,3]
    print("positive numbers:",count_pos(numbers))
main()


#fee calculator:

def calculator(course, marks):
    course = course.strip().lower()

    if course == "ai":
        fee = 40000
    elif course == "bi":
        fee = 50000
    elif course == "ci":
        fee = 60000
    else:
        print("Invalid course")
        return None

    if marks > 90:
        print("Discount applied: 5000")
        fee -= 5000

    return fee


def main():
    course = input("Enter course (AI/BI/CI): ")

    try:
        marks = int(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Please enter marks between 0 and 100")
            return

        total_fee = calculator(course, marks)

        if total_fee is not None:
            print("Final Fee:", total_fee)

    except ValueError:
        print("Please enter valid numeric marks")


main()
