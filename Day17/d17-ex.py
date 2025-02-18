def vow(str):
    vowel ="aeiou"
    count = 0
    for char in str.lower():
        if char in vowel:
            a.append(char)
    return a

print(vow("Hello"))