def computepay(h, r):
    if h <= 40:
        return (h*r)
    else:
        return (40*r+(h-40)*r*1.5)
hrs = input("Enter hours: ")
hrs = float(hrs)
rate = input("Enter rate: ")
rate = float(rate)
print("Pay: ", computepay(hrs, rate))
