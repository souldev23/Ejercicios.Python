#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_types = [0, 0, 0, 0, 0]
    for bird in arr:
        bird_types[bird-1] = bird_types[bird-1] + 1
    print(bird_types)
    max = 0
    index = 0
    aux = 0
    for type in bird_types:
        if aux==0:
            max=type
            index=aux
            aux=aux+1
        else:
            if type>max:
                max=type
                index=aux
                aux=aux+1
            else:
                aux=aux+1
    print(f"Max:{index+1}")

if __name__=='__main__':
    migratoryBirds([1, 4, 4, 4, 5, 3])
