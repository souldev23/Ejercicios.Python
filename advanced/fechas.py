from datetime import datetime as dt

def run() -> None:
    my_datetime = dt.now()
    print(my_datetime)
    my_str = my_datetime.strftime('%d/%m/%Y %H:%M:%S.%f')
    print(f'Fecha completa LATAM: {my_str}')
    my_str = my_datetime.strftime('%m/%d/%Y %H:%M:%S')
    print(f'Fecha completa USA: {my_str}')

if __name__ == '__main__':
    run()

