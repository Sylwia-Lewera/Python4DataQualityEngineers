"""
Write a code, which will:

1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""
import random
import string
# function used to create common dictionary from list of dictionaries generated
def create_common_dictionary(listOfDicts):
    commonDict = {}

    for dictionary_index, dictionary in enumerate(dictList):  # looping through enumerated list of dictionaries
        for key, value in dictionary.items():  # checking existing key, value pairs
            if key not in commonDict:
                commonDict[key] = value  # if key appears for the first time, it is added to the common dictionary
            else:
                if commonDict[key] < value:  # if key has another occurrence with bigger value
                    commonDict[key + '_' + str(
                        dictionary_index + 1)] = value  # original key is replaced, with new one and dic number
                    del commonDict[key]
    return commonDict


dictList = []  # list collection to store dictionaries created
dictNumber = random.randint(2, 10)  # selecting number of dictionaries to create
print("Number of dictionaries to add to the list:", dictNumber)

# for loop to create dictionaries with randomized content
for _ in range(dictNumber):
    dictElemCount = random.randint(2, 10)  # number of dictionary elements to create
    dictListItem = dict()  # dict collection to create dictionary for given iteration to append it to the list
    for _ in range(dictElemCount):
        # dictionary element creation with random letter key, and random int value
        dictListItem[random.choice(string.ascii_letters)] = random.randint(0, 100)

    dictList.append(dictListItem)  # adding created dictionary to the list

for item in dictList:
    print(item)

# Creating the common dictionary
commonDict = create_common_dictionary(dictList)

print("Common dictionary:", commonDict)
