import streamlit as st
import requests, urllib.parse

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 36px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 15px; border-radius: 12px; border: 2px solid #2E86AB; margin-bottom: 10px; }
.sub-box { background-color: #e3f2fd; padding: 12px; border-radius: 10px; border: 2px solid #2196f3; margin: 8px 0; }
.quiz-box { background-color: #fff8e1; padding: 15px; border-radius: 12px; border: 3px solid #ff9800; margin: 15px 0; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 8px; padding: 8px; font-weight: bold; min-height: 38px; font-size: 12px; }
.stButton > button:hover { background-color: #2E86AB; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App - Mit Quiz</div>', unsafe_allow_html=True)
st.markdown('<div class="search-box">', unsafe_allow_html=True)
thema = st.text_input("Suche", placeholder="", label_visibility="collapsed", key="haupt")
st.markdown('</div>', unsafe_allow_html=True)

def multi_suche(thema):
    try:
        headers = {'User-Agent': 'LernApp/1.0'}
        enc = urllib.parse.quote(thema.replace(" ", "_"))
        r = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers=headers, timeout=5)
        if r.status_code == 200 and 'extract' in r.json():
            d = r.json()
            return [{"titel": d.get("title"), "text": d.get("extract")}]
    except:
        pass
    return []

alle_faecher = {
"Französisch": {
    "Vokabeln": {"text": "le pain Brot la pomme Apfel le livre Buch aller gehen venir kommen faire machen dire sagen voir sehen vouloir wollen pouvoir können manger essen bon gut grand groß ici hier maintenant jetzt", "quiz": [{"q": "le pain =?", "a": ["Brot", "Apfel", "Haus"], "r": 0}, {"q": "aller =?", "a": ["gehen", "kommen", "machen"], "r": 0}]},
    "le la les lui leur": {"text": "LE=ihn/es OHNE a Je LE mange LA=sie Je LA vois LES=sie Plural LUI=ihm/ihr MIT a Person Je parle À Marie->LUI LEUR=ihnen AUX enfants->LEUR", "quiz": [{"q": "Je mange LE pain -> Je __ mange", "a": ["LE", "LUI", "Y"], "r": 0}, {"q": "Je parle À Marie -> Je __ parle", "a": ["LA", "LUI", "LE"], "r": 1}, {"q": "Je parle AUX enfants -> Je __ parle", "a": ["LUI", "LEUR", "LES"], "r": 1}]},
    "y en": {"text": "Y=dort Ort Sache Je vais À Paris->J'Y vais J'Y pense Sache EN=davon J'EN veux J'EN ai 3", "quiz": [{"q": "Je vais À Paris -> J'__ vais", "a": ["Y", "EN", "LE"], "r": 0}, {"q": "J'ai 3 frères Zahl -> J'__ ai 3", "a": ["Y", "EN", "LE"], "r": 1}]},
},
"Spanisch": {
    "Vokabeln Grundlagen": {"text": "el pan Brot la manzana Apfel el libro Buch la casa Haus el agua Wasser el tiempo Zeit ir gehen venir kommen hacer machen decir sagen ver sehen querer wollen poder können tomar nehmen comer essen bueno gut malo schlecht grande pequeño aquí aquí allí dort ahora ahora siempre immer mucho viel", "quiz": [{"q": "el pan =?", "a": ["Brot", "Wasser", "Buch"], "r": 0}, {"q": "ir =?", "a": ["gehen", "kommen", "machen"], "r": 0}, {"q": "la casa =?", "a": ["Haus", "Brot", "Apfel"], "r": 0}]},
    "lo la le les": {"text": "LO=ihn direkt Wen? Veo EL LIBRO->LO veo LA=sie Veo LA CASA->LA veo LE=ihm indirekt Wem? MIT a Hablo A JUAN->LE hablo", "quiz": [{"q": "Veo EL LIBRO -> __ veo", "a": ["LO", "LE", "LA"], "r": 0}, {"q": "Hablo A JUAN -> __ hablo", "a": ["LO", "LE", "LA"], "r": 1}]},
    "se lo doy WICHTIG": {"text": "LE+LO wird SE! FALSCH Le lo doy RICHTIG SE LO DOY! Se los doy Se la doy Me lo da Te lo doy Nos lo da Me lo das", "quiz": [{"q": "Le lo doy ist?", "a": ["FALSCH", "RICHTIG"], "r": 0}, {"q": "Richtig ist?", "a": ["SE LO DOY", "LE LO DOY", "LO LE DOY"], "r": 0}, {"q": "Les doy los libros ->?", "a": ["SE LOS DOY", "LES LOS DOY", "LOS LES DOY"], "r": 0}]},
    "ser estar": {"text": "SER=WAS IST permanent Soy Juan Name Soy de Alemania Herkunft Soy alto Eigenschaft Son las 3 Uhrzeit Es de madera Material ESTAR=WO?WIE?GERADE? Estoy en casa Ort Estoy cansado Zustand Está roto Ergebnis Estoy comiendo gerade estar+gerundio", "quiz": [{"q": "Soy Juan Name = SER oder ESTAR?", "a": ["SER", "ESTAR"], "r": 0}, {"q": "Estoy en casa Ort =?", "a": ["SER", "ESTAR"], "r": 1}, {"q": "Estoy cansado müde Zustand =?", "a": ["SER", "ESTAR"], "r": 1}, {"q": "Son las 3 Uhrzeit =?", "a": ["SER", "ESTAR"], "r": 0}]},
    "por para": {"text": "POR=Grund Durch Dauer Tausch Warum?Wodurch? Gracias POR todo Voy POR la calle durch POR dos horas Dauer 5€ POR libro Tausch PARA=Ziel Zweck Empfänger Frist Wofür? Para comer Zweck Para ti Empfänger Para Madrid Ziel Para mañana Frist", "quiz": [{"q": "Gracias ___ todo (Grund)", "a": ["POR", "PARA"], "r": 0}, {"q": "Esto es ___ comer (Zweck zum Essen)", "a": ["POR", "PARA"], "r": 1}, {"q": "Voy ___ Madrid (Ziel nach Madrid)", "a": ["POR", "PARA"], "r": 1}, {"q": "___ dos horas (Dauer 2 Stunden)", "a": ["POR", "PARA"], "r": 0}]},
    "Zeiten": {"text": "Present yo hablo comí comido Pretérito hablé Imperfecto hablaba iba era Futur hablaré Conditionnel hablaría Perfect he hablado había hablado", "quiz": [{"q": "yo hablo ist?", "a": ["Present ich spreche", "Vergangenheit", "Zukunft"], "r": 0}, {"q": "he hablado ist?", "a": ["Perfect ich habe gesprochen", "Present", "Futur"], "r": 0}]},
},
"Italienisch": {
    "Vokabeln Grundlagen": {"text": "il pane Brot la mela Apfel il libro Buch la casa Haus l'acqua Wasser andare gehen venire kommen fare machen dire sagen vedere sehen volere wollen potere können mangiare essen bere trinken dormire schlafen buono gut grande groß qui hier ora jetzt sempre immer molto viel bene gut", "quiz": [{"q": "il pane =?", "a": ["Brot", "Apfel", "Haus"], "r": 0}, {"q": "andare =?", "a": ["gehen", "kommen", "machen"], "r": 0}, {"q": "la casa =?", "a": ["Haus", "Brot", "Wasser"], "r": 0}]},
    "lo la gli li": {"text": "LO=ihn/es masc Vedo IL LIBRO->LO vedo LA=sie fem Vedo LA CASA->LA vedo LI=sie masc Plural Vedo I LIBRI->LI vedo LE=sie fem Plural Vedo LE CASE->LE vedo GLI=ihm/ihr/ihnen MIT a Parlo A GIOVANNI->GLI parlo Parlo AI bambini->GLI parlo GLI=le+ihm/ihr/ihnen", "quiz": [{"q": "Vedo IL LIBRO -> __ vedo", "a": ["LO", "GLI", "LA"], "r": 0}, {"q": "Parlo A GIOVANNI -> __ parlo", "a": ["LO", "GLI", "LA"], "r": 1}, {"q": "Vedo I LIBRI (Plural masc) -> __ vedo", "a": ["LI", "LO", "GLI"], "r": 0}]},
    "ci ne": {"text": "CI=y dort/daran Ort Sache Vado A Parigi->CI vado Vado A CASA->CI vado CI penso daran Sache NE=en davon de Zahl Voglio DEL pane->NE voglio Ho 3 fratelli Zahl->NE ho 3 NE ho molti viele", "quiz": [{"q": "Vado A Parigi -> __ vado", "a": ["CI", "NE", "LO"], "r": 0}, {"q": "Voglio DEL pane -> __ voglio", "a": ["CI", "NE", "LO"], "r": 1}, {"q": "Ho 3 fratelli -> __ ho 3", "a": ["CI", "NE", "LO"], "r": 1}]},
    "glielo essere stare": {"text": "GLIELO=gli+lo zusammen wie SE LO DOY Glielo do Ich gebe es ihm Glielo dico Ich sage es ihm Me lo da Te lo do Ce lo ha ESSERE=WAS IST permanent Sono Giovanni Name Sono di Germania Herkunft Sono alto Eigenschaft Sono le 3 Uhrzeit! STARE=WO?WIE?GERADE? Sto a casa Ort Sto male krank Zustand Sta rotto kaputt Ergebnis Sto mangiando gerade stare+gerundio Sto leggendo", "quiz": [{"q": "Glielo do bedeutet?", "a": ["Ich gebe es ihm", "Ich gebe ihn", "Ich bin dort"], "r": 0}, {"q": "Sono Giovanni = ESSERE oder STARE?", "a": ["ESSERE permanent", "STARE Ort Zustand"], "r": 0}, {"q": "Sto a casa = ESSERE oder STARE?", "a": ["ESSERE", "STARE Ort"], "r": 1}, {"q": "Sto mangiando =?", "a": ["gerade am Essen stare+gerundio", "permanent"], "r": 0}]},
    "Zeiten": {"text": "Present io parlo mangio Passato prossimo ho parlato ero andato Imperfetto parlavo Futuro parlerò Condizionale parlerei", "quiz": [{"q": "io parlo ist?", "a": ["Present", "Vergangenheit", "Zukunft"], "r": 0}, {"q": "ho parlato ist?", "a": ["Passato prossimo Perfekt", "Present", "Futur"], "r": 0}]},
},
"Latein": {
    "Vokabeln Grundlagen": {"text": "panis Brot malum Apfel liber Buch casa Haus aqua Wasser ire gehen venire kommen facere machen dicere sagen videre sehen velle wollen posse können edere essen bonus gut malus schlecht magnus groß parvus klein novus neu vetus alt pulcher schön felix glücklich hic hier nunc jetzt semper immer multus viel ego ich tu du is ea id er sie es nos wir vos ihr", "quiz": [{"q": "panis =?", "a": ["Brot", "Apfel", "Haus"], "r": 0}, {"q": "ire =?", "a": ["gehen", "kommen", "machen"], "r": 0}, {"q": "ego =?", "a": ["ich", "du", "er"], "r": 0}]},
    "Kasus": {"text": "Nom Wer?Was? Subjekt puella Mädchen Puella videt Das Mädchen sieht Gen Wessen? puellae des Mädchens Filius puellae Sohn des Mädchens Dat Wem? puellae dem Mädchen Do librum puellae Ich gebe dem Mädchen Buch Akk Wen?Was? puellam das Mädchen Video puellam Ich sehe Mädchen Abl Womit?Wo?Wann? cum puella mit Mädchen in villa in Villa", "quiz": [{"q": "Nominativ fragt?", "a": ["Wer?Was?", "Wessen?", "Wem?"], "r": 0}, {"q": "Genitiv fragt?", "a": ["Wessen?", "Wer?", "Wen?"], "r": 0}, {"q": "puellam ist welcher Kasus?", "a": ["Akkusativ", "Nominativ", "Genitiv"], "r": 0}]},
    "Deklinationen": {"text": "1.a puella puellae puellae puellam puella Gen puellae 2.o servus Sklave Gen servi bellum Krieg Gen belli 3.rex König Gen regis corpus Körper Gen corporis caput Kopf Gen capitis 4.u fructus Frucht Gen fructus 5.e res Sache Gen rei dies Tag", "quiz": [{"q": "puella Genitiv?", "a": ["puellae", "puellam", "puella"], "r": 0}, {"q": "servus Genitiv?", "a": ["servi", "servum", "servus"], "r": 0}, {"q": "rex Genitiv?", "a": ["regis", "rex", "regem"], "r": 0}]},
    "AcI": {"text": "AcI Akkusativ mit Infinitiv nach sagen denken wissen Dico eum venire Ich sage dass er kommt wörtlich Ich sage ihn zu kommen eum Akk venire Inf Präsens Dico eum venisse dass er gekommen ist Perfekt Inf Dico eum venturum esse dass er kommen wird Futur Scio eam venire Ich weiß dass sie kommt", "quiz": [{"q": "Dico eum venire =?", "a": ["Ich sage dass er kommt", "Ich komme", "Er sagt"], "r": 0}, {"q": "eum ist im AcI?", "a": ["Akkusativ", "Nominativ", "Genitiv"], "r": 0}]},
    "Gerundium Partizip": {"text": "Gerundium amandum das Lieben Gen amandi Dat amando Akk amandum Abl amando Ad amandum Zum Lieben Causa amandi Wegen des Liebens Partizipien PPA amans liebend Präsens Aktiv amans puella liebendes Mädchen PPP amatus geliebt worden Perfekt Passiv amata puella geliebtes Mädchen PFA amaturus im Begriff zu lieben Futur Aktiv", "quiz": [{"q": "amans =?", "a": ["liebend PPA Präsens Aktiv", "geliebt PPP", "im Begriff zu lieben"], "r": 0}, {"q": "amatus =?", "a": ["geliebt worden PPP Perfekt", "liebend", "im Begriff"], "r": 0}, {"q": "Ad amandum =?", "a": ["Zum Lieben", "des Liebens", "durch Lieben"], "r": 0}]},
    "Konjugationen": {"text": "amo amare amavi amatum lieben moneo monere monui monitum mahnen lego legere legi lectum lesen audio audire audivi auditum hören sum esse fui sein eo ire ii itum gehen", "quiz": [{"q": "amo amare heißt?", "a": ["lieben", "mahnen", "lesen"], "r": 0}, {"q": "sum esse fui =?", "a": ["sein", "gehen", "hören"], "r": 0}]},
},
"Physik": {
    "Mechanik Grundlagen": {"text": "Bewegung Ort Geschwindigkeit v=s/t m/s 100km/h=27,8m/s Beschleunigung a=v/t m/s² Freier Fall s=0,5*g*t² g=9,81 2s Fall 19,6m v=g*t 2s 19,6m/s", "quiz": [{"q": "v=s/t v ist?", "a": ["Geschwindigkeit", "Strecke", "Zeit"], "r": 0}, {"q": "100km/h =? m/s", "a": ["27,8", "100", "360"], "r": 0}, {"q": "Freier Fall s=?", "a": ["0,5*g*t²", "g*t", "v*t"], "r": 0}]},
    "Newton Gesetze": {"text": "Newton1 Trägheit ohne Kraft bleibt Körper in Ruhe oder gleichförmig geradeaus Newton2 F=m*a 1N=1kg*1m/s² Kraft=Masse*Beschleunigung Beispiel 2kg*3m/s²=6N Gewicht Fg=m*g 70kg*9,81=686N a=F/m Newton3 Actio=Reactio Kräfte treten immer paarweise auf Wand drückt dich zurück wie du Wand Rakete stößt Gas nach unten Gas stößt Rakete nach oben", "quiz": [{"q": "Newton2 F=?", "a": ["m*a", "m*g", "s/t"], "r": 0}, {"q": "Gewicht Fg=?", "a": ["m*g", "m*a", "m*s"], "r": 0}, {"q": "Newton3 bedeutet?", "a": ["Actio=Reactio Kraft=Gegenkraft", "F=m*a", "Ohne Kraft Ruhe"], "r": 0}, {"q": "70kg Gewicht?", "a": ["686N", "70N", "9,81N"], "r": 0}]},
    "Energie Leistung": {"text": "Energie Erhaltung Energie bleibt erhalten wird nur umgewandelt nie vernichtet Formen kinetisch Bewegung 0,5*m*v² Auto 1000kg 20m/s 200000J potentiell Höhe m*g*h 70kg 10m 6867J Wärme Licht elektrisch chemisch Leistung P=E/t Watt Watt=Joule/Sekunde kW kWh 1kWh=3,6Mio J 100W Lampe 10h 1kWh", "quiz": [{"q": "Kinetische Energie?", "a": ["0,5*m*v²", "m*g*h", "m*a"], "r": 0}, {"q": "Potentielle Energie?", "a": ["m*g*h", "0,5*m*v²", "F*m"], "r": 0}, {"q": "1kWh =?", "a": ["3,6 Mio Joule", "1000 Joule", "360 Joule"], "r": 0}]},
    "Stromkreis": {"text": "Strom Elektronen fließen U Volt Spannung Druck I Ampere Stromstärke Menge pro Zeit R Ohm Widerstand Hindernis Ohmsches Gesetz R=U/I I=U/R U=R*I Beispiel 12V 3Ω I=4A Reihe Rges=R1+R2 2+3=5Ω Spannung teilt sich Parallel 1/R=1/R1+1/R2 2Ω parallel 2Ω =1Ω Strom teilt sich Leistung P=U*I 230V*10A=2300W Energie kWh Gefahren 50mA schon gefährlich Steckdose 230V", "quiz": [{"q": "Ohm R=U/I? R=?", "a": ["U/I", "U*I", "I/U"], "r": 0}, {"q": "12V 3Ω I=?", "a": ["4A", "36A", "15A"], "r": 0}, {"q": "Reihe 2Ω+3Ω Rges=?", "a": ["5Ω", "1,2Ω", "6Ω"], "r": 0}, {"q": "Parallel 2Ω//2Ω Rges=?", "a": ["1Ω", "4Ω", "2Ω"], "r": 0}, {"q": "P=U*I 230V 10A P=?", "a": ["2300W", "23W", "230W"], "r": 0}]},
    "Optik": {"text": "Licht 300000km/s Reflexion Einfallswinkel=Ausfallswinkel Spiegel Brechung Übergang Luft Glas Wasser Stab knickt Prisma weiß in Farben Regenbogen Linse Sammellinse brennt Brennpunkt Brennweite f=1/D Dioptrien Auge Linse Netzhaut kurzsichtig Brille - weit+ Farben rot 700nm blau 400nm Laser gebündelt monochromatisch", "quiz": [{"q": "Einfallswinkel =?", "a": ["Ausfallswinkel", "doppelter", "halber"], "r": 0}, {"q": "Weißes Licht durch Prisma?", "a": ["Regenbogen Farben", "bleibt weiß", "wird schwarz"], "r": 0}]},
    "Kern Atom": {"text": "Atom Kern Proton+ Neutron Hülle Elektron Kernspaltung Uran235 Neutron spaltet setzt Energie frei E=mc² 1g Uran = 3 Tonnen Kohle Kettenreaktion moderiert Kraftwerk unkontrolliert Bombe Fusion Sonne Wasserstoff zu Helium 15Mio Grad Alpha Beta Gamma Strahlung Halbwertszeit", "quiz": [{"q": "Kernspaltung Brennstoff?", "a": ["Uran235", "Eisen", "Kohle"], "r": 0}, {"q": "E=mc² sagt?", "a": ["Masse ist Energie", "F=m*a", "v=s/t"], "r": 0}]},
},
"Deutsch": {"Konjunktiv": {"text": "er sei er habe er solle Wenn I=Indikativ dann II hätten", "quiz": [{"q": "Konjunktiv I wofür?", "a": ["indirekte Rede", "irreal"], "r": 0}]}},
"Mathe": {"Brüche": {"text": "1/4+2/4=3/4", "quiz": [{"q": "1/4+2/4?", "a": ["3/4", "3/8"], "r": 0}]}},
"Geschichte": {"mauer": {"text": "Mauer 13.8.61-9.11.89 28J", "quiz": [{"q": "Wann Mauerbau?", "a": ["13.8.61", "1989"], "r": 0}]}},
"Geographie": {"Platten": {"text": "5cm/Jahr", "quiz": [{"q": "5cm/Jahr was?", "a": ["Platten", "Wachstum"], "r": 0}]}},
"Biologie": {"Zelle": {"text": "Mito Kraftwerk", "quiz": [{"q": "Kraftwerk?", "a": ["Mito", "Kern"], "r": 0}]}},
"Chemie": {"Atombau": {"text": "Proton+ Neutron Elektron", "quiz": [{"q": "Proton?", "a": ["positiv", "negativ"], "r": 0}]}},
}

if thema:
    st.write("---")
    for erg in multi_suche(thema):
        st.info(f"{erg['titel']}: {erg['text']}")

st.write("---")
st.markdown("### 📖 Fächer:")

cols = st.columns(3)
fach_liste = list(alle_faecher.keys())
for i, fach_name in enumerate(fach_liste):
    if cols[i % 3].button(fach_name, key=f"btn_{fach_name}"):
        st.session_state['fach'] = fach_name
        st.session_state.pop('unter', None)

if 'fach' in st.session_state:
    fach = st.session_state['fach']
    st.write("---")
    st.markdown(f"## 📚 {fach}")

    sub_suche = st.text_input(f"In {fach} suchen", placeholder="", key="sub_suche", label_visibility="collapsed")

    unter_dict = alle_faecher[fach]
    anzeige = {}
    if sub_suche:
        ss = sub_suche.lower()
        for k,v in unter_dict.items():
            if ss in k.lower() or ss in v["text"].lower():
                anzeige[k]=v
    else:
        anzeige = unter_dict

    if not sub_suche:
        u_cols = st.columns(2)
        for j, (u_name, u_data) in enumerate(unter_dict.items()):
            if u_cols[j % 2].button(u_name, key=f"u_{fach}_{u_name}"):
                st.session_state['unter'] = u_name
                st.session_state['q_idx'] = 0
                st.session_state['q_score'] = 0

    # ZEIGE UNTERTHEMA MIT QUIZ FIX
    if 'unter' in st.session_state and st.session_state['unter'] in unter_dict:
        u_name = st.session_state['unter']
        u_data = unter_dict[u_name]
        st.write("---")
        st.markdown(f"### {u_name}")
        st.write(u_data["text"])

        # QUIZ IMMER ANZEIGEN - FIX!
        if "quiz" in u_data:
            st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
            st.markdown(f"### 🎯 Quiz: {u_name}")

            quiz_list = u_data["quiz"]
            idx = st.session_state.get('q_idx', 0)
            score = st.session_state.get('q_score', 0)

            if idx < len(quiz_list):
                fr = quiz_list[idx]
                st.markdown(f"**Frage {idx+1}/{len(quiz_list)}: {fr['q']}**")
                st.caption(f"Score: {score}/{len(quiz_list)}")
                for o_idx, opt in enumerate(fr['a']):
                    if st.button(opt, key=f"quiz_{u_name}_{idx}_{o_idx}"):
                        if o_idx == fr['r']:
                            st.success(f"✅ Richtig! {opt}")
                            st.session_state['q_score'] = score + 1
                        else:
                            st.error(f"❌ Falsch! Richtig: {fr['a'][fr['r']]}")
                        st.session_state['q_idx'] = idx + 1
                        st.rerun()
            else:
                st.markdown(f"## 🎉 Fertig! {score}/{len(quiz_list)}")
                if score == len(quiz_list):
                    st.balloons()
                    st.success("🌟 PERFEKT! Alles richtig!")
                elif score >= len(quiz_list)/2:
                    st.success(f"Gut! {score}/{len(quiz_list)}")
                else:
                    st.warning(f"Üben! {score}/{len(quiz_list)}")
                if st.button("🔄 Nochmal", key=f"again_{u_name}"):
                    st.session_state['q_idx'] = 0
                    st.session_state['q_score'] = 0
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    if sub_suche:
        for u_name, u_data in anzeige.items():
            st.write("---")
            st.markdown(f"### {u_name}")
            st.write(u_data["text"])
            if "quiz" in u_data:
                if st.button(f"Quiz starten: {u_name}", key=f"sq_{u_name}"):
                    st.session_state['unter'] = u_name
                    st.session_state['q_idx'] = 0
                    st.session_state['q_score'] = 0
                    st.rerun()

    if st.button("❌ Schließen"):
        for k in ['fach','unter','q_idx','q_score']:
            st.session_state.pop(k, None)
        st.rerun()
