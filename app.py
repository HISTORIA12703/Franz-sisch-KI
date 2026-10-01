import streamlit as st
import requests

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

# ===== LAYOUT DIREKT OBEN IM CODE =====
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: #2E86AB;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }
    .search-box {
        background-color: #f0f7ff;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #2E86AB;
        margin-bottom: 20px;
    }
    .fach-button {
        background-color: #ffffff;
        border: 2px solid #2E86AB;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 16px;
    }
    .stButton > button {
        width: 100%;
        background-color: white;
        color: #2E86AB;
        border: 2px solid #2E86AB;
        border-radius: 10px;
        padding: 12px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #2E86AB;
        color: white;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Alle Fächer - Mit Internet Suche</div>', unsafe_allow_html=True)

# ===== SUCHE OBEN MIT LAYOUT =====
st.markdown('<div class="search-box">', unsafe_allow_html=True)
st.markdown("### 🔍 Wonach möchtest du suchen?")
thema = st.text_input("", placeholder="z.B. USA, Atombombe, Football, Fotosynthese, y en, Pythagoras, Ableitung, Revolution, Atombau...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

def suche_wikipedia(thema):
    try:
        url = f"https://de.wikipedia.org/api/rest_v1/page/summary/{thema}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {"titel": data.get("title"), "text": data.get("extract"), "link": data.get("content_urls", {}).get("desktop", {}).get("page", "")}
    except:
        pass
    return None

faecher = {
"Französisch": """
**LE LA LUI Y EN AUSFÜHRLICH:**

LE=IHN ES männlich COD direkt Wen?Was? OHNE a: Je mange LE pain -> Je LE mange. Je vois LE livre -> Je LE vois. WANN? Kein a dahinter!

LA=SIE weiblich COD: Je vois MARIE -> Je LA vois. Je mange LA pomme -> Je LA mange.

LES=SIE Plural COD: Je vois LES pommes -> Je LES vois.

LUI=IHM IHR COI Wem? MIT a: Je parle À MARIE -> Je LUI parle. Je donne le livre À PAUL -> Je LUI donne. WANN? Mit à vor Person!

LEUR=IHNEN Plural COI: Je parle AUX enfants -> Je LEUR parle.

Y=DORT DORTHIN DARAN Ort mit à chez dans: Je vais À PARIS -> J'Y vais dorthin. Je pense À l'examen Sache -> J'Y pense daran. WANN? Ort oder à+Sache nicht Person!

EN=DAVON Menge mit de du des Zahl: Je veux DU pain -> J'EN veux davon. J'ai 2 pommes -> J'EN ai 2. Je parle DE mon voyage -> J'EN parle davon. WANN? de/du/des/Zahl!

REIHENFOLGE: me te se nous vous + le la les + lui leur + y + en + VERB. Il ME LE donne, Il Y EN a, Je M'Y habitue.

DIREKTE INDIREKTE: Il dit qu'il est malade bleibt bei Präsens. Il a dit qu'il ÉTAIT malade Present->Imparfait J'ai mangé->avait mangé Futur->Conditionnel. Fragen Où?->où il allait Que?->ce que Tu viens?->si il venait. Befehl Viens!->de venir.

ZEITEN: Passé 14 Verben mit être aller venir, Imparfait je parlais Gewohnheit, Futur parlerai serai aurai.
""",
"Spanisch": """
**SE LO DOY + SER ESTAR + POR PARA:**

LO LA Wen?Was? direkt OHNE a: Veo EL LIBRO -> LO veo. LE LES Wem? MIT a: Hablo A JUAN -> LE hablo.

VERBOTEN LE LO! RICHTIG SE LO DOY! le/les+lo/la->SE! Se lo doy Ich gebe es ihm.

SER permanent WAS IST: Soy Juan Identität, Soy de Alemania Herkunft, Soy alto groß, Son las 3 Uhrzeit. Merke WAS IST ES?

ESTAR Ort Zustand gerade: Estoy en casa Ort, Estoy cansado müde Zustand, Está roto kaputt Ergebnis, Estoy comiendo esse gerade Verlaufsform!

POR Grund Durch Tausch Dauer: Gracias POR todo Grund, Voy POR calle durch, POR mañana morgens, POR 2 horas Dauer, 5€ POR libro Tausch.

PARA Ziel Zweck Empfänger Frist: Para comer zum Essen Zweck, Para ti für dich Empfänger, Para Madrid nach Madrid Ziel, Para mañana bis morgen Frist.

TRICK POR=Warum? Wodurch? PARA=Wofür? Wohin? Für wen?
""",
"Englisch": """
**ENGLISCH AUSFÜHRLICH:**

ZEITEN: Present I go Gewohnheit he goes mit s Do you go? Past I went einmalig Yesterday ed went Did you go? Perfect I have gone Ergebnis have has+PP Signal already yet since for Past Perfect I had gone Vorvergangenheit Future will spontan going to geplant I am going tomorrow Plan.

INDIREKTE: He says he IS ill bleibt bei says. He said he WAS ill Present->Past Past->Past Perfect will->would. Where are you?->where he WAS What?->what he DID Do you come?->if he CAME ob. Befehl Come!->to come.

IF: Type0 If you heat water it boils If+Present Present Type1 If I GO I WILL go If+Present will Type2 If I WENT I WOULD go If+Past would Type3 If I HAD GONE I WOULD HAVE GONE If+Past Perfect would have+PP.

PASSIVE be+PP: A cake IS MADE am is are+PP was were+PP has been+PP will be+PP is being+PP. BY A cake was made BY ME.
""",
"Italienisch": "ci ne = y en Ci vado J'y vais Ne voglio J'en veux glielo Glielo do Essere permanent Sono tedesco Stare Ort Zustand Sto a casa Sto mangiando al del nel a+il=al Futur parlerò Passato sono andato",
"Latein": "ego tu is Kasus Nom Gen Dat Akk Abl puella servus rex AcI Dico eum venire Gerundium amandum PPA amans PPP amatus Zeiten amo amabam amavi amaveram amabo",
"Deutsch": "Konjunktiv I er sei er habe er solle Wenn I=Indikativ dann II sie hätten Kasus Nom Gen Dat Akk Adjektiv Nebensatz Verb Ende Präsens Perfekt Präteritum Plusquam Futur",
"Mathe": "Brüche 1/4+2/4=3/4 1/2+1/3=5/6 Multi Divi Kehrwert Prozent Dreisatz Gleichungen 2x+4=10 x=3 Mitternacht x=(-b±√(b²-4ac))/2a pq Geometrie Pythagoras a²+b²=c² Kreis 2πr πr² Quader a*b*c Kugel 4/3πr³ Trigo sin=GK/Hyp Ableitung x^n->n*x^(n-1) Integral Wahrscheinlichkeit P=Ereignis/alle Binomial",
"Geschichte": "Franz Rev 1789 Bastille 97% 3.Stand Freiheit Gleichheit Brüderlichkeit 1793 Ludwig geköpft Napoleon 1799 Industrialisierung Watt 1769 Fabriken 1.WK 1914 Sarajevo Schützengraben Verdun Versailles 1919 2.WK 1939 Polen Holocaust 6Mio Auschwitz D-Day 6.6.44 8.5.45 Hiroshima Nagasaki Kalter Krieg Mauer 13.8.61-9.11.89 28J Kuba62 BRD 23.5.49 DDR 7.10.49 3.10.90 Einheit",
"Geographie": "Plattentektonik Kruste Mantel Kern 5cm/Jahr divergent Rücken konvergent Himalaya Erdbeben Richter Vulkan Hotspot Klima Wetter täglich Klima 30J Zonen Polar Gemäßigt Tropen Klimawandel CO2 280->420 +1,2°C Bevölkerung 8Mrd Migration Urbanisierung Globalisierung Container",
"Biologie": "Zelle Prokaryot kein Kern Eukaryot mit Kern Tier Membran Zytoplasma Kern Mitochondrien Kraftwerk ATP Zucker+O2->CO2+H2O Ribosomen ER Golgi Lysosom Pflanze Zellwand Chloroplast Fotosynthese 6CO2+6H2O->Zucker+O2 Vakuole Fotosynthese Chloroplast Thylakoid Licht Dunkel Calvin Genetik DNA A-T C-G Gen Chromosom 46 Mitose Meiose Mendel Evolution Darwin Herz 4 Kammern AB0 Gehirn",
"Physik": "Newton1 ohne Kraft bleibt Newton2 F=m*a 2kg*3=6N Gewicht m*g g=9,81 70kg=686N Newton3 Actio=Reactio v=s/t a=v/t s=0,5*g*t² Energie 0,5*m*v² m*g*h Erhaltung Leistung Watt Strom U Volt I Ampere R=U/I Reihe R1+R2 Parallel 1/R=1/R1+1/R2 P=U*I Optik Einfall=Ausfall Brechung Linse Auge Farben",
"Chemie": "Atombau Kern Proton+ Neutron Hülle Elektron Ordnungszahl PSE Gruppen Valenz Gruppe1 +1 Gruppe17 -1 Isotope C12 C14 Bindungen Ionen NaCl kovalent H2O Metall Elektronengas Oktett 8 Säuren Base pH 0-6 sauer 7 neutral 8-14 basisch HCl NaOH Neutralisation HCl+NaOH->NaCl+H2O Redox Oxidation e- abgeben Reduktion aufnehmen OIL RIG Rost Fe+O2->Fe2O3"
}

if thema:
    st.write("---")
    st.markdown(f"### 📖 Ergebnis für '{thema}':")

    wiki = suche_wikipedia(thema)
    if wiki:
        st.info(f"**🌐 {wiki['titel']} (aus Wikipedia)**\n\n{wiki['text']}")
        if wiki['link']:
            st.markdown(f"[🔗 Mehr bei Wikipedia]({wiki['link']})")
        st.write("---")

    s = thema.lower()
    treffer = 0
    for name, text in faecher.items():
        if s in text.lower() or s in name.lower():
            st.markdown(f"**📚 {name}:**")
            st.write(text)
            st.write("---")
            treffer += 1

    if not wiki and treffer == 0:
        st.error("Nichts gefunden - versuche USA, Atombombe, Football, Fotosynthese, y en, Pythagoras...")

st.write("---")

# UNTEN FÄCHER MIT LAYOUT
st.markdown("### 📖 Oder wähle ein Fach:")
st.markdown('<p style="color:#666;">Klicke auf ein Fach für die ausführliche Erklärung:</p>', unsafe_allow_html=True)

cols = st.columns(4)
fach_liste = list(faecher.keys())

for i, fach_name in enumerate(fach_liste):
    col = cols[i % 4]
    if col.button(fach_name, key=fach_name):
        st.session_state['fach'] = fach_name

if 'fach' in st.session_state:
    st.write("---")
    st.markdown(f"<h2 style='color:#2E86AB;'>📚 {st.session_state['fach']}</h2>", unsafe_allow_html=True)
    st.write(faecher[st.session_state['fach']])
    st.write("---")
    if st.button("❌ Schließen"):
        del st.session_state['fach']
        st.rerun()

st.markdown("---")
st.caption("app.py - Layout direkt oben im Code - Oben Suche, Unten Fächer als Buttons - Mit Internet Suche")
