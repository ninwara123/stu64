# project_path = 'C:/fra361_st4_voca_ui'
project_path = 'D:/stu64'

# from os import name
from os import path, read
import os
from tkinter.constants import E
import pygame as pg
from pygame.draw import rect
from object import Text, Button,InputBox,user
import time
from tkinter import filedialog, mainloop                                                                     
import shutil
import cv2
import upload_pic as ulp
from function import resize,pic
import face_recognition as face
import numpy as np
import csv
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import pyaudio

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
red = (250, 0, 0)
mint = (120,255,255)
orange = (242,157,0)
### creat object ###########################################################################################
#global
u1 = user()
micc = True
#login_page
register_btn = Button(729, 388 , 217, 87)
login_btn = Button(969, 388, 217, 87)
distance_box = InputBox(723, 273.3, 471,60,45,17,0)  # distance input box
#register_page
firstname_register = InputBox(695, 170, 472,49,35,12,1)  # distance input box
surname_register = InputBox(695, 257, 472,49,35,12,1)  # distance input box
nickname_register = InputBox(695, 351, 472, 49,35,12,1)  # spinner's speed input box
username_register = InputBox(695, 439, 472,49,35,12,0)  # distance input box
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
animal_btn = Button(123,125,375,310)
#animal_lesson
a1 = Button(148,527,161,129)
a2 = Button(449,113,114,203)
a3 = Button(455,520,73,158)
a4 = Button(879,146,274,309)
a5 = Button(930,554,308,114)
#classroon
classroon_btn = Button(455,125,375,310)
#classroom_lesson
p1 = Button(94,250,189,138)
p2 = Button(344,366,36,48)
p3 = Button(459,633,64,44)
p4 = Button(743,560,69,39)
p5 = Button(1024,214,104,123)
#food
food_btn = Button(860,125,375,310)
#food_lesson
n1 = Button(208,260,560-208,440-260)
n2 = Button(100,500,480,220)
n3 = Button(650,290,870-650,480-290)
n4 = Button(650,500,250,220)
n5 = Button(940,263,210,535-263)
#test
redu_btn = Button(1056,100,63,63)
back_test_btn = Button(1130,100,63,63)
next_test_btn = Button(1200,100,63,63)
correct_btn = Button(800,250,400,400)
back_to_lesson = Button(172,12,66,66)
### variables #############################################################################################
enter_press = 0
click = 0
regis_click = 0
login_click = 0
pro_correct = 0
progress_percent = 0.00
progress_point = 0
csv_member_list = []
boi_state = 0
sound_count = 0
pic_i_run = []
#list
wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
input_registor = [surname_register,firstname_register,nickname_register,username_register]
input_boxes = [distance_box]
EXAMNO = [0,0] # no.EXAMNO , check change EXAMNO
memprofile = []    # 'username', 'firstname', 'surname', 'nickname','type_of_pic'
hold_p = ['0','0','0']        # 'animal_hold_p','classroom_hold_p','food_hold_p'
test_pass =['','','']      # 'animal_pass','classroom_pass','food_pass'
point_pass = ['','','']
# state variables
page = 'start'
newstatus = 0
practice_pass = 0 
take_pic_state = 0
add_pic_state = 0
user_status = 'nohave' 
pass_test_flag = 0
mark_pass = ''
pic_i_test_object = []
#path
filepath = ""
user_data_path = project_path +'/user_data'

#words
animal_word_pack = [0,['Turtle','Starfish','Octopus','Jellyfish','Seahorse']]
classroon_word_pack  =  [1,['Calculator','Calendar','Magnifying Glass','Notice Board','Scissors']]
food_word_pack =  [2,['Omelette','Spaghetti','Cookies','Croissant','Lemonade']]
word_test = [] #no.set , word 

#test 
type_test_inputbox = InputBox(393,530,494,61,50,12,1)
animal_boxes = [type_test_inputbox]
animal_key_check_button = Button(1000,600,280,120)
animal_key_check_i = 0

### face recognition #####################################################################
capper = True
txt_member_list = []
csv_list = []
mempicture_list = []
user_image = []
user_face_encoding = []
known_face_encodings = []
known_face_names = []
mmmmooo = []
is_human = 0
k = 0
text_check = 3
call_name = 1
### run code ###############################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
while(1):
    (pos_x, pos_y) = pg.mouse.get_pos()

