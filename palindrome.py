def palindrome(str):
    
    if str[::1]==str[::-1]:
        return True
    else:
        return False
str="loil"
print(palindrome(str))
    