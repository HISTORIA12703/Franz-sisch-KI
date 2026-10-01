import streamlit as st
import requests, urllib.parse, random

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 38px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 15px; border-radius: 12px; border: 2px solid #2E86AB; margin-bottom: 10px; }
.sub-box { background-color: #e3f2fd; padding: 12px; border-radius: 10px; border: 2px solid #2196f3; margin: 8px 0; }
.quiz-box { background-color: #fff8e1; padding: 15px; border-radius: 10px; border: 2px solid #ffc107; margin: 10px 0; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 8px; padding: 6px; font-weight: bold; min-height: 38px; font-size: 12px; }
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
            return [{"quelle": "Wikipedia", "titel": d.get("title"), "text": d.get("extract")}]
    except:
        pass
    return []

# ALLE FÄCHER MIT UNTERBEGRIFFEN + QUIZ
alle_faecher = {
"Französisch": {
    "Vokabeln": {"text": "le pain Brot la pomme Apfel le livre Buch la maison Haus aller gehen venir kommen faire machen dire sagen voir sehen vouloir wollen pouvoir können manger essen bon gut grand groß ici hier maintenant jetzt", "quiz": [{"q": "Was heißt le pain?", "a": ["Brot", "Apfel", "Haus", "Wasser"], "r": 0}, {"q": "Was heißt aller?", "a": ["gehen", "kommen", "machen", "sehen"], "r": 0}]},
    "le la les lui leur": {"text": "LE=ihn/es OHNE a Je LE mange LA=sie Je LA vois LES=sie Plural LUI=ihm/ihr MIT a Je parle À Marie->LUI LEUR=ihnen AUX enfants->LEUR", "quiz": [{"q": "Je mange LE pain -> Je __ mange", "a": ["LE", "LUI", "Y", "EN"], "r": 0}, {"q": "Je parle À Marie -> Je __ parle", "a": ["LE", "LUI", "LA", "Y"], "r": 1}, {"q": "Je parle AUX enfants -> Je __ parle", "a": ["LUI", "LEUR", "LES", "Y"], "r": 1}]},
    "y en": {"text": "Y=dort Ort Sache Je vais À Paris->J'Y vais J'Y pense Sache EN=davon J'EN veux J'EN ai 3", "quiz": [{"q": "Je vais À Paris -> J'__ vais", "a": ["Y", "EN", "LUI", "LE"], "r": 0}, {"q": "Je veux DU pain -> J'__ veux", "a": ["Y", "EN", "LE", "LUI"], "r": 1}]},
    "Reihenfolge": {"text": "me te se nous vous + le la les + lui leur + y + en + VERB Il ME LE donne Il Y EN a", "quiz": [{"q": "Richtige Reihenfolge?", "a": ["le la les + lui leur + y + en + VERB", "y + en + le la + VERB", "lui leur + me te + VERB"], "r": 0}]},
    "indirekte Rede": {"text": "Il dit qu'il est malade bleibt Il a dit qu'il ÉTAIT malade Present->Imparfait Que->ce que Si->si Befehl de venir", "quiz": [{"q": "Il dit: Je suis malade -> Il dit qu'il __ malade (sagt jetzt)", "a": ["est", "était", "sera", "a été"], "r": 0}, {"q": "Il a dit: Je suis malade -> Il a dit qu'il __ malade (sagte früher)", "a": ["est", "était", "sera", "est"], "r": 1}]},
},
"Spanisch": {
    "Vokabeln": {"text": "el pan Brot la manzana Apfel ir gehen venir kommen hacer machen decir sagen ver sehen querer wollen poder können", "quiz": [{"q": "el pan?", "a": ["Brot", "Apfel", "Buch", "Haus"], "r": 0}]},
    "se lo doy": {"text": "LE+LO wird SE! FALSCH Le lo doy RICHTIG SE LO DOY! Se los doy Me lo da", "quiz": [{"q": "FALSCH oder RICHTIG: Le lo doy", "a": ["FALSCH", "RICHTIG"], "r": 0}, {"q": "Richtig ist?", "a": ["SE LO DOY", "LE LO DOY", "LO LE DOY"], "r": 0}]},
    "ser estar": {"text": "SER=WAS IST permanent Soy Juan ESTAR=WO WIE GERADE Estoy en casa Estoy cansado Está roto Estoy comiendo", "quiz": [{"q": "Soy alto = SER oder ESTAR?", "a": ["SER permanent", "ESTAR Zustand"], "r": 0}, {"q": "Estoy en casa = SER oder ESTAR?", "a": ["SER", "ESTAR Ort"], "r": 1}, {"q": "Estoy cansado =?", "a": ["SER", "ESTAR Zustand"], "r": 1}]},
    "por para": {"text": "POR=Grund Durch Dauer Gracias POR todo Voy POR calle POR 2 horas PARA=Ziel Zweck Para comer Para ti Para Madrid Para mañana", "quiz": [{"q": "Gracias ___ todo (Grund)", "a": ["POR", "PARA"], "r": 0}, {"q": "Esto es ___ comer (Zweck)", "a": ["POR", "PARA"], "r": 1}]},
},
"Englisch": {
    "Zeiten": {"text": "Present I go he goes Past I went Perfect I have gone have+PP since for Past Perfect I had gone Future will going to", "quiz": [{"q": "He __ every day (Gewohnheit)", "a": ["goes", "went", "has gone", "will go"], "r": 0}, {"q": "Signal für Present Perfect?", "a": ["already yet since for", "yesterday", "tomorrow"], "r": 0}]},
    "if Sätze": {"text": "Type0 If you heat water it boils Type1 If I GO I WILL go Type2 If I WENT I WOULD go Type3 If I HAD GONE I WOULD HAVE GONE", "quiz": [{"q": "If I GO I __ go (Type1 möglich)", "a": ["WILL", "WOULD", "WOULD HAVE GONE"], "r": 0}, {"q": "If I WENT I __ go (Type2 irreal jetzt)", "a": ["WILL", "WOULD", "WOULD HAVE GONE"], "r": 1}]},
    "Passive": {"text": "be+PP IS MADE WAS MADE HAS BEEN MADE WILL BE MADE BY ME", "quiz": [{"q": "Active I make a cake -> Passive A cake __ MADE", "a": ["IS", "WAS", "HAS BEEN"], "r": 0}]},
},
"Mathe": {
    "Brüche": {"text": "1/4+2/4=3/4 1/2+1/3=5/6 Multi 3/8 Divi Kehrwert 2 Prozent /100", "quiz": [{"q": "1/4+2/4=?", "a": ["3/4", "3/8", "2/4", "1/4"], "r": 0}, {"q": "1/2:1/4=?", "a": ["2", "1/8", "1/4", "1/2"], "r": 0}]},
    "Gleichungen": {"text": "2x+4=10 x=3 Mitternacht x=(-b±√(b²-4ac))/2a pq", "quiz": [{"q": "2x+4=10 x=?", "a": ["3", "5", "7", "2"], "r": 0}, {"q": "Mitternacht x=?", "a": ["(-b±√(b²-4ac))/2a", "a+b", "a*b"], "r": 0}]},
    "Pythagoras": {"text": "a²+b²=c² nur 90° 3²+4²=5²", "quiz": [{"q": "a²+b²=?", "a": ["c²", "a²", "b²"], "r": 0}, {"q": "3 4 5 gilt weil?", "a": ["9+16=25", "3+4=5", "3*4=5"], "r": 0}]},
    "Ableitung": {"text": "x^n->n*x^(n-1) x³->3x² f'=0 Extrem", "quiz": [{"q": "x³ abgeleitet?", "a": ["3x²", "x²", "3x", "x³"], "r": 0}]},
},
"Geschichte": {
    "französische revolution": {"text": "1789 3.Stand 97% Bastille 14.7. Menschenrechte Ludwig geköpft Napoleon", "quiz": [{"q": "Wann Bastille?", "a": ["14.7.1789", "1789", "1799", "1815"], "r": 0}, {"q": "Wer war 97%?", "a": ["3.Stand Bürger", "1.Stand Klerus", "2.Stand Adel"], "r": 0}]},
    "1 weltkrieg": {"text": "1914-18 Sarajevo Princip Franz Ferdinand Schützengraben Verdun 700k Versailles 17Mio", "quiz": [{"q": "Auslöser 1.WK?", "a": ["Attentat Sarajevo", "Bastille", "Mauerfall"], "r": 0}, {"q": "Wann Waffenstillstand?", "a": ["11.11.1918", "1914", "1939"], "r": 0}]},
    "2 weltkrieg": {"text": "1939-45 Polen Holocaust 6Mio Hiroshima 60Mio", "quiz": [{"q": "Beginn 2.WK?", "a": ["1.9.1939 Polen", "1914", "1945"], "r": 0}, {"q": "Holocaust wie viele Juden?", "a": ["6Mio", "1Mio", "10000"], "r": 0}]},
    "mauer": {"text": "Mauer 13.8.61-9.11.89 28J 155km 140 Tote Einheit 3.10.90", "quiz": [{"q": "Wann Mauerbau?", "a": ["13.8.1961", "1989", "1945"], "r": 0}, {"q": "Wie lange Mauer?", "a": ["28 Jahre", "10 Jahre", "5 Jahre"], "r": 0}]},
},
"Geographie": {
    "Plattentektonik": {"text": "Kruste 5-70km Mantel 2900km Kern 5cm/Jahr divergent Rücken konvergent Himalaya Erdbeben Richter", "quiz": [{"q": "Wie schnell Platten?", "a": ["5cm/Jahr", "5m/Jahr", "5km/Jahr"], "r": 0}, {"q": "Wo entsteht Himalaya?", "a": ["Kollision Kontinent Kontinent", "Auseinander"], "r": 0}]},
    "Klima": {"text": "Wetter täglich Klima 30J CO2 280->420 +1,2°C", "quiz": [{"q": "Klima ist?", "a": ["30 Jahre Durchschnitt", "Heute Regen", "Morgen Sonne"], "r": 0}, {"q": "CO2 früher heute?", "a": ["280->420 ppm", "gleich", "weniger"], "r": 0}]},
},
"Biologie": {
    "Zelle": {"text": "Mitochondrien Kraftwerk ATP Zucker+O2->CO2+H2O+36 ATP Ribosomen Protein ER Straße Golgi Post", "quiz": [{"q": "Kraftwerk Zelle?", "a": ["Mitochondrien", "Kern", "Membran"], "r": 0}, {"q": "Mitochondrien macht?", "a": ["ATP Energie", "DNA", "Zucker"], "r": 0}]},
    "Fotosynthese": {"text": "6CO2+6H2O+Licht->Zucker+O2 Chloroplast Thylakoid O2 aus Wasser", "quiz": [{"q": "Fotosynthese Formel?", "a": ["6CO2+6H2O->Zucker+O2", "Zucker+O2->CO2+H2O", "H2O->O2"], "r": 0}, {"q": "O2 kommt aus?", "a": ["Wasser H2O", "CO2", "Zucker"], "r": 0}]},
    "Genetik": {"text": "DNA A-T C-G 46 Chromosomen Mitose 1->2 Meiose 1->4 Mendel 3:1", "quiz": [{"q": "DNA A paart mit?", "a": ["T", "C", "G", "A"], "r": 0}, {"q": "Wie viele Chromosomen Mensch?", "a": ["46", "23", "100"], "r": 0}]},
},
"Physik": {
    "Newton": {"text": "F=m*a Gewicht m*g g=9,81 v=s/t s=0,5*g*t²", "quiz": [{"q": "F=?", "a": ["m*a", "m+g", "m/g"], "r": 0}, {"q": "g=?", "a": ["9,81 m/s²", "10 m/s² genau", "5"], "r": 0}]},
    "Strom": {"text": "R=U/I Reihe R1+R2 Parallel 1/R=1/R1+1/R2 P=U*I", "quiz": [{"q": "R=U/I? R=?", "a": ["U/I", "U*I", "U+I"], "r": 0}, {"q": "Reihe 2Ω+3Ω=?", "a": ["5Ω", "1Ω", "6Ω"], "r": 0}]},
},
"Chemie": {
    "Atombau": {"text": "Proton+ 1u Neutron 1u Elektron 1/1836 Ordnungszahl=Protonen Gruppe1 +1 Gruppe17 -1 Gruppe18 8 stabil", "quiz": [{"q": "Proton Ladung?", "a": ["positiv +1", "negativ", "neutral"], "r": 0}, {"q": "Elektron Masse vs Proton?", "a": ["1/1836 viel kleiner", "gleich", "größer"], "r": 0}]},
    "pH Säuren": {"text": "pH 0-6 sauer 7 neutral 8-14 basisch HCl stark NaOH stark Neutralisation HCl+NaOH->NaCl+H2O", "quiz": [{"q": "pH 1 ist?", "a": ["sauer", "neutral", "basisch"], "r": 0}, {"q": "Neutralisation Säure+Base->?", "a": ["Salz+Wasser", "nur Wasser", "nur Salz"], "r": 0}]},
    "Redox": {"text": "Oxidation e- abgeben Zahl steigt Reduktion e- aufnehmen OIL RIG Rost 4Fe+3O2->2Fe2O3", "quiz": [{"q": "Oxidation ist?", "a": ["e- abgeben", "e- aufnehmen", "nichts"], "r": 0}]},
},
"Deutsch": {
    "Konjunktiv": {"text": "er sei er habe er solle Wenn I=Indikativ dann II hätten", "quiz": [{"q": "sie sagt sie sei krank = Konjunktiv?", "a": ["I indirekte", "II irreal"], "r": 0}]},
},
"Italienisch": {
    "ci ne glielo": {"text": "CI=y NE=en Glielo do ESSERE permanent STARE Ort Zustand", "quiz": [{"q": "CI entspricht französisch?", "a": ["Y", "EN", "LE"], "r": 0}]},
},
"Latein": {
    "Kasus": {"text": "Nom Wer? Gen Wessen? Dat Wem? Akk Wen? Abl Womit? puella puellae puellae puellam puella", "quiz": [{"q": "Genitiv Wessen? puellae?", "a": ["des Mädchens", "das Mädchen", "dem Mädchen"], "r": 0}]},
},
}

if thema:
    st.write("---")
    for erg in multi_suche(thema):
        st.info(f"{erg['titel']}: {erg['text']}")

st.write("---")
st.markdown("### 📖 Alle 12 Fächer mit Quiz:")

cols = st.columns(3)
fach_liste = list(alle_faecher.keys())
for i, fach_name in enumerate(fach_liste):
    if cols[i % 3].button(fach_name, key=f"btn_{fach_name}"):
        st.session_state['fach'] = fach_name
        st.session_state.pop('unter', None)
        st.session_state.pop('quiz_idx', None)

if 'fach' in st.session_state:
    fach = st.session_state['fach']
    st.write("---")
    st.markdown(f"## 📚 {fach}")

    st.markdown('<div class="sub-box">', unsafe_allow_html=True)
    sub_suche = st.text_input(f"In {fach} suchen:", placeholder="", key="sub_suche", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    unter_dict = alle_faecher[fach]
    anzeige = {}

    if sub_suche:
        ss = sub_suche.lower()
        for u_name, u_data in unter_dict.items():
            if ss in u_name.lower() or ss in u_data["text"].lower():
                anzeige[u_name] = u_data
    else:
        anzeige = unter_dict

    if not sub_suche:
        u_cols = st.columns(2)
        for j, (u_name, u_data) in enumerate(unter_dict.items()):
            if u_cols[j % 2].button(u_name, key=f"u_{fach}_{u_name}"):
                st.session_state['unter'] = u_name
                st.session_state['quiz_idx'] = 0
                st.session_state['quiz_score'] = 0

    # Zeige ausgewähltes Unterthema
    if 'unter' in st.session_state and st.session_state['unter'] in unter_dict:
        u_name = st.session_state['unter']
        u_data = unter_dict[u_name]
        st.write("---")
        st.markdown(f"### {u_name}")
        st.write(u_data["text"])

        # Internet Fakten
        for erg in multi_suche(f"{u_name} {fach}"):
            st.caption(f"🌐 {erg['titel']}: {erg['text'][:200]}...")

        # QUIZ BEREICH
        if "quiz" in u_data and u_data["quiz"]:
            st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
            st.markdown(f"### 🎯 Quiz zu {u_name}")

            quiz_list = u_data["quiz"]
            idx = st.session_state.get('quiz_idx', 0)
            score = st.session_state.get('quiz_score', 0)

            if idx < len(quiz_list):
                frage = quiz_list[idx]
                st.markdown(f"**Frage {idx+1}/{len(quiz_list)}: {frage['q']}**")
                st.write(f"Score: {score}/{len(quiz_list)}")

                for opt_idx, opt in enumerate(frage['a']):
                    if st.button(opt, key=f"quiz_{u_name}_{idx}_{opt_idx}"):
                        if opt_idx == frage['r']:
                            st.success("✅ Richtig!")
                            st.session_state['quiz_score'] = score + 1
                        else:
                            st.error(f"❌ Falsch! Richtig wäre: {frage['a'][frage['r']]}")
                        st.session_state['quiz_idx'] = idx + 1
                        st.rerun()
            else:
                st.markdown(f"### 🎉 Fertig! Score: {score}/{len(quiz_list)}")
                if score == len(quiz_list):
                    st.balloons()
                    st.success("Perfekt! Alles richtig! 🌟")
                elif score >= len(quiz_list)/2:
                    st.success(f"Gut gemacht! {score}/{len(quiz_list)} richtig!")
                else:
                    st.warning(f"Nochmal üben! {score}/{len(quiz_list)}")

                if st.button("🔄 Nochmal", key=f"retry_{u_name}"):
                    st.session_state['quiz_idx'] = 0
                    st.session_state['quiz_score'] = 0
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    # Wenn Suche aktiv und mehrere Treffer
    if sub_suche and anzeige:
        for u_name, u_data in anzeige.items():
            st.markdown(f"### {u_name}")
            st.write(u_data["text"])
            if "quiz" in u_data and st.button(f"Quiz zu {u_name} starten", key=f"startquiz_{u_name}"):
                st.session_state['unter'] = u_name
                st.session_state['quiz_idx'] = 0
                st.session_state['quiz_score'] = 0
                st.rerun()

    if st.button("❌ Fach schließen"):
        del st.session_state['fach']
        st.session_state.pop('unter', None)
        st.rerun()

st.caption("Alle Fächer mit Unterbegriffen + Suche + Quiz + leere Leiste + Chemie")
