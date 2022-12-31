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
    NiboyMt is filled with living things.''')
    scene.ask_user('Press any key to continue...')
    scene.set_message('''
    lil T is thirsty, he needs some water. 
    Then he meets a snail who knows a place where they
    can drink water, but in need of help.
    The snail told lil T a place where the can drink
    water. Lil T said he could carry the snail there. 
    The snail told Lil T her name. It was Misa.
    But when they are halfway there, a man is guarding
    a gate with no lock. The man said if they 
    answer a question they can pass through
    the gate. 
    ''')
    while True:
        answer = scene.ask_user('what is 1000-994? (a: 3, b: 7, c: 6)')
        if answer == 'c':
            break
        # answer != 'c'
        scene.ask_user('It\'s wrong. Press any key to continue... ')
    scene.set_message('''They got the answer correct so the man let
    them go pass the gate. After a few days, Misa touched poison ivy
    Lil T had to walk 4 miles to get to the nearest store. Then,
    he brought 62 bags of lots and lots of useful things including lots
    of poison itch resist. But, when he got out of the store,
    there were coyoties that didn't see him but, he did not want to push
    his luck, so he walked the long way, which was 9 and a half miles
    long. By the time he got back Misa was already worried sick.
    He put some poison itch resist on her every 5 minutes. After,
    they finally got water. Lil T got lots of bottles to store
    water just in case the whole thing happened again.''')

    answer = scene.ask_user('Where to go next?(1, RanchoBernardo 2, MiddleNardo)')
    try:
        answer = int(answer)  # string to number
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
    scene.ask_user('Press any key to continue ...')
    scene.set_message('''
    Lil T is hungry, he and the snail needs to eat launch.
    Just when they were about to start walking, they saw
    a poor little bird, who knows a place where they cold sit down and rest
    he said there were also a bunch of shops that sold different types of 
    things. They agreed that they would find some houses that people still
    lived in and they would do stuff for them to earn money so they would
    have enough money buy some food, drinks, a cooler and still have enough
    money for each of them to buy some stuff that they wanted.''')
    scene.ask_user('Press any key to continue ...')
    scene.set_message('''So , they pooled over their there money and
    discovered that together, they had more than enough money to buy a cooler
    and 3 meals a day. But, they could only get 3 meals a day for about 8
    days with their money so, they decided to just get 2 meals a day.
    They had enough money to get a burger for each of them and a
    big box of french fries for them to share for breakfast and dinner.''')
    scene.ask_user('Press any key to continue ...')
    scene.set_message('''As they started walking, they saw a vending machine 
    so, they bought a few snacks to eat along the road so they wouldn't get
    too hungry. About 2 miles down the road, they were hungry so they opened 
    1 of the bigger snacks that they bought to share. But, when it was
    nighttime, they weren't there yet so, they hurried off to the closest
    house they could find. The house was old and rusty-looking but the 
    structure was still good and they figured they have would have to walk a
    long time before they reached the next house so, they decided to just stay put''')
    scene.ask_user('Press any key to continue ...')
    scene.load_background('pictures/RanchoBernardoHouse-1.jpg')
    scene.set_message('''When they knocked on the the door, a grumpy looking
    old women opened the door, tripped them and used a lasso to tie them up.
    "We come in peace!"they all screamed.''')
    scene.ask_user('Press any key to continue ...')
    scene.set_message('''The old women said she thought they
    were the cows. And she asked them why they were here and Lil T and his
    friends told her the whole story. After they were done with their story,
    the old women led them into her living room and told they could stay
    as long as they wanted. To their amazement, her living room looked
    tidy, neat, sturdy and stable.''')
    scene.ask_user('Press any key to continue ...')
    scene.set_message(''' The lady said if they were headed somewhere
    she could give them a ride if they wanted.They said they would really
    appreciate it if she would give them a ride to sllacksville tomorrow
    morning. The following morning they rode a horse to sllacksville town
    and said their thank yous and good byes.''')
    scene.ask_user('Press any key to continue ...')
    scene.load_background('pictures/DownTownRanchoBernardo.jpg')
    scene.set_message('''They walked for a few minutes until they saw what they were looking for, a
    bunch of roads packed very tight together with a bunch of houses packed tight together. They
    walked by a lot of houses and there were still roads packed together very tightly but, instead
    of a lot of houses on the road there were a bunch of stands and markets.''')
    scene.ask_user('press any key to continue...')
    scene.set_message(''' They bought breakfast
    at one of the stands that sold food. Then, they found a good spot to sit down and eat. After
    The were done eating, they went to one of the stands that had printers and they paid them
    some money to use their printers to print some fliers so people would they were willing to do
    house jods. When they were done printing their 5 big stacks of fliers they hung them all over
    the town and, left 2 big stacks of fliers to give one to all the towns people.''')
    scene.ask_user('Press any key to continue ...')
    scene.set_message('''When they were done passing out all the towns people, they built a giant, warm,
    sturdy, comfortable shelter with sicks, metal sticks, some rope, a bunch of blankets, a few nets,
    a few rocks and a bucket for a toilet. before night, they were done. The following morning, they got a 
    lot of house jobs all around town and, before long, they had over 500$. But, they decided it still wasn't
    enough for all of them to get enough food, three meals a day, 7 days a week so they kept working hard
    but, they changed their food orders to 3 meals a day. After 3 weeks of working hard, they had lots of
    money, over 2,300$ so they got more food for each of their meals and one day, Lil T announced that they
    had earned more than enough money to buy food so they could each get 20$ and spend it on whatever they
    wanted''')
    scene.ask_user('Press any key to continue ...')
    scene.set_message('''1 month later, they already had at least 4,500$ so they decided in order to ever
    get home, they had to leave this town and keep going with their journey back home. So they announced
    their retirement to the towns people''')
    scene.ask_user('Press any key to continue ...')
    scene.set_message('''On the road they
    saw a dead end, it's not really
    a dead end, but it looks like a dead end.
    The small group of friends thought they were lost.
    Then they finally noticed that it was not a dead
    end, it was just a door that won't open.
    And then they saw it a math equation with no 
    answer on it, but there are blocks with numbers on
    it. Plus there is a hole just the right size for
    Any block to fit in.
    ''')
    niboy = scene.ask_user('Press <4> key to continue ...')
    while niboy != '4':
        niboy = scene.ask_user('It was wrong. Press <4> key to continue ...')
        pass
    answer = scene.ask_user('what is 36 divided by 6?')
    while answer != '6':
        answer = scene.ask_user('The answer was wrong. What is 36 divided by 6?')
        pass

    scene.set_message('''They had worked hard the past few days so they
    played tennis together. But, they accidentally hit somebody so that
    person got mad at them for hitting him. It was because he did not 
    think about weather it was a accident or not before he got mad at them.''')
    scene.ask_user('press any key to continue...')
    scene.set_message('''He was now too mad at them to think about 
    weather it was a accident or not. So they told him that it was a
    accident. However, he did not believe them so, they said sorry. 
    But then, they told him that they will proof that it was a 
    accident by, looking at the videos in the security-camras.
    And, it proofed him wrong. He said sorry because he did not
    even believe them one bit when they first told him that it was
    a accident. In order to proof he was sorry, he let them sleep 
    at his house for 2 days and, he cooked lots of yummy food 
    for them all. Lil T asked his new friend what his name was
    and he told Lil T what his name was. His name was Andy.
    ''')
    scene.ask_user('press any key to continue...')
    scene.set_message('''And, they decided to play "what do you like?"And so, they did.
    And when it was Andy's turn, Andy said his hobby was treasure hunting Lil T gave
    Andy a treasure map. And they had lots of fun. The next day, they played tennis, went
    swimming together, played soccer, and played some indoor games''')
    scene.ask_user('press any key to continue...')
    scene.set_message('''The following morning, they played a little bit more tennis
    and chinese chess. Soon, Lil T and his friends had to go on with their trip home.''')
    answer = scene.ask_user('''where to  next?(1, NiboyMt 2, MiddleNardo)''')
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
    scene.ask_user('press <enter> key to continue...')
    scene.set_message('''as they kept walking they saw a duck, 
    so they said" you can tag along if you want" so the bird decided to
    tag along. ''')
    scene.ask_user('press any key to continue...')
    scene.set_message('''soon they arrived at a gate with
    a slot. They realized that they had to put money in the slot, 
    but they didn't have money. Then they found a machine that trades
    money for things. So they put a apple in a hole on the machine
    and money came out. And they put 1 dollar in the slot.''')
    key = scene.ask_user('press <5> key to continue...')
    while key != '5':
        key = scene.ask_user('It is not <5> key. Press <5> key to continue...')
        pass

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
    scene.ask_user('press any key to continue...')
    scene.set_message('''Soon the friends had reached a small town
    called Picky-Sunset. And found a place for them to sit
    down and rest. But they were under a tree, and there was a
    person hiding behind the tree. And the person was holding
    a long piece of rope, which he flung across the tree and the
    other end landed in his other hand. A he quickly tied them up.
    He said he will only free them if they answer his question.''')
    scene.ask_user('press any key to continue...')
    answer = scene.ask_user('How many continents are there?')
    while answer != '7':
        answer = scene.ask_user('It is wrong. How many continents are there?')
        pass
    scene.load_background('pictures/FBI.jpg')
    scene.set_message('''The person turned out to be a F.B.I agent that was
    guarding the town for a while. And that was because the president
    had a top secret mission that includes himself.''')
    scene.ask_user('press any key to continue...')
    scene.set_message(''' He sent out some
    F.B.I agents to make sure that nobody knows so, nobody else would
    know about the top secret mission. That F.B.I agent thought they
    were spies sent from other countries. ''')
    scene.ask_user('press any key to continue...')
    scene.set_message('''So to proof they were not spies
    they showed their passports, and there were not even one single spy stamp
    in any of their passports so he let them go.''')
    scene.ask_user('press any key to continue...')
    scene.set_message(''' And kindly offered all of them lots of
     food to take along their big journey. The question he
    had asked them has a answer that spies would not know.''')
    scene.ask_user('press any key to continue...')
    scene.set_message('''They said they would take the food.''')

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
    scene.set_message('SweetHome is lil T\'s house.')
    scene.set_message('''lil T ran through the front door
    with such excitement that he ran into his little brother.
    his mom was making peanut butter and jelly sandwich.
    Then they sat down and ate lunch while lil T explained the
    whole story to his family.''')
    key = scene.ask_user('press <enter> key to continue...')
    while key != 'return':
        key = scene.ask_user('It is not <enter> key. Press <enter> key to continue...')
        pass
    nini = scene.ask_user('Press <7> key to leave!')
    while nini != '7':
        nini = scene.ask_user('Press <7> key to leave!')
        pass
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
    mama = scene.ask_user('Press <f> key to continue ...')
    while mama != 'f':
        mama = scene.ask_user('That was not <f> key. Press <f> key to continue ...')
        pass
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
