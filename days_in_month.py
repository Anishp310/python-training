#import stdin

month=input("enter the name of the month : ")

month="month".lower()

if (month == "january" or "march"
    or "may" or "july" or "august"
    or "october" or "december"):
    print("31")

elif(month == "february"):
    print("28")

elif(month == ("april" or "june" or "september" or "november")):
    print("30")

else:
    print("invalid choice")