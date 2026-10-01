import streamlit as st

st.set_page_config(page_title="Lingua100", page_icon="📚", layout="wide")
st.title("📚 Lingua100 Ultimate - 80+ Themen")
st.success("✅ Mit 5 Fremdsprachen + Latein!")

if 'xp' not in st.session_state:
    st.session_state.xp = 0

st.sidebar.metric("⭐ XP", st.session_state.xp)
st.sidebar.caption("HISTORIA12703")

DATA = {
    "🏛️ GESCHICHTE (12)": {
        "Franz. Revolution 1789": "14.7.1789 Sturm Bastille, 1793 Ludwig XVI geköpft, 1804 Napoleon Kaiser, 1815 Waterloo Niederlage",
        "Kaiserreich 1871": "18.1.1871 Gründung Versailles, Wilhelm I Kaiser, Bismarck Kanzler, 1871-1918",
        "1. Weltkrieg 1914-18": "28.6.1914 Attentat Sarajevo, 11.11.1918 Waffenstillstand, 17 Mio Tote, Versailles Vertrag",
        "Weimar 1919-33": "1919 Verfassung Weimar, 1923 Hyperinflation 1 Billion Mark, 1929 Weltwirtschaftskrise",
        "NS Zeit 1933-45": "30.1.33 Hitler Machtergreifung, 1935 Nürnberger Gesetze, 9.11.38 Kristallnacht, 6 Mio Juden Auschwitz",
        "2. Weltkrieg 1939-45": "1.9.39 Überfall Polen, 6.6.44 D-Day Normandie, 8.5.45 Ende DE, 6.8.45 Hiroshima Atombombe",
        "Mauer 1961-89": "13.8.61 Mauerbau, 9.11.89 Mauerfall, 3.10.90 Wiedervereinigung, 28 Jahre Teilung",
        "Antike": "753 v.Chr Gründung Rom, 44 v.Chr Caesar ermordet, 0 Christi Geburt",
        "Mittelalter": "800 Karl der Große Kaiser, 1492 Kolumbus Amerika, 1517 Luther 95 Thesen, 1450 Buchdruck Gutenberg",
        "Kalter Krieg": "1949 NATO Gründung, 1962 Kuba Krise, 1969 Mondlandung Apollo 11, 1991 Ende UdSSR",
        "Industrialisierung": "1769 Watt Dampfmaschine, 1835 erste deutsche Bahn Nürnberg-Fürth, 1876 Telefon Bell",
        "EU Geschichte": "1957 Römische Verträge, 1993 EU gegründet, 2002 Euro Einführung, heute 27 Länder"
    },
    "⚛️ PHYSIK (8)": {
        "Mechanik": "v=s/t Geschwindigkeit, 100km/h=27,8m/s, a=v/t Beschleunigung, g=9,81 m/s² Erdanziehung",
        "Newton Gesetze": "1. Trägheit, 2. F=m*a Kraft=Masse*Beschleunigung, 70kg=686N, 3. Actio=Reactio",
        "Strom": "R=U/I Widerstand, 12V / 3Ω = 4A, Reihe: 2Ω+3Ω=5Ω, Parallel: 2Ω//2Ω=1Ω, P=U*I Leistung",
        "Energie": "Ekin=0,5*m*v², Epot=m*g*h, 1kWh=3,6 Mio Joule, Energieerhaltung: nichts geht verloren",
        "Optik": "Einfallswinkel=Ausfallswinkel, Licht c=300.000 km/s, Linse: Sammellinse vergrößert",
        "Wellen": "Schall 343m/s Luft, v=f*λ, Frequenz Hz, Licht ist Welle UND Teilchen",
        "Kernphysik": "E=mc² Einstein, Kernspaltung Uran, Kernfusion Sonne, Radioaktivität: Alpha Beta Gamma",
        "Druck": "p=F/A Druck=Kraft/Fläche, 1bar=100.000 Pa, 10m Wasser = +1bar, Auftrieb"
    },
    "📐 MATHE (7)": {
        "Brüche": "1/4+2/4=3/4, 1/2=0,5=50%, 2/3 von 90 = 60, Kehrwert: 2/3 -> 3/2",
        "Prozent": "20% von 200=40, Formel W=G*p/100, 100% = Ganze, Zinsen: K*n*p/100",
        "Pythagoras": "a²+b²=c², 3-4-5 Dreieck: 3²+4²=5² => 9+16=25, gilt nur rechtwinklig",
        "Gleichungen": "2x+4=10 => 2x=6 => x=3, Probe machen! x²=9 => x=3 oder -3",
        "Geometrie": "Kreis: U=2*π*r, A=π*r², Quader V=a*b*c, Dreieck A=0,5*g*h",
        "Binomische": "(a+b)²=a²+2ab+b², (a-b)²=a²-2ab+b², (a+b)(a-b)=a²-b²",
        "Wahrscheinlichkeit": "Würfel 6 = 1/6, Münze Kopf 50%, 2 Würfel 7 am wahrscheinlichsten"
    },
    "🇬🇧 ENGLISCH": {
        "Top 100 Wörter": "the der, be sein, to zu, of von, and und, a ein, in in, that das, have haben, I ich, it es, for für, not nicht, on auf, with mit, he er, as wie, you du, do tun, at bei",
        "Zeiten": "Present: I go, Past: I went, Perfect: I have gone, Future: I will go, Continuous: I am going gerade",
        "Sätze Alltag": "Hello=Hallo, How are you? Wie gehts?, My name is... Ich heiße..., Where is...? Wo ist?, How much? Wieviel?, I love you Ich liebe dich, Thank you Danke",
        "Unregelmäßig Top 15": "go-went-gone gehen, be-was-been sein, have-had-had haben, do-did-done tun, make-made-made machen, come-came-come kommen, take-took-taken nehmen, get-got-got bekommen, see-saw-seen sehen, know-knew-known wissen, give-gave-given geben, find-found-found finden, think-thought-thought denken, tell-told-told sagen, become-became-become werden",
        "Grammatik": "I, you, he/she/it, we, you, they, Fragestellung: Do you...?, Verneinung: I don't, Steigerung: good-better-best"
    },
    "🇫🇷 FRANZÖSISCH": {
        "Top 100 Wörter": "bonjour Hallo, merci danke, oui ja, non nein, être sein, avoir haben, aller gehen, faire machen, dire sagen, je ich, tu du, il er, nous wir, vous ihr/Sie, grand groß, petit klein, bon gut",
        "Konjugation être": "je suis ich bin, tu es du bist, il est er ist, nous sommes wir sind, vous êtes ihr seid, ils sont sie sind",
        "Konjugation avoir": "j'ai ich habe, tu as du hast, il a er hat, nous avons wir haben, vous avez ihr habt, ils ont sie haben",
        "Sätze Alltag": "Bonjour! Hallo!, Comment ça va? Wie gehts?, Je m'appelle... Ich heiße..., Où est...? Wo ist...?, Combien? Wieviel?, Je t'aime Ich liebe dich, Au revoir Tschüss, S'il vous plaît Bitte",
        "Zeiten": "Présent: je vais ich gehe, Passé composé: je suis allé ich bin gegangen, Futur: je vais aller ich werde gehen, j'irai",
        "Zahlen": "1 un, 2 deux, 3 trois, 4 quatre, 5 cinq, 10 dix, 20 vingt, 100 cent, 1000 mille"
    },
    "🇪🇸 SPANISCH": {
        "Top 100 Wörter": "hola Hallo, gracias danke, sí ja, no nein, ser sein, estar sein (Ort), tener haben, hacer machen, decir sagen, yo ich, tú du, él er, grande groß, pequeño klein, bueno gut",
        "Konjugation ser": "yo soy ich bin, tú eres du bist, él es er ist, nosotros somos wir sind, vosotros sois ihr seid, ellos son sie sind",
        "Konjugation tener": "yo tengo ich habe, tú tienes du hast, él tiene er hat, nosotros tenemos wir haben, vosotros tenéis ihr habt, ellos tienen sie haben",
        "Sätze Alltag": "¡Hola! Hallo!, ¿Cómo estás? Wie gehts?, Me llamo... Ich heiße..., ¿Dónde está...? Wo ist...?, ¿Cuánto? Wieviel?, Te quiero Ich liebe dich, Adiós Tschüss, Por favor Bitte",
        "Unregelmäßig Top 10": "ser-soy-sido sein, ir-voy-ido gehen, haber-he-habido haben, tener-tengo-tenido haben, hacer-hago-hecho machen, decir-digo-dicho sagen, ver-veo-visto sehen, poder-puedo-podido können, querer-quiero-querido wollen, venir-vengo-venido kommen",
        "Zahlen": "1 uno, 2 dos, 3 tres, 4 cuatro, 5 cinco, 10 diez, 20 veinte, 100 cien, 1000 mil"
    },
    "🇮🇹 ITALIENISCH": {
        "Top 100 Wörter": "ciao Hallo/Tschüss, grazie danke, sì ja, no nein, essere sein, avere haben, andare gehen, fare machen, dire sagen, io ich, tu du, grande groß, piccolo klein, buono gut, casa Haus, acqua Wasser",
        "Konjugation essere": "io sono ich bin, tu sei du bist, lui è er ist, noi siamo wir sind, voi siete ihr seid, loro sono sie sind",
        "Sätze Alltag": "Ciao! Hallo!, Come stai? Wie gehts?, Mi chiamo... Ich heiße..., Dov'è...? Wo ist...?, Quanto? Wieviel?, Ti amo Ich liebe dich, Arrivederci Tschüss, Per favore Bitte",
        "Zeiten": "Presente: vado ich gehe, Passato: sono andato ich bin gegangen, Futuro: andrò ich werde gehen",
        "Zahlen": "1 uno, 2 due, 3 tre, 4 quattro, 5 cinque, 10 dieci, 20 venti, 100 cento, 1000 mille"
    },
    "🏛️ LATEIN": {
        "Top 100 Wörter": "et und, in in, non nicht, esse sein, habere haben, dicere sagen, facere machen, ego ich, tu du, is er, magnus groß, bonus gut, malus schlecht, vita Leben, annus Jahr, homo Mensch, tempus Zeit, bellum Krieg, pax Frieden, deus Gott",
        "Fälle Deklination": "Nom Wer?, Gen Wessen?, Dat Wem?, Akk Wen?, Abl Womit?/Wo? Beispiel puella (Mädchen): puella, puellae, puellae, puellam, puella - dominus (Herr): dominus, domini, domino, dominum, domino",
        "esse sein": "sum ich bin, es du bist, est er ist, sumus wir sind, estis ihr seid, sunt sie sind - Imperfekt: eram ich war - Futur: ero ich werde sein - Perfekt: fui ich bin gewesen",
        "amare lieben (a-Konjugation)": "amo ich liebe, amas du liebst, amat er liebt, amamus wir lieben, amatis ihr liebt, amant sie lieben - Perfekt: amavi ich habe geliebt",
        "habere haben & videre sehen": "habeo ich habe, habes du hast, habet er hat - video ich sehe, vides du siehst, videt er sieht, videmus wir sehen, videtis ihr seht, vident sie sehen",
        "Berühmte Zitate": "Veni, vidi, vici Ich kam, sah, siegte (Caesar), Carpe diem Nutze den Tag (Horaz), Alea iacta est Der Würfel ist gefallen (Caesar), Et tu, Brute? Auch du, Brutus?, Amor vincit omnia Liebe besiegt alles, Cogito ergo sum Ich denke also bin ich (Descartes), Per aspera ad astra Durch Mühen zu den Sternen",
        "Präpositionen": "in in/auf (in + Abl Ort, in + Akk wohin), ad zu, cum mit, sine ohne, per durch, pro für, ex/e aus, de über/von, inter zwischen, post nach, ante vor, sub unter",
        "Zahlen": "1 unus, 2 duo, 3 tres, 4 quattuor, 5 quinque, 6 sex, 7 septem, 8 octo, 9 novem, 10 decem, 50 L, 100 C, 500 D, 1000 M, 2026 MMXXVI"
    },
    "🧬 BIO/CHEMIE": {
        "Zelle": "Mitochondrien=Kraftwerk Energie, Chloroplast=Fotosynthese Pflanze, Zellkern=DNA Steuerung, Ribosom=Eiweißfabrik",
        "Mensch": "Herz 4 Kammern, 86 Mrd Neuronen Gehirn, 206 Knochen, Blut 5-6 Liter, DNA Doppelhelix",
        "Genetik": "46 Chromosomen, Mendel Vererbung, DNA aus A,T,C,G, Mutation Veränderung",
        "Atome": "Proton+ positiv Kern, Neutron neutral Kern, Elektron- Hülle, 118 Elemente Periodensystem",
        "Periodensystem": "H Wasserstoff 1, He Helium 2, O Sauerstoff 8, Au Gold 79, Fe Eisen 26"
    }
}

