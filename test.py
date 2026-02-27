#Bubble sort
data = []
n = int(input('Enter number of elements in unsorted list '))
for i in range(n):
    ele = int(input('Enter element ' + str(i) + '')) #indicate which element needs to be entered
    data += ele
#Dislpay the list
print('You entered:')
for i in data:
    print(i)

print()
#begin sort
for i in range(n-1): #passes
    for j in range(0,n-1-i): #swaps per pass
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]

#display sorted list
print('List after sorting ')
for i in data:
    print(i)