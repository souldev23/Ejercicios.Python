class FibonacciSeries():
    def __init__(self, max: int) -> None:
        self.max = max

    def __iter__(self) -> None:
        self.n1 = 0
        self.n2 = 1
        self.iter = 2
        self.count = 0
        return self

    def __next__(self) -> int:        
        if(self.count == 0):
            self.count += 1
            return self.n1
        elif(self.count == 1):
            self.count += 1
            return self.n2
        else:
            if self.count >= self.max:
                raise StopIteration
            fibo =  self.n1 + self.n2            
            self.n1 = self.n2; self.n2 = fibo; self.count += 1
            return fibo

if __name__ == '__main__':
    fibonacci = FibonacciSeries(7)
    for element in fibonacci:
        print(element)