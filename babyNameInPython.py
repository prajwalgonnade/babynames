import os, datetime, urllib, zipfile

downloadStartTime = datetime.datetime.now() #Recording start time of download
  
urllib.urlretrieve("http://www.ssa.gov/oact/babynames/state/namesbystate.zip", 'babyname.zip') #Downloading the data zip file from URL

downloadEndTime = datetime.datetime.now() #Recording end time of download

downloadSpan = downloadEndTime - downloadStartTime #Calculate total download time

size = os.path.getsize("babyname.zip") #Get size of the data zip file

internetSpeed = (size/(1000*1000))/downloadSpan.total_seconds() #Calculating internet download speed in MBPS units

if (internetSpeed < 1 ): #Checking internet download speed.. Should be greater than 1MBPS
    print ("Internet is slow, download speed is " + str(round(internetSpeed,2)) + " MBPS")
else:
    print ("Great.. download speed is " + str(round(internetSpeed,2)) + " MBPS")
    
zipOpen = open('babyname.zip', 'rb') #Open the file to read in binary mode
unzip = zipfile.ZipFile(zipOpen) #Read and write the datazip file

for name in unzip.namelist():
    outpath = os.getcwd() + '/babyname/' #Output directory for Zip extract
    unzip.extract(name, outpath) #Extract data zip file
zipOpen.close() #Close the zipOpen file object

dirName=r"./babyname" #Specify path of the directory where files are extracted
nameDict ={} #Dictonary where names will be collected from all the files
namedictM ={} #Dictionary where Male names will be collected from all the files for year 2013
namedictF ={} #Dictionary where Female names will be collected from all the files for year 2013
namedictCommon = {} #Names which are common in both the Male and Female

startTime=datetime.datetime.now() #Recording start time of the script

for fileName in os.listdir(dirName): #Listing all the files in the directory 
    if ".TXT" in fileName.upper(): #Convert all filenames to upper case and check if condition for text files
        filePath= None 
        filePath = dirName + "\\" + fileName
        with open(filePath) as f: #Traversing Each line in a file
            lines = f.readlines() #Reading file content line by line
            for line in lines:
                tmp =[]
                tmp = line.rstrip('\n').split(",") #Taking out the name from the line
                if nameDict.has_key(str(tmp[3])) == True:
                    nameDict[str(tmp[3])] = nameDict[str(tmp[3])]+int(tmp[4]) #If the name is repeated then increment the count 
                else:
                    nameDict[str(tmp[3])] = int(tmp[4]) #If new entry for Name, add it in dictionary 
                   
                if (str(tmp[1])=="M" and str(tmp[2])=="2013"):
                    if namedictM.has_key(str(tmp[3])) == True:# Checking Male members in 2013
                        namedictM[str(tmp[3])] = int(namedictM[str(tmp[3])])+ int(tmp[4]) #If the name is repeated then add it to the count 
                    else:
                        namedictM[str(tmp[3])]= int(tmp[4]) #If new entry for Name, add it in Male dictionary
                elif (str(tmp[1])=="F" and str(tmp[2])=="2013"):# Checking Female members in 2013
                    if namedictF.has_key(str(tmp[3])) == True:
                        namedictF[str(tmp[3])] = int(namedictF[str(tmp[3])])+ int(tmp[4]) #If the name is repeated then add it to the count 
                    else:
                        namedictF[str(tmp[3])]= int(tmp[4]) #If new entry for Name, add it in Female dictionary
                        
        f.close() #Close the file object

popularName = [key for key,val in nameDict.iteritems() if val == max(nameDict.values())] #Finding maximum value for the name

for key in namedictM: #Ierating over Male member
    if namedictF.has_key(key) == True: #Checking whether Male name is present in Female name
        #namedictCommon[key] = int(namedictF[key])+ int(namedictM[key]) #If the name is found then add the count 
         namedictCommon[key] = abs(int(namedictF[key]) - int(namedictM[key])) # Take absolute value of the difference between Male and Female Count
 
Names = sorted(namedictCommon, key=namedictCommon.get, reverse=False)  # Sorting dictionary and storing first 5 names     

print "Most popular baby name is : %s with %s occurences"%((str(popularName),nameDict[str(popularName[0])]))
print "Top 10 most ambiguous name in 2013 are :"
print "%s with difference %s and with %s Females and %s Males"%(Names[0],namedictCommon[Names[0]],namedictF[Names[0]],namedictM[Names[0]])
print "%s with difference %s and with %s Females and %s Males"%(Names[1],namedictCommon[Names[1]],namedictF[Names[1]],namedictM[Names[1]])
print "%s with difference %s and with %s Females and %s Males"%(Names[2],namedictCommon[Names[2]],namedictF[Names[2]],namedictM[Names[2]])
print "%s with difference %s and with %s Females and %s Males"%(Names[3],namedictCommon[Names[3]],namedictF[Names[3]],namedictM[Names[3]])
print "%s with difference %s and with %s Females and %s Males"%(Names[4],namedictCommon[Names[4]],namedictF[Names[4]],namedictM[Names[4]])
print "%s with difference %s and with %s Females and %s Males"%(Names[5],namedictCommon[Names[5]],namedictF[Names[5]],namedictM[Names[5]])
print "%s with difference %s and with %s Females and %s Males"%(Names[6],namedictCommon[Names[6]],namedictF[Names[6]],namedictM[Names[6]])
print "%s with difference %s and with %s Females and %s Males"%(Names[7],namedictCommon[Names[7]],namedictF[Names[7]],namedictM[Names[7]])
print "%s with difference %s and with %s Females and %s Males"%(Names[8],namedictCommon[Names[8]],namedictF[Names[8]],namedictM[Names[8]])
print "%s with difference %s and with %s Females and %s Males"%(Names[9],namedictCommon[Names[9]],namedictF[Names[9]],namedictM[Names[9]])

'''
print "Top 5 most ambiguous name in 2013 are :"
print "%s with %s occurances"%(Names[0],namedictCommon[Names[0]])
print "%s with %s occurances"%(Names[1],namedictCommon[Names[1]])
print "%s with %s occurances"%(Names[2],namedictCommon[Names[2]])
print "%s with %s occurances"%(Names[3],namedictCommon[Names[3]])
print "%s with %s occurances"%(Names[4],namedictCommon[Names[4]])
'''
endTime=datetime.datetime.now()#Recording end time of the script
span = endTime -startTime #Calcuting execution run time
print "Execution time for script : %s"%span