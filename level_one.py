__author__ = 'Slaphsot135'

class room:
    def __init__(self,above,right,below,left):
        self.above=above
        self.right=right
        self.below=below
        self.left=left

r0=room(1,None,None,11)
r1=room(None,2,0,5)
r2=room(3,None,None,1)
r3=room(None,None,2,None)
r4=room(None,None,5,None)
r5=room(4,1,11,6)
r6=room(None,5,7,None)
r7=room(6,11,8,None)
r8=room(7,9,None,None)
r9=room(11,None,10,8)
r10=room(9,12,None,None)
rooms=[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,'death','victory']
global curroom
curroom=0
def UP():
    global curroom
    if rooms[curroom].above:
        curroom=rooms[curroom].above
        print 'above'
    else:
        print 'no above room'
def LEFT():
    global curroom
    if rooms[curroom].left:
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
    if rooms[curroom].below or rooms[curroom].below == 0:
        curroom=rooms[curroom].below
    else:
        print 'no below room'
while True:
    print curroom
    if rooms[curroom]=='death':
        print 'you died'
        break
    elif rooms[curroom]=='victory':
        print 'Congratulations! You Win!'
        break
    else:
        move=raw_input('Which direction do you want to move?>>> ')
        move=move.upper()
        try:
            globals()[move]()
        except:
            print 'no such command'