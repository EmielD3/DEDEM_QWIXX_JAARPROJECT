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

# Functie die een hele rij knoppen maakt en het slotje
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

aantal_missers = 0
misser_knoppen = ['-MIS1-', '-MIS2-', '-MIS3-', '-MIS4-']

layout_missers = [
    psg.Text('Elke mislukte worp -5'),
    psg.Button('', key='-MIS1-', size=(2,1)),
    psg.Button('', key='-MIS2-', size=(2,1)),
    psg.Button('', key='-MIS3-', size=(2,1)),
    psg.Button('', key='-MIS4-', size=(2,1))
]

t_rood = psg.Text('Rood: 0', key='-TROOD-')
t_geel = psg.Text('Geel: 0', key='-TGEEL-')
t_groen = psg.Text('Groen: 0', key='-TGROEN-')
t_blauw = psg.Text('Blauw: 0', key='-TBLAUW-')
t_totaal = psg.Text('Totaal: 0', key='-TTOTAAL-')

# Layout samenstellen
layout = [
    layout_rood,
    layout_geel,
    layout_groen,
    layout_blauw,
    layout_missers,
    [t_rood, t_geel, t_groen, t_blauw, t_totaal],
    [b_exit, b_reset]
]

window = psg.Window('DEDEM_02_QWIXX', layout)
window.finalize()

aantal = {
    'rood': 0,
    'geel': 0,
    'groen': 0,
    'blauw': 0
}

# Dictionary om bij te houden of het slotje van een kleur aan staat (True/False)
slot_aan = {
    'rood': False,
    'geel': False,
    'groen': False,
    'blauw': False
}

def bereken_score(aantal_kruisjes):
    return aantal_kruisjes * (aantal_kruisjes + 1) // 2

def update_scores():
    # Rood tellen
    totaal_rood = aantal['rood']
    if slot_aan['rood']:
        totaal_rood += 1
    score_rood = bereken_score(totaal_rood)

    # Geel tellen
    totaal_geel = aantal['geel']
    if slot_aan['geel']:
        totaal_geel += 1
    score_geel = bereken_score(totaal_geel)

    # Groen tellen
    totaal_groen = aantal['groen']
    if slot_aan['groen']:
        totaal_groen += 1
    score_groen = bereken_score(totaal_groen)

    # Blauw tellen
    totaal_blauw = aantal['blauw']
    if slot_aan['blauw']:
        totaal_blauw += 1
    score_blauw = bereken_score(totaal_blauw)

    strafpunten = aantal_missers * 5

    totaal = (score_rood + score_geel + score_groen + score_blauw - strafpunten)

    window['-TROOD-'].update(f'Rood: {score_rood}')
    window['-TGEEL-'].update(f'Geel: {score_geel}')
    window['-TGROEN-'].update(f'Groen: {score_groen}')
    window['-TBLAUW-'].update(f'Blauw: {score_blauw}')
    window['-TTOTAAL-'].update(f'Totaal: {totaal}')

def update_knop(event):
    if event == '-brSLOT-':
        if aantal['rood'] >= 5 and window['-br12-'].get_text() == 'X':
            slot_aan['rood'] = not slot_aan['rood']
            if slot_aan['rood']:
                window[event].update(disabled=True)
            update_scores()

    elif event == '-bgSLOT-':
        if aantal['geel'] >= 5 and window['-bg12-'].get_text() == 'X':
            slot_aan['geel'] = not slot_aan['geel']
            if slot_aan['geel']:
                window[event].update(disabled=True)
            update_scores()

    elif event == '-bgrSLOT-':
        if aantal['groen'] >= 5 and window['-bgr2-'].get_text() == 'X':
            slot_aan['groen'] = not slot_aan['groen']
            if slot_aan['groen']:
                window[event].update(disabled=True)
            update_scores()

    elif event == '-bbSLOT-':
        if aantal['blauw'] >= 5 and window['-bb2-'].get_text() == 'X':
            slot_aan['blauw'] = not slot_aan['blauw']
            if slot_aan['blauw']:
                window[event].update(disabled=True)
            update_scores()

    else:
        # kruisje verwijderen
        if window[event].get_text() == 'X':
            nummer = haal_nummer_uit_key(event)
            window[event].update(nummer)
            if event in rode_knoppen:
                aantal['rood'] -= 1
            elif event in gele_knoppen:
                aantal['geel'] -= 1
            elif event in groene_knoppen:
                aantal['groen'] -= 1
            elif event in blauwe_knoppen:
                aantal['blauw'] -= 1

        # kruisje zetten
        else:
            window[event].update('X')
            if event in rode_knoppen:
                aantal['rood'] += 1
            elif event in gele_knoppen:
                aantal['geel'] += 1
            elif event in groene_knoppen:
                aantal['groen'] += 1
            elif event in blauwe_knoppen:
                aantal['blauw'] += 1
                
        update_scores()

# Startscores instellen
update_scores()

doorgaan = True
while doorgaan:
    event, values = window.read()
    print(f"event: {event}")
    print(f"values: {values}")

    if event == psg.WIN_CLOSED or event == '-EXIT-':
        doorgaan = False
        
    # Reset alle waarden van de knoppen en missers
    elif event == '-RESET-':
        keuze = psg.popup_yes_no('Ben je zeker dat je alles wilt resetten?')
        if keuze == 'Yes':
            aantal = {'rood': 0, 'geel': 0, 'groen': 0, 'blauw': 0}
            slot_aan = {'rood': False, 'geel': False, 'groen': False, 'blauw': False}
            aantal_missers = 0
        
            for knop_lijst in [rode_knoppen, gele_knoppen, groene_knoppen, blauwe_knoppen]:
                for knop in knop_lijst:
                    nummer = haal_nummer_uit_key(knop)
                    window[knop].update(nummer, disabled=False)
            
            for slot in slotknoppen:
                window[slot].update('', disabled=False)
                
            for misser in misser_knoppen:
                window[misser].update('')
                
            update_scores()

    elif event in misser_knoppen:
        if window[event].get_text() == 'X':
            window[event].update('')
            aantal_missers -= 1
        else:
            window[event].update('X')
            aantal_missers += 1
            
            if aantal_missers == 4:
                psg.popup('Einde spel: 4 missers bereikt.')

        update_scores()

    else:
        update_knop(event)

window.close()