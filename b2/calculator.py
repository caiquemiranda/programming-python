operation = input("""
                  Please type in the math operation you would like to complete:
                  + for addiction
                  - for subtraction
                  / for division 
                  * for division
                  """)

n_1 = int(input('Enter your first number: '))
n_2 = int(input('Enter your second number: '))

print(f'{n_1}+{n_2} = {n_1 + n_2}')
print(f'{n_1}-{n_2} = {n_1 - n_2}')
print(f'{n_1}/{n_2} = {n_1 / n_2}')
print(f'{n_1}*{n_2} = {n_1 * n_2}')