##### CODE START PAGE #######################################################################################
    if page == 'start':
        screen.blit(ulp.first_page,(0,0))
        pg.display.update()
        pg.time.delay(2000)
        filenames = os.listdir(user_data_path)
        for filename in filenames:
            if '.csv' in filename:
                # print(filename)
                csv_list.append(filename)
                user_data_file = open('user_data/'+filename,'r', encoding="utf8")
                reader = csv.reader(user_data_file)
                for row in reader:
                    memprofile = row[0:6]
                    # print(memprofile)
                    if memprofile[5] == '1':
                        txt_member_list.append(filename)
                user_data_file.close()
        # print(len(txt_member_list))
        if len(txt_member_list) == 0:
            page = "login"
        else:
            page = 'login'
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

##### CODE SCAN PAGE #########################################################################################
    elif page == 'scan':
        for o in range(len(txt_member_list)):
            file_name,type_file = txt_member_list[o].split(".")
            user_data_file = open('user_data/'+file_name+'.csv','r', encoding="utf8")
            reader = csv.reader(user_data_file)
            for row in reader:
                memprofile = row[0:6]
                mempicture_list.append(file_name+"."+memprofile[4])
            user_data_file.close()
        #ใบหน้าคนที่ต้องการรู้จำเป็นreference #คนที่1
        for i in range(len(txt_member_list)):
            # print(i)
            file_name,type_file = txt_member_list[i].split(".")
            # print(file_name+"\n"+type_file)
            try:
                known_face_encodings.append(face.face_encodings(face.load_image_file("user_data/"+mempicture_list[i]))[0])
                known_face_names.append(file_name)
            except:
                continue
        face_locations = []
        face_encodings = []
        face_names = []
        face_percent = []
        # print(known_face_names)
        video_capture = cv2.VideoCapture(0) 
        while capper == True:
            k += 1 
            print(page,k)
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0,0), fx=0.3,fy=0.3)
            rgb_small_frame = small_frame[:,:,::-1]
            face_names = []
            face_percent = []
            face_locations = face.face_locations(rgb_small_frame, model="cnn")
            face_encodings = face.face_encodings(rgb_small_frame, face_locations)
            for face_encoding in face_encodings:
                face_distances = face.face_distance(known_face_encodings, face_encoding)
                best = np.argmin(face_distances)
                face_percent_value = 1-face_distances[best]
                if face_percent_value >= 0.5:
                    name = known_face_names[best]
                    filenames = os.listdir(user_data_path)
                    for filename in filenames:
                        if name+'.csv' == filename:
                            user_status = 'have'
                    if  user_status == 'have' :     
                        user_data_file = open('user_data/'+file_name+'.csv','r', encoding="utf8")
                        reader = csv.reader(user_data_file)
                        for row in reader:
                            memprofile = row[0:6]
                            hold_p = row[6:9]
                            test_pass = row[9:12]
                        user_data_file.close()
                    capper = False
                    page = "profile"

                    print("findddddd")
            if k >= 5:
                page = "login"
                capper = False
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

##### CODE LOGIN PAGE ########################################################################################
    elif page == 'login':
        screen.blit(ulp.login_page, (0,0))
        if wrong[4] == 1 and distance_box.active != True:
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
            login_btn_status = True
        if (login_btn.mouse_on() or enter_press == 1) :
            screen.blit(ulp.login_green_btn, (969, 388))
            if (pg.mouse.get_pressed()[0] == 1 or enter_press == 1)and csv_list != []:  # button get click
                enter_press = 0
                if login_btn_status is True:  # เพิ่มกรณีที่ไม่มีไฟล์ด้วย 
                    if  u1.SerchLogin(distance_box.text) == 'have' : 
                        click = 1   
                        wrong[4] = 0 
                    else :  
                        wrong[4] = 1
                if distance_box.text == '  ':
                    wrong[4] = 1 
                    please = True  # get error message
        if click == 1 and pg.mouse.get_pressed()[0] == 0:
            click = 2
            memprofile,hold_p,test_pass,point_pass = u1.ReadData(distance_box.text)
            
        if regis_click == 1 and pg.mouse.get_pressed()[0] == 0:
            regis_click = 0
            wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            page = 'register'
        if click == 2 :
            output = gTTS(text="สวัสดีน้อง"+memprofile[3],lang="th",slow=False)
            output.save("s/login_name"+memprofile[0]+".mp3")
            
            click = 0
            distance_box.text = "  "
            distance_box.txt_surface = distance_box.font.render(distance_box.text, True, pg.Color("black"))
            page = "profile"
            call_name = 1
        distance_box.draw(screen)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_RETURN:    
                    enter_press = 1 
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()

