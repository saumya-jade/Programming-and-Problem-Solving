day=int(input())
month=int(input())
year=int(input())
def leap(y):
    return(y%4==0 and y%100!=0)or(y%400==0)
if year<=0 or month<1 or month>12:
    print("Invalid Date")
else:
    if month in [1,3,5,7,8,10,12]:
        md=31
    elif month in [4,6,9,11]:
        md=30
    else:
        md=29 if leap(year) else 28
    if day<1 or day>md:
        print("Invalid Date")
    else:
        day+=1
        if day>md:
            day=1
            month+=1
            if month>12:
                month=1
                year+=1
        print(f"{day:02d}-{month:02d}-{year}")
