##Task1
def vow(str):
    vowel ="aeiou"
    count = 0
    for char in str.lower():
        if char in vowel:
            count+=1
    return count

print(vow("Hello"))

##Task2

def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0].lower() != s[-1].lower():
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("malayalam"))

##Task3
def power(base,exp):
    if exp ==0:
        return 1
    return base * power(base,exp -1)

print(power(2,2))

