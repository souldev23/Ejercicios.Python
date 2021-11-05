from functools import reduce

my_list = [2, 2, 2, 2, 2]

def run():
    all_multi = reduce(lambda x, y: x * y, my_list)
    print(all_multi)

if __name__ == '__main__':
    run()