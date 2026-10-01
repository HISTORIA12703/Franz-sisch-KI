import streamlit as st
import random

st.set_page_config(page_title="5 Sprachen KI", page_icon="🌍")
st.title("🌍 5 SPRACHEN KI + QUIZ")
st.write("---")

# SESSION STATE FÜR QUIZ
if "quiz_wort" not in st.session_state:
    st.session_state.quiz_wort = None
    st.session_state.quiz_loesung = None
    st.session_state.quiz_sprache = None
    st.session_state.score = 0

sprache = st.selectbox("1. Sprache:", [
    "Französisch",
    "Latein",
    "Spanisch",
    "Italienisch",
    "Deutsch"
])

thema = st.selectbox("2. Thema:", [
    "Pronomen",
    "Direkte und Indirekte Rede",
    "Grammatik Zeiten",
    "VOKABELN mit Übersetzung",
    "VOKABEL QUIZ"
])

# VOKABELN MIT ÜBERSETZUNG
vokabeln = {
    "Französisch": [
        ("bonjour", "hallo / guten Tag"),
        ("au revoir", "tschüss / auf Wiedersehen"),
        ("merci", "danke"),
        ("s'il vous plait", "bitte"),
        ("oui", "ja"), ("non", "nein"),
        ("l'homme", "der Mann"), ("la femme", "die Frau"),
        ("le garcon", "der Junge"), ("la fille", "das Mädchen"),
        ("l'ami", "der Freund"), ("la famille", "die Familie"),
        ("l'ecole", "die Schule"), ("le livre", "das Buch"),
        ("le professeur", "der Lehrer"), ("le pain", "das Brot"),
        ("l'eau", "das Wasser"), ("la maison", "das Haus"),
        ("le temps", "die Zeit / das Wetter"), ("le jour", "der Tag"),
        ("la nuit", "die Nacht"), ("la vie", "das Leben"),
        ("etre", "sein"), ("avoir", "haben"), ("faire", "machen"),
        ("aller", "gehen"), ("venir", "kommen"),
        ("vouloir", "wollen"), ("pouvoir", "können"),
        ("dire", "sagen"), ("voir", "sehen"), ("savoir", "wissen"),
        ("prendre", "nehmen"), ("donner", "geben"),
        ("manger", "essen"), ("boire", "trinken"),
        ("parler", "sprechen"), ("comprendre", "verstehen"),
        ("apprendre", "lernen"), ("aimer", "lieben / mögen"),
        ("grand", "groß"), ("petit", "klein"),
        ("bon", "gut"), ("mauvais", "schlecht"),
        ("beau", "schön"), ("nouveau", "neu"), ("vieux", "alt"),
        ("mais", "aber"), ("parce que", "weil"),
        ("tres", "sehr"), ("beaucoup", "viel"),
        ("avec", "mit"), ("sans", "ohne"), ("pour", "für"),
        ("dans", "in"), ("sur", "auf"), ("sous", "unter")
    ],
    "Latein": [
        ("esse", "sein"), ("habere", "haben"),
        ("dicere", "sagen"), ("facere", "machen / tun"),
        ("videre", "sehen"), ("audire", "hören"),
        ("ire", "gehen"), ("venire", "kommen"),
        ("dare", "geben"), ("capere", "nehmen / fangen"),
        ("amare", "lieben"), ("laudare", "loben"),
        ("pugnare", "kämpfen"), ("vincere", "siegen"),
        ("putare", "glauben / meinen"), ("scire", "wissen"),
        ("velle", "wollen"), ("posse", "können"),
        ("homo", "der Mensch"), ("vir", "der Mann"),
        ("femina", "die Frau"), ("rex", "der König"),
        ("regina", "die Königin"), ("populus", "das Volk"),
        ("urbs", "die Stadt"), ("bellum", "der Krieg"),
        ("amicus", "der Freund"), ("inimicus", "der Feind"),
        ("pater", "der Vater"), ("mater", "die Mutter"),
        ("filius", "der Sohn"), ("filia", "die Tochter"),
        ("domus", "das Haus"), ("liber", "das Buch"),
        ("verbum", "das Wort"), ("annus", "das Jahr"),
        ("dies", "der Tag"), ("nox", "die Nacht"),
        ("magnus", "groß"), ("parvus", "klein"),
        ("bonus", "gut"), ("malus", "schlecht"),
        ("novus", "neu"), ("vetus", "alt"),
        ("et", "und"), ("sed", "aber"), ("non", "nicht"),
        ("in", "in / auf"), ("ad", "zu / nach"), ("cum", "mit"),
        ("ex", "aus"), ("de", "von / über"), ("pro", "für"),
        ("omnis", "jeder / ganz"), ("totus", "ganz"),
        ("primus", "erster"), ("unus", "einer")
    ],
    "Spanisch": [
        ("hola", "hallo"), ("adiós", "tschüss"),
        ("gracias", "danke"), ("por favor", "bitte"),
        ("sí", "ja"), ("no", "nein"),
        ("el hombre", "der Mann"), ("la mujer", "die Frau"),
        ("el chico", "der Junge"), ("la chica", "das Mädchen"),
        ("el amigo", "der Freund"), ("la familia", "die Familie"),
        ("la escuela", "die Schule"), ("el libro", "das Buch"),
        ("el pan", "das Brot"), ("el agua", "das Wasser"),
        ("la casa", "das Haus"), ("el tiempo", "Zeit / Wetter"),
        ("el día", "der Tag"), ("la noche", "die Nacht"),
        ("la vida", "das Leben"),
        ("ser", "sein (permanent)"), ("estar", "sein (Ort/Zustand)"),
        ("tener", "haben"), ("hacer", "machen"),
        ("ir", "gehen"), ("venir", "kommen"),
        ("querer", "wollen"), ("poder", "können"),
        ("decir", "sagen"), ("ver", "sehen"), ("saber", "wissen"),
        ("tomar", "nehmen"), ("dar", "geben"),
        ("comer", "essen"), ("beber", "trinken"),
        ("hablar", "sprechen"), ("comprender", "verstehen"),
        ("aprender", "lernen"), ("amar", "lieben"),
        ("grande", "groß"), ("pequeño", "klein"),
        ("bueno", "gut"), ("malo", "schlecht"),
        ("bonito", "schön"), ("nuevo", "neu"), ("viejo", "alt"),
        ("pero", "aber"), ("porque", "weil"),
        ("muy", "sehr"), ("mucho", "viel"),
        ("con", "mit"), ("sin", "ohne"), ("para", "für (Zweck)"),
        ("por", "für (Grund) / durch"), ("en", "in"),
        ("sobre", "auf / über"), ("debajo", "unter")
    ],
    "Italienisch": [
        ("ciao", "hallo / tschüss"), ("grazie", "danke"),
        ("per favore", "bitte"), ("sì", "ja"), ("no", "nein"),
        ("l'uomo", "der Mann"), ("la donna", "die Frau"),
        ("il ragazzo", "der Junge"), ("la ragazza", "das Mädchen"),
        ("l'amico", "der Freund"), ("la famiglia", "die Familie"),
        ("la scuola", "die Schule"), ("il libro", "das Buch"),
        ("il pane", "das Brot"), ("l'acqua", "das Wasser"),
        ("la casa", "das Haus"), ("il tempo", "Zeit / Wetter"),
        ("il giorno", "der Tag"), ("la notte", "die Nacht"),
        ("la vita", "das Leben"),
        ("essere", "sein"), ("avere", "haben"), ("fare", "machen"),
        ("andare", "gehen"), ("venire", "kommen"),
        ("volere", "wollen"), ("potere", "können"),
        ("dire", "sagen"), ("vedere", "sehen"), ("sapere", "wissen"),
        ("prendere", "nehmen"), ("dare", "geben"),
        ("mangiare", "essen"), ("bere", "trinken"),
        ("parlare", "sprechen"), ("capire", "verstehen"),
        ("imparare", "lernen"), ("amare", "lieben"),
        ("grande", "groß"), ("piccolo", "klein"),
        ("buono", "gut"), ("cattivo", "schlecht"),
        ("bello", "schön"), ("nuovo", "neu"), ("vecchio", "alt"),
        ("ma", "aber"), ("perché", "weil"),
        ("molto", "sehr / viel"), ("già", "schon"), ("sempre", "immer"),
        ("con", "mit"), ("senza", "ohne"), ("per", "für"),
        ("in", "in"), ("su", "auf"), ("sotto", "unter"),
        ("ci", "dort / daran (=y)"), ("ne", "davon (=en)")
    ]
}

