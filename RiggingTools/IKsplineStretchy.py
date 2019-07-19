from functools import partial
import maya.cmds as cmds

'''
module to make IKspline stretchy
'''

def make_ikspline_stretchy(*args):
    '''main function to make joints stretching'''
    try:
        #get data of IKfandle and joint
        selected_ikHandle = cmds.ls(sl=True)[0]
        ikJoints = cmds.ikHandle(selected_ikHandle, q=True, jl=True)
        numberOfBones = len(ikJoints)
        ikCurve = cmds.ikHandle(selected_ikHandle, q=True, c=True)
        cmds.rebuildCurve(ikCurve, rt=0, kr=0, d=4, s=1)
        curveInfo = cmds.arclen(ikCurve, ch=True)
        #create Node of length
        multiDivArclen = cmds.shadingNode('multiplyDivide', asUtility=True)
        cmds.setAttr(multiDivArclen+'.operation', 2)
        cmds.addAttr(multiDivArclen, ln="stretchy", at='double', dv=0, k=True)
        #connect curve length 
        cmds.connectAttr(curveInfo+'.arcLength', multiDivArclen+'.input1X', f=True)
        cmds.connectAttr(multiDivArclen+'.outputX', multiDivArclen+'.stretchy', f=True)
        input2X = cmds.getAttr(multiDivArclen+'.input1X')
        cmds.setAttr(multiDivArclen+'.input2X', input2X) #multDivArclen.OutputX == 1
        #create Node of thickness
        multiDivThickness = cmds.shadingNode('multiplyDivide', asUtility=True)
        cmds.setAttr(multiDivThickness+'.operation', 3)
        cmds.connectAttr(multiDivArclen+'.stretchy', multiDivThickness+'.input1X', f=True)
        cmds.setAttr(multiDivThickness+'.input2X', -0.5)
        #cmds.addAttr( multiDivArclen, ln="stretchy", at='double', dv=0, k=True)

        cmds.cluster(ikCurve+'.cv[3]', n="cluster_end")
        cmds.cluster(ikCurve+'.cv[0]', ikCurve+'.cv[1]', ikCurve+'.cv[2]', n="cluster_root")

        for i in range(numberOfBones):
            cmds.connectAttr(multiDivArclen+'.stretchy', ikJoints[i]+'.scaleX', f=True)
            if i > 0 and i < numberOfBones:
                cmds.connectAttr(multiDivThickness+'.outputX', ikJoints[i]+'.scaleY', f=True)
                cmds.connectAttr(multiDivThickness+'.outputX', ikJoints[i]+'.scaleZ', f=True)
            #cmds.connectAttr( outMultDiv+'.outputX', item+'.scaleX', f=True)
    except:
        print "no curve selected"

def make_ikspline_stretchy_UI():
    '''
    Make int Field
    '''
    cmds.window()
    cmds.columnLayout()
    cmds.button(label="select IKspline to be stretchy", command=partial(make_ikspline_stretchy))
    cmds.showWindow()

make_ikspline_stretchy_UI()