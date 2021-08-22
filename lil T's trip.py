import sys
import rpgtool

def ask_user(question):
    print(f'{question} ',end='')
    sys.stdout.flush()
    answer=sys.stdin.readline().strip()
    return answer

def NiboyMt():
    scene.load_background('pictures/NiboyMt-color.jpg')
    scene.set_title('NiboyMt')
    scene.set_message('''
    NiboyMt is a mountain with a lot of dogs, leopards,
    ducks and turtles living on it, and it's also
    the number 2 coldest place on earth.
    ''')
    answer = scene.ask_user('where to go next?(1, RanchoBernardo 2, MiddleNardo)')
    try:
        answer = int(answer)
    except:
        return 0
    if answer < 1 or answer > 2:
        return 0
    return answer

def RanchoBernardo():
    scene.load_background('pictures/RanchoBernardo.jpg')
    scene.set_title('RanchoBernardo')
    scene.set_message('''RanchoBernardo is the world's famous grassy 
    land. There are also a lot of giraffes and 
    trees. That place is very warm.
    
    lil T still want to go home.''')
    answer = scene.ask_user('''where to go next?(1, NiboyMt 2, MiddleNardo)''')
    try:
        answer = int(answer)
    except:
        return 1
    if answer < 1 or answer > 2:
        return 1
    if answer == 1:
        return 0
    else:
        return 2

def MiddleNardo():
    scene.load_background('pictures/MiddleNardo.jpg')
    scene.set_title('MiddleNardo')
    scene.set_message('''MiddleNardo has four rivers and a fountain, 
    between  Niboy Mt., Rancho Bernardo, Hansor Dr. and Sweet Home.  
    And the fountain is covered by a invisible wall to make a space
    without water for people to stand there and enjoy the fountain.
    There are also 8 logs sitting on every side of
    the fountain used as chairs, and ladders to let people
    climb right next to the fountain to enjoy it!
    ''')
    answer = scene.ask_user('where to go next?(1, NiboyMt 2, RanchoBernardo 3, HansorDr 4, SweetHome)')
    try:
        answer = int(answer)
    except:
        return 2
    if answer < 1 or answer > 4:
        return 2
    if answer == 1:
        return 0
    if answer == 2:
        return 1
    return answer


def HansorDr():
    scene.load_background('pictures/HansorDr.jpg')
    scene.set_title('HansorDr')
    scene.set_message('''HansorDr is a desert with a lot
    of kangaroo rats and kangaroos living on it!
    ''')
    answer = scene.ask_user('where to go next?(1, MiddleNardo 2, SweetHome)')
    try:
        answer = int(answer)
    except:
        return 3
    if answer < 1 or answer > 2:
        return 3
    if answer == 1:
        return 2
    return 4

def SweetHome():
    scene.load_background('pictures/sweet-home.jpg')
    scene.set_title('SweetHome')
    scene.set_message('''SweetHome is lil T\'s house.
    
    THE END!!!''')
    scene.ask_user('Press any key to leave!')
    return -1

def main():
    scene.load_sprite('pictures/alpha-lil-T.png')
    scene.load_background('pictures/NiboyMt-color.jpg')
    scene.set_title('Introduction')
    scene.set_message('''Lil T goes out to play,
    but his friend live far away, so 
    he has to travel very far. 
    So he did. But when he got there
    he couldn't find his friend,
    so he waited 5 minutes for his 
    friend, and his friend showed up!
    So they play together for three 
    hours! But when it's time to go home, 
    lil T got lost on his way home! 
    ''')
    scene.ask_user('Press <enter> key to continue ...')
    state = 0
    while state >= 0:
        if state == 0:
            state = NiboyMt()
        else:
            if state == 1:
                state = RanchoBernardo()
            else:
                if state == 2:
                    state = MiddleNardo()
                else:
                    if state == 3:
                        state = HansorDr()
                    else:
                        if state == 4:
                            state = SweetHome()
    print('The End!')
    pass

scene = rpgtool.Scene((1024,730))
main()
