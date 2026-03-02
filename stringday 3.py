#counting characters in string
def count_char(text):
    count = 0
    for char in text:
        count += 1
    return count
def main():
    text=input("enter the character :")
    print("char count:",count_char(text))
main()
        
#counting the vowels in the strings
def vowel(text):
    count=0
    vowels="aeiouAEIOU"
    for char in text:
        if char in vowels:
            count+=1
    return count
def main():
    text=input("enter name:")
    print("vowels:",vowel(text))
main()
        
def rev(text):
   return text[::-1]
def main():
    text=input("enter name:")
    print("reversing:",rev(text))
main()
