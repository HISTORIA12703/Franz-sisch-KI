import streamlit as st
import requests, urllib.parse

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 40px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 20px; border-radius: 15px; border: 2px solid #2E86AB; margin-bottom: 15px; }
.sub-box { background-color: #e3f2fd; padding: 15px; border-radius: 10px; border: 2px solid #2196f3; margin: 10px 0; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 8px; padding: 8px; font-weight: bold; min-height: 40px; font-size: 13px; }
.stButton > button:hover { background-color: #2E86AB; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App</div>', unsafe_allow_html=True)
st.markdown('<div class="search-box">', unsafe_allow_html=True)
thema = st.text_input("Suche", placeholder="", label_visibility="collapsed", key="haupt")
st.markdown('</div>', unsafe_allow_html=True)

def multi_suche(thema):
    ergebnisse = []
    headers = {'User-Agent': 'LernApp/1.0'}
    try:
        enc = urllib.parse.quote(thema.replace(" ", "_"))
        r = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers=headers, timeout=5)
        if r.status_code == 200 and 'extract' in r.json():
            d = r.json()
            ergebnisse.append({"quelle": "Wikipedia", "titel": d.get("title"), "text": d.get("extract"), "link": d.get("content_urls", {}).get("desktop", {}).get("page", "")})
    except:
        pass
    return ergebnisse

# ALLE FÄCHER MIT UNTERGEORDNETEN BEGRIFFEN
alle_faecher = {
"Französisch": {
    "Vokabeln": "le pain Brot la pomme Apfel le livre Buch la maison Haus aller gehen venir kommen faire machen dire sagen voir sehen vouloir wollen pouvoir können manger essen bon gut grand groß ici hier maintenant jetzt",
    "le la les lui leur": "LE=ihn/es OHNE a Je LE mange LA=sie Je LA vois LES=sie Plural LUI=ihm/ihr MIT a Person Je parle À Marie->LUI LEUR=ihnen AUX enfants->LEUR",
    "y en": "Y=dort Ort Sache Je vais À Paris->J'Y vais J'Y pense Sache EN=davon de/du/des Zahl J'EN veux J'EN ai 3",
    "Reihenfolge": "me te se nous vous + le la les + lui leur + y + en + VERB Il ME LE donne Il Y EN a",
    "indirekte Rede": "Il dit qu'il est malade bleibt Il a dit qu'il ÉTAIT malade Present->Imparfait J'ai mangé->avait mangé Futur->Conditionnel Que->ce que Si->si Befehl de venir",
    "Zeiten": "Passé composé 14 Verben mit être aller venir je suis allé Imparfait je parlais Futur je parlerai Conditionnel je parlerais"
},
"Spanisch": {
    "Vokabeln": "el pan Brot la manzana Apfel ir gehen venir kommen hacer machen decir sagen ver sehen querer wollen poder können comer essen bueno gut grande groß aquí hier ahora jetzt",
    "lo la le les": "LO=ihn Veo EL LIBRO->LO veo LE=ihm MIT a Hablo A JUAN->LE hablo",
    "se lo doy": "LE+LO wird SE! FALSCH Le lo doy RICHTIG SE LO DOY! Se los doy Me lo da",
    "ser estar": "SER=WAS IST permanent Soy Juan Soy de Alemania Soy alto Son las 3 ESTAR=WO WIE GERADE Estoy en casa Estoy cansado Está roto Estoy comiendo gerade",
    "por para": "POR=Grund Durch Dauer Gracias POR todo Voy POR calle POR 2 horas PARA=Ziel Zweck Para comer Para ti Para Madrid Para mañana"
},
"Englisch": {
    "Vokabeln": "bread Brot apple Apfel go gehen come kommen make machen say sagen see sehen want wollen can können eat essen good gut big groß here hier now jetzt",
    "Zeiten": "Present I go he goes Do you? Past I went Did you? Perfect I have gone have+PP since for Past Perfect I had gone Future will going to",
    "indirekte Rede": "He says he IS ill bleibt He said he WAS ill Present->Past Where are you?->where he WAS Do you?->if he CAME Come!->to come",
    "if Sätze": "Type0 If you heat water it boils Type1 If I GO I WILL go Type2 If I WENT I WOULD go Type3 If I HAD GONE I WOULD HAVE GONE",
    "Passive": "be+PP IS MADE WAS MADE HAS BEEN MADE WILL BE MADE BY ME"
},
"Italienisch": {
    "Vokabeln": "il pane Brot la mela Apfel andare gehen venire kommen fare machen dire sagen vedere sehen volere wollen potere können mangiare essen",
    "lo gli ci ne": "LO=ihn Vedo IL LIBRO->LO GLI=ihm MIT a Parlo A GIOVANNI->GLI CI=y Ort Sache Vado A Parigi->CI vado NE=en davon NE voglio",
    "essere stare glielo": "Glielo do Me lo da ESSERE permanent Sono Giovanni STARE Ort Zustand gerade Sto a casa Sto mangiando"
},
"Latein": {
    "Vokabeln": "panis Brot malum Apfel liber Buch ego ich tu du is ea id er sie es bonus gut magnus groß",
    "Kasus": "Nom Wer? puella Gen Wessen? puellae Dat Wem? puellae Akk Wen? puellam Abl Womit? cum puella",
    "Deklinationen": "1.a puella Gen puellae 2.o servus Gen servi bellum Gen belli 3.rex Gen regis 4.u fructus 5.e res Gen rei",
    "AcI Gerundium Partizip": "AcI Dico eum venire Ich sage dass er kommt Gerundium amandum das Lieben PPA amans liebend PPP amatus geliebt"
},
"Deutsch": {
    "Vokabeln Grammatik Grund": "Nomen Verb Adjektiv Artikel der die das Pronomen ich du er",
    "Konjunktiv I II": "Konjunktiv I indirekte er sei er habe er solle Wenn I=Indikativ dann II sie haben Auto haben=haben gleich also sie hätten! Konjunktiv II irreal wäre hätte würde wenn ich Zeit hätte käme ich",
    "Kasus": "Nominativ Wer? Der Mann Genitiv Wessen? des Mannes Dativ Wem? dem Mann Akkusativ Wen? den Mann",
    "Nebensätze Zeiten": "Nebensatz Verb Ende dass er kommt weil er krank ist obwohl Zeiten Präsens gehe Perfekt bin gegangen Präteritum ging Plusquam war gegangen Futur werde gehen"
},
"Mathe": {
    "Brüche Prozent": "1/4+2/4=3/4 1/2+1/3=5/6 Multi 1/2*3/4=3/8 Divi Kehrwert 1/2:1/4=2 Prozent %= /100 Dreisatz 100%=50 1%=0,5 20%=10",
    "Gleichungen": "Waage beide Seiten gleich 2x+4=10 x=3 Mitternacht x=(-b±√(b²-4ac))/2a pq x=-p/2±√((p/2)²-q) D>0 2 Lösungen D=0 1 D<0 keine",
    "Geometrie": "Pythagoras a²+b²=c² nur 90° Rechteck a*b Kreis 2πr πr² Quader a*b*c Würfel a³ Zylinder πr²*h Kugel 4/3πr³ sin=GK/Hyp cos=AK/Hyp tan=GK/AK sin²+cos²=1",
    "Ableitung Integral": "x^n->n*x^(n-1) x³->3x² Produkt u'v+uv' Kette äußere*innere f'=0 Extrem Hoch Tief Integral ∫x^n=x^(n+1)/(n+1)+C Fläche F(b)-F(a)",
    "Wahrscheinlichkeit": "P=günstige/alle Würfel P(6)=1/6 UND multi ODER add Baum Pfad multi Binomial (n über k)*p^k*(1-p)^(n-k)"
},
"Geschichte": {
    "französische revolution": "1789 1.Stand 1% 10% Land keine Steuern 2.Stand 2% 20% keine Steuern 3.Stand 97% zahlt alles Ludwig XVI pleite Hunger Aufklärung Rousseau 5.5.89 Generalstände 14.7. Bastille 26.8. Menschenrechte 21.1.93 Ludwig geköpft Robespierre 40k 1799 Napoleon Ende Demokratie Menschenrechte",
    "industrialisierung": "1760 England Kohle Eisen Watt Dampfmaschine 1769 Fabriken Manchester 25k->300k 16h Kinderarbeit Marx 1848 SPD 1875 Eisenbahn 1835",
    "1 weltkrieg": "1914-18 Imperialismus Sarajevo 28.6.14 Princip Franz Ferdinand Mittelmächte DE Ö vs Entente FR RU EN Schlieffenplan Belgien Schützengraben 700km Verdun 700k 11.11.18 Waffenstillstand Versailles 28.6.19 132Mrd 17Mio Tote Weimar",
    "2 weltkrieg": "1939-45 Versailles Krise Hitler 33 1.9.39 Polen Blitzkrieg 1940 Frankreich 22.6.41 Russland 7.12.41 Pearl Harbor Holocaust 6Mio Auschwitz Wannsee 20.1.42 Stalingrad Jan43 D-Day 6.6.44 8.5.45 Hiroshima 6.8.45 140k Nagasaki 9.8. 70k 60Mio Tote UN",
    "kalter krieg mauer ddr brd": "1947-90 USA vs UdSSR Berlin Blockade 48-49 Luftbrücke NATO 49 Warschauer Pakt 55 Mauer 13.8.61-9.11.89 28J 155km 140 Tote Kuba 62 13 Tage Vietnam 65-75 Brandt Ostpolitik Gorbatschow Glasnost Montagsdemos 9.11.89 Fall 3.10.90 Einheit BRD 23.5.49 DDR 7.10.49",
    "usa adolf hitler": "USA 1776 Unabhängigkeit 13 Kolonien Washington 1861-65 Bürgerkrieg Lincoln Sklaverei Ende 340Mio Hitler 1889-1945 Braunau NSDAP 1933 Diktator 2.WK Holocaust Selbstmord 30.4.45"
},
"Geographie": {
    "Plattentektonik": "Kruste 5-70km Mantel 2900km Kern 5000° 5cm/Jahr divergent Rücken Island wächst konvergent Himalaya Anden Subduktion Erdbeben Vulkan transform San Andreas Erdbeben Hypozentrum unten Epizentrum oben Richter log10 Tsunami Vulkan Hotspot Hawaii Ring of Fire Schild flach Lava flüssig Schicht steil explosiv",
    "Klima": "Wetter täglich kurzfristig Klima 30J Durchschnitt 1991-2020 Zonen Polar -40 Eis Gemäßigt 4 Jahreszeiten Subtropen warm trocken Mittelmeer 30°C Tropen heiß feucht 25°C Wüste 50°C Tag -10°C Nacht Klimawandel CO2 280->420 +50% Treibhaus CO2 CH4 +1,2°C Meer +20cm Gletscher Extremwetter",
    "Bevölkerung Migration": "8Mrd 2026 Demografischer Übergang 5 Phasen hoch hoch wenig Wachstum früher Afrika Phase5 niedrig niedrig alt Deutschland Migration Push Krieg Armut Pull Arbeit Sicherheit Urbanisierung Landflucht 1900 10% Stadt 2026 56% Stadt Megacity 10Mio+ Tokio 37Mio",
    "Globalisierung": "Welt vernetzt Handel Internet Container 1960 Lieferketten iPhone USA Design China Bau Gewinner Firmen Verlierer Arbeiter Corona Abhängigkeit"
},
"Biologie": {
    "Zelle": "Prokaryot kein Kern 1μm keine Organellen nur Ribosomen Eukaryot mit Kern 10-100μm Organellen Tier Membran Zaun Doppellipid selektiv Zytoplasma Gel Kern Chef Doppelmembran DNA 46 Nucleolus Ribosomen Mitochondrien Kraftwerk 1000 Doppelmembran eigene DNA ATP Zucker+O2->CO2+H2O+36 ATP Ribosomen Arbeiter Protein ER Straße rau Protein glatt Lipide Golgi Post Vesikel Lysosom Müll pH5",
    "Pflanze Fotosynthese": "Pflanze Zellwand Beton Zellulose Holz Lignin Turgor Chloroplast Solar Fotosynthese Doppelmembran eigene DNA Chlorophyll grün absorbiert rot blau reflektiert grün Thylakoid Grana Vakuole Wassersack 90% Turgor Fotosynthese 6CO2+6H2O+Licht->Zucker+O2 Chloroplast Thylakoid Licht 2H2O->O2+4H++4e- O2 aus Wasser Elektron NADPH Calvin CO2+RuBP->Zucker ATP NADPH Nur 1-2% weil 45% PAR Photorespiration Atmung 50%",
    "Genetik Evolution": "DNA Doppelhelix Watson Crick 1953 A-T 2 C-G 3 Gen Abschnitt Chromosom 46 23 Paar Mitose 1->2 identisch Wachstum Meiose 1->4 halb 23 Crossing Over Mendel Erbsen 1865 dominant rezessiv 3:1 Mutation Strahlung Erbkrankheit Mukoviszidose Evolution Darwin 1859 Selektion Survival fittest Fossilien Archaeopteryx Homologie Wal Flosse Fledermaus Mensch Hand DNA Mensch Schimpanse 98% Affe 6Mio getrennt",
    "Mensch Körper": "Herz 4 Kammern 2 Vorhöfe 2 Kammern Rechts Lunge Links Körper 70 Schläge Blut 5L AB0 A B AB 0 Rhesus Gehirn 1,4kg Groß Denken Klein Bewegung Hirnstamm Atmung Lunge 300Mio Alveolen 70m² Niere filtert 180L Tag 1,5L Urin Immun angeboren weiß Fresser erworben Antikörper Gedächtnis Impfung"
},
"Physik": {
    "Mechanik Newton": "Newton1 ohne Kraft bleibt Ruhe gleichförmig Newton2 F=m*a 1N=1kg*1m/s² 2kg*3=6N Gewicht m*g g=9,81 70kg=686N a=F/m Newton3 Actio=Reactio Wand drückt dich Rakete Gas unten Rakete oben v=s/t 100km/h=27,8m/s a=v/t Freier Fall s=0,5*g*t² 2s 19,6m v=g*t",
    "Energie Leistung": "Energie bleibt erhalten umgewandelt nie vernichtet Kinetisch 0,5*m*v² Auto 1000kg 20m/s 200000J Potentiell m*g*h 70kg 10m 6867J Wärme Licht elektrisch chemisch Leistung P=E/t Watt kW kWh 3,6Mio J 100W 10h 1kWh",
    "Strom": "Elektronen fließen U Volt Druck I Ampere Menge R Ohm Hindernis R=U/I 12V 3Ω I=4A Reihe Rges=R1+R2 2+3=5Ω Parallel 1/R=1/R1+1/R2 2//2=1Ω P=U*I 230V 10A 2300W kWh Gefahren 50mA gefährlich",
    "Optik Kern": "Reflexion Einfall=Ausfall Brechung Wasser Stab knick Linse sammelt Brennpunkt f=1/D Auge kurz weitsichtig Farben weiß 400-700nm Prisma Regenbogen Laser gebündelt E=mc² Uran Spaltung Kettenreaktion"
},
"Chemie": {
    "Atombau PSE": "Kern Proton+ positiv 1u Neutron neutral 1u Hülle Elektron negativ 1/1836 Ordnungszahl=Protonen PSE nach Protonen Gruppen gleiche Valenz Gruppe1 Alkali 1 will weg +1 Gruppe17 Halogen 7 will 1 -1 Gruppe18 Edelgase 8 voll stabil Periode Schalen Isotope gleiche Prot andere Neut C12 6/6 C14 6/8 radioaktiv 5730 Jahre Halbwertszeit",
    "Bindungen": "Oktett 8 wollen voll Edelgase Ionen Metall gibt Nichtmetall nimmt Metall+Nichtmetall Na+ Cl- NaCl Salz Gitter hoch Schmelz 800°C spröde leitet flüssig nicht fest Kovalent teilen Nichtmetall+Nichtmetall H2O Molekül niedrig Schmelz Metall Elektronengas frei leitet glänzt verformbar",
    "Säuren Basen": "Brönsted Säure gibt H+ ab Base nimmt H+ Starke voll dissoziiert HCl->H++Cl- schwache teilweise pH=-log[H+] 0-6 sauer 7 neutral 8-14 basisch pH1 Magen pH7 Wasser pH14 Natronlauge Lackmus rot sauer blau basisch Phenolphthalein farblos sauer pink basisch HCl H2SO4 HNO3 stark NaOH stark Neutralisation Säure+Base->Salz+Wasser HCl+NaOH->NaCl+H2O H++OH-->H2O",
    "Redox": "Oxidation e- abgeben Zahl steigt Reduktion e- aufnehmen sinkt OIL RIG Rost Fe->Fe3++3e- Oxidation O2+4e-->2O2- Reduktion 4Fe+3O2->2Fe2O3 Verbrennung C+O2->CO2 C 0->+4 Oxidation O 0->-2 Reduktion Oxidationsmittel nimmt e- auf wird reduziert Reduktionsmittel gibt e- ab wird oxidiert"
}
}

if thema:
    st.write("---")
    st.markdown(f"### Fakten für '{thema}':")
    for erg in multi_suche(thema):
        st.info(f"**{erg['titel']}** {erg['text'][:500]}")
    s = thema.lower()
    for fach, unter in alle_faecher.items():
        for u_name, u_text in unter.items():
            if s in u_name.lower() or s in u_text.lower():
                st.write(f"**{fach} - {u_name}:** {u_text[:300]}...")

st.write("---")
st.markdown("### 📖 Alle 12 Fächer - Alle mit Suche:")

cols = st.columns(3)
fach_liste = list(alle_faecher.keys())

for i, fach_name in enumerate(fach_liste):
    if cols[i % 3].button(fach_name, key=f"btn_{fach_name}"):
        st.session_state['fach'] = fach_name
        if 'unter' in st.session_state:
            del st.session_state['unter']

if 'fach' in st.session_state:
    st.write("---")
    fach = st.session_state['fach']
    st.markdown(f"## 📚 {fach}")

    st.markdown('<div class="sub-box">', unsafe_allow_html=True)
    st.markdown(f"**In {fach} suchen:**")
    sub_suche = st.text_input(f"Suche in {fach}", placeholder="", key="sub_suche", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    unter_dict = alle_faecher[fach]

    if sub_suche:
        ss = sub_suche.lower()
        gefunden = False
        for u_name, u_text in unter_dict.items():
            if ss in u_name.lower() or ss in u_text.lower() or ss in u_text.lower().replace("ß","ss"):
                st.markdown(f"### {u_name}")
                st.write(u_text)
                # Internet extra
                for erg in multi_suche(f"{fach} {sub_suche}"):
                    st.caption(f"🌐 {erg['titel']}: {erg['text'][:300]}...")
                st.write("---")
                gefunden = True
        if not gefunden:
            st.warning(f"Nichts in {fach} für '{sub_suche}' gefunden - versuche anderen Begriff")
            for erg in multi_suche(sub_suche):
                st.info(f"Internet: {erg['text']}")
    else:
        st.write(f"**Alle Themen in {fach}:**")
        u_cols = st.columns(2)
        for j, (u_name, u_text) in enumerate(unter_dict.items()):
            if u_cols[j % 2].button(u_name, key=f"u_{fach}_{u_name}"):
                st.session_state['unter'] = u_name

        if 'unter' in st.session_state and st.session_state['unter'] in unter_dict:
            st.write("---")
            st.markdown(f"### {st.session_state['unter']}")
            st.write(unter_dict[st.session_state['unter']])
            # Internet Fakten dazu
            with st.spinner("Hole Internet Fakten..."):
                for erg in multi_suche(f"{st.session_state['unter']} {fach}"):
                    st.info(f"**🌐 {erg['quelle']}:** {erg['text']}")

    if st.button("❌ Schließen"):
        del st.session_state['fach']
        if 'unter' in st.session_state:
            del st.session_state['unter']
        st.rerun()

st.caption("Alle 12 Fächer mit Unterbegriffen + Suche + leere Suchleiste + Chemie da")
