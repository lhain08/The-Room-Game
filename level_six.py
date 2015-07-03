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


r0=empty(29,5,None,1,False)
r1=empty(2,0,8,None,False)
r2=empty(3,29,1,None,False)
r3=empty(None,32,2,None,False)
r4=empty(None,None,5,29,False)
r5=empty(4,None,6,0,False)
r6=empty(5,7,None,None,False)
r7=empty(None,None,None,6,False)
r8=empty(1,None,None,9,False)
r9=empty(None,8,10,None,False)
r10=empty(9,None,11,None,False)
r11=empty(10,12,None,None,False)
r12=empty(None,34,None,11,True)
r13=empty(None,14,None,None,False)
r14=empty(None,15,17,13,False)
r15=empty(None,16,29,14,False)
r16=empty(None,None,33,15,False)
r17=empty(14,29,18,None,False)
r18=empty(17,31,None,None,False)
r19=empty(20,29,29,29,False)
r20=empty(None,21,19,None,False)
r21=empty(None,22,29,20,False)
r22=empty(None,None,23,21,False)
r23=empty(22,None,24,29,False)
r24=empty(23,None,25,None,False)
r25=empty(24,None,None,26,False)
r26=empty(None,25,None,27,False)
r27=empty(29,26,None,28,False)
r28=empty(30,27,None,None,False)
rt=termination()
rv=victory()
tel32=teleporter(13,13)
tel33=teleporter(7,7)
tel34=teleporter(19,19)
rkey=keyroom(29,None,None,18)
rooms=[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,rt,rv,rkey,tel32,tel33,tel34]
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
    if x.up==29 or x.left==29 or x.right==29 or x.down==29:
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