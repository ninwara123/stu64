# from os import name
from os import path
import os
from tkinter.constants import E
import pygame as pg
from object import Text, Button,InputBox
import time
# from tkinter import *
from tkinter import filedialog, mainloop
import shutil
import cv2
import upload_pic as ulp
from function import resize,pic

### init ###################################################################################################
pg.init()
win_x, win_y = 1280, 720
screen = pg.display.set_mode((win_x, win_y))

### color ###################################################################################################                                                                                                                                                   
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
light_gray = (230, 230, 230)
green = (0, 200, 0)
red = (200, 0, 0)
mint = (120,255,255)
orange = (242,157,0)

### creat object ###########################################################################################
#global

#login_page
register_btn = Button(729, 388 , 217, 87)
login_btn = Button(969, 388, 217, 87)
distance_box = InputBox(723, 273.3, 471,60,45,17)  # distance input box

#register_page
firstname_register = InputBox(695, 170, 472,49,35,12)  # distance input box
surname_register = InputBox(695, 257, 472,49,35,12)  # distance input box
nickname_register = InputBox(695, 351, 472, 49,35,12)  # spinner's speed input box
username_register = InputBox(695, 439, 472,49,35,12)  # distance input box
regis_sub_btn = Button(823, 533, 217,60)

uploadpic = Button(167,180,500-167,548-180)
take_pic = Button(225,291,200,68)
add_pic = Button(225,395,200,68)
repic_btn = Button(550,180,45,45)
clear_pic = Button(0,670,100,50)

# profile_page
option = Button(1202,13,63,63)
lesson_btn = Button(597,487,268,106)
practice_btn = Button(904,487,268,106)

#setting_page
a1 = Button(0,0,1023,720)
a2 = Button(1265,79,15,720)
a3 = Button(1023,0,242,112)
a4 = Button(1023,252,242,468)
edit_profile_btn = Button(1036,120,1256-1036,176-120)
logout_profile_btn = Button(1036,187,1256-1036,241-187)

#edit_profile_page
save_sub_btn = Button(823, 533, 217,60)

#back
back_page_btn = Button(13,13,59,59)
back_home_btn = Button(93,13,59,59)

#animal
animal_btn = Button(123,50,375,310)

#classroon
classroon_btn = Button(455,50,375,310)

#food
food_btn = Button(860,50,375,310)

#test
back_test_btn = Button(1130,100,63,63)
next_test_btn = Button(1200,100,63,63)

### variables #############################################################################################
wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
click = 0
regis_click = 0
input_registor = [surname_register,firstname_register,nickname_register,username_register]
input_boxes = [distance_box]
Article = [0,0] # no.Article , check change Article


memprofile = ['  ','  ','  ','  ','','','','',''] #username,surname,lastname,nickname,typeofpic,animalpass,classroompass,foodpass,forbug
# state variables
page = 'start'
newstatus = 0
take_pic_state = 0
add_pic_state = 0
user_status = 'nohave' 

#path
filepath = ""
user_data_path = 'C:/fra361_st4_voca_ui/user_data'

#words
animal_word_pack = [5,['Turtle','Starfish','Octopus','Jellyfish','Seahorse']]
classroon_word_pack  =  [6,['Calculator','Calendar','Magnifying Glass','Notice Board','Scissors']]
food_word_pack =  [7,['Noodle','Spaghetti','Cookies','Croissant','Lamonade']]
word_test = [] #memprofile , word 

# practice_green_btn = pg.image.load('C:/fra361_st4_voca_ui/ui_photo/practice_button.png')



### run code ###############################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
while(1):

    (pos_x, pos_y) = pg.mouse.get_pos()

    if page == 'start':
        screen.blit(ulp.first_page,(0,0))
        pg.display.update()
        pg.time.delay(2000)
        page = 'login'
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

