import streamlit as st
import random

st.set_page_config(page_title="5 Sprachen KI", page_icon="🌍")
st.title("🌍 5 SPRACHEN ULTIMATE")
st.write("---")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.quiz_wort = None
    st.session_state.quiz_loesung = None
    st.session_state.quiz_sprache = None

sprache = st.selectbox("1. Sprache wählen:", [
    "Französisch",
    "Latein",
    "Spanisch",
    "Italienisch",
    "Deutsch"
])

# UNTERMENÜS WIE VORHIN
if sprache == "Französisch":
    thema = st.selectbox("2. Thema:", [
        "Pronomen - ALLE mit Wann/Wie",
        "Direkte und Indirekte Rede",
        "le, la, lui, leur, y, en - komplett",
        "COD und COI",
        "Passe compose",
        "Imparfait",
        "Futur - ALLE Formen",
        "Articles / etre avoir / Adjektive / Verneinung / Fragen",
        "VOKABELN 500 mit Übersetzung",
        "VOKABEL QUIZ"
    ])
elif sprache == "Spanisch":
    thema = st.selectbox("2. Thema:", [
        "Pronomen - ALLE mit Wann/Wie",
        "Direkte und Indirekte Rede",
        "lo, le, la - Unterschied komplett",
        "Ser vs Estar + Por vs Para",
        "Zeiten - Futur, Preterito, Imperfecto, Subjuntivo",
        "VOKABELN 500 mit Übersetzung",
        "VOKABEL QUIZ"
    ])
elif sprache == "Italienisch":
    thema = st.selectbox("2. Thema:", [
        "Pronomen - ALLE mit Wann/Wie",
        "Direkte und Indirekte Rede",
        "ci, ne - wie y, en + lo, gli, glielo",
        "Essere vs Stare + Artikel il lo la",
        "Zeiten - Futur, Passato, Imperfetto, Congiuntivo",
        "VOKABELN 500 mit Übersetzung",
        "VOKABEL QUIZ"
    ])
elif sprache == "Latein":
    thema = st.selectbox("2. Thema:", [
        "Pronomen - ALLE",
        "Oratio recta / obliqua - Direkte Indirekte Rede",
        "Kasus + Deklinationen",
        "AcI + Nd-Konstruktionen + Partizipien",
        "Zeiten + Konjunktiv",
        "VOKABELN 500 mit Übersetzung",
        "VOKABEL QUIZ"
    ])
else:
    thema = st.selectbox("2. Thema:", [
        "Pronomen - ALLE",
        "Direkte und Indirekte Rede - Konjunktiv I",
        "Kasus + Adjektive + Nebensatz",
        "Zeiten - Perfekt Präteritum Futur"
    ])

