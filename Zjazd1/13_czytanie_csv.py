print('1. Czytanie pliku csv')
path = 'rozliczenie.csv'
mode = 'r'
# path = r'C:\Users\vdi-student\Desktop\BigData2425\Zjazd1\rozliczenie.csv'
# path = 'C:\\Users\\vdi-student\\Desktop\\BigData2425\\Zjazd1\\rozliczenie.csv'

with open(path, mode) as file1:
    content = file1.readlines()
print(content)
for i in range(len(content)):
    content[i] = content[i].split(',')

print('\n2. Średnia wyplata')
total = 0
for line in content[1:]:
    total += int(line[1])
print(f'W sumie wszyscy zarabiają: {total}')
print(f'Średnia wypłata to:  {round(total/(len(content)-1),2)}')

print('\n3. Ile jest Pań na macierzynskim?')
counter = 0
for line in content[1:]:
#    if line[4] == 't\n' or line[4] == 't':
    if line[4][0].lower() == 't' and line[3] == 'k':
        counter += 1
print(f'Liczba Pań na macierzyńkim: {counter}')



# avg = sum(number_list)/len(number_list)

# from statistics import mean
# number_list = [45, 34, 10, 36, 12, 6, 80]
# avg = mean(number_list)