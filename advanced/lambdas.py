def run():
    palindrome = lambda string: string == string[::-1]
    print(palindrome('ose'))
    suma = lambda a, b: a + b
    print(suma(5, 9))

if(__name__ == '__main__'):
    run()