
import streamlit as st
import requests, urllib.parse

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 36px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 15px; border-radius: 12px; border: 2px solid #2E86AB; }
.quiz-box { background-color: #fff8e1; padding: 20px; border-radius: 12px; border: 3px solid #ff9800; margin: 20px 0; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 8px; min-height: 40px; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App - Mit Quiz</div>', unsafe_allow_html=True)
thema = st.text_input("Suche", placeholder="", label_visibility="collapsed", key="haupt")

alle_faecher = {
"Französisch": {
    "le la lui leur": {"text": "LE=ihn/es OHNE a Je LE mange LA=sie Je LA vois LUI=ihm/ihr MIT a Je parle À Marie->LUI LEUR=ihnen", "quiz": [("Je mange LE pain -> Je __ mange", "LE", "LUI"), ("Je parle À Marie -> Je __ parle", "LUI", "LE"), ("Je parle AUX enfants -> Je __ parle", "LEUR", "LUI")]},
    "y en": {"text": "Y=dort Ort Sache J'Y vais EN=davon J'EN veux", "quiz": [("Je vais À Paris -> J'__ vais", "Y", "EN"), ("J'EN veux = davon", "EN", "Y")]},
},
"Spanisch": {
    "se lo doy": {"text": "LE+LO wird SE! FALSCH Le lo doy RICHTIG SE LO DOY!", "quiz": [("Le lo doy ist?", "FALSCH", "RICHTIG"), ("Richtig: Le lo doy ->?", "SE LO DOY", "LE LO DOY")]},
    "ser estar": {"text": "SER=WAS IST permanent Soy Juan ESTAR=WO WIE GERADE Estoy en casa", "quiz": [("Soy Juan = SER oder ESTAR?", "SER", "ESTAR"), ("Estoy en casa =?", "ESTAR Ort", "SER"), ("Estoy cansado =?", "ESTAR Zustand", "SER")]},
    "por para": {"text": "POR=Grund Durch Dauer PARA=Ziel Zweck Para comer", "quiz": [("Gracias ___ todo (Grund)", "POR", "PARA"), ("Para comer (Zweck)", "PARA", "POR")]},
    "Vokabeln": {"text": "el pan Brot la casa Haus ir gehen", "quiz": [("el pan =?", "Brot", "Haus"), ("ir =?", "gehen", "kommen")]},
},
"Italienisch": {
    "Vokabeln": {"text": "il pane Brot la mela Apfel andare gehen venire kommen fare machen", "quiz": [("il pane =?", "Brot", "Apfel"), ("andare =?", "gehen", "kommen")]},
    "lo gli ci ne": {"text": "LO=ihn Vedo IL LIBRO->LO vedo GLI=ihm Parlo A GIOVANNI->GLI CI=y Vado A Parigi->CI vado NE=en NE voglio", "quiz": [("Vedo IL LIBRO -> __ vedo", "LO", "GLI"), ("Parlo A GIOVANNI -> __ parlo", "GLI", "LO"), ("Vado A Parigi -> __ vado", "CI", "NE"), ("Voglio DEL pane -> __ voglio", "NE", "CI")]},
    "essere stare glielo": {"text": "Glielo do Ich gebe es ihm Sono Giovanni permanent Sto a casa Ort Sto mangiando gerade", "quiz": [("Glielo do =?", "Ich gebe es ihm", "Ich bin dort"), ("Sono Giovanni =?", "ESSERE", "STARE"), ("Sto a casa =?", "STARE Ort", "ESSERE")]},
},
"Latein": {
    "Kasus": {"text": "Nom Wer? puella Gen Wessen? puellae Dat Wem? puellae Akk Wen? puellam Abl Womit? cum puella", "quiz": [("Nominativ fragt?", "Wer?Was?", "Wessen?"), ("puellam =?", "Akkusativ", "Nominativ"), ("Genitiv fragt?", "Wessen?", "Wer?")]},
    "Deklinationen": {"text": "1.a puella Gen puellae 2.o servus Gen servi 3.rex Gen regis 4.u fructus 5.e res", "quiz": [("puella Gen?", "puellae", "puellam"), ("servus Gen?", "servi", "servus"), ("rex Gen?", "regis", "rex")]},
    "AcI Gerundium": {"text": "AcI Dico eum venire Ich sage dass er kommt Gerundium amandum das Lieben PPA amans liebend PPP amatus geliebt PFA amaturus", "quiz": [("Dico eum venire =?", "Ich sage dass er kommt", "Ich komme"), ("amans =?", "liebend PPA", "geliebt"), ("Ad amandum =?", "Zum Lieben", "des Liebens")]},
},
"Physik": {
    "Newton": {"text": "F=m*a 1N=1kg*1m/s² Fg=m*g 70kg=686N v=s/t a=v/t Freier Fall s=0,5*g*t²", "quiz": [("F=m*a F=?", "m*a", "m/g"), ("70kg Gewicht?", "686N", "70N"), ("v=s/t v=?", "Geschwindigkeit", "Strecke")]},
    "Energie": {"text": "0,5*m*v² kinetisch m*g*h potentiell P=E/t Watt 1kWh=3,6Mio J", "quiz": [("Kinetisch 0,5*m*v²?", "kinetisch", "potentiell"), ("m*g*h?", "potentiell", "kinetisch"), ("1kWh=?", "3,6 Mio J", "1000 J")]},
    "Strom": {"text": "R=U/I I=U/R 12V 3Ω I=4A Reihe 2+3=5Ω Parallel 2//2=1Ω P=U*I 230V*10A=2300W", "quiz": [("R=U/I R=?", "U/I", "U*I"), ("12V 3Ω I=?", "4A", "36A"), ("Reihe 2+3=?", "5Ω", "1Ω"), ("Parallel 2//2=?", "1Ω", "4Ω"), ("230V*10A=?", "2300W", "23W")]},
    "Optik Kern": {"text": "Einfall=Ausfall Brechung Prisma Farben Linse f=1/D Uran Spaltung E=mc²", "quiz": [("Einfall=Ausfall ist?", "Reflexion", "Brechung"), ("Weiß durch Prisma?", "Farben", "bleibt weiß"), ("Uran Spaltung =?", "Kernspaltung", "Fusion")]},
},
"Mathe": {"Brüche": {"text": "1/4+2/4=3/4 1/2:1/4=2", "quiz": [("1/4+2/4=?", "3/4", "3/8")]}},
"Geschichte": {"Mauer": {"text": "13.8.61-9.11.89 28J 155km", "quiz": [("Mauerbau wann?", "13.8.61", "1989")]}},
"Chemie": {"pH": {"text": "pH 0-6 sauer 7 neutral 8-14 basisch", "quiz": [("pH1 ist?", "sauer", "basisch")]}},
}

st.write("---")
st.markdown("### 📖 Fächer:")

cols = st.columns(3)
fach_liste = list(alle_faecher.keys())
for i, f in enumerate(fach_liste):
    if cols[i % 3].button(f, key=f"fach_{f}"):
        st.session_state['fach'] = f
        st.session_state.pop('unter', None)

if 'fach' in st.session_state:
    fach = st.session_state['fach']
    st.write("---")
    st.markdown(f"## 📚 {fach}")

    sub_suche = st.text_input(f"In {fach} suchen", placeholder="", key=f"sub_{fach}")

    unter_dict = alle_faecher[fach]

    # Buttons für Unterbegriffe
    u_cols = st.columns(2)
    for j, u_name in enumerate(unter_dict.keys()):
        if u_cols[j % 2].button(u_name, key=f"u_{fach}_{u_name}"):
            st.session_state['unter'] = u_name

    # WENN UNTERTHEMA GEKLICKT -> TEXT + QUIZ DIREKT!
    if 'unter' in st.session_state and st.session_state['unter'] in unter_dict:
        u = st.session_state['unter']
        data = unter_dict[u]
        st.write("---")
        st.markdown(f"### {u}")
        st.write(data["text"])

        # QUIZ JETZT IMMER SOFORT SICHTBAR OHNE EXTRA KLICK!
        st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
        st.markdown(f"#### 🎯 Quiz zu {u} - Teste dich!")

        # Einfaches Quiz mit Radio - funktioniert immer
        for qi, (frage, richtig, falsch) in enumerate(data["quiz"]):
            st.markdown(f"**{qi+1}. {frage}**")
            antwort = st.radio(f"Wähle:", [f"--- Wählen ---", richtig, falsch] if richtig!= falsch else [f"--- Wählen ---", richtig, "andere"], key=f"radio_{fach}_{u}_{qi}", label_visibility="collapsed")
            if antwort!= "--- Wählen ---":
                if antwort == richtig:
                    st.success(f"✅ Richtig! {richtig}")
                else:
                    st.error(f"❌ Falsch! Richtig ist: {richtig}")
            st.write("")

        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("❌ Schließen"):
        for k in ['fach','unter']:
            st.session_state.pop(k, None)
        st.rerun()
