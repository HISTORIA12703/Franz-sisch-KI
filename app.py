import streamlit as st
import requests, urllib.parse

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 45px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 25px; border-radius: 15px; border: 2px solid #2E86AB; margin-bottom: 20px; }
.history-box { background-color: #fff3cd; padding: 20px; border-radius: 15px; border: 2px solid #ffc107; margin: 15px 0; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 10px; padding: 12px; font-weight: bold; }
.stButton > button:hover { background-color: #2E86AB; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App</div>', unsafe_allow_html=True)
st.markdown('<div class="search-box">', unsafe_allow_html=True)
st.markdown("### 🔍 Wonach möchtest du suchen?")
thema = st.text_input("", placeholder="z.B. USA, Atombombe, Fotosynthese, y en, Pythagoras...", label_visibility="collapsed", key="haupt")
st.markdown('</div>', unsafe_allow_html=True)

def suche_wikipedia(thema):
    try:
        headers = {'User-Agent': 'LernApp/1.0'}
        enc = urllib.parse.quote(thema.replace(" ", "_"))
        r = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers=headers, timeout=5)
        if r.status_code == 200 and 'extract' in r.json():
            d = r.json()
            return {"titel": d.get("title"), "text": d.get("extract"), "link": d.get("content_urls", {}).get("desktop", {}).get("page", "")}
        r2 = requests.get(f"https://de.wikipedia.org/w/api.php?action=opensearch&search={thema}&limit=1&namespace=0&format=json", headers=headers, timeout=5)
        if r2.status_code == 200:
            res = r2.json()
            if len(res)>1 and res[1]:
                enc2 = urllib.parse.quote(res[1][0].replace(" ", "_"))
                r3 = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc2}", headers=headers, timeout=5)
                if r3.status_code == 200:
                    d2 = r3.json()
                    return {"titel": d2.get("title"), "text": d2.get("extract"), "link": d2.get("content_urls", {}).get("desktop", {}).get("page", "")}
    except:
        pass
    return None

