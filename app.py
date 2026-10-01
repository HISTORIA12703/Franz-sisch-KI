import streamlit as st, random
st.set_page_config(page_title="LernBox", layout="wide")
st.title("📚 LernBox - Themen sind DA!")

THEMEN = {
 "Geschichte - Mauer": "13.8.1961 Mauerbau, 9.11.1989 Mauerfall, 3.10.1990 Wiedervereinigung, 28 Jahre Mauer",
 "Geschichte - 2.WK": "1.9.1939 Beginn Polen, D-Day 6.6.1944, 8.5.1945 Ende DE, 60 Mio Tote, Holocaust 6 Mio Juden",
 "Geschichte - 1.WK": "28.6.1914 Sarajevo Attentat, 11.11.1918 Ende, Schützengraben",
 "Physik - Strom": "R=U/I, 12V 3Ω=4A, Reihe 2+3=5Ω, Parallel 2//2=1Ω, P=U*I 230V*10A=2300W",
 "Physik - Kraft": "F=m*a, 70kg=686N, Actio=Reactio",
 "Mathe - Pythagoras": "a²+b²=c², 3-4-5 Dreieck 9+16=25",
 "Biologie - Zelle": "Mitochondrien Kraftwerk, Chloroplast Fotosynthese CO2+H2O->Zucker+O2",
 "Chemie - Atome": "Proton+ Neutron Kern, Elektron Hülle, 118 Elemente",
 "Deutsch - das dass": "das Haus Artikel, ich weiß, DASS du kommst mit ss nach Komma",
}

# ZEIGT SOFORT ALLE THEMEN!
st.success(f"{len(THEMEN)} Themen geladen!")
for name, text in THEMEN.items():
    with st.expander(f"📖 {name}", expanded=True):
        st.info(text)
        if st.button(f"✅ Verstanden: {name}", key=name):
            st.balloons()
            st.success("🎉 +3 XP!")

st.write("---")
st.markdown("### 🔍 Suche")
s=st.text_input("Tipp: Mauer, Strom, Pythagoras")
if s:
    for name,text in THEMEN.items():
        if s.lower() in name.lower() or s.lower() in text.lower():
            st.info(f"Gefunden {name}: {text}")
