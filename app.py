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

st.markdown('<div class="main-title">📚 Lern App - Mit Internet Fakten</div>', unsafe_allow_html=True)
st.markdown('<div class="search-box">', unsafe_allow_html=True)
st.markdown("### 🔍 Wonach möchtest du suchen? (Google + Wikipedia + Alles)")
thema = st.text_input("", placeholder="z.B. Adolf Hitler, USA, Atombombe, Fotosynthese, y en, ser estar, Pythagoras, DDR, Mauer...", label_visibility="collapsed", key="haupt")
st.markdown('</div>', unsafe_allow_html=True)

def multi_suche(thema):
    ergebnisse = []
    headers = {'User-Agent': 'LernApp/1.0 Schulprojekt'}

    # 1. Wikipedia DE
    try:
        enc = urllib.parse.quote(thema.replace(" ", "_"))
        r = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers=headers, timeout=5)
        if r.status_code == 200:
            d = r.json()
            if 'extract' in d:
                ergebnisse.append({"quelle": "Wikipedia DE", "titel": d.get("title"), "text": d.get("extract"), "link": d.get("content_urls", {}).get("desktop", {}).get("page", "")})
    except:
        pass

    # 2. Wikipedia EN für mehr Fakten (USA etc)
    try:
        enc_en = urllib.parse.quote(thema.replace(" ", "_"))
        r_en = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{enc_en}", headers=headers, timeout=5)
        if r_en.status_code == 200:
            d_en = r_en.json()
            if 'extract' in d_en and d_en.get("title") not in [x["titel"] for x in ergebnisse]:
                ergebnisse.append({"quelle": "Wikipedia EN", "titel": d_en.get("title"), "text": d_en.get("extract"), "link": d_en.get("content_urls", {}).get("desktop", {}).get("page", "")})
    except:
        pass

    # 3. Wikipedia Suche (falls direkter Artikel nicht gefunden)
    if not ergebnisse:
        try:
            search_url = f"https://de.wikipedia.org/w/api.php?action=opensearch&search={thema}&limit=3&namespace=0&format=json"
            r2 = requests.get(search_url, headers=headers, timeout=5)
            if r2.status_code == 200:
                res = r2.json()
                if len(res) > 1 and res[1]:
                    for name in res[1][:2]:
                        enc2 = urllib.parse.quote(name.replace(" ", "_"))
                        r3 = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc2}", headers=headers, timeout=5)
                        if r3.status_code == 200:
                            d2 = r3.json()
                            if 'extract' in d2:
                                ergebnisse.append({"quelle": "Wikipedia Suche", "titel": d2.get("title"), "text": d2.get("extract"), "link": d2.get("content_urls", {}).get("desktop", {}).get("page", "")})
        except:
            pass

    # 4. DuckDuckGo (wie Google - liefert Fakten aus vielen Quellen)
    try:
        ddg_url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(thema)}&format=json&pretty=1&no_html=1&skip_disambig=1"
        r_ddg = requests.get(ddg_url, headers=headers, timeout=5)
        if r_ddg.status_code == 200:
            d_ddg = r_ddg.json()
            if d_ddg.get("AbstractText"):
                ergebnisse.append({"quelle": f"DuckDuckGo / {d_ddg.get('AbstractSource','Web')}", "titel": d_ddg.get("Heading", thema), "text": d_ddg.get("AbstractText"), "link": d_ddg.get("AbstractURL","")})
            # Related Topics
            if d_ddg.get("RelatedTopics"):
                for topic in d_ddg["RelatedTopics"][:2]:
                    if isinstance(topic, dict) and topic.get("Text"):
                        ergebnisse.append({"quelle": "DuckDuckGo Fakt", "titel": topic.get("Text")[:50]+"...", "text": topic.get("Text"), "link": topic.get("FirstURL","")})
    except:
        pass

    return ergebnisse

