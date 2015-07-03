__author__ = 'Slaphsot135'
import random,time
class room(object):
    def __init__(self,message,death,Victory,teleport):
        self.message=message
        self.death=death
        self.victory=Victory
        self.teleport=teleport


class empty(room):
    def __init__(self,up,right,down,left):
        room.__init__(self,'Empty Room',False,False,False)
        self.up=up
        self.right=right
        self.down=down
        self.left=left

class termination(room):
    def __init__(self):
        room.__init__(self,'You Died',True,False,False)
class victory(room):
    def __init__(self):
        room.__init__(self,'Congratulations! You Win!',False,True,False)
class teleporter(room):
    def __init__(self):
        room.__init__(self,'Teleporting...',False,False,True)
    def teleportit(self):
        global curroom
        curroom=random.randint(0,13)



r0=empty(None,1,None,11)
r1=empty(None,None,2,0)
r2=empty(1,3,21,None)
r3=empty(None,None,4,2)
r4=empty(3,None,5,21)
r5=empty(4,None,None,6)
r6=empty(21,5,None,7)
r7=empty(19,6,None,8)
r8=empty(9,7,None,None)
r9=empty(10,19,8,13)
r10=empty(11,None,9,19)
r11=empty(None,0,10,12)
r12=empty(19,11,19,19)
r13=empty(19,9,None,15)
r14=empty(19,19,15,None)
r15=empty(14,13,16,None)
r16=empty(15,None,19,17)
r17=empty(None,16,18,None)
r18=empty(17,19,20,None)
rt=termination()
rv=victory()
tel=teleporter()
rooms=[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,rt,rv,tel]
global curroom
curroom=0
def UP():
    global curroom
    if rooms[curroom].up:
        curroom=rooms[curroom].up
    else:
        print 'no above room'
def LEFT():
    global curroom
    if rooms[curroom].left or rooms[curroom].left == 0:
        curroom=rooms[curroom].left
    else:
        print 'no left room'
def RIGHT():
    global curroom
    if rooms[curroom].right:
        curroom=rooms[curroom].right
    else:
        print 'no right room'
def DOWN():
    global curroom
    if rooms[curroom].down or rooms[curroom].down == 0:
        curroom=rooms[curroom].down
    else:
        print 'no below room'
while True:
    print curroom
    x=rooms[curroom]
    print x.message
    if x.death or x.victory:
        break
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