##### CODE REGISTER PAGE #####################################################################################
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
                wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                    is_human = 1
                    newstatus = 1
                    filepath = project_path+'/temp_data/capture.png'
                    takephoto.release()
                    cv2.destroyAllWindows()
            if add_pic.mouse_on():  #กดถ่ายรูปแล้ว upload รูป
                screen.blit(ulp.upload_pic_btn,(224,393))
                if pg.mouse.get_pressed()[0] == 1:
                    filepath=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",\
                    filetypes=(('JPG file','*.jpg'),('PNG file','*.png'))) # เลือกดึงรูปจาก computer เฉพาะ JPG,PNG
                    is_human = 1
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
        path = project_path+'/user_data'
        filenames = os.listdir(path)
        for filename in filenames:
            if '.csv' in filename:
                x1,x2 = filename.split(".")
                csv_member_list.append(x1)
        if username_register.text in csv_member_list  :
            wrong[3] = 1
        if username_register.text not in csv_member_list:
            wrong[3] = 0
        if wrong[3] == 1 and click == 0 :
            t1 = Text(820, 411, 30, "browallianewbold", red, 1, 'Username is already used') #text username 
            t1.draw(screen)
        if regis_sub_btn.mouse_on(): #กดปุ่ม register ทำการสร้างไฟล์ ข้อมูลของแต่ละ User
            screen.blit(ulp.register_green_btn, (823,533)) #600, 680, 260, 80
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if r_btn_status == True and wrong[3]== 0:
                    if newstatus ==1:
                        newpath = shutil.copy(filepath,"user_data")
                        not_use , typefi = newpath.split(".")
                    if newstatus ==0:
                        typefi = 'png'
                        newpath = shutil.copy(ulp.defualt_user_pic_path,"user_data")
                        is_human = 0
                    memprofile = [username_register.text, firstname_register.text, surname_register.text, nickname_register.text,typefi,is_human]
                    hold_p = ['0','0','0']
                    test_pass = ['','','']
                    point_pass = ['','','']
                    u1.WriteData(memprofile,hold_p,test_pass,point_pass)
                    if newstatus == 1:
                        if typefi == 'png':
                            os.rename(newpath,'user_data/'+username_register.text+'.png') 
                        elif typefi == 'jpg':
                            os.rename(newpath,'user_data/'+username_register.text+'.jpg')
                    if newstatus == 0:
                        os.rename(newpath,'user_data/'+username_register.text+'.png') 
                    newstatus = 0
                    re_pic = 0
                    click = 1
                    # wrong[1] == 0
                if r_btn_status == False:
                    wrong[1] = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "login"
                click =0
                for n in range (len(input_registor)):
                    input_registor[n].text = "  "
                    input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

##### CODE PROFILE PAGE ######################################################################################
    elif page == "profile" :
        screen.blit(ulp.profile_page,(0,0))
        userFirstName = memprofile[1]
        userSurName = memprofile[2]
        userNickName = memprofile[3]
        userFullName = userFirstName+"  "+userSurName
        t3 = Text(743, 216, 45, "browallianewbold", (0,0,0), 1, userFullName)
        t4 = Text(810, 294, 45, "browallianewbold", (0,0,0), 1, userNickName)
        filepath = project_path+'/user_data/'+str(memprofile[0])+"."+str(memprofile[4])
        pic_show_data = pic(filepath,400,440)
        screen.blit(pg.transform.scale(pic_show_data[4],(pic_show_data[0],pic_show_data[1])),(85+pic_show_data[2],155+pic_show_data[3])) 
        t3.draw(screen)
        t4.draw(screen)
        pg.draw.rect(screen,green,(797,361,int(355*(progress_percent/100)),48))
        t_percent = Text(935,370, 45 , "browallianewbold", black, 1, str(progress_percent)) #text username 
        t_percent.draw(screen)
        if lesson_btn.mouse_on():
            screen.blit(ulp.lesson_green_btn,(597,487))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if practice_btn.mouse_on():
            screen.blit(ulp.p_g_b,(904,487))
            # screen.blit(ulp.practice_green_btn(904,487))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            elif pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'practice'
                click =0
        ####################################################################################################################### 
        if option.mouse_on() :                  #---------setting
            backpage = "profile"                # แสดงรูปภาพ
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "profile"
                click =0
        ####################################################################################################################### 
        pg.display.update()
        if call_name == 1:
            playsound(project_path+"/s/login_name"+memprofile[0]+".mp3")
            call_name = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        ##### CALCULATE PERCENT PROGRESS #############################################################################
        progress_percent = 0.00
        progress_point = 0
        for n in range(3):
            if point_pass[n].find("A") != -1 :
                progress_point += 1
            if point_pass[n].find("B") != -1 :
                progress_point += 1
            if point_pass[n].find("C") != -1 :
                progress_point += 1
            if point_pass[n].find("D") != -1 :
                progress_point += 1
            if point_pass[n].find("E") != -1 :
                progress_point += 1
        progress_percent = round(((progress_point/15)*100),2)

