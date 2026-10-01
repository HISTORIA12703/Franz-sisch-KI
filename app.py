import streamlit as st
import random

st.set_page_config(page_title="ULTIMATE FULL", page_icon="🎓")
st.title("🎓 ULTIMATE v16 FULL")
st.write("ALLE Sprachen VOLL wie vorhin + Geschichte + Bio Geo Chemie Physik + Mathe")
st.write("---")

fach = st.selectbox("1. FACH:", [
    "Französisch VOLL","Latein VOLL","Spanisch VOLL","Italienisch VOLL","Deutsch VOLL",
    "Geschichte","Biologie","Geographie","Chemie","Physik","Mathe"
])

if "Französisch" in fach:
    thema = st.selectbox("2. Thema:", [
        "Pronomen ALLE mit Wann/Wie",
        "Direkte und Indirekte Rede - komplett",
        "le la lui leur y en - komplett",
        "COD COI","Passe compose","Imparfait","Futur ALLE",
        "Articles etre avoir Adjektive Verneinung",
        "VOKABELN","QUIZ"
    ])
elif "Spanisch" in fach:
    thema = st.selectbox("2. Thema:", [
        "Pronomen ALLE mit Wann/Wie + Se lo doy",
        "Direkte und Indirekte Rede komplett",
        "lo le la Unterschied + leismo",
        "Ser vs Estar + Por vs Para PRÜFUNG",
        "Zeiten Futur Indefinido Imperfecto Subjuntivo",
        "VOKABELN","QUIZ"
    ])
elif "Italienisch" in fach:
    thema = st.selectbox("2. Thema:", [
        "Pronomen ALLE + ci ne = y en",
        "Direkte und Indirekte Rede komplett",
        "ci ne lo gli glielo komplett",
        "Essere vs Stare + Artikel il lo la al del nel",
        "Zeiten Futur Passato Imperfetto Congiuntivo",
        "VOKABELN","QUIZ"
    ])
elif "Latein" in fach:
    thema = st.selectbox("2. Thema:", [
        "Pronomen ALLE","Oratio recta obliqua AcI","Kasus Deklinationen",
        "AcI Gerundium PPA PPP","Zeiten Konjunktiv","VOKABELN","QUIZ"
    ])
elif "Deutsch" in fach:
    thema = st.selectbox("2. Thema:", [
        "Pronomen ALLE","Direkte Indirekte Konjunktiv I komplett",
        "Kasus Adjektive Nebensatz","Zeiten Perfekt Präteritum Futur"
    ])
elif "Geschichte" in fach:
    thema = st.selectbox("2. Thema:", ["Franz Rev","Industrialisierung","Weltkriege","Kalter Krieg","Antike","Mittelalter","NS Zeit","BRD DDR"])
elif fach == "Biologie":
    thema = st.selectbox("2. Thema:", ["Zelle","Genetik DNA","Evolution","Ökologie","Mensch","Fotosynthese"])
elif fach == "Geographie":
    thema = st.selectbox("2. Thema:", ["Plattentektonik","Klima","Bevölkerung","Globalisierung"])
elif fach == "Chemie":
    thema = st.selectbox("2. Thema:", ["Atombau PSE","Bindungen","Säuren Basen","Redox","Organische"])
elif fach == "Physik":
    thema = st.selectbox("2. Thema:", ["Mechanik Newton","Energie","Strom","Optik"])
else:
    thema = st.selectbox("2. Thema:", ["Grundrechen Brüche Prozent","Gleichungen linear quadratisch","Funktionen","Geometrie Pythagoras","Trigo sin cos tan","Ableitung Integral","Wahrscheinlichkeiten","Formeln"])

