import os

print('yes or no')
shutdown = input('Do you wish to shutdown your computer? ')

if (shutdown == 'no'):
    exit()
else:
    os.system('shutdown /s /t 1')