# FÄCHER LOKAL RICHTIG
faecher = {
"Französisch": "LE=ihn/es OHNE a Je LE mange LA=sie Je LA vois LES=sie Plural LUI=ihm/ihr MIT a Person Je parle À Marie -> Je LUI parle LEUR=ihnen Y=dort Ort à+Sache Je vais À Paris -> J'Y vais J'Y pense Sache! EN=davon de/du/des Zahl J'EN veux J'EN ai 3 REIHENFOLGE me te se nous vous + le la les + lui leur + y + en + VERB",
"Spanisch": "SE LO DOY! LE+LO->SE! SER=WAS IST permanent Soy Juan ESTAR=WO WIE GERADE Estoy en casa POR=Grund Durch Dauer PARA=Ziel Zweck Empfänger",
"Englisch": "Present I go he goes Past I went Perfect I have gone Future will If Type0 boils Type1 If I GO I WILL Type2 If I WENT I WOULD Type3 If I HAD GONE I WOULD HAVE GONE Passive IS MADE",
"Italienisch": "ci=y ne=en CI vado NE voglio glielo Glielo do ESSERE permanent STARE Ort Zustand gerade Sto a casa Sto mangiando",
"Latein": "5 Kasus Nom Gen Dat Akk Abl AcI Dico eum venire Gerundium amandum PPA amans PPP amatus",
"Deutsch": "Konjunktiv I sei habe solle Wenn I=Indikativ dann II hätten",
"Mathe": "Brüche Pythagoras a²+b²=c² Mitternacht Ableitung x^n->n*x^(n-1) Wahrscheinlichkeit",
"Geographie": "Plattentektonik 5cm/Jahr Klima 30J CO2 280->420 Bevölkerung 8Mrd",
"Biologie": "Mitochondrien Kraftwerk Fotosynthese 6CO2+6H2O->Zucker+O2 DNA A-T C-G 46 Chromosomen Mitose Meiose Evolution",
"Physik": "Newton F=m*a Energie 0,5*m*v² Strom R=U/I P=U*I",
"Chemie": "Proton Neutron Elektron PSE Ionen NaCl kovalent H2O pH 0-14 Säure+Base->Salz+Wasser Redox Oxidation Abgabe Reduktion Aufnahme"
}

geschichte_themen = {
"französische revolution": "FRANZ REV 1789: 1.Stand 1% 10% Land keine Steuern 2.Stand 2% 20% Land keine Steuern 3.Stand 97% zahlt alles! Ludwig XVI pleite Hunger Aufklärung! 14.7. Bastille 26.8. Menschenrechte 21.1.93 Ludwig geköpft Robespierre 40k Tote 1799 Napoleon!",
"1 weltkrieg": "1.WK 1914-18: Sarajevo 28.6.14 Princip erschießt Franz Ferdinand! Schützengraben Verdun 700k! 11.11.18 Ende Versailles 28.6.19 132Mrd 17Mio Tote!",
"2 weltkrieg": "2.WK 1939-45: 1.9.39 Polen 1940 Frankreich 22.6.41 Russland 7.12.41 Pearl Harbor Holocaust 6Mio Auschwitz Wannsee 20.1.42 Stalingrad D-Day 6.6.44 8.5.45 Kapitulation Hiroshima 6.8.45 140k Nagasaki 9.8. 70k 60Mio Tote!",
"kalter krieg mauer ddr brd": "KALTER KRIEG: NATO 49 Warschauer Pakt 55 Mauer 13.8.61-9.11.89 28J 155km 140 Tote Kuba 62 Vietnam 65-75 Brandt Ostpolitik Gorbatschow Montagsdemos Mauerfall 9.11.89 3.10.90 Einheit BRD 23.5.49 DDR 7.10.49!",
"usa": "USA: 1776 Unabhängigkeit Washington 1861-65 Bürgerkrieg Lincoln Sklaverei Ende Pearl Harbor 7.12.41 Mondlandung 20.7.69 Armstrong 50 Staaten!",
"adolf hitler nationalsozialismus": "ADOLF HITLER 1889-1945: Geb 20.4.1889 Braunau Österreich Maler gescheitert 1.WK Soldat NSDAP 1920 1923 Putsch München Gefängnis Mein Kampf 1933 Machtergreifung 30.1.33 Reichskanzler Ermächtigungsgesetz Diktator Führer Gleichschaltung Propaganda Goebbels SS Himmler Gestapo Juden Verfolgung Nürnberger Gesetze 1935 Kristallnacht 9.11.38 1939-45 2.WK Holocaust 6Mio Juden Auschwitz Selbstmord 30.4.45 Berlin Bunker! Fakten: Diktatur 1933-45 totalitär Autobahn Propaganda Olympiade 36 aber Krieg Völkermord!"
}

