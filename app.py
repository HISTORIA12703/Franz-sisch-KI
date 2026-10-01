import streamlit as st
st.set_page_config(page_title="Lingua100", page_icon="📚", layout="wide")
st.title("📚 Lingua100 Ultimate")
st.success("✅ 50+ Themen - Suche geht!")

if 'xp' not in st.session_state: st.session_state.xp=0
st.sidebar.metric("⭐ XP", st.session_state.xp)
st.sidebar.info("HISTORIA12703")

DATA = {
 "Geschichte (12)": {
  "Franz. Revolution 1789": "14.7.1789 Bastille, 1793 Ludwig geköpft, 1804 Napoleon Kaiser, 1815 Waterloo",
  "Kaiserreich 1871": "18.1.1871 Versailles Gründung, Wilhelm I",
  "1.WK 1914-18": "28.6.1914 Sarajevo Attentat, 11.11.1918 Ende, 17 Mio Tote",
  "Weimar 1919-33": "1919 Verfassung, 1923 Inflation 1 Billion, 1929 Krise",
  "NS Zeit 1933-45": "30.1.33 Hitler Macht, 1935 Nürnberger, 9.11.38 Kristallnacht, 6 Mio Auschwitz",
  "2.WK 1939-45": "1.9.39 Polen, 6.6.44 D-Day, 8.5.45 Ende DE, Hiroshima 6.8.45",
  "Mauer 1961-89": "13.8.61 Bau, 9.11.89 Fall, 3.10.90 Einheit, 28 Jahre Mauer",
  "Antike": "753 v.Chr Rom Gründung, 44 v.Chr Caesar tot",
  "Mittelalter": "1492 Kolumbus Amerika, 1517 Luther Thesen, 1453 Buchdruck",
  "Kalter Krieg": "1949 NATO, 1962 Kuba Krise, 1969 Mond",
  "Industrialisierung": "1769 Dampfmaschine Watt, 1835 erste Bahn",
  "EU": "1957 Römische Verträge, 1993 EU, 2002 Euro, 27 Länder"
 },
 "Physik (8)": {
  "Mechanik": "v=s/t, 100km/h=27,8m/s, g=9,81 m/s²",
  "Newton": "F=m*a, 70kg = 686N, Actio=Reactio",
  "Strom": "R=U/I, 12V 3Ω=4A, Reihe 2+3=5Ω, Parallel 2//2=1Ω",
  "Energie": "kinetisch 0,5*m*v², potentiell m*g*h, 1kWh=3,6Mio J",
  "Optik": "Einfall=Ausfall, c=300.000km/s Lichtgeschwindigkeit",
  "Wellen": "Schall 343m/s, v=f*λ",
  "Kernphysik": "E=mc² Einstein, Uran Spaltung",
  "Druck": "p=F/A, 1bar=100.000Pa, 10m Wasser=+1bar"
 },
 "Mathe (7)": {
  "Brüche": "1/4+2/4=3/4, 1/2=0,5",
  "Prozent": "20% von 200=40",
  "Pythagoras": "a²+b²=c², 3-4-5 Dreieck: 9+16=25",
  "Gleichungen": "2x+4=10 => x=3",
  "Geometrie": "Kreis U=2πr A=πr², Quader V=a*b*c",
  "Binom": "(a+b)²=a²+2ab+b²",
  "Wahrscheinlichkeit": "Würfel 6=1/6, Münze 50%"
 },
 "Biologie": {"Zelle": "Mitochondrien Kraftwerk, Chloroplast Fotosynthese", "Genetik": "DNA Doppelhelix, 46 Chromosomen", "Mensch": "Herz 4 Kammern, 86 Mrd Neuronen"},
 "Chemie": {"Atome": "Proton+ Neutron Kern, Elektron Hülle", "Periodensystem": "118 Elemente, H=1, O=8, Au=Gold 79"},
 "Deutsch": {"Fälle": "Wer? Nom, Wessen? Gen, Wem? Dat, Wen? Akk", "das dass": "das Haus Artikel, dass mit ss nach Komma"},
 "Geographie": {"Deutschland": "16 Länder, Berlin, 83 Mio, 9 Nachbarn", "Europa": "EU 27, Wolga 3530km längster Fluss"}
}

suche = st.text_input("🔍 Suche", placeholder="Mauer, Strom, 1914...")
if suche:
 for fach, themen in DATA.items():
  for t, txt in themen.items():
   if suche.lower() in t.lower() or suche.lower() in txt.lower():
    st.info(f"{fach} - {t}: {txt}")

cols = st.columns(3)
for i, fach in enumerate(DATA.keys()):
 if cols[i%3].button(fach, use_container_width=True):
  st.session_state.fach=fach

if 'fach' in st.session_state:
 fach = st.session_state.fach
 st.header(fach)
 for tit, txt in DATA[fach].items():
  with st.expander(f"📚 {tit}", expanded=True):
   st.info(txt)
   if st.button(f"✅ Gelernt {tit}", key=f"btn_{tit}"):
    st.balloons()
    st.session_state.xp+=10
    st.rerun()
 if st.button("⬅️ Zurück"):
  del st.session_state.fach
  st.rerun()
