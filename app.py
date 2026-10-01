import streamlit as st
import requests, urllib.parse

# ChatGPT-Modus
try:
    from g4f.client import Client
    G4F=True
    gpt_client=Client()
except:
    G4F=False

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown('<h1 style="text-align:center;color:#2E86AB;">📚 Lern App - Quiz + ChatGPT</h1>', unsafe_allow_html=True)

def wiki(q):
    try:
        enc=urllib.parse.quote(q.replace(" ","_"))
        r=requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers={'User-Agent':'LernApp'}, timeout=3)
        if r.status_code==200:
            return r.json().get("extract","")
    except:
        pass
    return ""

# ALLE FÄCHER MIT QUIZZEN - JEDE HAT QUIZ!
DATEN = {
"Französisch": {
    "le la lui leur": {"text": "LE=ihn/es direkt OHNE a -> Je LE mange LA=sie -> Je LA vois LES=Plural -> Je LES vois LUI=ihm/ihr MIT a Person -> Je parle À Marie -> Je LUI parle LEUR=ihnen -> AUX enfants -> LEUR", "quiz": [["Je mange LE pain -> Je __ mange","LE","LUI"], ["Je parle À Marie -> Je __ parle","LUI","LE"], ["Je parle AUX enfants -> Je __ parle","LEUR","LUI"], ["Je vois Marie -> Je __ vois","LA","LUI"]]},
    "y en": {"text": "Y=dort Ort Sache -> J'Y vais EN=davon Menge Zahl -> J'EN ai 3 J'EN veux", "quiz": [["Je vais À Paris -> J'__ vais","Y","EN"], ["J'ai 3 frères -> J'__ ai 3","EN","Y"], ["Je veux DU pain -> J'__ veux","EN","Y"]]},
    "Vokabeln": {"text": "le pain Brot la pomme Apfel aller gehen venir kommen faire machen bon gut grand groß", "quiz": [["le pain =?","Brot","Apfel"], ["aller =?","gehen","kommen"]]},
},
"Spanisch": {
    "se lo doy WICHTIG": {"text": "REGEL: LE+LO wird SE! Du kannst NIE Le lo doy sagen! FALSCH! RICHTIG ist SE LO DOY! Les doy los libros -> SE LOS DOY Me lo da erlaubt nur LE/LES+LO/LA wird SE!", "quiz": [["Le lo doy ist?","FALSCH","RICHTIG"], ["Richtig ist?","SE LO DOY","LE LO DOY"], ["Les doy los libros ->?","SE LOS DOY","LES LOS DOY"]]},
    "ser estar": {"text": "SER=WAS IST permanent Soy Juan Name Soy alto Eigenschaft Son las 3 Zeit ESTAR=WO?WIE?GERADE? Estoy en casa Ort Estoy cansado Zustand Está roto Ergebnis Estoy comiendo gerade", "quiz": [["Soy Juan =?","SER permanent","ESTAR Ort"], ["Estoy en casa =?","ESTAR Ort","SER"], ["Estoy cansado =?","ESTAR Zustand","SER"], ["Son las 3 =?","SER Zeit","ESTAR"]]},
    "por para": {"text": "POR=Grund Durch Dauer Tausch Gracias POR todo POR dos horas Dauer PARA=Ziel Zweck Para comer Zweck Para ti Empfänger", "quiz": [["Gracias ___ todo Grund","POR","PARA"], ["Para comer Zweck","PARA","POR"], ["Voy PARA Madrid Ziel","PARA","POR"]]},
    "Vokabeln": {"text": "el pan Brot la casa Haus ir gehen venir kommen", "quiz": [["el pan =?","Brot","Haus"]]},
},
"Italienisch": {
    "lo la gli li": {"text": "LO=ihn Vedo IL LIBRO->LO vedo LA=sie Vedo LA CASA->LA vedo LI=masc Plural Vedo I LIBRI->LI vedo LE=fem Plural GLI=ihm/ihr/ihnen Parlo A GIOVANNI->GLI parlo", "quiz": [["Vedo IL LIBRO -> __ vedo","LO","GLI"], ["Parlo A GIOVANNI -> __ parlo","GLI","LO"], ["Vedo I LIBRI masc Plural -> __ vedo","LI","LO"]]},
    "ci ne": {"text": "CI=y dort/daran Vado A Parigi->CI vado NE=en davon Voglio DEL pane->NE voglio Ho 3 fratelli Zahl->NE ho 3", "quiz": [["Vado A Parigi -> __ vado","CI","NE"], ["Voglio DEL pane -> __ voglio","NE","CI"], ["Ho 3 fratelli -> __ ho 3","NE","CI"]]},
    "essere stare glielo": {"text": "Glielo do=Ich gebe es ihm Glielo dico Sono Giovanni permanent Sono di Germania ESSERE Sono le 3 Zeit STARE=WO WIE GERADE Sto a casa Ort Sto male krank Sto mangiando gerade stare+gerundio", "quiz": [["Glielo do =?","Ich gebe es ihm","Ich bin dort"], ["Sono Giovanni =?","ESSERE permanent","STARE Ort"], ["Sto a casa =?","STARE Ort","ESSERE"], ["Sto mangiando =?","gerade stare+gerundio","permanent"]]},
    "Vokabeln": {"text": "il pane Brot la mela Apfel andare gehen la casa Haus", "quiz": [["il pane =?","Brot","Apfel"]]},
},
"Latein": {
    "Kasus": {"text": "Nom Wer?Was? puella Subjekt Gen Wessen? puellae des Mädchens Dat Wem? puellae dem Mädchen Akk Wen? puellam das Mädchen Abl Womit?Wo? cum puella", "quiz": [["Wer?Was? =?","Nominativ","Genitiv"], ["Wessen? =?","Genitiv","Nominativ"], ["puellam =?","Akkusativ","Nominativ"]]},
    "Deklinationen": {"text": "1.a puella Gen puellae 2.o servus Gen servi 3.rex Gen regis corpus Gen corporis 4.u fructus Gen fructus 5.e res Gen rei", "quiz": [["puella Gen?","puellae","puellam"], ["servus Gen?","servi","servus"], ["rex Gen?","regis","rex"]]},
    "AcI Gerundium Partizip": {"text": "AcI Dico eum venire Ich sage dass er kommt eum Akk venire Inf Gerundium amandum das Lieben Ad amandum Zum Lieben PPA amans liebend PPP amatus geliebt", "quiz": [["Dico eum venire =?","Ich sage dass er kommt","Ich komme"], ["amans =?","liebend PPA","geliebt PPP"], ["Ad amandum =?","Zum Lieben","des Liebens"]]},
},
"Physik": {
    "Newton F=m*a": {"text": "Newton1 ohne Kraft bleibt Körper in Ruhe/gerade Newton2 F=m*a 1N=1kg*1m/s² Beispiel 2kg*3m/s²=6N Gewicht Fg=m*g 70kg*9,81=686N Newton3 Actio=Reactio Wand drückt dich zurück Rakete stößt Gas nach unten Gas stößt Rakete nach oben", "quiz": [["F=m*a F=?","m*a","m*g"], ["Gewicht Formel?","m*g","m*a"], ["70kg Gewicht?","686N","70N"], ["Actio=Reactio =?","Newton3","Newton2"]]},
    "Strom R=U/I": {"text": "U Volt Spannung Druck I Ampere Menge R Ohm Widerstand R=U/I I=U/R U=R*I 12V 3Ω I=4A Reihe Rges=R1+R2 2+3=5Ω Spannung teilt sich Parallel 1/R=1/R1+1/R2 2Ω//2Ω=1Ω Strom teilt sich P=U*I 230V*10A=2300W kWh Energie Gefahren 50mA gefährlich", "quiz": [["R=U/I R=?","U/I","U*I"], ["12V 3Ω I=?","4A","36A"], ["Reihe 2Ω+3Ω=?","5Ω","1,2Ω"], ["Parallel 2Ω//2Ω=?","1Ω","4Ω"], ["P=U*I 230V*10A=?","2300W","23W"]]},
    "Energie": {"text": "Energie bleibt erhalten nur umgewandelt Kinetisch 0,5*m*v² Auto 1000kg 20m/s=200kJ Potentiell m*g*h 70kg 10m=6867J Leistung P=E/t Watt 1kWh=3,6Mio J", "quiz": [["0,5*m*v² =?","kinetisch","potentiell"], ["m*g*h =?","potentiell","kinetisch"], ["1kWh =?","3,6 Mio J","1000 J"]]},
    "Mechanik": {"text": "v=s/t 100km/h=27,8m/s a=v/t Freier Fall s=0,5*g*t² g=9,81 2s Fall 19,6m v=g*t", "quiz": [["100km/h =?","27,8 m/s","100 m/s"], ["Freier Fall s=?","0,5*g*t²","g*t"]]},
},
"Mathe": {
    "Pythagoras": {"text": "a²+b²=c² nur rechtwinklig 3²+4²=5² 9+16=25", "quiz": [["a²+b²=?","c²","a²"], ["3 4 5 weil?","9+16=25","3+4=5"]]},
    "Brüche": {"text": "1/4+2/4=3/4 1/2:1/4=2 Kehrwert", "quiz": [["1/4+2/4=?","3/4","3/8"], ["1/2:1/4=?","2","1/8"]]},
},
"Geschichte": {"Mauer": {"text": "Mauer 13.8.61-9.11.89 28 Jahre 155km 140 Tote Einheit 3.10.90", "quiz": [["Mauerbau wann?","13.8.61","9.11.89"], ["Wie lange?","28 Jahre","10 Jahre"]]}},
"Biologie": {"Fotosynthese": {"text": "6CO2+6H2O+Licht->Zucker+O2 O2 kommt aus Wasser H2O Chloroplast", "quiz": [["Formel?","6CO2+6H2O->Zucker+O2","Zucker+O2->CO2"], ["O2 aus?","Wasser H2O","CO2"]]}},
"Chemie": {"pH": {"text": "pH 0-6 sauer 7 neutral 8-14 basisch Säure+Base->Salz+Wasser", "quiz": [["pH1 =?","sauer","basisch"], ["pH7 =?","neutral","sauer"], ["Säure+Base->?","Salz+Wasser","nur Wasser"]]}},
}