##### CODE THIS PAGE END ####################################################################################

    elif page == 'login':
        screen.blit(ulp.login_page, (0,0))
        if wrong[2] == 1:
            t3 = Text(730,352, 30, "browallianewbold", (255,101,101), 1, 'Incorrect username')
            t3.draw(screen)
        if register_btn.mouse_on():
            screen.blit(ulp.register_green_btn, (728, 388))
            if pg.mouse.get_pressed()[0] == 1: #next state
                regis_click = 1
        if regis_click == 1 and pg.mouse.get_pressed()[0] == 0:
            regis_click = 0
            page = 'register'
            distance_box.text = "  "
            distance_box.txt_surface = distance_box.font.render(distance_box.text, True, pg.Color("black"))

        if distance_box.text == '  ': # ใส่เพราะแก้บัค
            t3 = Text(740, 290.3, 45, "browallianewbold", (192,192,192), 1, 'Username') #text username 
            t3.draw(screen)
        if distance_box.text == '  ' :
            login_btn_status = False
        elif distance_box.text != '  ' :
            wrong[2] = 0
            login_btn_status = True
        
        if login_btn.mouse_on():
            screen.blit(ulp.login_green_btn, (969, 388))
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if login_btn_status is True:  # เพิ่มกรณีที่ไม่มีไฟล์ด้วย 
                    wrong[2] = 0
                    
                    filenames = os.listdir(user_data_path)
                    for filename in filenames:
                        if distance_box.text+'.txt' == filename:
                            user_status = 'have'
                    if  user_status == 'have' :     
                        file = open('user_data/'+distance_box.text+".txt","r")

                        for i in file:
                            u_n,f_n,s_n,n_n,t_p,animal_pass,classroom_pass,food_pass,fix_bug = i.split(",")
                            memprofile = [u_n,f_n,s_n,n_n,t_p,animal_pass,classroom_pass,food_pass,fix_bug]
                            
                            click = 1


                        file.close()

                    print('memprofile')
                    print(memprofile)
                    if user_status == 'nohave' :  
                        wrong[2] = 1
                    
                if distance_box.text == '  ':
                    wrong[2] = 1 
                    please = True  # get error message

        if click == 1 and pg.mouse.get_pressed()[0] == 0:
            click = 0
            distance_box.text = "  "
            distance_box.txt_surface = distance_box.font.render(distance_box.text, True, pg.Color("black"))
            page = "profile"

        if regis_click == 1 and pg.mouse.get_pressed()[0] == 0:
            regis_click = 0
            page = 'register'

        distance_box.draw(screen)

        pg.display.update()
        for event in pg.event.get():
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()

