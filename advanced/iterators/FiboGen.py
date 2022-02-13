from time import sleep

def fibonacci_gen(max: int) -> int:
    a, b = 0, 1
    while True:
        if(a > max):
            return a

        yield a
        a, b = b, a+b

if __name__ == "__main__":
    fibonacci = fibonacci_gen(7)
    for element in fibonacci:
        print(element)
        sleep(1)