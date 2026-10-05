import PySimpleGUI as psg

# kleuren van de rijen
ROOD = '#f42a2a'
GEEL = '#e8b800'
GROEN = '#3fa56a'
BLAUW = '#2a5fb8'

# zo moet ik het lettertype niet bij elke knop zetten
psg.set_options(font=('Arial Bold', 14))

# Alle rode buttons
b_rood2 = psg.Button('2', key='-br2-', button_color=('white', ROOD), size=(3, 1))
b_rood3 = psg.Button('3', key='-br3-', button_color=('white', ROOD), size=(3, 1))
b_rood4 = psg.Button('4', key='-br4-', button_color=('white', ROOD), size=(3, 1))
b_rood5 = psg.Button('5', key='-br5-', button_color=('white', ROOD), size=(3, 1))
b_rood6 = psg.Button('6', key='-br6-', button_color=('white', ROOD), size=(3, 1))
b_rood7 = psg.Button('7', key='-br7-', button_color=('white', ROOD), size=(3, 1))
b_rood8 = psg.Button('8', key='-br8-', button_color=('white', ROOD), size=(3, 1))
b_rood9 = psg.Button('9', key='-br9-', button_color=('white', ROOD), size=(3, 1))
b_rood10 = psg.Button('10', key='-br10-', button_color=('white', ROOD), size=(3, 1))
b_rood11 = psg.Button('11', key='-br11-', button_color=('white', ROOD), size=(3, 1))
b_rood12 = psg.Button('12', key='-br12-', button_color=('white', ROOD), size=(3, 1))

# Alle gele buttons
b_geel2 = psg.Button('2', key='-bg2-', button_color=('white', GEEL), size=(3, 1))
b_geel3 = psg.Button('3', key='-bg3-', button_color=('white', GEEL), size=(3, 1))
b_geel4 = psg.Button('4', key='-bg4-', button_color=('white', GEEL), size=(3, 1))
b_geel5 = psg.Button('5', key='-bg5-', button_color=('white', GEEL), size=(3, 1))
b_geel6 = psg.Button('6', key='-bg6-', button_color=('white', GEEL), size=(3, 1))
b_geel7 = psg.Button('7', key='-bg7-', button_color=('white', GEEL), size=(3, 1))
b_geel8 = psg.Button('8', key='-bg8-', button_color=('white', GEEL), size=(3, 1))
b_geel9 = psg.Button('9', key='-bg9-', button_color=('white', GEEL), size=(3, 1))
b_geel10 = psg.Button('10', key='-bg10-', button_color=('white', GEEL), size=(3, 1))
b_geel11 = psg.Button('11', key='-bg11-', button_color=('white', GEEL), size=(3, 1))
b_geel12 = psg.Button('12', key='-bg12-', button_color=('white', GEEL), size=(3, 1))

# Alle groene buttons
b_groen2 = psg.Button('2', key='-bgr2-', button_color=('white', GROEN), size=(3, 1))
b_groen3 = psg.Button('3', key='-bgr3-', button_color=('white', GROEN), size=(3, 1))
b_groen4 = psg.Button('4', key='-bgr4-', button_color=('white', GROEN), size=(3, 1))
b_groen5 = psg.Button('5', key='-bgr5-', button_color=('white', GROEN), size=(3, 1))
b_groen6 = psg.Button('6', key='-bgr6-', button_color=('white', GROEN), size=(3, 1))
b_groen7 = psg.Button('7', key='-bgr7-', button_color=('white', GROEN), size=(3, 1))
b_groen8 = psg.Button('8', key='-bgr8-', button_color=('white', GROEN), size=(3, 1))
b_groen9 = psg.Button('9', key='-bgr9-', button_color=('white', GROEN), size=(3, 1))
b_groen10 = psg.Button('10', key='-bgr10-', button_color=('white', GROEN), size=(3, 1))
b_groen11 = psg.Button('11', key='-bgr11-', button_color=('white', GROEN), size=(3, 1))
b_groen12 = psg.Button('12', key='-bgr12-', button_color=('white', GROEN), size=(3, 1))

# Alle blauwe buttons
b_blauw2 = psg.Button('2', key='-bb2-', button_color=('white', BLAUW), size=(3, 1))
b_blauw3 = psg.Button('3', key='-bb3-', button_color=('white', BLAUW), size=(3, 1))
b_blauw4 = psg.Button('4', key='-bb4-', button_color=('white', BLAUW), size=(3, 1))
b_blauw5 = psg.Button('5', key='-bb5-', button_color=('white', BLAUW), size=(3, 1))
b_blauw6 = psg.Button('6', key='-bb6-', button_color=('white', BLAUW), size=(3, 1))
b_blauw7 = psg.Button('7', key='-bb7-', button_color=('white', BLAUW), size=(3, 1))
b_blauw8 = psg.Button('8', key='-bb8-', button_color=('white', BLAUW), size=(3, 1))
b_blauw9 = psg.Button('9', key='-bb9-', button_color=('white', BLAUW), size=(3, 1))
b_blauw10 = psg.Button('10', key='-bb10-', button_color=('white', BLAUW), size=(3, 1))
b_blauw11 = psg.Button('11', key='-bb11-', button_color=('white', BLAUW), size=(3, 1))
b_blauw12 = psg.Button('12', key='-bb12-', button_color=('white', BLAUW), size=(3, 1))

# De slotjes zijn knoppen met een afbeelding
b_rood_slot = psg.Button(key='-brSLOT-', image_filename='slot_rood.png', button_color=('white', ROOD), border_width=0)
b_geel_slot = psg.Button(key='-bgSLOT-', image_filename='slot_geel.png', button_color=('white', GEEL), border_width=0)
b_groen_slot = psg.Button(key='-bgrSLOT-', image_filename='slot_groen.png', button_color=('white', GROEN), border_width=0)
b_blauw_slot = psg.Button(key='-bbSLOT-', image_filename='slot_blauw.png', button_color=('white', BLAUW), border_width=0)

b_exit = psg.Button('EXIT', key='-EXIT-')

layout = [[b_rood2, b_rood3, b_rood4, b_rood5, b_rood6, b_rood7,
           b_rood8, b_rood9, b_rood10, b_rood11, b_rood12, b_rood_slot],

          [b_geel2, b_geel3, b_geel4, b_geel5, b_geel6, b_geel7,
           b_geel8, b_geel9, b_geel10, b_geel11, b_geel12, b_geel_slot],

          [b_groen12, b_groen11, b_groen10, b_groen9, b_groen8, b_groen7,
           b_groen6, b_groen5, b_groen4, b_groen3, b_groen2, b_groen_slot],

          [b_blauw12, b_blauw11, b_blauw10, b_blauw9, b_blauw8, b_blauw7,
           b_blauw6, b_blauw5, b_blauw4, b_blauw3, b_blauw2, b_blauw_slot],

          [b_exit]]

window = psg.Window('DEDEM_02_QWIXX', layout)

doorgaan = True
while doorgaan:
    event, values = window.read()

    print(f"event: {event}")
    print(f"values: {values}")

    if event == psg.WIN_CLOSED or event == '-EXIT-':
        doorgaan = False

window.close()