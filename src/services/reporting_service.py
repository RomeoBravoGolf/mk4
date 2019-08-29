import os
import csv
import datetime

def report(time):
    ans = {}
    for filename in os.listdir("../out/"):
        date = datetime.datetime.strptime(filename[:-4], '%Y-%m-%d_%H:%M:%S')
        if date < time:
            with open("../out/"+filename) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[0] in ans.keys():
                        ans[row[0]] = ans[row[0]] + row[1]
                    else:
                        ans[row[0]] = row[1]
            os.remove(filename)
