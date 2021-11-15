import csv
x = 4
x = "userdata_test"+str(x)
# keys = ['name', 'age', 'job', 'city']
 #username,surname,lastname,nickname,typeofpic,animalpass,classroompass,foodpass,forbug
header = ['username', 'firstname', 'surname', 'nickname','type_of_pic','animal_hold_p','animal_pass','classroom_hold_p','classroom_pass','food_hold_p','food_pass']
# data = [
#     ['Albania+++++++++', 28748, 'AL', 'ALB'],
#     ['Algeria+++++++++', 2381741, 'DZ', 'DZA'],
#     ['American Samoa+++++++++++', 199, 'AS', 'ASM'],
#     ['Andorra++++++++', 468, 'AD', 'AND'],
#     ['Angola+++++++++++', 1246700, 'AO', 'AGO']
# ]

with open('user_data/'+x+'.csv', 'w') as f:
    f.close()
# with open('user_data/'+x+'.csv', 'r+', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write multiple rows
#     writer.writerows(data)


keys = ['username', 'firstname', 'surname', 'nickname','type_of_pic','animal_hold_p','animal_pass','classroom_hold_p','classroom_pass','food_hold_p','food_pass']
# keys =[]
rows = [
        {
        'username' : 'q', 
        'firstname': 'waraset' , 
        'surname': 'wongsawat', 
        'nickname' : 'nin',
        'type_of_pic'  : '.jpg',
        'animal_hold_p' :0,'classroom_hold_p':0,'food_hold_p':0,
        'animal_pass':1,'classroom_pass':2,'food_pass':2
        }
        ,
        {'animal_pass':0,'classroom_pass':0,'food_pass':0}
        ,{'animal_pass':0,'classroom_pass':0,'food_pass':0}
        ,{'animal_pass':0,'classroom_pass':0,'food_pass':0}
        ,{'animal_pass':0,'classroom_pass':0,'food_pass':0}
        ]

with open('user_data/'+x+'.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()    # add column names in the CSV file
    writer.writerows(rows)



# f = open('user_data/'+x+'.csv')
# f.close()

# # check closed status
# print(f.closed)

# with open('user_data/'+x+'.csv') as f:
#     reader = csv.reader(f)
#     # next(reader)
#     for row in reader:
#         print(row)

memprofile = []
hold_p = []
test_pass =[]

with open('user_data/'+x+'.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    print(csv_reader)
    for line_no, line in enumerate(csv_reader, 1):
        
        # print(line_no)
        # print(line) 
        if line_no == 1:
            print('Header:')
            # print(line[0:5])  # header
            # memprofile = line[0:5]
            # print(memprofile)
            print('Data:')
        elif line_no == 2:
            hold_p = line[5]
            test_pass.append(line[6:11:2])
            print(type(hold_p))

        else:
            test_pass.append(line[6:11:2])
            # print(line) 
        # print("test pass")
        # print(test_pass)