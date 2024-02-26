def minimum_coins(num, coins_list):
    result = 0
    ordered_coins = coins_list.sort(reverse = True)
    #Con éste comando se ordena la lista
    for coin in coins_list:
        while num >= coin:
            local_result = int(float(num) / float(coin))
            result = result + local_result
            num = num - (coin * local_result)

    return result

elements = []
#Define una lista

amount = int(input("Enter the amount: "))
elements_number = int(input("Enter number of elements on the array: "))

for i in range(0,elements_number):
    element = int(input())
    elements.append(element)

#print(elements)
if (elements_number == 0):
    print(0)
if (elements_number == 1):
    print([0])
minimum_coins_array = minimum_coins(amount,elements)
print(minimum_coins_array)
