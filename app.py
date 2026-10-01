import streamlit as st
import random

st.set_page_config(page_title="LERN APP FINAL", page_icon="🎓", layout="wide")
st.title("🎓 FINALE LERN-APP - Für Prüfungen!")
st.write("Alle Fächer SEHR ausführlich mit Beispielen + Merksätzen + Übungen")
st.write("---")

fach = st.selectbox("📚 FACH WÄHLEN:", [
    "Französisch - PRÜFUNG",
    "Spanisch - PRÜFUNG", 
    "Italienisch - PRÜFUNG",
    "Latein - PRÜFUNG",
    "Deutsch - PRÜFUNG",
    "Geschichte - LERNEN",
    "Biologie - LERNEN",
    "Geographie - LERNEN",
    "Chemie - LERNEN",
    "Physik - LERNEN",
    "Mathe - LERNEN"
])

if "Französisch" in fach or "Spanisch" in fach or "Italienisch" in fach:
    thema = st.selectbox("📖 THEMA:", [
        "1. Pronomen ALLE - mit Übungen",
        "2. Direkte/Indirekte Rede - komplett mit Zeitänderung",
        "3. Objektpronomen (y en / ci ne / lo le)",
        "4. Zeiten + Ser/Estar - ALLE Formen",
        "5. VOKABELN 500 + QUIZ"
    ])
else:
    thema = st.selectbox("📖 THEMA:", [
        "1. Grundlagen - ausführlich",
        "2. Mittel - ausführlich", 
        "3. Fortgeschritten - ausführlich",
        "4. Prüfungs-Spezial",
        "5. Formeln + Vokabeln"
    ])

