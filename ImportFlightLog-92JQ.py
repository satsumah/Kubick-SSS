# 0, ID
# 1, AircraftID
# 2, FlightDate
# 3, StartingHobbs
# 4, EndingHobbs
# 5, HobbsHours
# 6, StartingTach
# 7, EndingTach
# 8, TachHours
# 9, LFCycles
# 10, RCycles
# 11, Landings
# 12, FlightTypes
# 13, Notes
# 14, Initials
# 15, DateEntered

import csv
from datetime import date, timedelta, datetime

def peek(f):
    pos = f.tell()
    line = f.readline()


# These can stay the same
today = date.today()
d1 = today.strftime("%m/%d/%Y")
print("d1 = ", d1)
logentries = []

# Change these before running
startingEntry = 0
aircraftID = 1
infile = 'N92JQ.csv'
outfile = 'output-92JQ.csv'

with open(infile, newline='') as csvfile:
    csvreader = csv.reader(csvfile, quotechar='"')
    next(csvreader)
    for row in csvreader:
        if row[3] == '':
            break
        try:
            startingEntry = startingEntry + 1
            if row[0] == '':
                flightDateObject = datetime.strptime(flightDate, '%m/%d/%Y')
                flightDateObject += timedelta(days=1)
                flightDate = flightDateObject.strftime('%m/%d/%Y')
            else:    
                flightDate = row[0]
            startingHobbs = float(row[2].strip().replace(',',''))
            endingHobbs = float(row[3].strip().replace(',',''))
            hobbsHours = ''
            startingTach = 0
            endingTach = 0
            tachHours = 0
            lFCycles = row[4]
            rCycles = row[5]
            landings = row[6]
            flightTypes = "Initial Entries"
            notes = row[14]
            initials = "ZZ-Import"
            dateEntered = d1

            logentries.append([
                startingEntry,
                aircraftID,
                flightDate,
                startingHobbs,
                endingHobbs,
                hobbsHours,
                startingTach,
                endingTach,
                tachHours,
                lFCycles,
                rCycles,
                landings,
                flightTypes,
                notes,
                initials,
                dateEntered]
            )
        
        except TypeError as err:
            print("Invalid typing - {0}".format(err))
        except ValueError as err:
            print("Bad data passed - {0}".format(err))

with open(outfile, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in logentries:
        csvwriter.writerow(row)