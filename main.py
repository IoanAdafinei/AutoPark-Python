from car import Car

try:
    with open('date.in') as file:
        fullFile = file.read()
except FileNotFoundError:
    print("File not found")

newFile = fullFile.split()

numberOfCars = len(newFile)

marca = newFile[0]
model = newFile[1]
token = newFile[2]
pretCumparare = newFile[3]
pretVanzare = newFile[4]
cars = [Car(marca, model, token, pretCumparare, pretVanzare)]

for i in range(5, numberOfCars, 5):
    marca = newFile[i]
    model = newFile[i + 1]
    token = newFile[i + 2]
    pretCumparare = newFile[i + 3]
    pretVanzare = newFile[i + 4]
    cars.append(Car(marca, model, token, pretCumparare, pretVanzare))

cars.sort(key = lambda x: (x.marca, x.model, x.token))

# with open('date.out', 'w') as file:
#     for i in range(0, int(numberOfCars / 5)):
#         file.write(cars[i].marca)
#         file.write(' ')
#         file.write(cars[i].model)
#         file.write(' ')
#         file.write(cars[i].token) 
#         file.write(' ')
#         file.write(cars[i].pretCumparare)
#         file.write(' ')
#         file.write(cars[i].pretVanzare)
#         file.write('\n')

k = 1
sum = 0

with open('date.out', 'w') as file:
    for i in range(0, int(numberOfCars / 5 - 1)):
        if cars[i].marca == cars[i+1].marca:
            k += 1
        else:
            file.write(cars[i].marca)
            file.write(" ")
            file.write(str(k))
            file.write('\n')
            sum += k
            k = 1
    file.write(cars[-1].marca)
    file.write(' ')
    file.write(str(int(numberOfCars / 5) - sum))
    file.write('\n')


try:
    with open('marci.in') as file:
        marciFile = file.read()
except FileNotFoundError:
    print("File not found")

fileMarca = marciFile.split()

profit = 0

for i in fileMarca:
    for item in cars:
        if item.marca == i:
            profit += int(item.pretVanzare) - int(item.pretCumparare)
    cars = [item for item in cars if item.marca != i]

newNumberOfCars = len(cars)

with open('date.out', 'a') as file:
    for i in range(0, int(newNumberOfCars)):
        file.write(cars[i].marca)
        file.write(' ')
        file.write(cars[i].model)
        file.write(' ')
        file.write(cars[i].token) 
        file.write(' ')
        file.write(cars[i].pretCumparare)
        file.write(' ')
        file.write(cars[i].pretVanzare)
        file.write('\n')
    file.write(str(profit))