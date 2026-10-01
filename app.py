import streamlit as st

st.set_page_config(page_title="ALLE FÄCHER SUCHE", page_icon="🔍")
st.title("🔍 v22 FINAL - ALLE FÄCHER + SUCHE")
st.write("Sprachen VOLL + Geschichte Bio Geo Chemie Physik Mathe MIT SUCHE")
st.write("---")

db = {
    "Französisch": {
        "pronomen le la lui y en reihenfolge": "le=ihn la=sie COD Wen?Was? ohne a, lui=ihm COI Wem? mit a, y=dort Ort mit a J'y vais, en=davon Menge mit de J'en veux, Reihenfolge me le lui y en+VERB Il me le donne",
        "direkte indirekte rede": "Il dit qu'il est malade Zeit BLEIBT bei il dit, Il a dit qu'il était malade Zeit ÄNDERN Present->Imparfait Passe->Plus-que-parf Futur->Conditionnel que->ce que ob->si Befehl de+Inf",
        "passé imparfait futur": "Passe avoir/etre+Partizip 14 Verben mit etre aller venir Elle est allee, Imparfait Gewohnheit je parlais, Futur parlerai serai aurai irai ferai proche Je vais manger"
    },
    "Spanisch": {
        "pronomen se lo doy": "lo=ihn direkt Wen? le=ihm indirekt Wem? SE LO DOY! le+lo->se lo FALSCH Le lo doy RICHTIG Se lo doy",
        "ser estar por para": "SER permanent Soy aleman Es grande, ESTAR Ort Zustand Estoy cansado Estoy en casa, POR Grund Durch Tausch Gracias por todo Por la mañana, PARA Zweck Ziel Für dich Para ti Para comer POR=Warum PARA=Wofür"
    },
    "Italienisch": {
        "ci ne y en glielo": "Franz y=Ital ci=dort Ci vado=J'y vais, Franz en=Ital ne=davon Ne voglio=J'en veux, gli+lo=glielo Glielo do, Gleiches System!",
        "essere stare": "Essere permanent Sono tedesco, Stare Ort Zustand gerade Sto a casa Sto mangiando=esse gerade"
    },
    "Geschichte": {
        "französische revolution 1789": "14. Juli 1789 Bastille 3.Stand 97% zahlt Freiheit Gleichheit Brüderlichkeit Menschenrechte 26.8.1789 Ludwig XVI geköpft 1793 Napoleon 1799",
        "industrialisierung": "1760 England Dampfmaschine Watt Fabriken Städte Arbeiter arm Marx 1848",
        "erster weltkrieg 1914": "Sarajevo 28.6.1914 Attentat Schützengraben Verdun 11.11.18 Ende Versailles 1919",
        "zweiter weltkrieg 1939 holocaust": "1.9.39 Polen 1939-45 Holocaust 6 Mio Auschwitz Wannsee 20.1.42 Atombombe 8.5.45 Ende",
        "kalter krieg mauer berlin": "1947-90 USA vs UdSSR Blockade 48 Luftbrücke Mauer 13.8.61-9.11.89 Kuba Krise 62 Vietnam",
        "antike rom griechen": "Griechen Demokratie 508 Athen Sokrates Platon, Rom Republik 509 Caesar 44 Augustus Pax Romana 476 Fall",
        "mittelalter": "500-1500 Lehnswesen König Vasall Ritter Bauer Kirche Kreuzzüge 1096 Pest 1347 Hanse",
        "ns zeit": "30.1.33 Hitler Kanzler Nürnberger 35 Pogromnacht 9.11.38 KZ Dachau Wannsee 6 Mio Juden Weiße Rose Stauffenberg 20.7.44",
        "brd ddr wiedervereinigung": "BRD 23.5.49 Grundgesetz Adenauer Wirtschaftswunder Brandt Ostpolitik DDR 7.10.49 SED Stasi Mauer 61 Montagsdemos Leipzig 89 Mauerfall 9.11.89 3.10.90 Einheit Kohl"
    },
    "Biologie": {
        "zelle mitochondrien": "Prokaryot Bakterien ohne Kern, Eukaryot mit Kern Tier Membran Zytoplasma Kern Mitochondrien Kraftwerk ATP Energie Zucker+O2->CO2+H2O Pflanze extra Zellwand Chloroplast Vakuole",
        "fotosynthese zellatmung": "6 CO2+6 H2O+Licht->C6H12O6+6 O2 Chloroplast Chlorophyll grün macht Sauerstoff, Zellatmung umgekehrt macht Energie",
        "genetik dna mendel": "DNA Doppelhelix A-T C-G Gen Chromosom 46 Mitose Meiose Mendel dominant rezessiv 3:1 Mutation",
        "evolution darwin": "Darwin Selektion Survival fittest Fossilien Homologie Hand Wal Affe Mensch 6 Mio Jahre"
    },
    "Geographie": {
        "plattentektonik erdbeben vulkan": "Kruste Mantel Kern Platten 5cm/Jahr divergent Rücken konvergent Himalaya Subduktion Erdbeben Richter Hypozentrum Vulkan Hotspot Hawaii",
        "klima klimawandel": "Wetter täglich Klima 30 Jahre Zonen Polar Gemäßigt Subtropen Tropen Klimawandel 1,2 Grad CO2 280->420ppm",
        "bevölkerung migration": "8 Mrd 2026 Demografischer Übergang Push Pull Migration Urbanisierung Stadt"
    },
    "Chemie": {
        "atombau pse": "Atom Kern Proton+ Neutron Hülle Elektron Proton Ordnungszahl PSE Gruppen Valenzelektronen Gruppe1 1e will weg +1 Gruppe17 7e will 1 -1 Isotope C12 C14",
        "bindungen salz": "Ionen Metall gibt an Nichtmetall NaCl Salz kovalent teilen H2O Metall Elektronengas leitet Oktett 8",
        "säuren basen ph": "Säure gibt H+ ab Base nimmt auf pH 0-6 sauer 7 neutral 8-14 basisch HCl NaOH Neutralisation HCl+NaOH->NaCl+H2O",
        "redox rost": "Oxidation e- abgeben Reduktion aufnehmen OIL RIG Rost Fe->Fe3+"
    },
    "Physik": {
        "newton mechanik": "Newton1 ohne Kraft bleibt, Newton2 F=m*a Beispiel 2kg*3=6N, Newton3 Actio=Reactio v=s/t a=v/t g=9,81",
        "energie": "Energie bleibt nur umgewandelt Kinetisch 0,5*m*v² Potentiell m*g*h Leistung Watt",
        "strom ohm": "Spannung U Volt Strom I Ampere R=U/I Ohm Reihe R1+R2 Parallel 1/R=1/R1+1/R2 P=U*I",
        "optik licht": "Reflexion Einfall=Ausfall Brechung Linse Sammellinse Brennpunkt Auge"
    },
    "Mathe": {
        "brüche prozent": "Add gleich Nenner 1/4+2/4=3/4 ungleich Hauptnenner 1/2+1/3=5/6 Multi Zähler*Zähler Divi Kehrwert 1/2:1/4=2 Prozent /100 20% von 50=10",
        "gleichungen mitternacht pq": "Linear 2x+4=10 x=3 Waage Prinzip, Quadratisch ax²+bx+c=0 Mitternacht x=(-b±√(b²-4ac))/2a pq x=-p/2±√((p/2)²-q) D=b²-4ac",
        "geometrie pythagoras kreis": "Pythagoras a²+b²=c² nur rechtwinklig 3 4 5 Rechteck A=a*b Dreieck g*h/2 Kreis U=2πr A=πr² Kugel V=4/3πr³",
        "trigo sin cos tan": "sin=GK/Hyp cos=AK/Hyp tan=GK/AK GAGA sin²+cos²=1",
        "ableitung integral": "Ableitung Steigung x^n->n*x^(n-1) x³->3x² Extrem f'=0 f''>0 Min, Integral Fläche ∫x^n=x^(n+1)/(n+1)+C ∫a^b=F(b)-F(a)",
        "wahrscheinlichkeit": "P=Ereignis/alle UND multi ODER add Baum Pfad multi Binomial (n über k)*p^k*(1-p)^(n-k) E=n*p"
    }
}