# GESCHICHTE MIT SUCHE WIE VORHIN
geschichte_themen = {
"französische revolution": """
**FRANZÖSISCHE REVOLUTION 1789 - AUSFÜHRLICH RICHTIG:**
WER? 1.Stand Klerus Kirche 1% Bevölkerung 10% Landbesitz keine Steuern 2.Stand Adel 2% 20% Land keine Steuern 3.Stand Bürger Bauer Handwerker 97% zahlt alle Steuern 50% Einkommen!

WARUM? 4 Gründe: 1.Absolutismus Ludwig XVI "L'état c'est moi" Ich bin der Staat Verschwendung Versailles 2000 Räume 2.Pleite Kriege Amerika Unabhängigkeit unterstützt 1Mrd Schulden 50% Staatshaushalt Zinsen! 3.Hunger 1788 schlechte Ernte Brotpreis +65% 70% Lohn nur für Brot! 4.Aufklärung Rousseau Volkssouveränität Volk soll herrschen Montesquieu Gewaltenteilung Locke Menschenrechte!

WANN GENAU?
5.5.1789 Generalstände Einberufung Versailles 3 Stände beraten getrennt 3.Stand will Kopfabstimmung
17.6.1789 Nationalversammlung 3.Stand erklärt sich zu Nationalversammlung
20.6.1789 Ballhausschwur Wir weichen nicht bis Verfassung!
14.7.1789 Sturm Bastille Gefängnis Paris Symbol Unterdrückung 7 Gefangene befreit Beginn Revolution!
26.8.1789 Menschenrechte Erklärung Freiheit Gleichheit Brüderlichkeit Eigentum Widerstand!
5.10.1789 Frauen ziehen nach Versailles König nach Paris holen
1791 Verfassung konstitutionelle Monarchie König bleibt aber Verfassung
10.8.1792 Sturm Tuilerien Republik
21.1.1793 Ludwig XVI geköpft Guillotine Place de la Concorde
1793-94 Schreckensherrschaft Robespierre Wohlfahrtsausschuss 40000 Tote Guillotine Verdächtige
1795-99 Direktorium 5 Direktoren Korruption
9.11.1799 Napoleon Putsch 18.Brumaire Ende Revolution Konsulat!

FOLGEN: Ende Feudalismus Leibeigenschaft abgeschafft Demokratie Volk wählt Nationalismus Völker wollen eigenen Staat Code Napoleon 1804 Gleichheit vor Gesetz Eigentum!
""",
"industrialisierung": """
**INDUSTRIALISIERUNG AB 1760 RICHTIG:**
WAS? Handarbeit -> Maschinen Fabriken Massenproduktion!

WO? Erst England 1760 weil Kohle Eisen Kolonien Kapital!

WARUM ENGLAND? Kohle Eisen vorhanden Kolonien Rohstoffe Kapital durch Handel Erfindungen!

ERFINDUNGEN: 1769 James Watt Dampfmaschine verbessert 1764 Spinning Jenny Spinnmaschine 1785 mechanischer Webstuhl 1807 erstes Dampfschiff 1814 erste Lokomotive Stephenson!

FOLGEN: Fabriken statt Heimarbeit Manchester 25000 Einwohner 1772 -> 300000 1850! Arbeiter 16h Tag 6 Tage Woche Kinderarbeit ab 6 Jahren 14h! Slums Krankheiten Cholera! Neue Klassen Fabrikbesitzer Bourgeoisie reich Arbeiter Proletariat arm!

IDEEN: Marx Engels Kommunistisches Manifest 1848 Proletarier aller Länder vereinigt euch! Gewerkschaften streiken! SPD 1875 Deutschland!

DEUTSCHLAND: Später ab 1835 erste Eisenbahn Nürnberg-Fürth Adler 6km! Ruhrgebiet Kohle Stahl Krupp! 2.Phase ab 1870 Elektrizität Chemie Elektromotor!

HEUTE: 3.Industrialisierung Computer 4. KI!
""",
"1 weltkrieg": """
**1.WELTKRIEG 1914-18 RICHTIG:**
URSACHEN: Imperialismus Kolonien Wettrüsten Deutschland England Flotte Nationalismus Bündnisse!

BÜNDNISSE: Mittelmächte Deutschland Österreich-Ungarn Osmanisches Reich vs Entente Frankreich Russland England später USA Italien!

AUSLÖSER: Attentat Sarajevo 28.6.1914 Gavrilo Princip serbischer Nationalist erschießt Franz Ferdinand Thronfolger Österreich-Ungarn und Frau Sophie!

ABLAUF: 28.7. Österreich erklärt Serbien Krieg 1.8. Deutschland Russland 3.8. Deutschland Frankreich 4.8. England Deutschland wegen Belgien!

SCHLIEFFENPLAN: Deutschland schnell durch Belgien nach Frankreich Paris in 6 Wochen dann Russland! Scheitert Marneslacht 1914!

WESTFRONT: Schützengraben 700km Nordsee bis Schweiz Verdun 1916 700000 Tote "Blutpumpe" Somme 1916 1Mio Tote Panzer erste Gas Chlor 1915!

OSTFRONT: Russland Tannenberg 1914 Deutschland siegt 1917 Russische Revolution Lenin Frieden Brest-Litowsk!

USA: 1917 Kriegseintritt wegen U-Boot Krieg Lusitania 1915 versenkt Zimmermann Telegramm!

ENDE: 11.11.1918 Waffenstillstand 11 Uhr Compiegne! 9.11. Kaiser Wilhelm II abdankt Republik!

VERSAILLES 28.6.1919: Deutschland allein Schuld Art 231 Reparationen 132Mrd Goldmark Gebietsverlust 13% Elsass-Lothringen an Frankreich Kolonien weg Armee 100000! 17Mio Tote!

FOLGE: Weimarer Republik 1919-33 instabil wegen Versailles!
""",
"2 weltkrieg": """
**2.WELTKRIEG 1939-45 RICHTIG:**

URSACHEN: Versailles 1919 Demütigung Weltwirtschaftskrise 1929 6Mio Arbeitslose Hitler NSDAP 1933 Machtergreifung!

BEGINN: 1.9.1939 Überfall Polen Blitzkrieg Panzer Luftwaffe 3.9. England Frankreich erklären Deutschland Krieg!

BLITZKRIEG: 1940 Dänemark Norwegen April Mai Frankreich 6 Wochen besetzt! 1940 Luftschlacht England England hält!

BALKAN RUSSLAND: 1941 Balkanfeldzug Jugoslawien Griechenland 22.6.1941 Unternehmen Barbarossa Russland 3Mio Soldaten größte Invasion! Moskau Winter -40 scheitert!

AFRIKA: Rommel Wüstenfuchs vs Montgomery El Alamein 1942!

PAZIFIK: 7.12.1941 Pearl Harbor Japan greift USA an USA Krieg! 1942 Midway Wende Pazifik!

HOLOCAUST: 6Mio Juden ermordet Auschwitz 1,1Mio! Wannsee Konferenz 20.1.1942 Heydrich Endlösung! Ghettos Einsatzgruppen Vergasung!

WENDE: Stalingrad 1942-43 6.Armee Paulus 300000 eingekesselt 91k Gefangene 6k zurück! 1943 Kursk größte Panzerschlacht! Italien kapituliert 1943!

D-DAY: 6.6.1944 Normandie Operation Overlord 150000 Alliierte landen Eisenhower!

ENDE EUROPA: 30.4.45 Hitler Selbstmord Berlin 8.5.45 Kapitulation Jodl Keitel!

ATOMBOMBE: 6.8.1945 Hiroshima Little Boy Uran 140000 Tote sofort + später 9.8. Nagasaki Fat Man Plutonium 70000! Grund Japan kapituliert 2.9.1945! Folgen Strahlung Krebs!

FOLGEN: 60Mio Tote 6Mio Deutsche Deutschland geteilt BRD DDR 1949 UN 1945 gegründet!
""",
"kalter krieg": """
**KALTER KRIEG 1947-1990 RICHTIG:**
WAS? USA Kapitalismus Demokratie Marktwirtschaft vs UdSSR Kommunismus Diktatur Planwirtschaft! Kein direkter Krieg Stellvertreter Kriege!

BERLIN: Blockade 24.6.48-12.5.49 UdSSR sperrt West Berlin 2Mio Menschen! Luftbrücke USA 277000 Flüge Rosinenbomber 1 Jahr! NATO 4.4.1949 Westen USA England Frankreich BRD! Warschauer Pakt 14.5.1955 Osten UdSSR DDR!

MAUER: 13.8.1961 Sonntag Nacht Stacheldraht Walter Ulbricht Niemand hat Absicht Mauer zu errichten! 155km 3,6m hoch 302 Türme 140 Tote Peter Fechter 1962 verblutet!

KUBA KRISE: 16.-28.10.1962 13 Tage fast Atomkrieg! UdSSR Raketen auf Kuba 150km USA! Kennedy vs Chruschtschow Blockade! Chruschtschow zieht zurück!

VIETNAM: 1965-75 USA vs Nordvietnam Dschungel Napalm USA verliert 58000 Tote 2Mio Vietnamesen!

ENTSPANNUNG: Brandt 1969 Kanzler Ostpolitik Wandel durch Annäherung Kniefall Warschau 1970! 1975 Helsinki!

GORBATSCHOW: 1985 Generalsekretär Glasnost Offenheit Perestroika Umbau! Lässt los!

ENDE: Montagsdemos Leipzig ab 4.9.89 Wir sind das Volk Wir sind EIN Volk! Ungarn öffnet Grenze 10.9.89 15000 DDR Bürger! Mauerfall 9.11.89 22:30 Schabowski Pressekonferenz sofort unverzüglich! 3.10.90 Einheit Kohl!

HEUTE: NATO Osterweiterung Russland Konflikt Ukraine!
""",
"usa geschichte": """
**USA GESCHICHTE RICHTIG:**
1776 Unabhängigkeit 13 Kolonien England 4.7.1776 Declaration Jefferson Wir halten Wahrheiten für selbstverständlich Leben Freiheit Streben nach Glück! George Washington erster Präsident 1789-97!

1861-65 Bürgerkrieg Nord Industrie vs Süd Sklaverei Baumwolle! Abraham Lincoln 1860 Präsident Sklaverei abschaffen! Süd tritt aus Konföderation! 1863 Gettysburg Wende! 1865 Nord siegt 620000 Tote! 1865 13.Amendment Sklaverei abgeschafft! Lincoln ermordet 14.4.65!

1898 Spanisch-Amerikanisch Kuba Philippinen USA Weltmacht!

1917 1.WK 1941 Pearl Harbor 7.12.41 Japan greift an 2400 Tote! USA 2.WK D-Day Atombombe!

1947-90 Kalter Krieg Supermacht vs UdSSR!

1969 Mondlandung 20.7.69 Neil Armstrong Ein kleiner Schritt für Mensch großer für Menschheit Apollo 11!

BÜRGERRECHTE: 1964 Martin Luther King I have a dream 1963 1964 Civil Rights Act Rassentrennung verboten!

HEUTE: 50 Staaten 340Mio Einwohner Hauptstadt Washington 1776 Unabhängigkeit größte Wirtschaft Dollar Weltwährung!
""",
"mauer ddr brd": """
**MAUER DDR BRD RICHTIG:**

BRD: 23.5.1949 Grundgesetz Bonn Grundrechte Demokratie Soziale Marktwirtschaft! Adenauer 1949-63 Westintegration Wirtschaftswunder 1950s! Brandt 1969-74 Ostpolitik Kniefall! Schmidt Kohl 1982-98 Einheit 1990!

DDR: 7.10.1949 Ost Berlin Sowjetische Zone SED Sozialistische Einheitspartei Planwirtschaft 5 Jahres Plan Mangel Trabant 15 Jahre Wartezeit! Stasi Ministerium Staatssicherheit 91000 hauptamtlich 173000 IM inoffizielle Mitarbeiter Spitzel! Mangel Bananen! Mauer 1961! Montagsdemos 1989 Nikolaikirche Leipzig!

MAUER: 13.8.61 Bau 9.11.89 Fall 28 Jahre! 155km um West Berlin 3,6m hoch Todesstreifen Hund Lauf Anlage! 140 Tote beim Fluchtversuch letzte Chris Gueffroy 5.2.89! Checkpoint Charlie!

EINHEIT: 9.11.89 Fall 18.3.90 freie Wahl DDR 3.10.90 Beitritt nach Art 23! Kohl Kohl Birne Kanzler Einheit! Treuhand Abwicklung DDR Betriebe Arbeitslosigkeit! Heute Ost-West Unterschied noch!

BERLIN: 1945 geteilt 4 Sektoren 1961 Mauer 1989 Fall Hauptstadt seit 1991 wieder Berlin!
"""
}

