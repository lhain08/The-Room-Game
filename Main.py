__author__ = 'Slaphsot135'
import os
def delete_module(modname, paranoid=None):
    from sys import modules
    try:
        thismod = modules[modname]
    except KeyError:
        raise ValueError(modname)
    these_symbols = dir(thismod)
    if paranoid:
        try:
            paranoid[:]  # sequence support
        except:
            raise ValueError('must supply a finite list for paranoid')
        else:
            these_symbols = paranoid[:]
    del modules[modname]
    for mod in modules.values():
        try:
            delattr(mod, modname)
        except AttributeError:
            pass
        if paranoid:
            for symbol in these_symbols:
                if symbol[:2] == '__':  # ignore special symbols
                    continue
                try:
                    delattr(mod, symbol)
                except AttributeError:
                    pass
while True:
    lvls=[]
    print 'for a list of levels enter "Rooms"'
    level=raw_input('choose Level(level_one, level_two...)>>')
    if level.upper()=='ROOMS':
        listlevels=os.listdir(os.getcwd())
        for i,x in enumerate(listlevels):
            if 'Main' in x or x=='.idea' or '.pyc' in x:
                listlevels.pop(i)
        listlevels.pop()
        print listlevels
    else:

        import importlib
        try:
            if level in lvls:
                reload(level)
            else:
                importlib.import_module(level)
                lvls.append(level)

            delete_module(level)
        except:
            print 'failure'
        t=raw_input('Try again?>>>')
        if t.upper()=='YES' or t.upper()=='Y':
            xx=None
        elif t.upper()=='NO' or t.upper()=='N':
            print 'Goodbye'
            break