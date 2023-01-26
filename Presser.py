import os
import math
import time
from datetime import datetime
import sys
import io

# modules #
def text(presses, current_adders=0, current_pressers=0, current_multipliers=0): 
    print('You currently have {:,} points. '.format(presses))
    if current_adders > 0:
        print('You currently have {:,} adders. '.format(current_adders))
    if current_pressers > 0:
        print('You currently have {:,} pressers. '.format(current_pressers))
    if current_multipliers > 0:
        print('You currently have {:,} multipliers. '.format(current_multipliers))

def reset(marks, u1, u2, u3):
    print('\n'*10)
    text(marks, u1, u2, u3)

def scrolling_text(text, speed=0.05):
    for i in range(len(text)):
        print(text[i], end='')
        time.sleep(speed)
    print()


# Start program  #
game_active = False


# Get User info and set up save dir  #
user = os.getlogin()
dir = 'C:/Users/' + user + '/Desktop/PresserSave'
if os.path.exists(dir):
    os.chdir(dir)
else:
    os.mkdir(dir)
    os.chdir(dir)

# initalize varribles #
game_active = True
points = 0
current_adders = 0
current_pressers = 0
current_multipliers = 0
total_collect_points = 0
afk_message = False
active_stamp = False

#  look/apply for save file  #
if os.path.exists('save_file.txt'):
    scrolling_text('Save File found!\nDo you want to use it? (y/n)')
    if 'y' in input():
        print('getting data')
        f = io.open('save_file.txt', 'r')
        lines = f.read()
        data = lines.split('.')
        p = data[0]
        ca = data[1]
        cp = data[2]
        cm = data[3]
        f.close()
        print('data retrieved\napplying data')
        if os.path.exists('time_signiture.txt'):
            f = io.open('time_signiture.txt', 'r')
            date = f.read()
            print(date)
            d1 = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
            d2 = datetime.now()
            timedelta = d2 -d1
            total_collect_points = math.trunc(timedelta.total_seconds())
            afk_message = True
            time_stamp_a = datetime.now()
            time_stamp_a = time_stamp_a.strftime('%S')
            time_stamp_a = str(time_stamp_a)
            if time_stamp_a[0] == '0':
                time_stamp_a = time_stamp_a[1]
            try:
                time_stamp_a = int(time_stamp_a)
            except:
                active_stamp = True
            active_stamp = True
            f.close()

        points += total_collect_points + int(p)
        current_adders += int(ca)
        current_pressers += int(cp)
        current_multipliers += int(cm)


### GAME LOOP ###
while game_active:
    reset(points, current_adders, current_pressers, current_multipliers)
    if afk_message:
        afk_message = False
        print('You got {:,} points while you were idle'.format(total_collect_points))
        total_collect_points = 0
    next_action = input('Press enter to get points, input a 1 to open up shop, input a 2 for help, 3 to leave  ')

    # Shop #
    if '1' in next_action:
        scrolling_text('\nWelcome to the shop, your options are ')
        scrolling_text('1) Adders ({} points)'.format(10))
        scrolling_text('2) Pressers ({} points)'.format(50)) 
        scrolling_text('3) Multipliers ({} points)'.format(100))
        scrolling_text('You currently have {} points'.format(points)) 
        next_action = input('Enter the coorsponding number to buy or enter nothing to exit  ')
        if '1' in next_action:
            if points >= 10:
                points -= 10
                current_adders += 1
                if current_adders > 64:
                    current_adders = 64
                    scrolling_text('You are already maxed out on that... but I will take your money lol')
            else:
                required = math.abs(points - 10)
                print('\n not enough funding {} points required'.format(required))
        elif '2' in next_action:
            if points >= 50:
                points -= 50
                current_pressers += 1
                if current_pressers > 64:
                    current_pressers = 64
                    scrolling_text('You are already maxed out on that... but I will take your money lol')
            else:
                required = math.abs(points - 50)
                print('\n not enough funding {} points required'.format(required))
        elif '3' in next_action:
            if points >= 100:
                points -= 100
                current_multipliers += 1
                if current_multipliers > 64:
                    current_multipliers = 64
                    scrolling_text('You are already maxed out on that... but I will take your money lol')
            else:
                required = math.abs(points - 100)
                print('\n not enough funding {} points required'.format(required))
        else:
            pass
    

    # Help #
    elif '2' in next_action:
        scrolling_text('\nPress enter to gain points... then buy things for more points... lol')
        input('\n\npress enter to continue')
        pass


    # Exit #
    elif '3' in next_action:
        scrolling_text('Do you want to save? (y/n)')
        if 'y' in input():
            f = io.open('save_file.txt', 'w+')
            p = str(points)
            ca = str(current_adders)
            cp = str(current_pressers)
            cm = str(current_multipliers)
            save_code = p + '.' + ca + '.' + cp +'.' + cm
            f.write(save_code)
            f.close()
            if current_pressers > 0:
                f = io.open('time_signiture.txt', 'w+')
                f.write(str(datetime.now()))
                f.close()
        sys.exit()


    # points thingy # 
    else:
        points += 1
        if current_adders > 0:
            points += current_adders
        if current_multipliers > 0:
            points += 2 ** current_multipliers
        #Time shenagnigiuns
        if current_pressers > 0:
            print('t1')

            if active_stamp == False:
                print('inactive')
                time_stamp_a = datetime.now()
                time_stamp_a = time_stamp_a.strftime('%S')
                time_stamp_a = str(time_stamp_a)
                if time_stamp_a[0] == '0':
                    time_stamp_a = time_stamp_a[1]
                try:
                    time_stamp_a = int(time_stamp_a)
                except:
                    active_stamp = True
                active_stamp = True

            elif active_stamp:
                print('active')
                time_stamp_b = datetime.now()
                time_stamp_b = time_stamp_b.strftime('%S')
                time_stamp_b = str(time_stamp_b)
                if time_stamp_b[0] == '0':
                    time_stamp_b = time_stamp_b[1]
                try:
                    time_stamp_b = int(time_stamp_b)
                except:
                    continue
                if time_stamp_a <time_stamp_b:
                    print('TRUEEEE')
                    total_collect_points = time_stamp_b - time_stamp_a
                    points += total_collect_points
                    if math.floor(total_collect_points) > 1:
                        afk_message = True
                    active_stamp = False
