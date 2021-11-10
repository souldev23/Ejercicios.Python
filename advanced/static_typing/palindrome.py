def isPalindrome(word:str) -> bool:
    word = word.lstrip().rstrip().lower()

    return word == word[::-1]

def run():
    print(isPalindrome("Ana "))
    print(isPalindrome())

if __name__ == '__main__':
    run()
