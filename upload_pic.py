# project_path = 'C:/fra361_st4_voca_ui'
project_path = 'D:/stu64'

from tkinter.filedialog import test
import pygame as pg
# from main_code import project_path
#### my path  'C:/fra361_st4_voca_ui/ui_photo
# my_ui_pic_path = 'C:/fra361_st4_voca_ui/ui_photo'

ui_pic_path = project_path+'/ui_photo'

#first
first_page = pg.image.load(ui_pic_path+"/first_page.jpg")
#login
login_page = pg.image.load(ui_pic_path+'/login_page.jpg')
login_green_btn = pg.image.load(ui_pic_path+'/new_login_button.png')
register_green_btn = pg.image.load(ui_pic_path+'/new_regis_button.png')


#register
register_page = pg.image.load(ui_pic_path+'/new_register_page.jpg')
back_btn = pg.image.load(ui_pic_path+'/back_button.png')
add_pic_btn = pg.image.load(ui_pic_path+'/add_picture.png')
take_pic_btn = pg.image.load(ui_pic_path+'/take_photo_button.png')
upload_pic_btn = pg.image.load(ui_pic_path+'/upload_photo_button.png')
repic1_btn = pg.image.load(ui_pic_path+'/re1.png')
repic2_btn = pg.image.load(ui_pic_path+'/re2.png')
bgwhite = pg.image.load(ui_pic_path+'/background_pic.png')

defualt_user_pic_path = ui_pic_path+'/defualt_profile.png'

#profile
profile_page = pg.image.load(ui_pic_path+'/home_page.jpg')
lesson_green_btn = pg.image.load(ui_pic_path+'/lesson_button.png')
practice_green_btn = pg.image.load(ui_pic_path+'/lesson_button.png')
p_g_b = pg.image.load(ui_pic_path+'/practice_button.png')
practice_green_btn = pg.image.load(ui_pic_path+'/practice_button.png')

all_setting_btn = pg.image.load(ui_pic_path+'/all.png')


#setting
edit_profile_secl_btn = pg.image.load(ui_pic_path+'/edit_profile_button.png')
logout_profile_secl_btn = pg.image.load(ui_pic_path+'/log_out_button.png')

#edit_profile_page
edit_profile_page = pg.image.load(ui_pic_path+'/edit_profile_page.jpg')
save_green_btn =  pg.image.load(ui_pic_path+'/save_button.png')

#back
back_page_green_btn = pg.image.load(ui_pic_path+'/back_button.png')
back_home_green_btn = pg.image.load(ui_pic_path+'/home_button.png')



#lesson_page

lesson_page =  pg.image.load(ui_pic_path+'/lesson_page.jpg')

#animal_lesson_page
animal_lesson_page = pg.image.load(ui_pic_path+'/lesson_animal.jpg')
a1_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Starfish.png')
a2_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Jellyfish.png')
a3_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Seahorse.png')
a4_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Octopus.png')
a5_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Turtle.png')
#classroon_lesson_page
classroon_lesson_page = pg.image.load(ui_pic_path+'/lesson_classroom.jpg')
p1_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Notice Board.png')
p2_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Scissors.png')
p3_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Calculator.png')
p4_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Magnifying Glass.png')
p5_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Calendar.png')
#food_lesson_page
food_lesson_page = pg.image.load(ui_pic_path+'/food_lesson.jpg')
n1_mouseon = pg.image.load(ui_pic_path+'/mouse_on_spa.png')
n2_mouseon = pg.image.load(ui_pic_path+'/mouse_on_egg.png')
n3_mouseon = pg.image.load(ui_pic_path+'/mouse_on_cookie.png')
n4_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Croissant.png')
n5_mouseon = pg.image.load(ui_pic_path+'/mouse_on_lemon.png')

#practice_page
back_to_lesson_pic =  pg.image.load(ui_pic_path+'/choose_button.png')
back_test_pic = pg.image.load(ui_pic_path+'/backword_green.png')
next_test_pic = pg.image.load(ui_pic_path+'/nextword_green.png')
redu_test_pic = pg.image.load(ui_pic_path+'/reword_green.png')
practice_page =  pg.image.load(ui_pic_path+'/practice_page.jpg')
record_pic = pg.image.load(ui_pic_path+'/recording_pic.png')
corect_Ans = pg.image.load(ui_pic_path+'/spell_correct_pic.png')
incorect_Ans = pg.image.load(ui_pic_path+'/spell_incorrect_pic.png')
pro_incorrect_pic = pg.image.load(ui_pic_path+'/pronounce_incorrect_pic.png')
pro_correct_pic = pg.image.load(ui_pic_path+'/pronounce_correct_pic.png')
#practice_page
pass_chioce = pg.image.load(ui_pic_path+'/pass_pic.png')
test_page = pg.image.load(ui_pic_path+'/final_practice_game.jpg')
correct_icon = pg.image.load(ui_pic_path+'/correct.jpg')
success = pg.image.load((ui_pic_path+'/section.jpg'))

# animal_test_pic_1 = pg.image.load(ui_pic_path+'/test_pic/animal_test_1.jpg')
# animal_test_pic_2 = pg.image.load(ui_pic_path+'/test_pic/animal_test_2.jpg')
# animal_test_pic_3 = pg.image.load(ui_pic_path+'/test_pic/animal_test_3.jpg')
# # animal_test_pic_4 = pg.image.load(ui_pic_path+'/test_pic/animal_test_4.jpg')
# # animal_test_pic_5 = pg.image.load(ui_pic_path+'/test_pic/animal_test_5.jpg')
# # classroom_test_pic_1 = pg.image.load(ui_pic_path+'/test_pic/classroom_1.jpg')
# # classroom_test_pic_2 = pg.image.load(ui_pic_path+'/test_pic/classroom_2.jpg')
# # classroom_test_pic_3 = pg.image.load(ui_pic_path+'/test_pic/classroom_3.jpg')
# # # classroom_pic_4 = pg.image.load(ui_pic_path+'/test_pic/classroom_4.jpg')
# # # classroom_pic_5 = pg.image.load(ui_pic_path+'/test_pic/classroom_5.jpg')
# food_test_pic_1 = pg.image.load(ui_pic_path+'/test_pic/food_test_1.jpg')
# food_test_pic_2 = pg.image.load(ui_pic_path+'/test_pic/food_test_2.jpg')
# food_test_pic_3 = pg.image.load(ui_pic_path+'/test_pic/food_test_3.jpg')
# food_test_pic_4 = pg.image.load(ui_pic_path+'/test_pic/animal_test_4.jpg')
# food_test_pic_5 = pg.image.load(ui_pic_path+'/test_pic/animal_test_5.jpg')

# animal_list_test_pic = [animal_test_pic_1,animal_test_pic_2,animal_test_pic_3,animal_test_pic_1,animal_test_pic_2]
# classroom_list_test_pic = [classroom_test_pic_1,classroom_test_pic_2,classroom_test_pic_3,classroom_test_pic_4,classroom_test_pic_5]
# food_list_test_pic = [food_test_pic_1,food_test_pic_2,food_test_pic_3,food_test_pic_4,food_test_pic_5]
# pic_i_test_object = [animal_list_test_pic,animal_list_test_pic,animal_list_test_pic]







#########################################################################################