if st.button("Erklären / Starten"):
    st.write("---")

    if "VOKABELN mit" in thema:
        if sprache == "Deutsch":
            st.write("Deutsch hat keine Vokabeln - ist ja deine Sprache!")
            st.write("Hier gibt es nur Grammatik und Konjunktiv I")
        else:
            st.subheader(f"{sprache} VOKABELN mit Übersetzung")
            liste = vokabeln.get(sprache, [])
            for fremd, deutsch in liste:
                st.write(f"**{fremd}** = {deutsch}")
            st.write(f"--- Total: {len(liste)} Vokabeln")

    elif "QUIZ" in thema:
        if sprache == "Deutsch":
            st.write("Kein Vokabel-Quiz für Deutsch!")
            st.write("Aber Grammatik-Quiz: Konjunktiv I")
            st.write("Er sagt: Ich bin krank -> Er sagt, er ___ krank")
            st.write("Lösung: sei")
        else:
            liste = vokabeln.get(sprache, [])
            wort, loesung = random.choice(liste)
            st.session_state.quiz_wort = wort
            st.session_state.quiz_loesung = loesung
            st.session_state.quiz_sprache = sprache
            st.subheader(f"QUIZ {sprache}")
            st.write(f"Was heißt: **{wort}** ?")
            st.write(f"Score: {st.session_state.score}")

    elif "Pronomen" in thema:
        if "Franz" in sprache:
            st.write("je tu il elle nous vous ils, le la lui y en VOR Verb")
            st.write("Je le vois, J'y vais, J'en veux")
        elif "Spanisch" in sprache:
            st.write("yo tu el ella, lo la = direkt, le = indirekt")
            st.write("Se lo doy = Ich gebe es ihm, Me lo da")
        elif "Italienisch" in sprache:
            st.write("io tu lui lei, lo la gli, ci=dort(y), ne=davon(en)")
            st.write("Ci vado=J'y vais, Ne voglio=J'en veux, Glielo do")
        elif "Latein" in sprache:
            st.write("ego tu is nos, meus tuus suus, hic ille is, qui quae quod")
        else:
            st.write("ich du er sie es wir ihr sie, mich dich ihn, mir dir ihm")

    elif "Direkte" in thema:
        if "Franz" in sprache:
            st.write("Il dit qu'il est malade, il a dit qu'il etait malade")
            st.write("Ou->ou, Que->ce que, ob->si, Befehl de+Inf")
        elif "Spanisch" in sprache:
            st.write("Dice que esta enfermo, Dijo que estaba enfermo")
            st.write("Presente->Imperfecto, Futuro->Condicional, ob->si")
        elif "Italienisch" in sprache:
            st.write("Dice che e malato, Ha detto che era malato")
            st.write("Presente->Imperfetto, Futuro->Condizionale, ob->se")
        elif "Latein" in sprache:
            st.write("Dicit Gallos venire=AcI, Rogat ubi sit=Konj, Imperat ut veniat")
        else:
            st.write("Er sagt, er sei krank - Konjunktiv I! sei habe solle")

    elif "Grammatik" in thema:
        if "Franz" in sprache:
            st.write("Futur proche Je vais manger, Futur simple parlerai serai")
            st.write("Passe J'ai mange, Imparfait Je parlais, Subjonctif")
        elif "Spanisch" in sprache:
            st.write("Futur hablare tendre, Indefinido hable, Imperf hablaba")
            st.write("Ser permanent, Estar Zustand/Ort, Por Grund, Para Zweck")
            st.write("Subjuntivo: quiero que hables")
        elif "Italienisch" in sprache:
            st.write("Futur parlero saro avro, Passato ho parlato sono andato")
            st.write("Imperfetto parlavo, Essere vs Stare, Congiuntivo")
            st.write("al del nel = a+il de+il in+il")
        elif "Latein" in sprache:
            st.write("amo amabam amabo amavi amaveram, AcI, PPA PPP PFA")
        else:
            st.write("Perfekt habe gespielt, Präteritum spielte, Futur werde spielen")
            st.write("Nebensatz Verb am Ende!")

# QUIZ ANTWORT BEREICH
if st.session_state.quiz_wort and "QUIZ" in thema:
    antwort = st.text_input(f"Deine Übersetzung für {st.session_state.quiz_wort}:")
    if st.button("Prüfen"):
        richtige = st.session_state.quiz_loesung.lower()
        if antwort.lower() in richtige or richtige in antwort.lower():
            st.success(f"Richtig! {st.session_state.quiz_wort} = {st.session_state.quiz_loesung}")
            st.session_state.score += 1
        else:
            st.error(f"Falsch! {st.session_state.quiz_wort} = {st.session_state.quiz_loesung}")
        # Neues Wort
        liste = vokabeln.get(st.session_state.quiz_sprache, [])
        wort, loesung = random.choice(liste)
        st.session_state.quiz_wort = wort
        st.session_state.quiz_loesung = loesung
        st.write(f"Nächstes Wort: **{wort}** ?")
        st.experimental_rerun()

st.caption("v11.0 mit Quiz und Übersetzung - by HISTORIA12703")