##### CODE THIS PAGE END ####################################################################################
    
    elif page == 'register':
        screen.blit(ulp.register_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_btn,(16,12))
            if pg.mouse.get_pressed()[0] == 1:
                for n in range (len(input_registor)):
                    input_registor[n].text = "  "
                    input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                r_btn_status = False
                newstatus = 0
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "login"
                click =0

        if username_register.text == '  '  or firstname_register.text == '  ' \
            or surname_register.text == '  ' or nickname_register== '  ':
                r_btn_status = False
        if username_register.text != '  ' and firstname_register.text != '  ' \
            and surname_register.text != '  ' and nickname_register!= '  ':
            r_btn_status = True
            wrong[1] = 0



        if uploadpic.mouse_on() and newstatus == 0: # ลากเม้าไปโดน blit รูป add picture
            screen.blit(ulp.add_pic_btn,(128,150))
            if take_pic.mouse_on():
                if pg.mouse.get_pressed()[0] == 1: 
                    take_pic_state = 1
                screen.blit(ulp.take_pic_btn,(224,289))
            while take_pic_state == 1:
                takephoto = cv2.VideoCapture(0)
                ret, frame = takephoto.read()
                cv2.imshow('video',frame)
                if (cv2.waitKey(1) & 0xFF == 13):
                    cv2.imwrite("temp_data/capture.png",frame)
                    take_pic_state = 0
                    newstatus = 1
                    # C:/fra361_st4_voca_ui/temp_data
                    filepath = "C:/fra361_st4_voca_ui/temp_data/capture.png"
                    takephoto.release()
                    cv2.destroyAllWindows()
            if add_pic.mouse_on():  #กดถ่ายรูปแล้ว upload รูป
                screen.blit(ulp.upload_pic_btn,(224,393))
                if pg.mouse.get_pressed()[0] == 1:
                    filepath=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",\
                    filetypes=(('JPG file','*.jpg'),('PNG file','*.png'))) # เลือกดึงรูปจาก computer เฉพาะ JPG,PNG
                    print("\n file path ########## \n")
                    print(filepath)
                    newstatus = 1
                    re_pic = 1
                    r_btn_status = True  
                    add_pic_state = 0 
                else:
                    add_pic_state = 0  

        if newstatus == 1: #เปลงไฟลภาพให้พอดีกับกรอบรูป ##function
            image = cv2.imread(filepath)
            Profile_pic = pg.image.load(filepath)
            [h,w,d] = image.shape
            if h>w:
                ww = int(398*(w/h))
                hh = 440
                jj = int((398-(398*w/h))/2)
                kk = 0
            if w>h:
                ww = int(398)
                hh = int(440*(h/w))
                jj = 0
                kk = int((440-(440*h/w))/2)
            screen.blit(ulp.bgwhite,(128,150))
            screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))


        if regis_sub_btn.mouse_on(): #กดปุ่ม register ทำการสร้างไฟล์ ข้อมูลของแต่ละ User
            screen.blit(ulp.register_green_btn, (823,533)) #600, 680, 260, 80
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if r_btn_status == True :
                    if newstatus ==1:
                        newpath = shutil.copy(filepath,"user_data")
                        not_use , typefi = newpath.split(".")
                    if newstatus ==0:
                        typefi = 'png'
                        newpath = shutil.copy(ulp.defualt_user_pic_path,"user_data")
                    # f = open(path_to_file, mode)
                    file = open('user_data/'+username_register.text+".txt","w")
                    file = open('user_data/'+username_register.text+".txt","a")
                    file.write("'"+username_register.text+"','"+firstname_register.text+"','"+\
                        surname_register.text+"','"+nickname_register.text+","+typefi+",0,0,0,""\n")               
                    file.close() 
                    if newstatus == 1:
                        if typefi == 'png':
                            os.rename(newpath,'user_data/'+username_register.text+'.png') 

                        elif typefi == 'jpg':
                            os.rename(newpath,'user_data/'+username_register.text+'.jpg')

                    if newstatus == 0:
                        os.rename(newpath,'user_data/'+username_register.text+'.png') 

                    for n in range (len(input_registor)):
                            input_registor[n].text = "  "
                            input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                    newstatus = 0
                    re_pic = 0
                    click = 1
                    # wrong[1] == 0
                if r_btn_status == False:
                    wrong[1] = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "login"
                click =0

        if wrong[1] == 1: #ติดปัญหาเด้งขึ้น
            t1 = Text(800-6,503, 30, "browallianewbold", (255,101,101), 1, 'Please enter all information')
            t1.draw(screen)


        for box in input_registor: 
            box.draw(screen)
        pg.display.update()
        for event in pg.event.get():
            for box in input_registor:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()

##### CODE THIS PAGE END ####################################################################################

    elif page == "profile" :
        screen.blit(ulp.profile_page,(0,0))

        userName = memprofile[1].replace("'","").replace(" ","")
        userSurName = memprofile[2].replace("'","").replace(" ","")
        userNickName = memprofile[3].replace("'","").replace(" ","")
        userFullName = userName+"  "+userSurName
        t3 = Text(743, 216, 45, "browallianewbold", (0,0,0), 1, userFullName)
        t4 = Text(810, 294, 45, "browallianewbold", (0,0,0), 1, userNickName)
        filepath = 'C:/fra361_st4_voca_ui/user_data/'+str(memprofile[0].replace("'",""))+"."+str(memprofile[4])
        pic_show_data = pic(filepath,400,440)

        screen.blit(pg.transform.scale(pic_show_data[4],(pic_show_data[0],pic_show_data[1])),(85+pic_show_data[2],155+pic_show_data[3])) 
        t3.draw(screen)
        t4.draw(screen)



        if lesson_btn.mouse_on():
            screen.blit(ulp.lesson_green_btn,(597,487))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if practice_btn.mouse_on():
            # screen.blit(ulp.p_g_b(904,487))
            # screen.blit(ulp.practice_green_btn(904,487))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'practice'
                click =0
        ####################################################################################################################### 
        if option.mouse_on() :                  #---------setting
            backpage = "profile"                # แสดงรูปภาพ
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                # backpage = "profile"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "profile"
                click =0
        ####################################################################################################################### 


        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