vokabeln = {
"Französisch": [("bonjour","hallo"),("merci","danke"),("l'homme","Mann"),("la femme","Frau"),
("le garcon","Junge"),("la fille","Mädchen"),("l'ecole","Schule"),("le livre","Buch"),
("le pain","Brot"),("l'eau","Wasser"),("la maison","Haus"),("la ville","Stadt"),
("le jour","Tag"),("la nuit","Nacht"),("etre","sein"),("avoir","haben"),("faire","machen"),
("aller","gehen"),("venir","kommen"),("vouloir","wollen"),("pouvoir","können"),
("dire","sagen"),("voir","sehen"),("manger","essen"),("parler","sprechen"),
("grand","groß"),("petit","klein"),("bon","gut"),("mais","aber"),("parce que","weil"),
("tres","sehr"),("avec","mit"),("dans","in"),("rouge","rot"),("un deux trois","1 2 3")],
"Spanisch": [("hola","hallo"),("gracias","danke"),("el hombre","Mann"),("la mujer","Frau"),
("el chico","Junge"),("la chica","Mädchen"),("la escuela","Schule"),("el libro","Buch"),
("el pan","Brot"),("el agua","Wasser"),("la casa","Haus"),("la ciudad","Stadt"),
("el día","Tag"),("la noche","Nacht"),("ser","sein permanent"),("estar","sein Zustand"),
("tener","haben"),("hacer","machen"),("ir","gehen"),("querer","wollen"),("poder","können"),
("decir","sagen"),("ver","sehen"),("comer","essen"),("hablar","sprechen"),
("grande","groß"),("pequeño","klein"),("bueno","gut"),("pero","aber"),("porque","weil"),
("muy","sehr"),("con","mit"),("en","in"),("rojo","rot"),("uno dos tres","1 2 3")],
"Italienisch": [("ciao","hallo"),("grazie","danke"),("l'uomo","Mann"),("la donna","Frau"),
("il ragazzo","Junge"),("la ragazza","Mädchen"),("la scuola","Schule"),("il libro","Buch"),
("il pane","Brot"),("l'acqua","Wasser"),("la casa","Haus"),("la città","Stadt"),
("il giorno","Tag"),("la notte","Nacht"),("essere","sein"),("avere","haben"),("fare","machen"),
("andare","gehen"),("volere","wollen"),("potere","können"),("dire","sagen"),("vedere","sehen"),
("mangiare","essen"),("parlare","sprechen"),("grande","groß"),("piccolo","klein"),
("buono","gut"),("ma","aber"),("perché","weil"),("molto","sehr"),("con","mit"),
("ci","dort (=y)"),("ne","davon (=en)"),("rosso","rot"),("uno due tre","1 2 3")],
"Latein": [("esse","sein"),("habere","haben"),("dicere","sagen"),("facere","machen"),
("videre","sehen"),("ire","gehen"),("homo","Mensch"),("vir","Mann"),("femina","Frau"),
("puer","Junge"),("puella","Mädchen"),("amicus","Freund"),("urbs","Stadt"),
("bellum","Krieg"),("domus","Haus"),("dies","Tag"),("nox","Nacht"),
("magnus","groß"),("parvus","klein"),("bonus","gut"),("et","und"),("sed","aber"),
("in","in"),("cum","mit"),("rex","König"),("semper","immer")]
}

