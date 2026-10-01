import streamlit as st
import requests, urllib.parse

try:
    from g4f.client import Client
    G4F=True
    client=Client()
except:
    G4F=False

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")
st.markdown("""
<style>
.main-title { text-align: center; font-size: 32px; font-weight: bold; color: #2E86AB; }
.quiz-box { background-color: #fff8e1; padding: 12px; border-radius: 10px; border: 3px solid #ff9800; margin: 10px 0; }
.chat-box { background-color: #e8f5e9; padding: 12px; border-radius: 10px; border: 2px solid #4caf50; margin: 10px 0; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 8px; min-height: 36px; font-size: 12px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App - Lernen + Quiz + Chatbot</div>', unsafe_allow_html=True)

def wiki(t):
    try:
        enc=urllib.parse.quote(t.replace(" ", "_"))
        r=requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers={'User-Agent':'LernApp'}, timeout=4)
        if r.status_code==200 and 'extract' in r.json():
            return r.json().get("extract","")
    except:
        pass
    return ""

alle = {
"Französisch": {
    "Vokabeln": {"t":"le pain Brot la pomme Apfel aller gehen venir kommen faire machen bon gut","q":[("le pain =?","Brot","Apfel"),("aller =?","gehen","kommen")]},
    "le la les lui leur": {"t":"LE=ihn/es OHNE a Je LE mange LA=sie Je LA vois LUI=ihm/ihr MIT a Je parle À Marie->LUI LEUR=ihnen","q":[("Je LE mange =?","LE","LUI"),("Je parle À Marie -> Je __ parle","LUI","LE"),("AUX enfants -> __","LEUR","LUI")]},
    "y en": {"t":"Y=dort Ort Sache J'Y vais EN=davon J'EN ai 3","q":[("J'Y vais =?","Y","EN"),("J'EN ai 3 =?","EN","Y")]},
    "Reihenfolge": {"t":"me te se nous vous + le la les + lui leur + y + en + VERB Il ME LE donne","q":[("Il ME LE donne richtig?","JA","NEIN")]},
    "indirekte Rede": {"t":"Il dit qu'il EST malade bleibt Il a dit qu'il ÉTAIT malade Present->Imparfait","q":[("Il dit qu'il EST bleibt weil Präsens?","JA","NEIN")]},
},
"Spanisch": {
    "Vokabeln": {"t":"el pan Brot la casa Haus ir gehen","q":[("el pan =?","Brot","Haus")]},
    "se lo doy": {"t":"LE+LO wird SE! Le lo doy FALSCH SE LO DOY RICHTIG!","q":[("Le lo doy ist?","FALSCH","RICHTIG"),("Richtig?","SE LO DOY","LE LO DOY")]},
    "ser estar": {"t":"SER permanent Soy Juan ESTAR Ort Estoy en casa Estoy cansado","q":[("Soy Juan =?","SER","ESTAR"),("Estoy en casa =?","ESTAR","SER")]},
    "por para": {"t":"POR Grund Dauer PARA Ziel Zweck Para comer","q":[("Gracias POR todo =?","POR","PARA"),("Para comer =?","PARA","POR")]},
},
"Italienisch": {
    "Vokabeln": {"t":"il pane Brot andare gehen la casa Haus","q":[("il pane =?","Brot","Haus")]},
    "lo gli ci ne": {"t":"LO=ihn Vedo IL LIBRO->LO GLI=ihm Parlo A GIOVANNI->GLI CI=y Vado A Parigi->CI NE=en NE voglio","q":[("Vedo IL LIBRO -> __","LO","GLI"),("Vado A Parigi -> __","CI","NE")]},
    "essere stare glielo": {"t":"Glielo do Ich gebe es ihm Sono Giovanni permanent Sto a casa Ort","q":[("Glielo do =?","Ich gebe es ihm","Ich bin dort"),("Sono Giovanni =?","ESSERE","STARE")]},
},
"Latein": {
    "Kasus": {"t":"Nom Wer? Gen Wessen? Dat Wem? Akk Wen? Abl Womit? puella puellae puellam","q":[("Wessen? =?","Genitiv","Nominativ"),("puellam =?","Akkusativ","Nominativ")]},
    "Deklinationen": {"t":"1.a puella Gen puellae 2.o servus Gen servi 3.rex Gen regis","q":[("puella Gen?","puellae","puellam"),("rex Gen?","regis","rex")]},
    "AcI Gerundium": {"t":"Dico eum venire Ich sage dass er kommt amans liebend amatus geliebt","q":[("Dico eum venire =?","Ich sage dass er kommt","Ich komme"),("amans =?","liebend","geliebt")]},
},
"Physik": {
    "Newton": {"t":"F=m*a Gewicht m*g 70kg=686N v=s/t","q":[("F=?","m*a","m*g"),("70kg Gewicht?","686N","70N")]},
    "Strom": {"t":"R=U/I 12V 3Ω I=4A Reihe 2+3=5Ω Parallel 2//2=1Ω P=U*I 230V*10A=2300W","q":[("12V 3Ω I=?","4A","36A"),("Reihe 2+3=?","5Ω","1Ω"),("Parallel 2//2=?","1Ω","4Ω"),("230V*10A=?","2300W","23W")]},
    "Energie": {"t":"0,5*m*v² kinetisch m*g*h potentiell 1kWh=3,6Mio J","q":[("0,5*m*v² =?","kinetisch","potentiell"),("1kWh =?","3,6 Mio J","1000 J")]},
    "Optik Kern": {"t":"Einfall=Ausfall Reflexion Prisma Farben E=mc² Uran","q":[("Einfall=Ausfall =?","Reflexion","Brechung"),("E=mc² =?","Masse=Energie","F=m*a")]},
},
"Mathe": {"Brüche": {"t":"1/4+2/4=3/4 1/2:1/4=2","q":[("1/4+2/4=?","3/4","3/8")]}, "Pythagoras": {"t":"a²+b²=c² 3²+4²=5²","q":[("a²+b²=?","c²","a²")]}},
"Geschichte": {"Mauer": {"t":"Mauer 13.8.61-9.11.89 28J 3.10.90 Einheit","q":[("Mauerbau?","13.8.61","1989")]}, "2WK": {"t":"1939-45 Holocaust 6Mio Hiroshima","q":[("Beginn?","1.9.39","1914")]}},
"Biologie": {"Zelle": {"t":"Mito Kraftwerk ATP","q":[("Kraftwerk?","Mito","Kern")]}, "Fotosynthese": {"t":"6CO2+6H2O->Zucker+O2 O2 aus Wasser","q":[("O2 aus?","Wasser","CO2")]}},
"Chemie": {"pH": {"t":"pH 0-6 sauer 7 neutral 8-14 basisch","q":[("pH1 =?","sauer","basisch")]}, "Atombau": {"t":"Proton+ Neutron Elektron","q":[("Proton?","positiv","negativ")]}},
"Deutsch": {"Konjunktiv": {"t":"er sei er habe","q":[("er sei =?","Konj I","Konj II")]}},
"Englisch": {"Zeiten": {"t":"I go he goes I went I have gone","q":[("He __ every day","goes","go")]}, "if": {"t":"If I GO I WILL If I WENT I WOULD","q":[("If I GO I __","WILL","WOULD")]}},
"Geographie": {"Platten": {"t":"5cm/Jahr divergent Rücken konvergent Himalaya","q":[("Wie schnell?","5cm/Jahr","5m/Jahr")]}},
}

# OBEN: SUCHE + FÄCHER + QUIZ
thema = st.text_input("🔍 Suche in allen Fächern + Wikipedia", placeholder="", key="haupt")
if thema:
    w=wiki(thema)
    if w:
        st.info(f"🌐 {w[:400]}...")

st.markdown("### 📖 Fächer - Klick für Themen + Quiz:")
cols = st.columns(3)
for i, f in enumerate(alle.keys()):
    if cols[i % 3].button(f, key=f"fach_{f}"):
        st.session_state['fach']=f
        st.session_state.pop('unter',None)

if 'fach' in st.session_state:
    fach=st.session_state['fach']
    st.write("---")
    st.markdown(f"## 📚 {fach}")
    sub = st.text_input(f"In {fach} suchen", placeholder="", key=f"sub_{fach}")
    unter_dict = alle[fach]
    if sub:
        unter_dict = {k:v for k,v in unter_dict.items() if sub.lower() in k.lower() or sub.lower() in v["t"].lower()}

    u_cols = st.columns(2)
    for j, u_name in enumerate(unter_dict.keys()):
        if u_cols[j % 2].button(u_name, key=f"u_{fach}_{u_name}"):
            st.session_state['unter']=u_name

    if 'unter' in st.session_state and st.session_state['unter'] in alle[fach]:
        u = st.session_state['unter']
        data = alle[fach][u]
        st.write("---")
        st.markdown(f"### {u}")
        st.write(data["t"])
        # QUIZ - IMMER DA!
        st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
        st.markdown(f"#### 🎯 Quiz zu {u}")
        for qi, (frage, richtig, falsch) in enumerate(data["q"]):
            st.markdown(f"**{qi+1}. {frage}**")
            key=f"quiz_{fach}_{u}_{qi}"
            auswahl = st.radio("", ["--- Wählen ---", richtig, falsch], key=key, label_visibility="collapsed", horizontal=True)
            if auswahl!="--- Wählen ---":
                if auswahl==richtig:
                    st.success(f"✅ Richtig! {richtig}")
                else:
                    st.error(f"❌ Falsch! Richtig: {richtig}")
        st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
# UNTEN: CHATBOT WIE CHATGPT - BEIDES IN EINEM!
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
st.markdown("### 🤖 Chatbot wie ChatGPT - Frag mich hier unten!")
if G4F:
    st.markdown("✅ KI aktiv - antwortet wie ChatGPT selbst!")
else:
    st.markdown("⚠️ Für echten ChatGPT-Modus: requirements.txt `g4f` hinzufügen")
st.markdown('</div>', unsafe_allow_html=True)

if 'chat' not in st.session_state:
    st.session_state['chat']=[{"role":"assistant","content":"Hey! Ich bin dein Bot wie ChatGPT 📚 Stell mir Fragen - ich erkläre wie Lehrer mit Beispielen! Z.B. 'Erklär y en' oder 'ser estar Unterschied' oder 'Fotosynthese einfach'"}]

for msg in st.session_state['chat']:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

frage = st.chat_input("Frag mich wie ChatGPT... z.B. le la lui erklären")

if frage:
    st.session_state['chat'].append({"role":"user","content":frage})
    with st.chat_message("user"):
        st.write(frage)

    antwort=""
    if G4F:
        try:
            sys_prompt=f"Du bist Lern-Assistent wie ChatGPT, erkläre einfach Deutsch mit Beispielen. Wissen: {str(alle)[:2500]}"
            wk=wiki(frage)
            prompt=frage
            if wk:
                prompt=f"Frage: {frage}\nWikipedia: {wk[:500]}\nAntworte wie ChatGPT als Lehrer kurz mit Beispielen."
            resp=client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"system","content":sys_prompt},{"role":"user","content":prompt}])
            antwort=resp.choices[0].message.content
        except Exception as e:
            antwort=f"{wiki(frage)[:400]}"
    else:
        w=wiki(frage)
        if w:
            antwort=f"🌐 {w[:500]}...\n\nFrag weiter wie bei ChatGPT!"
        else:
            antwort="Frag z.B. 'le la lui', 'ser estar', 'Fotosynthese', 'Newton', 'pH' - ich erkläre wie ChatGPT! Mit g4f in requirements noch schlauer!"

    with st.chat_message("assistant"):
        st.write(antwort)
    st.session_state['chat'].append({"role":"assistant","content":antwort})
    st.rerun()
