
def palindromo(sentence):
    """
    Retorna verdadero si el enunciado es un palindromo, y false en caso contrario.

    sentence -> String or Int

    >>> palindromo("Anita lava la tina")
    True

    >>> palindromo("12321")
    True

    >>> palindromo("Hola mundo")
    False
    """
    sentence = str(sentence).lower().replace(' ', '')
    return sentence == sentence[::-1]

# Si deseamos usar directamente el doctest al ejecutar el archivo como 
# py docstring.py -v
# Se desplegara el detalle de las pruebas, además se pueden ejecutar pruebas de archivos externos usando
# el método testfule() por ejemplo: doctest.testfile("doctest.txt")
if __name__=='__main__':
    import doctest
    doctest.testmod()
        