##### CODE SETTING PAGE ######################################################################################
    elif page =="setting" :
        (pos_x, pos_y) = pg.mouse.get_pos() # ถ้าเม้ากดยังจุดใดก็ตามที่ไม่ใช้ในกล่อง setting ให้กลับไปยัง state ก่อนหน้า like : pop-up
        case1 = Button(0,0,1280,110)
        case2 = Button(0,111,1025,720-111)
        case3 = Button(1026,254,1280-1026,720-254)
        screen.blit(ulp.all_setting_btn,(1023,12)) 
        if (case1.mouse_on() or case2.mouse_on() or case3.mouse_on()) :
            if pg.mouse.get_pressed()[0] == 1  :
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = backpage
                click =0
        if edit_profile_btn.mouse_on() and backpage !="edit_profile" : # กดเม้าไปยัง edit profile สร้างตัวแปรของหน้า edit profile
            screen.blit(ulp.edit_profile_secl_btn,(1034,122))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                m1  = memprofile[1].replace("'","")
                m2  = memprofile[2].replace("'","")
                m3  = memprofile[3].replace("'","")
                m0  = memprofile[0].replace("'","")
                firstname_register1 = InputBox(695, 170, 472,49,35,14,1,m1)  # distance input box
                surname_register1 = InputBox(695, 257, 472,49,35,14,1,m2)  # distance input box
                nickname_register1 = InputBox(695, 351, 472, 49,35,14,1,m3)  # spinner's speed input box
                username_register1 = InputBox(695, 439, 472,49,35,12,0,m0)
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

##### CODE LOGOUT PAGE #######################################################################################
    elif page =="logout":
        memprofile=[]
        wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        page = "start"
        logout_status = 1
        txt_member_list = []
        mempicture_list = []
        known_face_encodings = []
        known_face_names = []
        txt_member_list = []
        mempicture_list = []
        k = 0
        capper = True
        call_name = 1