##### CODE THIS PAGE END ###################################################################################

    elif page =="setting" :
        (pos_x, pos_y) = pg.mouse.get_pos() # ถ้าเม้ากดยังจุดใดก็ตามที่ไม่ใช้ในกล่อง setting ให้กลับไปยัง state ก่อนหน้า like : pop-up
        case1 = a1.x <= pos_x <= a1.x + a1.w and a1.y <= pos_y <= a1.y + a1.h
        case2 = a2.x <= pos_x <= a2.x + a2.w and a2.y <= pos_y <= a2.y + a2.h
        case3 = a3.x <= pos_x <= a3.x + a3.w and a3.y <= pos_y <= a3.y + a3.h
        case4 = a4.x <= pos_x <= a4.x + a4.w and a4.y <= pos_y <= a4.y + a4.h
        screen.blit(ulp.all_setting_btn,(1023,12)) 
        if (case1 or case2 or case3 or case4 ) :
            if pg.mouse.get_pressed()[0] == 1  :
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = backpage
                click =0
            # pg.time.delay(5)
        if edit_profile_btn.mouse_on() and backpage !="edit_profile" : # กดเม้าไปยัง edit profile สร้างตัวแปรของหน้า edit profile
            screen.blit(ulp.edit_profile_secl_btn,(1034,122))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                m1  = memprofile[1].replace("'","")
                m2  = memprofile[2].replace("'","")
                m3  = memprofile[3].replace("'","")
                m0  = memprofile[0].replace("'","")
                firstname_register1 = InputBox(695, 170, 472,49,35,14,m1)  # distance input box
                surname_register1 = InputBox(695, 257, 472,49,35,14,m2)  # distance input box
                nickname_register1 = InputBox(695, 351, 472, 49,35,14,m3)  # spinner's speed input box
                username_register1 = InputBox(695, 439, 472,49,35,12,m0)
                edit_member = [surname_register1,firstname_register1,nickname_register1]
                newstatus = 1
                page = "edit_profile"
                click =0
        if logout_profile_btn.mouse_on():
            screen.blit(ulp.logout_profile_secl_btn,(1034,186))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "logout"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    elif page =="logout":
        memprofile=["","","","","",""]
        # wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        logout_status = 1
        page = "login"

