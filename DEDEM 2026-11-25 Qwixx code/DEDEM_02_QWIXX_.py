import PySimpleGUI as psg

# kleuren van de rijen
ROOD = '#f42a2a'
GEEL = '#e8b800'
GROEN = '#3fa56a'
BLAUW = '#2a5fb8'
ZWART = '#000000'
WIT = '#FFFFFF'

# zo moet ik het lettertype niet bij elke knop zetten
psg.set_options(font=('Arial Bold', 14))

# Lijsten met sleutels per kleur 
rode_knoppen = ['-br2-', '-br3-', '-br4-', '-br5-', '-br6-', '-br7-',
                '-br8-', '-br9-', '-br10-', '-br11-', '-br12-']

gele_knoppen = ['-bg2-', '-bg3-', '-bg4-', '-bg5-', '-bg6-', '-bg7-',
                '-bg8-', '-bg9-', '-bg10-', '-bg11-', '-bg12-']

groene_knoppen = ['-bgr12-', '-bgr11-', '-bgr10-', '-bgr9-', '-bgr8-', '-bgr7-',
                  '-bgr6-', '-bgr5-', '-bgr4-', '-bgr3-', '-bgr2-']

blauwe_knoppen = ['-bb12-', '-bb11-', '-bb10-', '-bb9-', '-bb8-', '-bb7-',
                  '-bb6-', '-bb5-', '-bb4-', '-bb3-', '-bb2-']

def haal_nummer_uit_key(key):
    tekst = key.strip('-')
    cijfers = '0123456789'
    nummer = ''
    
    for karakter in tekst:
        if karakter in cijfers:
            nummer += karakter
    return nummer

# Functie die een hele rij knoppen maakt en het slotje met het idee van de toets dat het makkelijker ging
def maak_rij_knoppen(knoppen_lijst, kleur, slot_key, afbeelding):
    rij = []
    for key in knoppen_lijst:
        nummer = haal_nummer_uit_key(key)
        knop = psg.Button(nummer, key=key, button_color=(WIT, kleur), size=(3, 1))
        rij.append(knop)
    
    slot_knop = psg.Button(key=slot_key, image_filename=afbeelding, button_color=(WIT, kleur))
    rij.append(slot_knop)
    
    return rij

# Maken van de rijen via de functie
layout_rood = maak_rij_knoppen(rode_knoppen, ROOD, '-brSLOT-', 'slot_rood.png')
layout_geel = maak_rij_knoppen(gele_knoppen, GEEL, '-bgSLOT-', 'slot_geel.png')
layout_groen = maak_rij_knoppen(groene_knoppen, GROEN, '-bgrSLOT-', 'slot_groen.png')
layout_blauw = maak_rij_knoppen(blauwe_knoppen, BLAUW, '-bbSLOT-', 'slot_blauw.png')

b_exit = psg.Button('EXIT', key='-EXIT-')
b_reset = psg.Button('RESET', key='-RESET-')

# Alle slotknoppen in een lijst
slotknoppen = ['-brSLOT-', '-bgSLOT-', '-bgrSLOT-', '-bbSLOT-']

# Layout samenstellen
layout = [
    layout_rood,
    layout_geel,
    layout_groen,
    layout_blauw,
    [b_exit, b_reset]]

window = psg.Window('DEDEM_02_QWIXX', layout)
window.finalize()

aantal = {
    'rood': 0,
    'geel': 0,
    'groen': 0,
    'blauw': 0
}

def update_knop(event):

    if event == '-brSLOT-':
        if aantal['rood'] >= 5 and window['-br12-'].get_text() == 'X':
            window[event].update(disabled=True)

    elif event == '-bgSLOT-':
        if aantal['geel'] >= 5 and window['-bg12-'].get_text() == 'X':
            window[event].update(disabled=True)

    elif event == '-bgrSLOT-':
        if aantal['groen'] >= 5 and window['-bgr2-'].get_text() == 'X':
            window[event].update(disabled=True)

    elif event == '-bbSLOT-':
        if aantal['blauw'] >= 5 and window['-bb2-'].get_text() == 'X':
            window[event].update(disabled=True)

    else:
        window[event].update('X', disabled=True)

        if event in rode_knoppen:
            aantal['rood'] += 1

        elif event in gele_knoppen:
            aantal['geel'] += 1

        elif event in groene_knoppen:
            aantal['groen'] += 1

        elif event in blauwe_knoppen:
            aantal['blauw'] += 1

doorgaan = True
while doorgaan:
    event, values = window.read()
    print(f"event: {event}")
    print(f"values: {values}")

    if event == psg.WIN_CLOSED or event == '-EXIT-':
        doorgaan = False
#rese alle waarden van de knoppen
    elif event == '-RESET-':
        keuze = psg.popup_yes_no('ben je zeker dat je alles wilt resetten?')
        if keuze == 'Yes':
            aantal = {'rood': 0, 'geel': 0, 'groen': 0, 'blauw': 0}
        
            for knop_lijst in [rode_knoppen, gele_knoppen, groene_knoppen, blauwe_knoppen]:
                for knop in knop_lijst:
                    nummer = haal_nummer_uit_key(knop)
                    window[knop].update(nummer, disabled=False)
            
            for slot in slotknoppen:
                window[slot].update('', disabled=False)

    else:
        update_knop(event)

window.close()