# SUCHE
st.subheader("🔍 SUCHE - Gib Thema ein für ALLE Fächer:")
suche = st.text_input("z.B. Französische Revolution, Fotosynthese, y en, Se lo doy, Pythagoras, Mauer, Atombau, Zelle, Ableitung, Por Para, Ser Estar:", "")

if suche:
    s = suche.lower()
    treffer = 0
    for fach, themen in db.items():
        for thema, text in themen.items():
            if s in thema or s in text.lower() or any(w in thema for w in s.split() if len(w)>2):
                st.markdown(f"**{fach} - {thema.upper()}**")
                st.write(text)
                st.write("---")
                treffer += 1
    if treffer == 0:
        st.error(f"Nichts für '{suche}'")
        st.write("Versuch: Revolution, Weltkrieg, Mauer, Fotosynthese, Zelle, Atombau, y en, ci ne, Ser Estar, Por Para, Pythagoras, Ableitung")
else:
    st.write("**Oder Fach wählen:**")
    fach = st.selectbox("Fach:", list(db.keys()))
    if fach:
        st.subheader(f"📚 {fach}")
        such2 = st.text_input(f"In {fach} suchen:", key="2")
        for thema, text in db[fach].items():
            if not such2 or such2.lower() in thema or such2.lower() in text.lower():
                with st.expander(thema):
                    st.write(text)

st.caption("v22 FINAL - ALLE FÄCHER MIT SUCHE!")
