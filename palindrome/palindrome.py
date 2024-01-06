def is_palindrome(string):
    string = string.lower()
    length = len(string)
    for i in range(length//2):
        if string[i] != string[length - 1 - i]:
            return False
    return True

# Much more efficent solution found on StackOverflow
def is_palindrome2(string):
    return string == string[::-1]