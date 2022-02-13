"""
Test del método fibonacci de la clase Recursiva

>>> recursivo = Recursiva()
>>> recursivo.fibonacci(5)
120
"""

class Recursiva:
    def fibonacci(self, num):
        if num==0:
            return 1
        else:
            return num * self.fibonacci(num-1)