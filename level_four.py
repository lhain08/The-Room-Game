__author__ = 'Slaphsot135'
import random,time
key=False
class room(object):
    def __init__(self,message,death,Victory,teleport,locked,type):
        self.message=message
        self.death=death
        self.victory=Victory
        self.teleport=teleport
        self.locked=locked
        self.type=type


class empty(room):
    def __init__(self,up,right,down,left,locked):
        room.__init__(self,'Empty Room',False,False,False,locked,'empty')
        self.up=up
        self.right=right
        self.down=down
        self.left=left

class termination(room):
    def __init__(self):
        room.__init__(self,'You Died',True,False,False,False,'termination')
class victory(room):
    def __init__(self):
        room.__init__(self,'Congratulations! You Win!',False,True,False,False,'victory')
class teleporter(room):
    def __init__(self):
        room.__init__(self,'Teleporting...',False,False,True,False,'teleporter')
    def teleportit(self):
        global curroom
        curroom=random.randint(0,8)
class keyroom(room):
    def __init__(self,up,right,down,left):
        room.__init__(self,'You Found a Key!',False,False,False,False,'Keyroom')
        self.up=up
        self.right=right
        self.down=down
        self.left=left


r0=empty(1,9,7,4,False)
r1=empty(2,None,0,None,False)
r2=empty(None,None,1,3,False)
r3=empty(None,2,None,17,False)
r4=empty(None,0,None,5,False)
r5=empty(6,4,None,None,False)
r6=empty(17,20,5,None,False)
r7=empty(0,None,8,None,False)
r8=empty(7,19,17,17,False)
r9=empty(None,10,None,0,True)
r10=empty(11,19,None,9,False)
r11=empty(None,12,10,None,False)
r12=empty(17,13,19,11,False)
r13=empty(14,None,None,12,False)
r14=empty(15,None,13,17,False)
r15=empty(None,None,14,16,False)
r16=empty(18,15,17,17,False)
rt=termination()
rv=victory()
tel=teleporter()
rkey=keyroom(None,None,None,6)
rooms=[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,rt,rv,tel,rkey]
global curroom
curroom=0
def UP():
    global curroom
    if rooms[curroom].up or rooms[curroom].up == 0:
        if rooms[rooms[curroom].up].locked:
            if key:
                curroom=rooms[curroom].up
            else:
                print 'Locked'
        else:
            curroom=rooms[curroom].up
    else:
        print 'no above room'
def LEFT():
    global curroom
    if rooms[curroom].left or rooms[curroom].left == 0:
        if rooms[rooms[curroom].left].locked:
            if key:
                curroom=rooms[curroom].left
            else:
                print 'Locked'
        else:
            curroom=rooms[curroom].left
    else:
        print 'no left room'
def RIGHT():
    global curroom
    if rooms[curroom].right or rooms[curroom].right == 0:
        if rooms[rooms[curroom].right].locked:
            if key:
                curroom=rooms[curroom].right
            else:
                print "Locked"
        else:
            curroom=rooms[curroom].right
    else:
        print 'no right room'
def DOWN():
    global curroom
    if rooms[curroom].down or rooms[curroom].down == 0:
        if rooms[rooms[curroom].down].locked:
            if key:
                curroom=rooms[curroom].down
            else:
                print 'Locked'
        else:
            curroom=rooms[curroom].down
    else:
        print 'no below room'
while True:
    print curroom
    x=rooms[curroom]
    print x.message
    if x.death or x.victory:
        break
    if x.type=='Keyroom':
        key=True
        x.message='Empty Room'
    if x.up==17 or x.left==17 or x.right==17 or x.down==17:
        print 'WARNING: You are near a Death Room'
    move=raw_input('Which direction do you want to move?>>> ')
    move=move.upper()
    try:
        globals()[move]()
    except:
        print 'no such command'
    x=rooms[curroom]
    if x.teleport:
        print x.message
        time.sleep(.25)
        x.teleportit()