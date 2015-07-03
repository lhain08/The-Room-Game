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
    def __init__(self,min,max):
        room.__init__(self,'Teleporting...',False,False,True,False,'teleporter')
        self.min=min
        self.max=max
    def teleportit(self):
        global curroom
        curroom=random.randint(self.min,self.max)
class keyroom(room):
    def __init__(self,up,right,down,left):
        room.__init__(self,'You Found a Key!',False,False,False,False,'Keyroom')
        self.up=up
        self.right=right
        self.down=down
        self.left=left


r0=empty(1,6,None,2,False)
r1=empty(None,None,0,20,False)
r2=empty(20,0,3,None,False)
r3=empty(2,None,4,None,False)
r4=empty(3,20,5,None,False)
r5=empty(4,20,22,None,False)
r6=empty(None,23,7,0,True)
r7=empty(6,None,8,None,False)
r8=empty(7,None,9,None,False)
r9=empty(8,10,20,20,True)
r10=empty(None,None,11,9,False)
r11=empty(10,20,12,20,False)
r12=empty(11,15,None,13,False)
r13=empty(20,12,None,14,False)
r14=empty(20,13,21,22,False)
r15=empty(20,18,16,12,False)
r16=empty(15,17,None,None,False)
r17=empty(18,None,None,16,False)
r18=empty(19,None,17,15,False)
r19=empty(24,20,18,20,False)
rt=termination()
rv=victory()
tel1=teleporter(2,5)
tel2=teleporter(6,9)
rkey=keyroom(5,None,20,20)
rooms=[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,rt,rv,rkey,tel1,tel2]
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
    if x.up==20 or x.left==20 or x.right==20 or x.down==20:
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