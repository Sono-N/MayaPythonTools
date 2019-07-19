'''
    this module makes helix curve
'''
import math
import maya.cmds as cmds

def helix(radius, pitch, sr, sp, ncvs,*args):
    '''
    create helix curve
    '''
    deg = 3
    spas = ncvs - deg
    knots = ncvs + deg -1
    points = []
    points.append((radius, 0, 0.5))
    #cmds.joint(p=(0,0,0))
    d = 1
    for i in range(ncvs):
        radius = radius*sr
        pitch = pitch*sp
        x = radius * math.cos(i)
        y = pitch * i
        z = -radius * math.sin(i)
        if i%d == 0:
            points.append((x, y, z))
    cmds.curve(d=3, p=points)

def do_helix(*args):
    radius = cmds.floatField("radius", value=True, q=True)
    pitch = cmds.floatField("pitch", value=True, q=True)
    sr = cmds.floatField("sr", value=True, q=True)
    sp = cmds.floatField("sp", value=True, q=True)
    ncv = cmds.intField("ncv", value=True, q=True)
    helix(radius, pitch, sr, sp, ncv)


def do_helix_UI():
    '''
    main rondom copy function
    '''
    cmds.window()
    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.text(label="radius")
    cmds.floatField("radius", value=3)
    cmds.text(label="pitch")
    cmds.floatField("pitch", value=0.4)
    cmds.text(label="sr")
    cmds.floatField("sr", value=1.0)
    cmds.text(label="sp")
    cmds.floatField("sp", value=1.0)
    cmds.text(label="ncv")
    cmds.intField("ncv", value=20)
    cmds.text(label="execute")
    cmds.button(label="DoHelix", command=do_helix)
    cmds.showWindow()

do_helix_UI()