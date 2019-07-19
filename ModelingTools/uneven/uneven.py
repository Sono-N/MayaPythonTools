'''
Randomly shift selected vertices in each direction of xyz in the specified range
'''
import random
from functools import partial
import maya.cmds as cmds

def uneven(*args):
    '''
    Make selected list and move vertices
    '''
    diffx = cmds.floatSliderGrp("xin", q=True, value=True)
    diffy = cmds.floatSliderGrp("yin", q=True, value=True)
    diffz = cmds.floatSliderGrp("zin", q=True, value=True)

    #get selected list
    objlist = cmds.ls(sl=True)
    objname = objlist[0]
    if cmds.objectType(objname, isType='mesh'):
        for name in objlist:
            x = random.uniform(-diffx/2, diffx/2) 
            y = random.uniform(-diffy/2, diffy/2)
            z = random.uniform(-diffz/2, diffz/2)
            print x, y, z
            cmds.move(x, y, z, name, r=True)
    else:
        #get num of vertex
        vnum = cmds.polyEvaluate(v=True)
        #get and change coordinates for every vertex
        for i in range(vnum):
            name = objname + ".vtx[" + str(i) + "]"
            cdn = cmds.pointPosition(name)
            print name
            x = cdn[0] + random.uniform(-diffx/2, diffx/2) 
            y = cdn[1] + random.uniform(-diffy/2, diffy/2)
            z = cdn[2] + random.uniform(-diffz/2, diffz/2)
            print x, y, z
            cmds.move(x, y, z, name)



winname = 'uneven'
#-----check window existance-----
if cmds.window(winname, exists=True):
    cmds.deleteUI(winname)

#-----make window first-----
winname = cmds.window(title="unEvenTool")

cmds.menuBarLayout()

#---int Slider Grp---
cmds.floatSliderGrp("xin", field=True, label='x', minValue=0, maxValue=10,\
    fieldMinValue=0, fieldMaxValue=100, value=0, width=400)
cmds.floatSliderGrp("yin", field=True, label='y', minValue=-0, maxValue=10,\
    fieldMinValue=0, fieldMaxValue=100, value=0, width=400)
cmds.floatSliderGrp("zin", field=True, label='z', minValue=-0, maxValue=10,\
    fieldMinValue=0, fieldMaxValue=100, value=0, width=400)

cmds.button(label='UnevenDo', command=partial(uneven))

cmds.showWindow(winname)
