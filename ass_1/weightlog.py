#######################################
# This is a weight log book programe
# which you tpye in the weight and it
# spit out the Avg. weight and Typed in one
#######################################


LstofUserWeight=[]
userinput=input("What's your current weight?")

import csv
with open('weightlog.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(userinput)
    csvfile.close()

import csv
with open('weightlog.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        LstofUserWeight.append(float(srow))
    csvfile.close()

print("Your Average Weight is "+str(sum(LstofUserWeight)/len(LstofUserWeight))+" Kg.")
print("Your current weight is "+str(userinput)+" Kg.")