faecher = {
"Französisch": "le la lui y en REIHENFOLGE me te se nous vous + le la les + lui leur + y + en + VERB J'y vais J'en veux Il dit qu'il est malade Il a dit qu'il était malade que->ce que si de+Inf Passé 14 Verben mit être aller venir Imparfait je parlais Futur parlerai",
"Spanisch": "SE LO DOY le+lo->se lo Ser permanent Soy aleman Estar Ort Zustand Estoy en casa Estoy cansado Por Grund Durch Para Zweck Ziel",
"Englisch": "Zeiten Present I go Past I went Perfect I have gone Future will If Sätze If I go will If I went would If I had gone would have gone Passive is made",
"Italienisch": "ci ne = y en Ci vado Ne voglio glielo Glielo do Essere permanent Sono tedesco Stare Ort Zustand Sto a casa Sto mangiando al del nel",
"Latein": "ego tu is Kasus Nom Gen Dat Akk Abl AcI Dico eum venire Gerundium amandum PPA amans PPP amatus Zeiten amo amabam amavi",
"Deutsch": "Konjunktiv I er sei er habe Wenn I=Indikativ dann II sie hätten Kasus Nom Gen Dat Akk Nebensatz Verb Ende",
"Mathe": "Brüche 1/4+2/4=3/4 Gleichungen 2x+4=10 x=3 Mitternacht Pythagoras a²+b²=c² Ableitung x^n->n*x^(n-1) Wahrscheinlichkeit",
"Geographie": "Plattentektonik 5cm/Jahr Klima Wetter vs Klima 30J Klimawandel CO2 280->420 Bevölkerung 8Mrd Migration Urbanisierung",
"Biologie": "Zelle Mitochondrien Kraftwerk Fotosynthese 6CO2+6H2O->Zucker+O2 DNA A-T C-G Gen Chromosom 46 Mitose Meiose Mendel Evolution Darwin Herz 4 Kammern AB0",
"Physik": "Newton F=m*a v=s/t g=9,81 Energie 0,5*m*v² m*g*h Strom R=U/I Reihe Parallel P=U*I Optik Einfall=Ausfall Brechung",
"Chemie": "Atombau Proton Neutron Elektron PSE Bindungen NaCl Säuren pH 0-14 Redox Oxidation Abgabe Reduktion Aufnahme"
}

