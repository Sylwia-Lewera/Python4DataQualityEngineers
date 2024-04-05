"""
1.create list of 100 random numbers from 0 to 1000
2. sort list from min to max(without using sort())
3. calculate average for even and odd numbers
4. print both average result in console
Each line of code should be commented with description.
"""
import random


def bubble_sort(arr):
    """
function for sorting list element in ascending order using bubble sort algorithm
    :type arr: list to sort in ascending order
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


randList = []  # list for storing random numbers generated

for i in range(101):  # loop to create list of 100 elements
    randList.append(random.randint(0, 1000))  # adding random number from 0 to 1000 to the list
bubble_sort(randList)  # sorting list from min to max
print(randList)  # printing sorted list

# calculate average for even and odd numbers
evenNumbers = [x for x in randList if x % 2 == 0]  # list to store even elements of list generated
evenAvg = sum(evenNumbers) / len(evenNumbers)  # calculate average of even list elements
print("even list elements average", evenAvg)
oddNumbers = [x for x in randList if x % 2 == 1]  # list to store odd elements of list generated
oddAvg = sum(oddNumbers) / len(oddNumbers)  # calculate average of odd list elements
print("odd list elements average", oddAvg)
