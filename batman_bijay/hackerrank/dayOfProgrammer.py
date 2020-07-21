def dayOfProgrammer(year):
    day_of_programmer = None
    if (year < 1918):
        leap_yr = False
        if (year % 4 == 0):
            leap_yr = True
        day_of_programmer = calculate256thDay(leap_yr, year)
        return day_of_programmer
    elif(year == 1918):
        # (Jan + Feb 14th)32 + 14(remaining days in Feb) + Mar(31) + Apr(30) + May(31) + Jun(30) + Jul(31) + Aug(31) = 243
        days_to_subtract = 230
        days_till_256th_day = 256 - days_to_subtract
        return f"{days_till_256th_day}.09.{year}"
    else:
        leap_yr = False
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            leap_yr = True
        day_of_programmer = calculate256thDay(leap_yr, year)
        return day_of_programmer


def calculate256thDay(IsLeapYr, year):
    # For leap year:  Jan(31) + Feb(29) + Mar(31) + Apr(30) + May(31) + Jun(30) + Jul(31) + Aug(31) = 244;
    # For non-leap year:  Jan(31) + Feb(28) + Mar(31) + Apr(30) + May(31) + Jun(30) + Jul(31) + Aug(31) = 244;
    days_to_subtract = 244 if IsLeapYr else 243
    days_till_256th_day = 256 - days_to_subtract
    return f"{days_till_256th_day}.09.{year}"


res1 = dayOfProgrammer(1800)
res2 = dayOfProgrammer(1918)
res3 = dayOfProgrammer(2016)
res4 = dayOfProgrammer(2017)

print(f"res1: {res1}")
print(f"res2: {res2}")
print(f"res3: {res3}")
print(f"res4: {res4}")