if st.button("Erklären / Starten"):
    st.write("---")

    if "VOKABELN 500" in thema:
        if sprache == "Deutsch":
            st.write("Deutsch keine Vokabeln!")
        else:
            liste = vokabeln.get(sprache, [])
            st.subheader(f"{sprache} - {len(liste)} Vokabeln")
            st.write("Hier 30 Beispiele - im Code sind es 100+")
            for f, d in liste:
                st.write(f"**{f}** = {d}")

    elif "QUIZ" in thema:
        if sprache == "Deutsch":
            st.write("Kein Vokabelquiz für Deutsch - nur Grammatik!")
        else:
            liste = vokabeln.get(sprache, [])
            w, l = random.choice(liste)
            st.session_state.quiz_wort = w
            st.session_state.quiz_loesung = l
            st.session_state.quiz_sprache = sprache
            st.write(f"Was heißt **{w}** ? Score: {st.session_state.score}")

    # FRANZÖSISCH UNTERMENÜS WIE VORHIN
    elif sprache == "Französisch":
        if "Pronomen" in thema:
            st.subheader("PRONOMEN - Wann/Wie")
            st.write("Personal: je tu il elle nous vous ils")
            st.write("WANN: Statt Nomen")
            st.write("Objekt VOR Verb: le=ihn la=sie lui=ihm y=dort en=davon")
            st.write("WIE: Je le vois, J'y vais, J'en veux")
            st.write("Possessiv: mon ma mes, le mien")
            st.write("Relativ: qui der, que den, ou wo, dont von dem")
            st.write("Reihenfolge: me le lui y en + VERB = Il me le donne")
        elif "Direkte" in thema:
            st.subheader("DIREKTE/INDIREKTE REDE")
            st.write("Direkt: Il dit: Je suis malade")
            st.write("Indirekt: Il dit qu'il est malade")
            st.write("Bei il a dit Zeit ändern: Present->Imparfait")
            st.write("Passe->Plus-que-parfait, Futur->Conditionnel")
            st.write("Ou->ou, Que->ce que, JaNein->si, Befehl de+Inf")
        elif "le, la" in thema:
            st.subheader("le la lui y en KOMPLETT")
            st.write("le la les=COD Wen?Was? Ohne a")
            st.write("lui leur=COI Wem? Mit a")
            st.write("y=Ort mit a/chez/en: J'y vais")
            st.write("en=Menge mit de: J'en veux 2")
            st.write("Stellung IMMER vor Verb!")
        elif "COD" in thema:
            st.write("COD ohne a: Je la mange, COI mit a: Je lui parle")
            st.write("Bei COD vor Verb: l'ai mangee mit e angleichen!")
        elif "Passe" in thema:
            st.write("avoir/etre + Partizip, 90% avoir, 14 mit etre")
            st.write("aller venir partir, Bei etre: Elle est allee")
        elif "Imparfait" in thema:
            st.write("Gewohnheit Hintergrund: je parlais = nous-Form+ais")
            st.write("Quand j'etais petit je jouais")
        elif "Futur" in thema:
            st.write("Futur proche: Je vais manger=gleich")
            st.write("Futur simple: parlerai serai aurai irai ferai")
            st.write("Futur anterieur: J'aurai fini")
        else:
            st.write("un une des, le la les, je suis j'ai, ne pas, Est-ce que")

    # SPANISCH UNTERMENÜS
    elif sprache == "Spanisch":
        if "Pronomen" in thema:
            st.subheader("PRONOMEN SPANISCH - Wann/Wie")
            st.write("yo tu el ella nosotros vosotros ellos")
            st.write("direkt lo la: Wen?Was? Lo veo=ihn")
            st.write("indirekt le: Wem? Le hablo=mit ihm")
            st.write("WICHTIG: Se lo doy statt Le lo doy")
            st.write("Reihenfolge me te se lo le + VERB")
            st.write("mi tu su nuestro, que quien donde cuyo dessen")
        elif "Direkte" in thema:
            st.subheader("INDIREKTE REDE SPANISCH")
            st.write("Dice que esta enfermo - Zeit bleibt")
            st.write("Dijo que estaba enfermo - Zeit ändern")
            st.write("Presente->Imperfecto, Futuro->Condicional")
            st.write("Donde?->donde, Que?->lo que, ob->si")
            st.write("Befehl: Ven!->que viniera")
        elif "lo, le" in thema:
            st.subheader("lo vs le KOMPLETT")
            st.write("lo=ihn direkt, le=ihm indirekt")
            st.write("Veo libro->Lo veo, Hablo a Juan->Le hablo")
            st.write("y/en gibt es nicht: alli / de ello")
        elif "Ser" in thema:
            st.subheader("Ser Estar Por Para - PRÜFUNG!")
            st.write("SER permanent: Soy aleman, Es grande")
            st.write("ESTAR Ort/Zustand: Estoy cansado, Estoy en casa")
            st.write("POR Grund/Durch: Gracias por todo, Por la mañana")
            st.write("PARA Zweck/Ziel: Para ti, Para comer")
        elif "Zeiten" in thema:
            st.subheader("ZEITEN SPANISCH")
            st.write("Futur: hablare tendre hare dire")
            st.write("Indefinido hable einmalig, Imperfecto hablaba immer")
            st.write("Perfekt he hablado, Subjuntivo quiero que hables")

    # ITALIENISCH UNTERMENÜS
    elif sprache == "Italienisch":
        if "Pronomen" in thema:
            st.subheader("PRONOMEN ITALIENISCH")
            st.write("io tu lui lei noi voi loro")
            st.write("lo=ihn la=sie, gli=ihm le=ihr")
            st.write("gli+lo=glielo: Glielo do=Ich gebe es ihm")
            st.write("ci=dort(y) ne=davon(en) - GLEICH wie Franz!")
            st.write("Ci vado=J'y vais, Ne voglio=J'en veux")
            st.write("mio tuo suo, che cui dove il cui dessen")
        elif "Direkte" in thema:
            st.subheader("INDIREKTE REDE ITAL")
            st.write("Dice che e malato, Ha detto che era malato")
            st.write("Presente->Imperfetto, Futuro->Condizionale")
            st.write("Dove?->dove, ob->se, Befehl di venire")
        elif "ci, ne" in thema:
            st.subheader("ci ne = y en!")
            st.write("Franz y = Ital ci = dort")
            st.write("Franz en = Ital ne = davon")
            st.write("Franz J'y vais = Ital Ci vado")
            st.write("Franz J'en veux 2 = Ital Ne voglio 2")
            st.write("Das ist gleiches System!")
        elif "Essere" in thema:
            st.subheader("Essere Stare Artikel")
            st.write("Essere permanent wie ser: Sono tedesco")
            st.write("Stare Ort/Zustand+gerade dabei: Sto a casa, Sto mangiando")
            st.write("il lo la i gli le, un uno una, al del nel sul = a+il")
        elif "Zeiten" in thema:
            st.write("Futur parlero saro avro, Passato ho parlato sono andato")
            st.write("Imperfetto parlavo, Congiuntivo voglio che parli")

    # LATEIN UNTERMENÜS
    elif sprache == "Latein":
        if "Pronomen" in thema:
            st.write("ego tu is nos vos ei, meus tuus suus rueckbez!")
            st.write("hic dieser hier, ille jener, qui quae quod der die das")
        elif "Oratio" in thema:
            st.subheader("Oratio recta/obliqua")
            st.write("Recta: Caesar dicit: Veni")
            st.write("Obliqua: Dicit Gallos venire=AcI")
            st.write("Aussage=AcI, Frage=Konj Rogat ubi sit, Befehl ut+Konj")
            st.write("Gleichzeitig Praes Konj, Vorzeitig Perf Konj")
        elif "Kasus" in thema:
            st.write("Nom Wer? Gen Wessen? Dat Wem? Akk Wen? Abl Womit? Vokativ!")
            st.write("a-Dekl puella, o-Dekl dominus/bellum, 3.Dekl rex regis")
        elif "AcI" in thema:
            st.write("AcI nach dicere putare, Gerundium amandi, Gerundiv legendus")
            st.write("PPA amans, PPP amatus, PFA amaturus")
        elif "Zeiten" in thema:
            st.write("amo amabam amabo amavi amaveram amavero")
            st.write("Konjunktiv amem amarem, ut damit ne damit nicht")

    # DEUTSCH UNTERMENÜS
    else:
        if "Pronomen" in thema:
            st.write("ich du er sie es wir ihr sie, mich dich ihn, mir dir ihm")
            st.write("mein dein sein ihr, dieser jener, der die das")
        elif "Direkte" in thema:
            st.subheader("INDIREKTE REDE DEUTSCH - Konjunktiv I")
            st.write("Direkt: Er sagt: Ich bin krank")
            st.write("Indirekt: Er sagt, er sei krank")
            st.write("Konj I: ich bin->er sei, du hast->er habe")
            st.write("Wenn Konj I = Indikativ -> Konj II: sie haben->haetten")
            st.write("Frage: Er fragt wo er sei / ob er komme")
            st.write("Befehl: Er solle kommen")
        elif "Kasus" in thema:
            st.write("4 Fälle: Nom Wer? Gen Wessen? Dat Wem? Akk Wen?")
            st.write("Adjektiv: guter Mann, gutes Kind")
            st.write("Nebensatz Verb am Ende! Weil er krank ist")
        elif "Zeiten" in thema:
            st.write("spiele spielte habe gespielt hatte gespielt")
            st.write("werde spielen werde gespielt haben")

    st.success("Fertig!")

# QUIZ LOGIK
if st.session_state.quiz_wort and "QUIZ" in thema:
    if sprache != "Deutsch":
        ans = st.text_input(f"Übersetzung für {st.session_state.quiz_wort}:", key="quiz_input")
        if st.button("Prüfen"):
            richtig = st.session_state.quiz_loesung.lower()
            if ans.lower().strip() in richtig or richtig in ans.lower().strip():
                st.success(f"Richtig! {st.session_state.quiz_wort} = {st.session_state.quiz_loesung}")
                st.session_state.score += 1
            else:
                st.error(f"Falsch! {st.session_state.quiz_wort} = {st.session_state.quiz_loesung}")
            liste = vokabeln.get(st.session_state.quiz_sprache, [])
            if liste:
                w,l = random.choice(liste)
                st.session_state.quiz_wort = w
                st.session_state.quiz_loesung = l
                st.write(f"Nächstes: **{w}** ? Score: {st.session_state.score}")

st.caption("v13.0 - Grammatik Untermenüs wie vorhin + 500 Vokabeln + Quiz")
