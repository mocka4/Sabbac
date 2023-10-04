import random
from time import sleep

def Numbiz(number):
    
    number = [1,2,3,4,5,6,7,8,9]
    choice = random.choice(number)
    print(choice)
        
    

import os

def Viewer():
    path = os.getcwd()
    directory = os.listdir(path)
    print(f' Current Working Directory is: {directory}')


import shutil
import os
def Save_File():
    Save = os.mkdir('Stolen')
    file = '.py'
    path = os.getcwd()
    dir_list = os.listdir(path)
    if file == '.py':
        shutil.copy('cli.py', 'Stolen')
        print('Susccessfully copied to Stolen')
    else:
        print('Could not save file')





import socket

def Listener():
    host = '0.0.0.0'
    port = 4000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print(f' Listening at {host} on port {port}')
    SEPARATOR = '<sep>'
    client_socket, client_address = s.accept()
    print(f' {client_address[0]}: {client_address[1]} connected!')





def Client():
    

    import subprocess
    import os
    import socket

    host = '127.0.0.1'
    port = 4000
    SEPARATOR ='<sep>'
    s = socket.socket()
    s.connect((host, port))
    cwd = os.getcwd()
    s.send(cwd.encode())


def HowOld():
    birth_year = input('enter your birthyear:')
    age = 2023 - int(birth_year)
    print(f' Oooh, So You Are {age} Years Old Huh')    




import os

def Sizer():
    file = input('Enter file to Gauge')
    size = os.path.getsize(file)
    print(f' The file is {size} bytes')


def Reader():
    filename = input('Enter filename to read')
    f = open(filename, 'r')
    text = f.read()
    print(text)
    f.close()



import os
def Delete():
    filename = input('Enter file to delete:-')
    remove = os.remove(filename)
    print(f' {filename} deleted succesfully')

import shutil
import os

def Writer():
    filename = 'cli.py'
    cwd = os.getcwd()
    list = os.listdir()
    for file in list:
        if filename == 'cli.py':
            print('It is there')
            break
        else:
            print(' file not available')
            exit()


    fd = 'Danger.py'
    targetfile = 'cli.py'
    file = open(fd, 'w')
    data = file.write(targetfile)
    print(data)
    file.close()


    


    
class dog:

    def threaten():
        print('hou!! hou!!!hou!!hou!!hou!!!hou!!')

    def breed(colour):
        breed = input('Enter its breed')

        print(breed + " " + colour)


import random
import string

def generate(length):
    chars = string.ascii_letters + string.digits
    password = ' '.join(random.choice(chars) for _ in range(length))
    print(password)


import os
from time import sleep

def search_file(file):
    cwd = os.getcwd()
    print(cwd)
    path = '/'
    dir_list = os.listdir(path)
    print(dir_list)
    
    



import os
def Users():
      users = os.listdir('C://Users')
      print(users)


class snake:
      name = 'anaconda'

      def change_name(self, new_name):
            self.name = new_name




class liquor:

      quartz  = 'r20'
      cans = 'r16'

      def change_price(self, new_price):
            self.quartz = new_price


      def increase(self, price):
          self.quartz = price


      def decrease(self, price):
          self.quartz = price


      def special(self, rounds):
          self.quartz = rounds


      def ocl(self, cans):
          self.cans = cans


      def cans_only(self, a, b):
          self.cans = (a, b)


      def delivered(self, cases, pilet):
          self.quartz = cases
          self.cans = pilet


