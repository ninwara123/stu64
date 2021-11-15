# str="ABC"
# if str.find("A")!=-1 and str.find("B")!=-1:
#   print("Found the string")
# else:
#   print("Not found!!!")

# print(str.find("A"))
progress_percent = 0.00
progress_point = 0
test_pass = ['A','AD','ED' ]

if test_pass[0] != '' or test_pass[1] != '' or test_pass[2] != '':
    progress_percent = 0.00
    progress_point = 0
    for n in range(3):
        if test_pass[n].find("A") != -1 :
            progress_point += 1
        if test_pass[n].find("B") != -1 :
            progress_point += 1
        if test_pass[n].find("C") != -1 :
            progress_point += 1
        if test_pass[n].find("D") != -1 :
            progress_point += 1
        if test_pass[n].find("E") != -1 :
            progress_point += 1
    progress_percent = round(((progress_point/15)*100),2)

print(progress_percent)
# print(int(progress_percent))