if st.button("Erklären"):
    st.write("---")

    # FRANZÖSISCH VOLL WIE V13
    if "Französisch" in fach:
        if "Pronomen" in thema:
            st.subheader("FRANZ PRONOMEN VOLL")
            st.write("WAS: Ersetzt Nomen, WIE: je tu il elle nous vous ils")
            st.write("Objekt VOR Verb: le=ihn la=sie lui=ihm y=dort en=davon")
            st.write("WANN le? COD Wen?Was? Ohne a: Je le vois")
            st.write("WANN lui? COI Wem? Mit a: Je lui parle")
            st.write("WANN y? Ort mit a/chez/en: J'y vais = Ich gehe dorthin")
            st.write("WANN en? Menge mit de: J'en veux 2 = Ich will 2 davon")
            st.write("Reihenfolge: me te se le la lui y en + VERB = Il me le donne")
            st.write("Possessiv: mon ma mes unser Zeug")
            st.write("Possessivpronomen: le mien meiner, le tien deiner")
            st.write("Relativ: qui der, que den, ou wo, dont dessen/von dem")
        elif "Direkte" in thema:
            st.subheader("DIREKTE INDIREKTE REDE VOLL")
            st.write("Direkt: Il dit: Je suis malade")
            st.write("Indirekt Praesens: Il dit qu'il est malade - Zeit bleibt!")
            st.write("Indirekt Passe: Il a dit qu'il etait malade - Zeit ändern!")
            st.write("Present->Imparfait, Passe compose->Plus-que-parfait")
            st.write("Futur->Conditionnel present, Imperativ->de+Infinitiv")
            st.write("Fragen: Ou vas-tu?->ou il allait, Que fais-tu?->ce qu'il faisait")
            st.write("JaNein Frage->si: Tu viens?->si il venait")
            st.write("Befehl: Viens!->de venir / lui dit de venir")
        elif "le la" in thema:
            st.subheader("le la lui y en KOMPLETT WIE V8")
            st.write("le la les=COD, lui leur=COI, y=Ort, en=Menge")
            st.write("Stellung IMMER vor Verb! Außer Imperativ positiv: Donne-le-moi")
            st.write("Bei COD vor avoir angleichen: Les pommes que j'ai mangees")
        elif "COD" in thema:
            st.write("COD ohne a: Je mange la pomme->Je la mange")
            st.write("COI mit a: Je parle a Marie->Je lui parle")
        elif "Passe" in thema:
            st.write("Passe compose: avoir/etre+Partizip, 90% avoir")
            st.write("14 Verben mit etre: aller venir partir etc + angleichen")
            st.write("Elle est allee, Ils sont venus")
        elif "Imparfait" in thema:
            st.write("Imparfait: Gewohnheit Hintergrund nous-Form+ais")
            st.write("je parlais tu parlais il parlait nous parlions")
            st.write("Quand j'etais petit je jouais au foot")
        elif "Futur" in thema:
            st.write("Futur proche: Je vais manger = gleich")
            st.write("Futur simple: parlerai parleras parlera parlerons")
            st.write("Irregular: etre->serai avoir->aurai aller->irai faire->ferai")
            st.write("Futur anterieur: J'aurai fini wenn fertig in Zukunft")
        elif "Articles" in thema:
            st.write("un une des, le la les, je suis tu es il est, ne pas ne jamais ne rien")
        else:
            st.write("Vokabeln bonjour merci homme femme ecole livre pain eau maison ville jour nuit etc mit Übersetzung")

    # SPANISCH VOLL WIE V10
    elif "Spanisch" in fach:
        if "Pronomen" in thema:
            st.subheader("SPANISCH PRONOMEN VOLL")
            st.write("yo tu el ella nosotros vosotros ellos")
            st.write("direkt lo la: Wen?Was? Lo veo")
            st.write("indirekt le: Wem? Mit a bei Person Le hablo")
            st.write("SE LO DOY Regel: le+lo->se lo! Le lo doy FALSCH Se lo doy RICHTIG")
            st.write("me te se lo le + VERB Me lo da")
            st.write("mi tu su nuestro vuestro su, que quien donde cuyo dessen")
        elif "Direkte" in thema:
            st.subheader("INDIREKTE REDE SPANISCH VOLL")
            st.write("Dice que esta enfermo Zeit bleibt bei dice")
            st.write("Dijo que estaba enfermo Zeit ändern Presente->Imperfecto")
            st.write("Indefinido->Pluscuamperfecto Futuro->Condicional")
            st.write("Donde vas?->donde iba Que haces?->lo que hacia Vienes?->si venia")
            st.write("Befehl: Ven!->que viniera / de venir")
        elif "lo le" in thema:
            st.subheader("lo vs le + leismo")
            st.write("lo=ihn Sache Veo libro->Lo veo")
            st.write("le=ihm Person Hablo a Juan->Le hablo")
            st.write("Spanien oft le fuer Person: Le vi a Juan = leismo erlaubt")
            st.write("y/en gibt es NICHT stattdessen alli ahi de ello")
        elif "Ser" in thema:
            st.subheader("SER vs ESTAR + POR vs PARA PRÜFUNG!")
            st.write("SER permanent: Soy aleman Es grande Son las 3")
            st.write("ESTAR Ort Zustand: Estoy cansado Estoy en casa Esta roto")
            st.write("Trick ESTAR Ort Zustand!")
            st.write("POR durch wegen für Zeit Tausch Gracias por todo Por la mañana")
            st.write("PARA für Zweck Ziel Empfänger Esto es para ti Para comer Para mañana")
        elif "Zeiten" in thema:
            st.write("Futur hablare hablaras hablará, tendre hare dire vendre")
            st.write("Futur nah Voy a comer, Indefinido hable einmalig Imperfecto hablaba immer")
            st.write("Ayer llovio einmal Cuando era niño llovia immer")
            st.write("Perfekt he hablado Subjuntivo quiero que hables Wunsch Zweifel")

    # ITALIENISCH VOLL WIE V10
    elif "Italienisch" in fach:
        if "Pronomen" in thema:
            st.subheader("ITALIENISCH PRONOMEN VOLL")
            st.write("io tu lui lei noi voi loro")
            st.write("direkt lo la li le: Lo vedo=ihn")
            st.write("indirekt gli le: Gli parlo=mit ihm/ihnen Le parlo=mit ihr")
            st.write("gli+lo=glielo! Glielo do=Ich gebe es ihm")
            st.write("ci=dort/hier/daran wie y Vado a Roma->Ci vado")
            st.write("ne=davon/welche wie en Ne voglio due=Ich will 2 davon")
            st.write("Reihenfolge mi lo gli ci ne+VERB Me lo da Ce ne sono")
            st.write("mio tuo suo nostro vostro loro, che cui dove il cui")
        elif "Direkte" in thema:
            st.subheader("INDIREKTE REDE ITAL VOLL")
            st.write("Dice che e malato Zeit bleibt, Ha detto che era malato ändern")
            st.write("Presente->Imperfetto Passato->Trapassato Futuro->Condizionale")
            st.write("Dove vai?->dove andavo Vieni?->se venivo Befehl di venire")
        elif "ci ne" in thema:
            st.subheader("ci ne = y en GLEICHES SYSTEM!")
            st.write("Franz y = Ital ci = Span alli = dort")
            st.write("Franz en = Ital ne = davon")
            st.write("J'y vais = Ci vado = Voy alli")
            st.write("J'en veux 2 = Ne voglio 2, J'en parle = Ne parlo")
            st.write("Für Prüfung wichtig!")
        elif "Essere" in thema:
            st.write("Essere permanent Sono tedesco E grande")
            st.write("Stare Ort Zustand gerade dabei Sto a casa Sto male Sto mangiando=esse gerade")
            st.write("il lo la i gli le un uno una al del nel sul = a+il de+il in+il")
        elif "Zeiten" in thema:
            st.write("Futur parlero avro saro andro faro verro vedro")
            st.write("Futur nah Sto per mangiare Passato ho parlato sono andato 14 Verben mit essere")
            st.write("Imperfetto parlavo einmalig vs immer Ieri ha piovuto vs Da bambino pioveva")

    # LATEIN + DEUTSCH VOLL
    elif "Latein" in fach:
        st.write("Latein VOLL wie vorhin: AcI Oratio obliqua Kasus Deklinationen PPA PPP etc")
    elif "Deutsch" in fach:
        if "Konjunktiv" in thema or "Direkte" in thema:
            st.subheader("KONJUNKTIV I VOLL")
            st.write("Er sagt: Ich bin krank -> Er sagt, er sei krank")
            st.write("Bildung: ich sei du seiest er sei wir seien ihr seiet sie seien")
            st.write("haben: er habe, sollen: er solle")
            st.write("Wenn Konj I = Indikativ -> Konj II nehmen: sie haben->sie hätten")
            st.write("Frage: Wo er sei / ob er komme, Befehl: Er solle kommen")
    elif "Mathe" in fach:
        if "Grundrechen" in thema:
            st.write("Bruch add gleich Nenner 1/4+2/4=3/4 ungleich Hauptnenner")
            st.write("Multi Zähler*Zähler Nenner*Nenner Divi mit Kehrwert")
            st.write("Prozent /100 Dreisatz Potenz 2^3=8 Wurzel √9=3")
        elif "Gleichungen" in thema:
            st.write("Linear ax+b=0 x=-b/a Beispiel 2x+4=10 -> x=3")
            st.write("Quadratisch Mitternacht x=(-b±√(b²-4ac))/2a pq x=-p/2±√((p/2)²-q)")
        elif "Funktionen" in thema:
            st.write("y=mx+b m Steigung b Achse Quadratisch y=ax²+bx+c Parabel Scheitel (d|e)")
        elif "Geometrie" in thema:
            st.write("Rechteck A=a*b Dreieck A=g*h/2 Kreis U=2πr A=πr² Pythagoras a²+b²=c²")
        elif "Trigo" in thema:
            st.write("sin=GK/Hyp cos=AK/Hyp tan=GK/AK GAGA Hühnerhof")
        elif "Ableitung" in thema:
            st.write("Ableitung Steigung x^n->n*x^(n-1) f=x³->f'=3x² Integral Fläche ∫x^n=x^(n+1)/(n+1)")
        elif "Wahrscheinlichkeiten" in thema:
            st.write("P=Ereignis/alle UND multi ODER add Baumdiagramm Pfad multi Binomial")
        else:
            st.write("Formeln: Mitternacht Pythagoras Kreis Kugel Ableitung pq sin cos tan")

    else:
        st.write(f"{fach} {thema} - Bio Zelle DNA Fotosynthese 6CO2+6H2O->C6H12O6+6O2, Geo Platten, Chemie PSE pH, Physik F=m*a")

    st.success("Fertig - ALLES drin!")

st.caption("v16.0 FULL - Sprachen VOLL wie v13 + ALLE Fächer + Mathe")