class cricket:
     import random
     from time import sleep
     
     '''this is a simple  cricket simulation'''
     print('Welcome To Wellis T20 League')
     sleep(2)
     teams = ['Royal_knights',
              'Kent',
              'St_porto',
              'Yorkshire',
              'Lions']
     
     
     four = '4runs'
     six = '6runs'
     shield = 'ball_blocked'
     alone = 'leave'
     out = 'caught'
     edged = 'dropped'
     sweeping = 'swept_away'
     pace = ['127kph', '133kph', '135kph', '137kph','141kgh', '146kph', '149kph', '153kph', '157kph']
     deliveries = ['good_ball', 'short_ball', 'outswinger', 'inswinger', 'offcutter', 'slow_ball']
     spin_ball = ['flipper', 'outspin', 'inspin', 'slow', 'pad_ball']
     spin_speed = ['87kph', '95kph', '98kph', '106kph', '112kph', '118kph']
     leg = 'Lbw'
     balls = (1,2,3,4,5)

     

     def bat1(self, boundary, maximum, caught):
         self.four = boundary
         self.six = maximum
         self.out = caught


     def bat2(self, defend, leave):
         self.shield = defend
         self.alone = leave


     def bat3(self, coverdrive, sweep):
         self.edged = coverdrive
         self.sweeping = sweep


     def bowl1(self, speed, delivery):
          self.pace = speed
          self.deliveries = delivery


     def bowl2(self, spin, gauge):
         self.spin_ball = spin
         self.spin_speed = gauge

     


     def Log(self):
         team_list = self.teams
         print('*****HERE IS THE LOG********')
         for t in team_list:
            sleep(2)
            print(t)
          
         
      
     def Lbw(self, leg):
         self.spin_ball = leg


     def Over_Seam(balls, pace):
         self.balls = balls
         self.pace = pace
         

    
    
     def table():
         print('Position   Teams          Played    Won     Lost    Points  ')               
         print('.1      |Royal_knights |   0     |  0    |  0     |   0     |')
         print('.2      |Kent          |   0     |  0    |  0     |   0     |')
         print('.3      |St porto      |   0     :  0    |  0     |   0     |')
         print('.4      |Yorkshire     |   0     |  0    |  0     |   0     |')
         print('.5      |Lions         |   0     |  0    |  0     |   0     |')


     def Draw():
         
         select  = cricket.teams
         team1 = random.choice(select)
         team2 = random.choice(select)
         print('The following Match is:', team1, 'Vs', team2)


     def Royal_knight_players():
        players = ['Rick_bolton (cp)', 'Ptrick_small (rhb)', 'Frank_cole (rhb)', 'Ernest_ope (lhb)', 'Solly_wade (rhb)', 'Tim_sadden (rhb)', 'Raul_luke (lhb)', 'Calvin_groove (rhb)', 'Oliver_james (rhb)', 'Bob_luther (lhb)', 'Bill_young (rhb)']
        print(' ********** Royal_knight Players **********') 
        for p in players:
            sleep(2)
            print(p)


     def Kent_players():
        players = ['Alex_harvey (cp)', 'James_siddle (rhb)', 'Edward_apples (lhb)', 'Graeme_fisher (lhb)', 'Sam_kingsley (rhb)', 'Elliot_roe (rhb)', 'Dwayne_bravo (rhb)', 'Luke_cannon (lhb)', 'Ronald_pope (rhb)', 'Franky_lewis (lhb)', 'Mason_houston (rhb)']
        print(' ********** Kent Players **********') 
        for p in players:
            sleep(2)
            print(p)
            
             
     def St_porto_players():
        players = ['Matt_raven (cp)', 'Hachelle_pyp (lhb)', 'Bobby_whale (rhb)', 'Sade_althor (rhb)', 'Luke_chase (lhb)', 'David_crew (rhb)', 'Jack_stew (rhb)', 'Kiddick_jones (rhb)', 'Gabriel_lord (rhb)', 'Will_richmond (rhb)', 'Huey_freeman (rhb)']
        print(' ********** St_porto Players **********') 
        for p in players:
            sleep(2)
            print(p)


     def Yorkshire_players():
        players = ['Timothy_quinn (cp)', 'Arnold_blue (rhb)', 'Peter_greenidge (rhb)', 'Calvin_joke (rhb)', 'Frank_peeps (lhb)', 'Zane_morevote (lhb)', 'Uri_sadler (rhb)', 'Andrew_trott (rhb)', 'Phil_lee (rhb)', 'Jeremy_boucher (rhb)', 'Fahil_adil (lhb)']
        print(' ********** Yorkshire Players **********') 
        for p in players:
            sleep(2)
            print(p)



     def Lions_players():
        players = ['Younus_khan (cp)', 'Rick_reason (rhb)', 'Brat_onions (rhb)', 'Nathan_dee (rhb)', 'Harold_jeans (lhb)', 'Maddy_cole (lhb)', 'Sean_piper (rhb)', 'Easy_flow (rhb)', 'Charles_roshkie (rhb)', 'Ollie_road (lhb)', 'Renny_grant (rhb)']
        print(' ********** Lions Players **********') 
        for p in players:
            sleep(2)
            print(p)       
        
        
        
