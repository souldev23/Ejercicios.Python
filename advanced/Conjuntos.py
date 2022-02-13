my_set1 = {7, 4, 6, 3, 23, 54}
my_set2 = {5, 7, 9, 6, 18, 37}

def union() -> set:
    return my_set1 | my_set2

def intersection() -> set:
    return my_set1 & my_set2

def difference(setA: set, setB: set) -> set:
    return setA - setB

def symmetric_diff() -> set:
    return my_set1 ^ my_set2

def run():
    print(union())
    print(intersection())
    print(difference(my_set1, my_set2))
    print(difference(my_set2, my_set1))
    print(symmetric_diff())

if __name__ == '__main__':
    run()