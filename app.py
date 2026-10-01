import streamlit as st
import requests

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")
st.title("📚 Lern App - Mit Internet Suche")
st.write("Sucht in Wikipedia und Internet - nicht nur lokal")
st.write("---")

# INTERNET SUCHE FUNKTION
def suche_internet(thema):
    try:
        # Wikipedia Suche
        url = f"https://de.wikipedia.org/api/rest_v1/page/summary/{thema}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return f"**{data.get('title')}** (aus Wikipedia)\n\n{data.get('extract')}\n\nMehr: {data.get('content_urls', {}).get('desktop', {}).get('page', '')}"

        # Wenn nicht gefunden, suche mit Wikipedia Search
        search_url = f"https://de.wikipedia.org/w/api.php?action=opensearch&search={thema}&limit=3&namespace=0&format=json"
        r2 = requests.get(search_url, timeout=5)
        if r2.status_code == 200:
            results = r2.json()
            if results[1]:
                erster = results[1][0]
                return suche_internet(erster)
    except:
        pass
    return None

# LOKALE DATENBANK ALS BACKUP
faecher = {
"Französisch": "le la lui y en REIHENFOLGE me le lui y en+VERB J'y vais J'en veux, Direkte Indirekte Il dit qu'il est malade Il a dit qu'il était malade, Zeiten Passé 14 Verben mit être",
"Spanisch": "SE LO DOY le+lo->se lo, Ser permanent Soy aleman ESTAR Ort Zustand Estoy cansado, Por Grund Para Zweck",
"Englisch": "Zeiten Present Past Perfect Future, If Sätze If I go will If I went would If I had gone would have gone, Passive is made, Football NFL Super Bowl Touchdown Quarterback",
"Geschichte": "Franz Revolution 1789 Bastille, Weltkriege 1914-18 Sarajevo 1939-45 Polen Holocaust, Mauer 13.8.61-9.11.89, USA 1776 Unabhängigkeit Pearl Harbor 1941 Atombombe Hiroshima 6.8.1945 Nagasaki",
"Geographie": "Plattentektonik 5cm/Jahr, Klima CO2 280->420, USA 50 Staaten Rocky Mountains Mississippi",
"Biologie": "Zelle Mitochondrien Kraftwerk, Fotosynthese 6CO2+6H2O->Zucker+O2, DNA A-T C-G",
"Physik": "Newton F=m*a, Energie 0,5*m*v² m*g*h, Strom R=U/I, Atombombe E=mc² Kernspaltung Uran Kettenreaktion 15 Kilotonnen",
"Chemie": "Atombau Proton Neutron Elektron PSE, Bindungen NaCl, Säuren pH 0-14, Uran Plutonium Atombombe",
"Mathe": "Brüche 1/4+2/4=3/4 Pythagoras a²+b²=c² Ableitung x^n->n*x^(n-1) Wahrscheinlichkeit",
"USA": "USA 50 Staaten 340 Mio Hauptstadt Washington 1776 Unabhängigkeit Bürgerkrieg 1861-65 Pearl Harbor 1941 Atombombe Hiroshima Nagasaki 1945 Mondlandung 1969 NASA",
"Atombombe": "Atombombe Kernwaffe E=mc² Uran 235 Spaltung Kettenreaktion Manhattan Projekt Oppenheimer 1945 Hiroshima 6.8.1945 140k Tote Little Boy 15 Kilotonnen Nagasaki 9.8.1945 21 Kilotonnen Folgen Strahlung Sievert Krebs",
"Football": "American Football NFL 32 Teams Super Bowl Finale Touchdown 6 Punkte Field Goal 3 Punkte Quarterback wirft Running Back rennt Dallas Cowboys Kansas City Chiefs Unterschied Soccer=Fußball Football=American Football mit Helm"
}

# EINGABE
thema = st.text_input("🔍 Was willst du lernen? (z.B. USA, Atombombe, Football, Fotosynthese, y en, Pythagoras):", "")

# AUSWAHL INTERNET ODER LOKAL
quelle = st.radio("Wo suchen?", ["Internet + Lokal (empfohlen)", "Nur Internet (Wikipedia)", "Nur Lokal"], horizontal=True)

if thema:
    st.write("---")

    if quelle in ["Internet + Lokal", "Nur Internet"]:
        st.subheader(f"🌐 Internet Ergebnis für '{thema}':")
        with st.spinner("Suche im Internet..."):
            ergebnis = suche_internet(thema)
            if ergebnis:
                st.write(ergebnis)
                # Auch englisches Wikipedia versuchen für USA Football
                if thema.lower() in ["usa", "football", "nfl", "super bowl", "atombombe", "atomic bomb"]:
                    try:
                        en_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{thema}"
                        r_en = requests.get(en_url, timeout=5)
                        if r_en.status_code == 200:
                            data_en = r_en.json()
                            st.write(f"\n**English:** {data_en.get('extract','')[:500]}")
                    except:
                        pass
            else:
                st.write("Kein Wikipedia Artikel gefunden, versuche andere Schreibweise")

    if quelle in ["Internet + Lokal", "Nur Lokal"]:
        st.subheader(f"📚 Lokales Ergebnis für '{thema}':")
        s = thema.lower()
        gefunden = False
        for name, text in faecher.items():
            if s in name.lower() or s in text.lower() or s in name.lower().replace("ß","ss"):
                st.markdown(f"**{name}:**")
                st.write(text)
                st.write("---")
                gefunden = True

        if not gefunden:
            st.write("Lokal nichts, aber Internet oben hat vielleicht was!")

else:
    st.write("**Fächer zum Klicken:**")
    fach = st.selectbox("Fach wählen:", list(faecher.keys()))
    st.write(faecher[fach])

    st.write("---")
    st.write("**Tipps zum Suchen:**")
    st.write("- USA -> findet USA Geschichte + Geographie + Atombombe + Football")
    st.write("- Atombombe -> findet Physik E=mc² + Geschichte Hiroshima + Chemie Uran")
    st.write("- Football -> findet Englisch NFL + Super Bowl + Touchdown")
    st.write("- Fotosynthese -> sucht Wikipedia Fotosynthese")
    st.write("- y en -> lokal Französisch")

st.caption("lern_app.py - Mit Internet Suche - Einfacher Name")
