import os
from time import sleep

print(os.getcwd())
os.chdir(r"C:\Users\vdi-student\Desktop")
print(os.getcwd())
os.mkdir('BigData')
sleep(2)
os.rename('Bigdata', 'Nowy')
sleep(2)
os.rmdir('Nowy')

os.system("cmd \c 'dir'")