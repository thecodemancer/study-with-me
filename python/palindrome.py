def is_palindrome(str):
    clean_str = str.replace(" ","").lower().replace(".","").replace(",","")
    if clean_str[::-1] == clean_str:
        return True
    else:
        return False

str = "Hello"  #False
output = is_palindrome(str)
print(output)
str = "racecar"  #True
output = is_palindrome(str)
print(output)
str = "A man, a plan, a canal, Panama" #True
output = is_palindrome(str)
print(output)
