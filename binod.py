patch-1
import os    #The OS module in python provides functions for interacting with the operating system


def checkBinod(file):       #this function will check there is any 'Binod' text in file or not
    with open(file, "r") as f: #we are opening file in read mode and using 'with' so need to take care of close()
=======
import time
import os
#Importing our Bindoer
print("To Kaise Hai Ap Log!")
time.sleep(1)
print("Chaliye Binod Karte Hai!")
def checkBinod(file):#Trying to find Binod In File Insted Of Manohar Ka Kotha
    with open(file, "r") as f:
        master
        fileContent = f.read()
    if 'binod' in fileContent.lower():
        print(
            f'**************Congratulations Binod found in {f}********************')
        return True


if __name__ == '__main__':
    ans = False
    print("************binod Detector********************")
    dir_contents = os.listdir()
    for item in dir_contents:
        if item.endswith('txt'):
            ans = checkBinod(item)
            if(ans is False):
                print('Binod not found Try Looking In Manohar Ka Kotha!!')