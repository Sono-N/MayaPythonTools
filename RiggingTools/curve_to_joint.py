'''
Module to create joints with given number of spans from a curve
'''
from functools import partial
import maya.cmds as cmds

def curve_to_joint(spans, *args):
    '''main function to create joint chain from NurbsCurve'''
    try:
        objlist = cmds.ls(sl=True)
        curve = objlist[0]
        #cmds.objectType(curve, isType='nurbsCurve')):
        d_curve=cmds.duplicate()
        if not isinstance(spans, int):
            spans = int(cmds.intField(spans, q=True, v=True))
        print "span is " + str(spans)
        cmds.rebuildCurve(d_curve, rt=0, kr=2, s=spans-1)
        for i in range(spans):
            position = cmds.pointOnCurve(d_curve, pr=i, p=True)
            cmds.joint(p=position)
        cmds.delete(d_curve)
    except:
        print "No curve Selected"

def curve_to_joint_UI():
    '''
    Make int Field
    '''
    cmds.window()
    cmds.columnLayout()
    num = cmds.intField(minValue=0)
    cmds.button(label="Curve to Joint", command=partial(curve_to_joint, num))
    cmds.showWindow()

curve_to_joint_UI()