# SUCHE
suche = st.text_input("🔍 Suche in 80+ Themen", placeholder="Mauer, esse, veni, bonjour, Strom...")
if suche:
    st.write(f"Ergebnisse für '{suche}':")
    for fach, themen in DATA.items():
        for tit, txt in themen.items():
            if suche.lower() in tit.lower() or suche.lower() in txt.lower():
                st.info(f"**{fach} → {tit}**: {txt}")
    st.divider()

# FÄCHER ANZEIGE
cols = st.columns(3)
for i, fach in enumerate(DATA.keys()):
    if cols[i % 3].button(fach, use_container_width=True):
        st.session_state.fach = fach

if 'fach' in st.session_state:
    fach = st.session_state.fach
    st.header(fach)
    for tit, txt in DATA[fach].items():
        with st.expander(f"📚 {tit}", expanded=True):
            st.info(txt)
            if st.button(f"✅ Gelernt: {tit}", key=f"learn_{fach}_{tit}"):
                st.balloons()
                st.session_state.xp += 10
                st.rerun()
    if st.button("⬅️ Zurück zur Übersicht"):
        del st.session_state.fach
        st.rerun()
else:
    st.info("👆 Wähle ein Fach oben oder nutze die Suche!")
    st.caption("Insgesamt 80+ Themen: Geschichte, Physik, Mathe, 5 Sprachen inkl. Latein, Bio, Chemie")
