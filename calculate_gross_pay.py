hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter Rate: ")
rate = float(rate)
if hrs <= 40:
    print(hrs*rate)
else:
    print(rate*40+(hrs-40)*rate*1.5)
