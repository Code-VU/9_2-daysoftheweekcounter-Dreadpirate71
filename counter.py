
def countDayOfTheWeek():
    # This first line is provided for you
    countEmails = dict()
    words = []
    days = []
    file_name = input("Enter a file name: ")  
    try:
        file_hand = open(file_name)
    except:
        print("Unable to open file:", file_name)
    for line in file_hand:
        days = []
        if line.startswith("From "):
            words = line.split()
            days.append(words[2])
            for day in days: 
                countEmails[day] = countEmails.get(day, 0) + 1
            print (countEmails)
            continue
# end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countDayOfTheWeek()