# OBEN LERNEN + QUIZ
st.text_input("🔍 Suche", placeholder="", key="suche")
st.markdown("### 📖 Fächer")
c = st.columns(3)
for i, fach in enumerate(DATEN.keys()):
    if c[i%3].button(fach, key=f"f_{fach}"):
        st.session_state['fach']=fach
        st.session_state.pop('unter',None)

if 'fach' in st.session_state:
    fach=st.session_state['fach']
    st.write("---")
    st.markdown(f"## {fach}")
    c2 = st.columns(2)
    for j, unter in enumerate(DATEN[fach].keys()):
        if c2[j%2].button(unter, key=f"u_{fach}_{unter}"):
            st.session_state['unter']=unter

    if 'unter' in st.session_state and st.session_state['unter'] in DATEN[fach]:
        u=st.session_state['unter']
        d=DATEN[fach][u]
        st.write("---")
        st.markdown(f"### {u}")
        st.info(d["text"])

        # HIER SIND DIE QUIZZE - GELBE BOX - IMMER!
        st.markdown("#### 🎯 QUIZ - Teste dich!")
        st.markdown('<div style="background:#fff8e1;padding:15px;border:3px solid #ff9800;border-radius:10px;">', unsafe_allow_html=True)
        for qi, q in enumerate(d["quiz"]):
            frage, richtig, falsch = q
            st.write(f"**{qi+1}. {frage}**")
            # Einfache Radio ohne horizontal damit es immer geht
            ans = st.radio(f"Frage {qi+1}", ["--- Wählen ---", richtig, falsch], key=f"q_{fach}_{u}_{qi}", label_visibility="collapsed")
            if ans!="--- Wählen ---":
                if ans==richtig:
                    st.success(f"✅ Richtig! {richtig}")
                else:
                    st.error(f"❌ Falsch! Richtig ist: {richtig}")
            st.write("")
        st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.markdown("---")
