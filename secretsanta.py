# Purpose of the program is to assign secret santas without anybody receiving themselves 

import random 

# secretSanta: (NonNegative > 1) --> Dictionary
def secretSanta(n):
    listofpeople = [x for x in range(1, n + 1)]
    random.shuffle(listofpeople)
    length = len(listofpeople)
    onethirdlength = length//3
    twothirdlength = (2*length)//3
    partition1 = listofpeople[0:onethirdlength]
    partition2 = listofpeople[onethirdlength:twothirdlength]
    partition3 = listofpeople[twothirdlength:length]
    secret_dict = {}
    for i in range(0, (length//3)):
        secret_dict[partition1[i]] = partition2[i]
        secret_dict[partition2[i]] = partition3[i]
        secret_dict[partition3[i]] = partition1[i]
    if ((length - 1) % 3 == 0):             # If this is the case, partition3 has an additional element
        secret_dict[partition3[onethirdlength]] = partition1[0]
        secret_dict[partition3[0]] = partition3[onethirdlength]
    elif ((length - 2) % 3 == 0):        # If this is the case, partitions 2 and 3 have an additional element
        secret_dict[partition2[onethirdlength]] = partition3[onethirdlength]
        secret_dict[partition3[onethirdlength]] = partition2[onethirdlength]
    for i in range(1, n + 1):
        print("Number", i, "has to get a gift for Number", secret_dict[i])
    return secret_dict

secretSanta(20)