# HAUPTSUCHE
if thema:
    st.write("---")
    st.markdown(f"### Ergebnis für '{thema}':")
    wiki = suche_wikipedia(thema)
    if wiki:
        st.info(f"**🌐 {wiki['titel']}**\n\n{wiki['text']}")
        if wiki['link']:
            st.markdown(f"[Mehr]({wiki['link']})")
        st.write("---")
    s = thema.lower()
    for name, text in faecher.items():
        if s in text.lower() or s in name.lower():
            st.markdown(f"**📚 {name}:**")
            st.write(text)
            st.write("---")
    # Geschichte auch suchen
    for g_name, g_text in geschichte_themen.items():
        if s in g_name or s in g_text.lower():
            st.markdown(f"**📚 Geschichte - {g_name}:**")
            st.write(g_text)
            st.write("---")

st.write("---")
st.markdown("### 📖 Fächer - Bei Geschichte musst du suchen:")

# FÄCHER BUTTONS
cols = st.columns(3)
fach_liste = list(faecher.keys()) + ["Geschichte"]

for i, fach_name in enumerate(fach_liste):
    col = cols[i % 3]
    if col.button(fach_name, key=f"btn_{fach_name}"):
        st.session_state['fach'] = fach_name

# WENN FACH GEWÄHLT
if 'fach' in st.session_state:
    st.write("---")

    if st.session_state['fach'] == "Geschichte":
        st.markdown("<h2 style='color:#ffc107;'>📚 Geschichte - Was willst du lernen?</h2>", unsafe_allow_html=True)
        st.markdown('<div class="history-box">', unsafe_allow_html=True)
        st.markdown("**Suche in Geschichte:** z.B. französische revolution, 1 weltkrieg, 2 weltkrieg, kalter krieg, mauer ddr, usa geschichte, industrialisierung")
        gesch_suche = st.text_input("Geschichte Thema suchen:", placeholder="z.B. revolution, weltkrieg, mauer, usa, industrialisierung...", key="gesch")
        st.markdown('</div>', unsafe_allow_html=True)

        if gesch_suche:
            s2 = gesch_suche.lower()
            gefunden = False
            for g_name, g_text in geschichte_themen.items():
                if s2 in g_name or s2 in g_text.lower():
                    st.markdown(f"### {g_name.upper()}")
                    st.write(g_text)
                    st.write("---")
                    gefunden = True
            if not gefunden:
                st.warning("Nichts in Geschichte gefunden - versuche revolution, weltkrieg, mauer, usa, industrialisierung, kalter")
        else:
            st.write("**Alle Geschichte Themen zum Klicken:**")
            g_cols = st.columns(2)
            for j, g_name in enumerate(geschichte_themen.keys()):
                g_col = g_cols[j % 2]
                if g_col.button(g_name, key=f"g_{g_name}"):
                    st.session_state['gesch_thema'] = g_name

            if 'gesch_thema' in st.session_state:
                st.write("---")
                st.markdown(f"## {st.session_state['gesch_thema']}")
                st.write(geschichte_themen[st.session_state['gesch_thema']])

    else:
        st.markdown(f"## {st.session_state['fach']}")
        st.write(faecher[st.session_state['fach']])

    if st.button("❌ Fach schließen"):
        del st.session_state['fach']
        if 'gesch_thema' in st.session_state:
            del st.session_state['gesch_thema']
        st.rerun()

st.caption("app.py - Geschichte mit eigener Suche wie vorhin")