# HAUPTSUCHE ANZEIGE
if thema:
    st.write("---")
    st.markdown(f"### 🔍 Alle Fakten für '{thema}' aus Internet:")

    with st.spinner("Suche bei Google, Wikipedia, DuckDuckGo..."):
        alle = multi_suche(thema)

    if alle:
        for erg in alle:
            st.markdown(f'<div class="result-box"><b>🌐 {erg["quelle"]}: {erg["titel"]}</b><br>{erg["text"]}</div>', unsafe_allow_html=True)
            if erg["link"]:
                st.markdown(f"[🔗 Mehr: {erg['link']}]({erg['link']})")
            st.write("")
    else:
        st.warning(f"Kein Internet Artikel direkt gefunden für '{thema}' - versuche anderen Begriff oder schau unten bei lokalen Fächern")

    st.write("---")
    s = thema.lower()
    # Lokal auch suchen
    for name, text in faecher.items():
        if s in text.lower() or s in name.lower():
            st.markdown(f"**📚 Lokal {name}:**")
            st.write(text)
            st.write("---")
    for g_name, g_text in geschichte_themen.items():
        if s in g_name or s in g_text.lower():
            st.markdown(f"**📚 Lokal Geschichte {g_name}:**")
            st.write(g_text)
            st.write("---")

st.write("---")
st.markdown("### 📖 Alle 12 Fächer:")

cols = st.columns(3)
fach_liste = ["Französisch","Spanisch","Englisch","Italienisch","Latein","Deutsch","Mathe","Geschichte","Geographie","Biologie","Physik","Chemie"]

for i, fach_name in enumerate(fach_liste):
    col = cols[i % 3]
    if col.button(fach_name, key=f"btn_{fach_name}"):
        st.session_state['fach'] = fach_name

if 'fach' in st.session_state:
    st.write("---")
    if st.session_state['fach'] == "Geschichte":
        st.markdown("## 📚 Geschichte - Mit Internet Suche!")
        st.markdown('<div class="history-box">', unsafe_allow_html=True)
        st.markdown("Suche auch bei Google + Wikipedia! z.B. Adolf Hitler, Mauer, DDR, USA, 2 weltkrieg, industrialisierung")
        gesch_suche = st.text_input("Geschichte Thema suchen (Internet + lokal):", placeholder="z.B. Adolf Hitler, Mauer, DDR, USA, Revolution...", key="gesch")
        st.markdown('</div>', unsafe_allow_html=True)

        if gesch_suche:
            st.markdown(f"### Internet Fakten für '{gesch_suche}':")
            with st.spinner("Suche im Internet..."):
                internet = multi_suche(gesch_suche)
            if internet:
                for erg in internet:
                    st.info(f"**{erg['quelle']}: {erg['titel']}**\n\n{erg['text']}\n\n{erg['link']}")
            else:
                st.warning("Kein Internet Ergebnis - zeige lokale Fakten:")

            st.write("---")
            st.markdown("### Lokale Fakten:")
            s2 = gesch_suche.lower()
            found = False
            for g_name, g_text in geschichte_themen.items():
                if s2 in g_name or s2 in g_text.lower():
                    st.markdown(f"**{g_name.upper()}**")
                    st.write(g_text)
                    st.write("---")
                    found = True
            if not found and not internet:
                st.error("Nichts gefunden - versuche Hitler, Mauer, DDR, USA, Revolution, Weltkrieg")
        else:
            g_cols = st.columns(2)
            for j, g_name in enumerate(geschichte_themen.keys()):
                if g_cols[j % 2].button(g_name, key=f"g_{g_name}"):
                    st.session_state['gesch_thema'] = g_name
            if 'gesch_thema' in st.session_state:
                st.write("---")
                st.markdown(f"## {st.session_state['gesch_thema']}")
                st.write(geschichte_themen[st.session_state['gesch_thema']])
                with st.spinner("Hole mehr Fakten aus Internet..."):
                    more = multi_suche(st.session_state['gesch_thema'])
                    for erg in more:
                        st.info(f"**{erg['quelle']}:** {erg['text'][:500]}...")

    else:
        st.markdown(f"## {st.session_state['fach']}")
        st.write(faecher[st.session_state['fach']])

    if st.button("❌ Schließen"):
        del st.session_state['fach']
        if 'gesch_thema' in st.session_state:
            del st.session_state['gesch_thema']
        st.rerun()

st.caption("app.py - Sucht jetzt bei Wikipedia DE + EN + DuckDuckGo (Google ähnlich) + lokal = viele Fakten!")
