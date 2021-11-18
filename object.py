import pygame as pg
import cv2
pg.init()

eng_alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',' ','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

regis_success = 0
class Text():
    def __init__(self, x, y,size,font,color,type,text):
        self.color = color
        self.font = font
        self.x = x
        self.y = y
        self.type = type
        self.size = size
        self.text = text
    def draw(self,screen):
        font = pg.font.SysFont(self.font,self.size)
        text = font.render(self.text,True,self.color)
        if self.type == 1:
            textRect = (self.x,self.y)
            screen.blit(text,textRect)
        if self.type == 2:
            textRect = text.get_rect()
            textRect.center = (self.x//2, self.y//2)
            screen.blit(text, textRect)
    def ison(self,screen):
        (poX, poY) = pg.mouse.get_pos()
        if poX in range(self.x, self.x + 200) and poY in range(self.y, self.y + 150):

            if pg.mouse.get_pressed()[0] == 0:
                self.color = (255,33,73)
                font = pg.font.SysFont(self.font, self.size)
                text = font.render(self.text, True, self.color)
                textRect = (self.x, self.y)
                screen.blit(text, textRect)
                screen.blit(text, textRect)
    def submit(self):
        (poX, poY) = pg.mouse.get_pos()
        if poX in range(self.x, self.x + 200) and poY in range(self.y, self.y + 150) and pg.mouse.get_pressed()[0] == 1:
            return True




class Button():
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.rect = pg.Rect(x, y, w, h)
    # def __init__(self, x=0, y=0, w=0, h=0):
    #     Rec.__init__(self, x, y, w, h)
        self.status = False
    def mouse_on(self):
        (pos_x, pos_y) = pg.mouse.get_pos()
        if self.x <= pos_x <= self.x + self.w and self.y <= pos_y <= self.y + self.h:
            self.status = True
        else:
            self.status = False
        return self.status
class InputBox:

    def __init__(self, x, y, w, h, fontsize ,space_in_y,first_upper_mode,text='  '):
        self.rect = pg.Rect(x, y, w, h)
        self.color = (0,0,0)  # inactive color
        self.text = text
        self.fontsize = fontsize
        self.space_in_y = space_in_y
        self.first_upper_mode = first_upper_mode
        # self.font = pg.font.SysFont("comicsans", fontsize)
        self.font = pg.font.SysFont("browallianewbold", fontsize)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos):  # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False

            self.color = pg.Color('dodgerblue2') if self.active else pg.Color((0,0,0))  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:

                if event.key == pg.K_RETURN:
                    self.active = not self.active
                    self.color = pg.Color('lightskyblue3') if self.active else pg.Color('dodgerblue2')

                if event.key == pg.K_BACKSPACE:
                    if len(self.text)>2:
                        self.text = self.text[:-1]
                else:
                    if len(self.text)<= 18:
                        if event.unicode.isdigit():
                            self.text += event.unicode
                        if event.unicode in eng_alphabet:
                            if self.first_upper_mode == 1:
                                if len(self.text)<3 and event.unicode.islower() == True:
                                    self.text += event.unicode.upper()
                                elif len(self.text)>=3:
                                    self.text += event.unicode
                            if self.first_upper_mode == 0:
                                self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, pg.Color("black"))
                pg.display.update()

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width())
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x, self.rect.y+self.space_in_y))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
import os 
import csv   
project_path = 'D:/stu64'
user_data_path = project_path +'/user_data'

class user():
    # def __init__(self,username,firstname,surname,nickname,typepic,ishuman,hold_p_1,hold_p_2,hold_p_3,pass_1,pass_2,pass_3):
        # self.filepath = filepath
        # self.memprofile = [username,firstname,surname,nickname,typepic,ishuman]
        # self.hold_p = [hold_p_1,hold_p_2,hold_p_3]
        # self.test_pass = [pass_1,pass_2,pass_3]
        # print(self.memprofile)
        # print(self.hold_p)
        # print(self.test_pass)
    def __init__(self):
        self.memprofile = []
        self.hold_p = []
        self.test_pass = []
        self.username = ''
        self.firstname = ''
        self.surname = ''
        self.nickname = ''
        self.typepic = ''
        self.ishuman = ''
        self.hold_p_1 = ''
        self.hold_p_2 = ''
        self.hold_p_3 = ''
        self.pass_1 = ''
        self.pass_2 = ''
        self.pass_3 = ''
        self.fullname = self.firstname + self.surname

    def WriteData(self,memprofile,hold_p,test_pass):
        row = []
        # row = row+self.memprofile+self.hold_p+self.test_pass
        row = memprofile + hold_p + test_pass
        print("row")
        print(row)
        # row = row.append(self.hold_p)
        # row = row.append(self.test_pass)
        user_data_file = open('user_data/'+memprofile[0]+'.csv','w', encoding='UTF8', newline='') 
        writer = csv.writer(user_data_file)
        writer.writerow(row)
        user_data_file.close()
        self.memprofile = memprofile
        self.hold_p = hold_p
        self.test_pass = test_pass
        self.username = self.memprofile[0]
        self.firstname = self.memprofile[1]
        self.surname = self.memprofile[2]
        self.nickname = self.memprofile[3]
        self.typepic = self.memprofile[4]
        self.ishuman = self.memprofile[5]
        self.hold_p_1 = self.hold_p[0]
        self.hold_p_2 = self.hold_p[1]
        self.hold_p_3 = self.hold_p[2]
        self.pass_1 = self.test_pass[0]
        self.pass_2 = self.test_pass[1]
        self.pass_3 = self.test_pass[2]
        self.fullname = self.firstname+' '+self.surname
        pass

    def ReadData(self,username):
        user_data_file = open('user_data/'+username+'.csv','r', encoding="utf8")
        reader = csv.reader(user_data_file)
        for row in reader:
            self.memprofile = row[0:6]
            self.hold_p = row[6:9]
            self.test_pass = row[9:12]        
        user_data_file.close()

        self.username = self.memprofile[0]
        self.firstname = self.memprofile[1]
        self.surname = self.memprofile[2]
        self.nickname = self.memprofile[3]
        self.typepic = self.memprofile[4]
        self.ishuman = self.memprofile[5]
        self.hold_p_1 = self.hold_p[0]
        self.hold_p_2 = self.hold_p[1]
        self.hold_p_3 = self.hold_p[2]
        self.pass_1 = self.test_pass[0]
        self.pass_2 = self.test_pass[1]
        self.pass_3 = self.test_pass[2]
        self.fullname = self.firstname+' '+self.surname
        return self.memprofile ,self.hold_p ,self.test_pass

    def SerchLogin(self,username):
        filenames = os.listdir(user_data_path)

        for filename in filenames:
            if username+'.csv' == filename:
                user_status = 'have'
                print(user_status)
                return user_status
            else:
                user_status = 'nohave'
                print(user_status)
            
        return user_status

