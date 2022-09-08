num = int(input('How many numbers sum you want? : '))

if (num < 0):
    print('Enter a positive number: ')
    
else:
    sum = 0
    while(num > 0):
        sum += num
        num -+ 1
        print(f'The sum is :{sum}')