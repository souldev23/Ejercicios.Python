def read():
    my_list = []
    with open('archivos/listado.txt','r', encoding='utf-8') as f:
        for line in f:
            my_list.append(int(line))
    print(my_list)

def write():
    persons = ['Saúl', 'Iker', 'Pedro', 'Santiago', 'Yesica', 'Samatha']
    with open('archivos/nombres.txt', 'w', encoding='utf-8') as f:
        for name in persons:
            f.write(name + "\n")

def run():
    write()

if __name__ == '__main__':
    run()