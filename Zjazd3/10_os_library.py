import os
import time

print('Hej')
time.sleep(2)
print(f'aktualnie w: {os.getcwd()}')
os.chdir(r'C:\Users\vdi-belfer\Desktop')
print(f'aktualnie w: {os.getcwd()}')
try:
    os.mkdir('test')
except FileExistsError:
    print('Folder istnieje')
time.sleep(2)
os.rename('test', 'TEST')
time.sleep(2)
os.rmdir('TEST')

os.system('cmd /c "ipconfig /all >> info.txt"')
