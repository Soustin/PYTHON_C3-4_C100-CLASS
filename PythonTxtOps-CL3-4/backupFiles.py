import os
import shutil
source = input("Name of The Directory you want to backup --> ")
destination = input("Name of The Directory you want to backup the files in --> ")
source = source + '/'
destination = destination + '/'
listOfFiles = os.listdir(source)

for file in listOfFiles :
    shutil.copy((source + file), destination)