##### CODE THIS PAGE END ###################################################################################

    elif page == "edit_profile":  
        
        # backpage =""
        # screen.blit(edit_profile_ui,(0,0))
        screen.blit(ulp.edit_profile_page,(0,0))
        if newstatus == 1:
            image = cv2.imread(filepath)
            Profile_pic = pg.image.load(filepath)
            [h,w,d] = image.shape
            if h>w:
                ww = int(398*(w/h))
                hh = 440
                jj = int((398-(398*w/h))/2)
                kk = 0
            if w>h:
                ww = int(398)
                hh = int(440*(h/w))
                jj = 0
                kk = int((440-(440*h/w))/2)
            screen.blit(ulp.bgwhite,(128,150))
            screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))

        t5 = Text(695, 439+13, 35, "browallianewbold", (0,0,0), 1, m0)
        t5.draw(screen)

        if option.mouse_on() :   #---------setting
            backpage = "edit_profile"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                # backpage = "edit_profile"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        
            
        if firstname_register1.text == '  ' or surname_register1.text == '  ' or nickname_register1== '  ':
                r_btn_status = False
        if firstname_register1.text != '  ' and surname_register1.text != '  ' and nickname_register1 != '  ':
            r_btn_status = True

        if save_sub_btn.mouse_on():
            screen.blit(ulp.save_green_btn, (823,522)) #600, 680, 260, 80
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if r_btn_status == True :
                    click =1
                    user_file_name = memprofile[0].replace("'","")
                    file = open('user_data/'+user_file_name+".txt","r+")
                    file.write(memprofile[0]+",'"+firstname_register1.text+"','"+surname_register1.text+"','"+nickname_register1.text+"',"+memprofile[4]+","+memprofile[5]+","+memprofile[6]+","+memprofile[7]+",")          
                    file.close() 
                    file = open('user_data/'+user_file_name+".txt","r")
                    for i in file:
                        u_n,f_n,s_n,n_n,t_p,animal_pass,classroom_pass,food_pass,fix_bug = i.split(",")
                        memprofile = [u_n,f_n,s_n,n_n,t_p,animal_pass,classroom_pass,food_pass,fix_bug]
                    
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        
        if back_page_btn.mouse_on():
            # print(" hold ")
            screen.blit(ulp.back_page_green_btn,(16,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page =  back_page_state
                # page = "profile"
                click =0
        # else :
        #     screen.blit(edit_profile_ui,(0,0))

        for box in edit_member:
            box.draw(screen)
            
        if option.mouse_on() :   #---------setting
            backpage = "edit_profile"
            screen.blit(ulp.all_setting_btn,(1023,12))  
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                backpage = "edit_profile"
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        pg.display.update()
        for event in pg.event.get():
            for box in edit_member:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit() 


##### CODE THIS PAGE END ####################################################################################

    elif page == 'lesson':
        screen.blit(ulp.lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "lesson"
                click =0

        if animal_btn.mouse_on():
            # print('animal_btn')
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'animal_lesson'
                click =0


        if classroon_btn.mouse_on():
            # print('classroon_btn')
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'classroon_lesson'
                click =0

        if food_btn.mouse_on():
            # print('food_btn')
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'food_lesson'
                click =0

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'animal_lesson':
        print('animal_lesson')
        screen.blit(ulp.animal_lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "animal_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "animal_lesson"
                click =0

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'classroon_lesson':
        print('classroon_lesson')
        screen.blit(ulp.classroon_lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "classroon_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "classroon_lesson"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'food_lesson':
        print('food_lesson')
        screen.blit(ulp.food_lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "food_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "food_lesson"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

##### CODE THIS PAGE END ###################################################################################

    elif page == 'practice':
        screen.blit(ulp.practice_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "practice"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "practice"
                click =0

        if animal_btn.mouse_on():
            
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                
                page = 'test_practice'
                word_test = animal_word_pack
                Article[0] = int(memprofile[word_test[0]])
                click =0


        if classroon_btn.mouse_on():
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'test_practice'
                word_test = classroon_word_pack
                Article[0] = int(memprofile[word_test[0]])
                click =0

        if food_btn.mouse_on():
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'test_practice'
                word_test = food_word_pack
                Article[0] = int(memprofile[word_test[0]])
                click =0

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'test_practice':
        
        screen.blit(ulp.test_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "practice"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "test_practice"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "test_practice"
                click =0

        if Article[0] > 0:
            if back_test_btn.mouse_on():
                if pg.mouse.get_pressed()[0] == 1:
                    click = 1
                if pg.mouse.get_pressed()[0] == 0 and click ==1:
                    Article[1] = 1
                    Article[0] -= 1
                    
                    click =0
        if Article[0] < 4:
            if next_test_btn.mouse_on():
                if pg.mouse.get_pressed()[0] == 1:
                    click = 1
                if pg.mouse.get_pressed()[0] == 0 and click ==1:
                    
                    Article[1] = 1
                    Article[0] += 1
                    
                    click =0
        if Article[1] == 1 :
            memprofile[word_test[0]] = str(Article[0])
            Article[1] = 0

            user_file_name = memprofile[0].replace("'","")
            file = open('user_data/'+user_file_name+".txt","r+")
            file.write(memprofile[0]+","+memprofile[1]+","+memprofile[2]+","+memprofile[3]+","+memprofile[4]+","\
                +memprofile[5]+","+memprofile[6]+","+memprofile[7]+",")          
            file.close() 
            file = open('user_data/'+user_file_name+".txt","r")
            for i in file:
                u_n,f_n,s_n,n_n,t_p,animal_pass,classroom_pass,food_pass,fix_bug = i.split(",")
                memprofile = [u_n,f_n,s_n,n_n,t_p,animal_pass,classroom_pass,food_pass,fix_bug]
            # print(memprofile)
                    

        # print('Article')
        # print(Article)
        # print('memprofile[word_test[0]]')
        # print(memprofile[word_test[0]])
        t3 = Text(500,300, 80, "browallianewbold", red, 1, word_test[1][Article[0]]) #text username 
        t3.draw(screen)

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 