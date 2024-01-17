year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

valueminusthree = year[-3]
print(f"Value at index -3: {valueminusthree}")

reversedyear = year[::-1]
print(f"\nOriginal order of Tuple: {year}")
print(f"\nReversed order of Tuple: {reversedyear}")

count2009 = year.count(2009)
print(f"\nNumber of times 2009 appears: {count2009}")

index2018 = year.index(2018)
print(f"\nIndex of 2018: {index2018}")

lengthtuple = len(year)
print(f"\nLength of the tuple: {lengthtuple}")