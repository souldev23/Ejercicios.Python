def dayOfProgrammer(year):
    # Write your code here
    print(year%100)
    if year>1919 or year%4==0:
        return f'12.09.{year}'
    elif (year%4==0 and year%400==0) and not year%100==0:
        return f'13.09.{year}'
    else:
        return f'13.09.{year}'

if __name__=='__main__':
    print(dayOfProgrammer(1917))