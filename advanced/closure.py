from typing import Any


def enclosing_function(base: int) -> int:

    def nested_funtion(pow: int) -> int:
        return base**pow

    return nested_funtion

def make_repeater_of(n: int):
    def repeater(msg: int):
        try:
            assert type(msg) == str, "Solo se pueden repetir cadenas."
            return (msg + "\n") * n
        except AssertionError as e:
            return e.args[0]
    return repeater

def make_division_by(n: int):
    def division(x):
        return x/n
    return division

def run():
    base2 = enclosing_function(2)
    print(base2(5))
    print(base2(6))
    base5 = enclosing_function(5)
    print(base5(2))
    print(base5(3))
    repeater5 = make_repeater_of(5)
    print(repeater5(True))

    divisor3 = make_division_by(3)
    print(divisor3(21))
    mitad = make_division_by(2)
    print(mitad(10))

if __name__ == '__main__':
    run()