# UNTEN CHATBOT WIE CHATGPT - GLEICHE SEITE!
st.markdown("## 🤖 Chatbot wie ChatGPT - Hier chatten!")
if G4F:
    st.success("✅ ChatGPT-Modus AN - ich antworte wie ChatGPT selbst!")
else:
    st.warning("⚠️ Für echten ChatGPT-Modus: requirements.txt `g4f` hinzufügen")

if 'chat' not in st.session_state:
    st.session_state['chat']=[{"role":"assistant","content":"Hey! Ich bin wie ChatGPT 🤖 Frag mich z.B. 'Erklär mir se lo doy mit Beispielen' oder 'Unterschied essere stare?' oder 'Was ist F=m*a?' Ich erkläre wie ein Lehrer!"}]

for m in st.session_state['chat']:
    with st.chat_message(m["role"]):
        st.write(m["content"])

frage = st.chat_input("Frag mich wie ChatGPT...")

if frage:
    st.session_state['chat'].append({"role":"user","content":frage})
    with st.chat_message("user"):
        st.write(frage)

    antwort=""
    if G4F:
        try:
            sys = f"Du bist Lern-Lehrer wie ChatGPT, erkläre auf Deutsch einfach mit Beispielen. Du kennst: {str(DATEN)[:3000]}"
            wk = wiki(frage)
            prompt = frage
            if wk:
                prompt = f"Frage: {frage}\nWikipedia: {wk[:600]}\nAntworte wie ChatGPT als Lehrer mit Beispielen kurz klar."
            r = gpt_client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"system","content":sys},{"role":"user","content":prompt}])
            antwort = r.choices[0].message.content
        except Exception as e:
            antwort = f"{wiki(frage)[:500] or 'Ich helfe dir! Frag z.B. ser estar, le la lui, Fotosynthese, Newton'}"
    else:
        w = wiki(frage)
        if w:
            antwort = f"🌐 {w[:600]}..."
        else:
            antwort = "Ich bin dein Chatbot wie ChatGPT! Frag z.B. 'Erklär mir le la lui leur', 'ser estar Unterschied', 'Fotosynthese', 'Newton', 'Strom Reihe Parallel', 'pH Wert' - ich erkläre wie ein Lehrer!"

    with st.chat_message("assistant"):
        st.write(antwort)
    st.session_state['chat'].append({"role":"assistant","content":antwort})
    st.rerun()
