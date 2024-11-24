path = 'rozliczenie.csv'
mode = 'r'
# path = r'C:\Users\vdi-student\Desktop\BigData2425\Zjazd1\rozliczenie.csv'
# path = 'C:\\Users\\vdi-student\\Desktop\\BigData2425\\Zjazd1\\rozliczenie.csv'

with open(path, mode) as file1:
    content = file1.readlines()
print(content)
for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3])
print(content[3][4])


