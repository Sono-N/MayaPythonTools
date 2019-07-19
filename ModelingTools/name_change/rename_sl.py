import maya.cmds as cmds
from functools import partial

def rename_sl(*args):
    new_name = cmds.textField('Rename', q = True, text =True)
    items = cmds.ls(sl=True)
    for item in items:
        cmds.rename(item , new_name)
def replace_sl(*args):
    name_to_replace = cmds.textField('RePlace_before', q = True, text =True)
    replace_name = cmds.textField('RePlace_after', q = True, text =True)
    items = cmds.ls(sl=True)
    for item in items:
        new_name = item.replace(name_to_replace, replace_name)
        cmds.rename(item , new_name)


def rename_sl_ui():
    '''
    main rondom copy function
    '''
    cmds.window()
    cmds.columnLayout()
    cmds.rowLayout(nc=3)
    cmds.text(label='input')
    rename_input = cmds.textField('Rename', text='new_name', ed=True)
    cmds.button(c=rename_sl, label='Rename')
    cmds.setParent('..')
    cmds.rowLayout(nc=5)
    cmds.text(label='before')
    cmds.textField('RePlace_before', text='name', ed=True)
    cmds.text(label='after')
    cmds.textField('RePlace_after', text='new_name', ed=True)
    cmds.button(c=replace_sl, label='Replace')
    cmds.setParent('..')
    #name_button = cmds.textFieldButtonGrp('Rename',label='input', text='name',ed = True, buttonLabel='Rename', bc=rename_sl)
    #name_button = cmds.textFieldButtonGrp('Replace',label='input', text='name',ed = True, buttonLabel='Replace', bc=rename_sl)
    cmds.showWindow()

rename_sl_ui()