##### CODE EDIT_PROFILE PAGE #################################################################################
    elif page == "edit_profile":  
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
            if pg.mouse.get_pressed()[0] == 1:
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
                    row = [memprofile[0], firstname_register1.text, surname_register1.text, nickname_register1.text,memprofile[4],memprofile[5],
                            hold_p[0],hold_p[1],hold_p[2],
                            test_pass[0],test_pass[1],test_pass[2]]
                    u1.WriteData(row[0:6],row[6:9],row[9:12])
                    memprofile,hold_p,test_pass = u1.ReadData(memprofile[0]) 
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(16,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page =  back_page_state
                click =0
        for box in edit_member:
            box.draw(screen)
        if option.mouse_on() :   #---------setting
            backpage = "edit_profile"
            screen.blit(ulp.all_setting_btn,(1023,12))  
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

##### CODE LESSON PAGE #######################################################################################
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
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "lesson"
                click =0
        if animal_btn.mouse_on():
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'animal_lesson'
                click =0
        if classroon_btn.mouse_on():
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'classroon_lesson'
                click =0
        if food_btn.mouse_on():
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
        # print('animal_lesson')
        screen.blit(ulp.animal_lesson_page, (0,0))
        if boi_state == 1:
            boi = pg.image.load(project_path+'/ui_photo/pop_up_animal_'+m0.lower()+'.png')
            screen.blit(boi,(0,0))
            pg.display.update()
            if sound_count == 1:
                playsound(project_path+'/sound_list/'+m0+".mp3") 
                playsound(project_path+'/sound_list/SP_'+m0+".mp3") 
                playsound(project_path+'/sound_list/'+m0+".mp3") 
                sound_count = 0                                                                          
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 0
                click = 0
        if a1.mouse_on() and boi_state == 0:
            screen.blit(ulp.a1_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                # 'Calculator','Calendar','Magnifying Glass','Notice Board','Scissors'
                m0 = "Starfish"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if a2.mouse_on() and boi_state == 0:
            screen.blit(ulp.a2_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Jellyfish'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if a3.mouse_on() and boi_state == 0:
            screen.blit(ulp.a3_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Seahorse'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if a4.mouse_on() and boi_state == 0:
            screen.blit(ulp.a4_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Octopus'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if a5.mouse_on() and boi_state == 0:
            screen.blit(ulp.a5_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Turtle'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if back_page_btn.mouse_on() and boi_state == 0:
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on() and boi_state == 0:
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() and boi_state == 0:   #---------setting
            backpage = "animal_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            # pg.display.update()
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
        # print('classroon_lesson')
        # classroon_lesson_page = pg.image.load(project_path+'/ui_photo/lesson_classroom.jpg')
        screen.blit(ulp.classroon_lesson_page,(0,0))
        # screen.blit(ulp.food_lesson_page, (0,0))
        if boi_state == 1:
            boi = pg.image.load(project_path+'/ui_photo/pop_up_classroom_'+m0.lower()+'.png')
            screen.blit(boi,(0,0))
            pg.display.update()
            if sound_count == 1:
                playsound(project_path+'/sound_list/'+m0+".mp3") 
                playsound(project_path+'/sound_list/SP_'+m0+".mp3") 
                playsound(project_path+'/sound_list/'+m0+".mp3") 
                sound_count = 0                                                                          
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 0
                click = 0
        if p1.mouse_on() and boi_state == 0:
            screen.blit(ulp.p1_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                # 'Calculator','Calendar','Magnifying Glass','Notice Board','Scissors'
                m0 = "Notice Board"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if p2.mouse_on() and boi_state == 0:
            screen.blit(ulp.p2_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Scissors'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if p3.mouse_on() and boi_state == 0:
            screen.blit(ulp.p3_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Calculator'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if p4.mouse_on() and boi_state == 0:
            screen.blit(ulp.p4_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Magnifying Glass'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if p5.mouse_on() and boi_state == 0:
            screen.blit(ulp.p5_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = 'Calendar'
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if back_page_btn.mouse_on() and boi_state == 0:
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on() and boi_state == 0:
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() and boi_state == 0:   #---------setting
            backpage = "classroon_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            # pg.display.update()
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
        # print('food_lesson')
        screen.blit(ulp.food_lesson_page, (0,0))
        if boi_state == 1:
            boi = pg.image.load(project_path+'/ui_photo/pop_up_food_'+m0.lower()+'.png')
            screen.blit(boi,(0,0))
            pg.display.update()
            if sound_count == 1:
                playsound(project_path+'/sound_list/'+m0+".mp3") 
                playsound(project_path+'/sound_list/SP_'+m0+".mp3") 
                playsound(project_path+'/sound_list/'+m0+".mp3") 
                sound_count = 0                                                                          
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 0
                click = 0
        if n1.mouse_on() and boi_state == 0:
            screen.blit(ulp.n1_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = "Spaghetti"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if n2.mouse_on() and boi_state == 0:
            screen.blit(ulp.n2_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = "Omelette"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if n3.mouse_on() and boi_state == 0:
            screen.blit(ulp.n3_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = "Cookies"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if n4.mouse_on() and boi_state == 0:
            screen.blit(ulp.n4_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = "Croissant"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if n5.mouse_on() and boi_state == 0:
            screen.blit(ulp.n5_mouseon,(0,0))
            if pg.mouse.get_pressed()[0] == 1:
                m0 = "Lemonade"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click == 1:   
                boi_state = 1
                click = 0
                sound_count = 1
        if back_page_btn.mouse_on() and boi_state == 0:
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on() and boi_state == 0:
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() and boi_state == 0:   #---------setting
            backpage = "food_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            # pg.display.update()
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

##### CODE PRACTICE PAGE #####################################################################################

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
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "practice"
                click =0

        if animal_btn.mouse_on():
            #?
            screen.blit(ulp.m_O_piccc,(48,122))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                
                page = 'test_practice'
                word_test = animal_word_pack
                for u in range(5):
                    pic_i_run.append(pg.image.load(project_path+'/practice_pic/'+ str(word_test[1][u]).lower() +'.png'))
                EXAMNO[0] = int(hold_p[word_test[0]])
                # print(EXAMNO[0])
                text_check = 0
                click =0

        if classroon_btn.mouse_on():
            #?
            screen.blit(ulp.m_O_piccc,(453,122))
            pic_i_run = []
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'test_practice'
                word_test = classroon_word_pack
                for u in range(5):
                    pic_i_run.append(pg.image.load(project_path+'/practice_pic/'+ str(word_test[1][u]).lower() +'.png'))
                EXAMNO[0] = int(hold_p[word_test[0]])
                # print(EXAMNO[0])
                text_check = 1
                click =0
        if back_to_lesson.mouse_on():
            screen.blit(ulp.back_to_lesson_pic,(172,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'lesson'
                click = 0
        if food_btn.mouse_on():
            #?
            screen.blit(ulp.m_O_piccc,(857,122))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'test_practice'
                word_test = food_word_pack

                for u in range(5):
                    pic_i_run.append(pg.image.load(project_path+'/practice_pic/'+ str(word_test[1][u]).lower() +'.png'))
                
                EXAMNO[0] = int(hold_p[word_test[0]])
                # print(EXAMNO[0])
                text_check = 2
                click =0
            # print(pic_i_run)
        
        if u1.PointPassAll(0) :
            t_s_1 = Text(123+30, 50+10+100, 50, "browallianewbold", green, 1, 'Success')
            t_s_1.draw(screen)
        
        if u1.PointPassAll(1) :
            t_s_2 = Text(455+30, 50+10+100, 50, "browallianewbold", green, 1, 'Success')
            t_s_2.draw(screen)
        
        if u1.PointPassAll(2) :
            t_s_3 = Text(860+30, 50+10+100, 50, "browallianewbold", green, 1, 'Success')
            t_s_3.draw(screen)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'test_practice':
        screen.blit(ulp.test_page, (0,0))
        if text_check == 0 :
            head_text = "Animals"
        if text_check == 1 :
            head_text = "Classroom"
        if text_check == 2 :
            head_text = "Foods"
        t5 = Text(294, 24, 50, "browallianewbold", (0,0,0), 1, head_text)
        t5.draw(screen)
        t6 = Text(40,110 , 80, "browallianewbold", (0,0,0), 1, str(EXAMNO[0]+1) +" / 5")
        t6.draw(screen)
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
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "test_practice"
                click =0
        if back_to_lesson.mouse_on():
            screen.blit(ulp.back_to_lesson_pic,(172,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                click =0
                if text_check == 0 :
                    page = "animal_lesson"
                if text_check == 1 :
                    page = "classroom_lesson"
                if text_check == 2 :
                    page = "food_lesson"
        if redu_btn.mouse_on():
            screen.blit(ulp.redu_test_pic,(1051,98))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                click =0
                pro_correct = 0
                type_test_inputbox.text = "  "
                type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))
        if EXAMNO[0] == 0:
            t2 = Text(90,250, 80, "browallianewbold", green, 1, "sri tao i sas na ja") 
            t2.draw(screen)
        if EXAMNO[0] > 0:
            if back_test_btn.mouse_on():
                screen.blit(ulp.back_test_pic,(1127,98))
                if pg.mouse.get_pressed()[0] == 1:
                    click = 1
                if pg.mouse.get_pressed()[0] == 0 and click ==1:
                    EXAMNO[1] = 1
                    EXAMNO[0] -= 1
                    pro_correct = 0
                    type_test_inputbox.text = "  "
                    type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))
                    click =0
        if EXAMNO[0] < 4:
            if next_test_btn.mouse_on():
                screen.blit(ulp.next_test_pic,(1201,98))
                if pg.mouse.get_pressed()[0] == 1:
                    click = 1
                if pg.mouse.get_pressed()[0] == 0 and click ==1:
                    pro_correct = 0
                    EXAMNO[1] = 1
                    EXAMNO[0] += 1
                    type_test_inputbox.text = "  "
                    type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))
                    click =0
        screen.blit(pic_i_run[EXAMNO[0]],(490,165))
        if practice_pass == 1:
            mic = sr.Microphone(1)
            r = sr.Recognizer()
            with mic as source:
                audio = r.listen(source)
                try: 
                    text1 = r.recognize_google(audio,language='en')
                    # print(text1)
                    if text1 == word_test[1][EXAMNO[0]].lower():
                        EXAMNO[1] = 1
                        pass_test_flag = 1 
                        micc = False
                        practice_pass = 0
                        pro_correct = 2
                    else:
                        pro_correct = 1
                    practice_pass = 0
                except :
                    practice_pass = 0
                    pro_correct = 1
                    continue
        if pro_correct == 2:
            screen.blit(ulp.pro_correct_pic,(0,0))
            type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))
            screen.blit(ulp.corect_Ans,(0,0))
            for i in range(5):
                if EXAMNO[0] == i and test_pass[word_test[0]].find(checklist_stamp[i]) != -1 :
                    t4 = Text(90,250, 80, "browallianewbold", green, 1, "PASS") 
                    t4.draw(screen)
            pg.display.update()
            pg.time.delay(3000)
            pro_correct = 0
        if pro_correct == 1:
            screen.blit(ulp.pro_incorrect_pic,(0,0))
        if type_test_inputbox.text.lower() == ("  "+word_test[1][EXAMNO[0]].lower()) :
            screen.blit(ulp.corect_Ans,(0,0))
        if type_test_inputbox.text.lower() != ("  "+word_test[1][EXAMNO[0]].lower()) and type_test_inputbox.text.lower() != ("  "):
            screen.blit(ulp.incorect_Ans,(0,0))
        if enter_press == 1:
            if type_test_inputbox.text.lower() == ("  "+word_test[1][EXAMNO[0]].lower()) :
                # print("true answer")
                # practice_pass = 1
                pass_test_flag = 1 
                screen.blit(ulp.record_pic,(0,0))
            enter_press = 0
        for box in animal_boxes:
            box.draw(screen)
        if EXAMNO[1] == 1 :
            EXAMNO[1] = 0
            hold_p[word_test[0]] = str(EXAMNO[0])
            u1.WriteData(memprofile,hold_p,test_pass,point_pass)
            memprofile,hold_p,test_pass,point_pass = u1.ReadData(memprofile[0])
            # print('memprofile')
            # print(memprofile)
            # print("hold_p")
            # print(hold_p)
            # print("test pass")
            # print(test_pass)   
        # for point
        checklist_stamp = ['A','B','C','D','E']
        if pass_test_flag == 1 :
            # print('pass')
            EXAMNO[1] = 1
            pass_test_flag = 0
            for i in range(5):
                if EXAMNO[0] == i and test_pass[word_test[0]].find(checklist_stamp[i]) == -1 : mark_pass = checklist_stamp[i]
            test_pass[word_test[0]] = test_pass[word_test[0]] + mark_pass
            if u1.PointPassAll(word_test[0]) == 0 :
                point_pass[word_test[0]] = point_pass[word_test[0]] + mark_pass
            mark_pass = ''
            if EXAMNO[0] < 4 :
                EXAMNO[0] += 1
            type_test_inputbox.text = "  "
            type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))
            u1.WriteData(memprofile,hold_p,test_pass,point_pass)
        for i in range(5):
            if EXAMNO[0] == i and test_pass[word_test[0]].find(checklist_stamp[i]) != -1 :
                screen.blit(ulp.pass_chioce,(177,98))
        if u1.TestPassAll(word_test[0]) :
            test_pass[word_test[0]] = ''
            type_test_inputbox.text = "  "
            type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))
            hold_p[word_test[0]] = 0
            output = gTTS(text="เก่งมากครับน้อง"+memprofile[3],lang="th",slow=False)
            output.save("s/good_job_name"+memprofile[0]+".mp3")
            playsound(project_path+"/s/good_job_name"+memprofile[0]+".mp3")
            os.remove(project_path+"/s/good_job_name"+memprofile[0]+".mp3")
            page = 'practice'
            u1.WriteData(memprofile,hold_p,test_pass,point_pass)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_RETURN:    
                    enter_press = 1 
            for box in animal_boxes:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()         