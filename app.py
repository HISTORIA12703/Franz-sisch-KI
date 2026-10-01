import streamlit as st
import requests, urllib.parse

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 42px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 25px; border-radius: 15px; border: 2px solid #2E86AB; margin-bottom: 20px; }
.history-box { background-color: #fff3cd; padding: 20px; border-radius: 15px; border: 2px solid #ffc107; margin: 15px 0; }
.result-box { background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 5px solid #4caf50; margin: 10px 0; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 10px; padding: 12px; font-weight: bold; min-height: 50px; }
.stButton > button:hover { background-color: #2E86AB; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App</div>', unsafe_allow_html=True)
st.markdown('<div class="search-box">', unsafe_allow_html=True)
st.markdown("### 🔍 Wonach möchtest du suchen?")
thema = st.text_input("", placeholder="", label_visibility="collapsed", key="haupt")
st.markdown('</div>', unsafe_allow_html=True)

def multi_suche(thema):
    ergebnisse = []
    headers = {'User-Agent': 'LernApp/1.0'}
    try:
        enc = urllib.parse.quote(thema.replace(" ", "_"))
        r = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers=headers, timeout=5)
        if r.status_code == 200 and 'extract' in r.json():
            d = r.json()
            ergebnisse.append({"quelle": "Wikipedia DE", "titel": d.get("title"), "text": d.get("extract"), "link": d.get("content_urls", {}).get("desktop", {}).get("page", "")})
    except:
        pass
    try:
        enc_en = urllib.parse.quote(thema.replace(" ", "_"))
        r_en = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{enc_en}", headers=headers, timeout=5)
        if r_en.status_code == 200:
            d_en = r_en.json()
            if 'extract' in d_en:
                ergebnisse.append({"quelle": "Wikipedia EN", "titel": d_en.get("title"), "text": d_en.get("extract"), "link": d_en.get("content_urls", {}).get("desktop", {}).get("page", "")})
    except:
        pass
    try:
        ddg_url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(thema)}&format=json&pretty=1&no_html=1"
        r_ddg = requests.get(ddg_url, headers=headers, timeout=5)
        if r_ddg.status_code == 200:
            d_ddg = r_ddg.json()
            if d_ddg.get("AbstractText"):
                ergebnisse.append({"quelle": f"DuckDuckGo", "titel": d_ddg.get("Heading", thema), "text": d_ddg.get("AbstractText"), "link": d_ddg.get("AbstractURL","")})
    except:
        pass
    return ergebnisse

faecher = {
"Französisch": "LE=ihn/es OHNE a Je LE mange LA=sie Je LA vois LUI=ihm/ihr MIT a Je parle À Marie -> LUI Y=Ort Sache J'Y vais EN=davon J'EN veux REIHENFOLGE me te se nous vous + le la les + lui leur + y + en + VERB",
"Spanisch": "SE LO DOY! LE+LO->SE! SER permanent Soy Juan ESTAR Ort Zustand Estoy en casa POR Grund Durch PARA Ziel",
"Englisch": "Present I go he goes Past I went Perfect I have gone If GO WILL WENT WOULD HAD GONE WOULD HAVE GONE Passive IS MADE",
"Italienisch": "ci=y ne=en CI vado NE voglio glielo Glielo do ESSERE permanent STARE Ort Zustand",
"Latein": "5 Kasus Nom Gen Dat Akk Abl AcI Dico eum venire Gerundium amandum",
"Deutsch": "Konjunktiv I sei habe solle",
"Mathe": "Brüche Pythagoras Mitternacht Ableitung Wahrscheinlichkeit",
"Geographie": "Plattentektonik Klima CO2 Bevölkerung",
"Biologie": "Mitochondrien Fotosynthese DNA 46 Mitose Evolution",
"Physik": "Newton F=m*a Energie Strom R=U/I",
"Chemie": "Atombau PSE NaCl pH Redox"
}

geschichte_themen = {
"französische revolution": "1789 3.Stand 97% Bastille Menschenrechte Ludwig geköpft Napoleon",
"1 weltkrieg": "1914-18 Sarajevo Verdun 11.11.18 Versailles 17Mio Tote",
"2 weltkrieg": "1939-45 Polen Holocaust 6Mio Auschwitz Hiroshima 60Mio Tote",
"kalter krieg mauer": "NATO 49 Mauer 13.8.61-9.11.89 28J Kuba 62 Einheit 3.10.90",
"adolf hitler": "1889-1945 Braunau NSDAP 1933 Machtergreifung Diktator 2.WK Holocaust Selbstmord 30.4.45"
}

if thema:
    st.write("---")
    st.markdown(f"### 🔍 Fakten für '{thema}':")
    with st.spinner("Suche..."):
        alle = multi_suche(thema)
    for erg in alle:
        st.markdown(f'<div class="result-box"><b>{erg["quelle"]}: {erg["titel"]}</b><br>{erg["text"]}</div>', unsafe_allow_html=True)
        if erg["link"]:
            st.markdown(f"[Mehr]({erg['link']})")

st.write("---")
st.markdown("### 📖 Alle 12 Fächer:")

cols = st.columns(3)
fach_liste = ["Französisch","Spanisch","Englisch","Italienisch","Latein","Deutsch","Mathe","Geschichte","Geographie","Biologie","Physik","Chemie"]

for i, fach_name in enumerate(fach_liste):
    if cols[i % 3].button(fach_name, key=f"btn_{fach_name}"):
        st.session_state['fach'] = fach_name

if 'fach' in st.session_state:
    st.write("---")
    if st.session_state['fach'] == "Geschichte":
        st.markdown("## 📚 Geschichte")
        gesch_suche = st.text_input("Geschichte suchen:", placeholder="", key="gesch")
        if gesch_suche:
            with st.spinner("Suche..."):
                internet = multi_suche(gesch_suche)
            for erg in internet:
                st.info(f"**{erg['quelle']}:** {erg['text']}")
    else:
        st.markdown(f"## {st.session_state['fach']}")
        st.write(faecher[st.session_state['fach']])
    if st.button("❌ Schließen"):
        del st.session_state['fach']
        st.rerun()