if st.button("🚀 LERNEN STARTEN", type="primary"):
    st.write("---")

    # FRANZÖSISCH LERNBAR
    if "Französisch" in fach:
        if "Pronomen" in thema:
            st.subheader("🇫🇷 PRONOMEN - SO LERNST DU ES FÜR PRÜFUNG")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**🎯 MERKSATZ:**")
                st.info("COD = Wen? Was? OHNE a -> le la les\nCOI = Wem? MIT a -> lui leur\nY = Ort mit à -> dort\nEN = Menge mit de -> davon")
                st.write("**📝 BEISPIELE ZUM ÜBEN:**")
                st.write("1. Je vois Marie -> Je **la** vois (wen? Marie)")
                st.write("2. Je parle à Marie -> Je **lui** parle (wem? mit a!)")
                st.write("3. Je vais à Paris -> J'**y** vais (wohin? Ort mit à)")
                st.write("4. Je veux du pain -> J'**en** veux (wieviel? mit de)")
            with col2:
                st.write("**⚠️ REIHENFOLGE - MUSS!**")
                st.error("me te se nous vous + le la les + lui leur + y + en + VERB")
                st.write("Beispiel: Il **me le** donne = Er gibt es mir")
                st.write("Il **y en** a = Es gibt davon dort")
                st.write("**✍️ ÜBUNG FÜR DICH:**")
                st.write("Übersetze: Ich sehe ihn dort")
                st.write("Lösung: Je l'y vois? FALSCH! -> Je le vois là-bas")
                st.write("Ich spreche davon: J'en parle")

        elif "Direkte" in thema:
            st.subheader("🇫🇷 INDIREKTE REDE - SCHRITT FÜR SCHRITT")
            st.write("**SCHRITT 1: Erkenne Einleitung**")
            st.write("Présent: il dit = Zeit BLEIBT | Passé: il a dit = Zeit ÄNDERN")
            st.write("**SCHRITT 2: Zeit ändern Tabelle**")
            st.table({
                "Direkt": ["Je suis (Present)", "J'ai mangé (Passé)", "J'irai (Futur)", "Viens! (Imperativ)"],
                "Indirekt nach il a dit": ["qu'il était (Imparfait)", "qu'il avait mangé (Plus-que-parf)", "qu'il irait (Conditionnel)", "de venir"]
            })
            st.write("**SCHRITT 3: Fragewörter**")
            st.write("Où -> où, Que -> ce que, Est-ce que -> si, Befehl -> de+Inf")

    # SPANISCH LERNBAR
    elif "Spanisch" in fach:
        if "Pronomen" in thema:
            st.subheader("🇪🇸 SPANISCH - MIT LERNTRICKS")
            st.write("**🎯 DER SE LO TRICK - 90% machen Fehler!**")
            st.warning("Du willst: Ich gebe es ihm = Le + lo = SE LO! Nie le lo!")
            st.write("FALSCH: Le lo doy | RICHTIG: **Se lo doy**")
            st.write("**LERNTRICK:** Stell dir vor le + lo verschmelzen zu SE LO wie Power Ranger!")
            st.write("**ÜBUNGEN:**")
            st.write("Ich gebe es ihr -> Se lo doy (ihr = le wird zu se)")
            st.write("Ich sage es ihnen -> Se lo digo")

    # GESCHICHTE LERNBAR
    elif "Geschichte" in fach:
        st.subheader("🏛️ GESCHICHTE - SO MERKST DU ES DIR")
        st.write("**FRANZÖSISCHE REVOLUTION - 5 W's:**")
        st.write("**WER?** 3. Stand 97% zahlen alles, 1.+2. Stand 3% zahlen nix")
        st.write("**WAS?** Sturm Bastille 14.7.1789, König geköpft 1793")
        st.write("**WANN?** 1789-1799")
        st.write("**WARUM?** Hunger Brot teuer + König pleite + Aufklärung")
        st.write("**WIE?** Freiheit Gleichheit Brüderlichkeit -> Napoleon")
        st.write("**📝 PRÜFUNGSFRAGE:** Nenne 3 Ursachen")
        st.write("Lösung: 1. Ungleiche Gesellschaft 2. Staatspleite 3. Hunger 4. Aufklärung")
        st.write("---")
        st.write("**WELTKRIEGE MERKSATZ:**")
        st.info("1.WK: 1914-18 Schützengraben wegen Sarajevo -> Versailles hart\n2.WK: 1939-45 Hitler Polen -> Holocaust -> Atombombe -> 8.Mai 45 Ende")

    # BIOLOGIE LERNBAR
    elif "Biologie" in fach:
        st.subheader("🧬 BIOLOGIE - MIT BILD IM KOPF")
        st.write("**ZELLE - FABRIK VERGLEICH:**")
        st.write("Zellmembran = Fabrikzaun (kontrolliert rein raus)")
        st.write("Zellkern = Chef Büro (DNA Baupläne)")
        st.write("Mitochondrien = Kraftwerk (macht Energie ATP)")
        st.write("Ribosomen = Arbeiter (bauen Proteine)")
        st.write("Chloroplast = Solaranlage (nur Pflanze, macht Zucker aus Licht)")
        st.write("**FORMEL FOTOSYNTHESE MUSS!**")
        st.error("6 CO2 + 6 H2O + Licht -> C6H12O6 (Zucker) + 6 O2")
        st.write("WO? Im Chloroplast, WANN? Nur bei Licht, WARUM? Macht Sauerstoff für uns!")
        st.write("**GENETIK MERKSATZ:** A-T und C-G wie Apfel-Theke und Citronen-Gurke!")

    # MATHE LERNBAR
    elif "Mathe" in fach:
        if "Grundlagen" in thema or "1." in thema:
            st.subheader("🧮 MATHE GRUNDLAGEN - MIT RECHENWEG")
            st.write("**BRÜCHE ADDITION - SCHRITT FÜR SCHRITT:**")
            st.write("Aufgabe: 1/2 + 1/3")
            st.write("1. Hauptnenner: 2 und 3 -> 6")
            st.write("2. Erweitern: 1/2 = 3/6 (mal 3), 1/3 = 2/6 (mal 2)")
            st.write("3. Addieren: 3/6+2/6=5/6 Zähler addieren!")
            st.write("**ÜBUNG:** 2/3 + 1/4 = ?")
            st.write("Lösung: Hauptnenner 12 -> 8/12+3/12=11/12")
            st.write("---")
            st.write("**GLEICHUNGEN - WAAGE PRINZIP:**")
            st.write("2x+4=10 | Was weg? +4 stört -> -4 auf BEIDEN Seiten!")
            st.write("2x+4-4=10-4 -> 2x=6 | :2 -> x=3")
            st.write("MERKE: Was du links machst, musst du rechts auch machen! Wie Waage!")
        
        elif "Fortgeschritten" in thema or "4." in thema:
            st.subheader("🧮 ABLEITUNG - SO VERSTEHST DU ES")
            st.write("**WAS IST ABLEITUNG?** Steigung in einem Punkt!")
            st.write("Stell dir Berg vor: An manchen Stellen steil, an manchen flach. Ableitung sagt wie steil!")
            st.write("**REGEL:** x^n -> n*x^(n-1) Exponent nach vorne, dann -1")
            st.write("Beispiel: f=x³ -> f'=3x²")
            st.write("x² -> 2x, x -> 1, 5 -> 0 (Konstante flach!)")
            st.write("**WOZU?** Hochpunkt/Tiefpunkt finden wo Steigung 0!")
            st.write("f'=0 setzen, lösen -> x, dann f'' prüfen: >0 Tiefpunkt, <0 Hochpunkt")
            st.write("**ÜBUNG:** f=x²-4x, wo Tiefpunkt?")
            st.write("f'=2x-4=0 -> x=2, f''=2>0 -> Tiefpunkt bei (2|-4)")

    # PHYSIK CHEMIE GEO
    elif "Physik" in fach:
        st.subheader("⚡ PHYSIK LERNBAR")
        st.write("**NEWTON - 3 GESETZE MIT BEISPIEL:**")
        st.write("1. Ohne Kraft bleibt alles wie es ist (Ball rollt weiter im All)")
        st.write("2. F=m*a: Mehr Masse -> mehr Kraft nötig! 100kg schieben schwerer als 1kg")
        st.write("Beispiel: 2kg * 3m/s² = 6 Newton")
        st.write("3. Actio=Reactio: Du drückst Wand, Wand drückt dich!")
        st.write("**ENERGIE BLEIBT!** Nur umgewandelt: Höhe (m*g*h) -> Bewegung (0,5*m*v²)")

    elif "Chemie" in fach:
        st.subheader("🧪 CHEMIE LERNBAR")
        st.write("**PSE MERKSATZ:** Gruppen=Spalten=gleiche Valenzelektronen!")
        st.write("Gruppe 1: 1 Elektron will weg -> +1 (Na+), Gruppe 17: 7 Elektronen will 1 -> -1 (Cl-)")
        st.write("Deshalb Na+ + Cl- -> NaCl Salz! Oktettregel: Alle wollen 8!")
        st.write("**pH:** 0-6 sauer (Zitrone), 7 neutral (Wasser), 8-14 basisch (Seife)")
        st.write("Säure gibt H+ ab, Base nimmt H+ auf")

    st.success("✅ Fertig zum Lernen! Mach dir Notizen!")

st.caption("v18.0 FINAL LERNBAR - Mit Merksätzen Übungen Prüfungsfragen")
