monday = float(input("enter the total number of steps you take on monday\n"))
tuesday = float(input("enter the total number of steps you take on tuesday\n"))
wednesday = float(input("enter the total number of steps you take wednesday\n"))
summary = monday + tuesday + wednesday
average = summary/3
print(f"the total steps take from monday, tuesday and wednesday is {summary} and the average i walked is {average}")
