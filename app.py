import streamlit as st

st.set_page_config(page_title="Franzoesisch KI", page_icon="🇫🇷")
st.title("Franzoesisch MEGA KI")
st.write("Version 6.0 - ALLES drin")
st.write("---")

thema = st.selectbox("Thema waehlen:", [
    "Pronomen - ALLE",
    "Direkte und Indirekte Rede",
    "le, la, lui, leur, y, en",
    "COD und COI",
    "Passe compose",
    "Imparfait",
    "Futur - ALLE Formen",
    "Articles - der die das",
    "etre und avoir",
    "Adjektive",
    "Verneinung - ne pas",
    "Fragen bilden"
])

if st.button("Erklaeren"):
    st.write("---")

    if "Pronomen" in thema:
        st.subheader("PRONOMEN ALLE")
        st.write("WAS: Ersetzt Nomen")
        st.write("Personal: je tu il elle nous vous ils")
        st.write("Objekt: le la lui y en VOR Verb!")
        st.write("Possessiv: mon ma mes, le mien")
        st.write("Relativ: qui der, que den, ou wo, dont von dem")
        st.write("Demonstrativ: celui dieser")

    elif "Direkte" in thema:
        st.subheader("DIREKTE / INDIREKTE REDE")
        st.write("Direkt: Il dit: Je suis malade")
        st.write("Indirekt Praesens: Il dit qu'il est malade")
        st.write("Indirekt Vergangenheit: Zeit aendern!")
        st.write("Present -> Imparfait")
        st.write("Passe comp -> Plus-que-parfait")
        st.write("Futur -> Conditionnel")
        st.write("Frage: Ou? -> ou, Que? -> ce que, JaNein -> si")
        st.write("Befehl: Viens! -> de venir")

    elif "le, la" in thema:
        st.subheader("le la lui leur y en")
        st.write("le = ihn, la = sie, les = sie Plural")
        st.write("WANN: COD, Wen? Was? Ohne a")
        st.write("Stellung VOR Verb: Je le vois")
        st.write("lui = ihm/ihr, leur = ihnen")
        st.write("WANN: COI, Wem? Mit a bei Person")
        st.write("y = dort, bei Ort mit a, chez, en")
        st.write("Tu vas a Paris? J'y vais")
        st.write("en = davon, bei de und Menge")
        st.write("Du gateau? J'en veux 2")

    elif "COD" in thema:
        st.subheader("COD vs COI")
        st.write("COD = direkt, ohne a, Wen? Was?")
        st.write("Je mange une pomme -> Je la mange")
        st.write("COI = indirekt, mit a, Wem?")
        st.write("Je parle a Marie -> Je lui parle")
        st.write("Bei COD vor Verb: l'ai mangee mit e!")

    elif "Passe" in thema:
        st.subheader("PASSE COMPOSE")
        st.write("WAS: Vergangenheit, was passiert ist")
        st.write("WIE: avoir/etre + Partizip")
        st.write("90% mit avoir")
        st.write("J'ai mange, tu as fini")
        st.write("14 Verben mit etre:")
        st.write("aller venir arriver partir")
        st.write("entrer sortir monter descendre")
        st.write("rester tomber naitre mourir")
        st.write("retourner passer")
        st.write("Bei etre angleichen:")
        st.write("Elle est allee, Ils sont alles")

    elif "Imparfait" in thema:
        st.subheader("IMPARFAIT")
        st.write("WAS: Gewohnheit, Hintergrund")
        st.write("WANN: Frueher immer, was gerade war")
        st.write("WIE: nous-Form + ais, ais, ait, ions, iez, aient")
        st.write("parler -> nous parlons -> je parlais")
        st.write("Beispiel: Quand j'etais petit, je jouais")
        st.write("Unterschied zu Passe comp:")
        st.write("Passe = einmalig, Imparfait = immer")

    elif "Futur" in thema:
        st.subheader("FUTUR - Zukunft")
        st.write("1. FUTUR COMPOSE - nah, gleich")
        st.write("WANN: Gleich, bald")
        st.write("WIE: aller + Infinitiv")
        st.write("Je vais manger, Tu vas dormir")
        st.write("Beispiel: Je vais bientot partir")
        st.write("")
        st.write("2. FUTUR SIMPLE - spaeter, irgendwann")
        st.write("WANN: Spaeter, Vermutung, Wille")
        st.write("WIE: Infinitiv + Endung")
        st.write("Endung: ai, as, a, ons, ez, ont")
        st.write("parler -> je parlerai")
        st.write("finir -> je finirai")
        st.write("Viele unregelmaessig:")
        st.write("etre -> ser-, avoir -> aur-")
        st.write("aller -> ir-, faire -> fer-")
        st.write("venir -> viendr-, voir -> verr-")
        st.write("Beispiel: Un jour je serai riche")
        st.write("")
        st.write("3. FUTUR ANTERIEUR")
        st.write("WANN: Zukunft vor Zukunft")
        st.write("WIE: Futur von avoir/etre + Partizip")
        st.write("J'aurai fini avant toi")

    elif "Articles" in thema:
        st.subheader("ARTICLES")
        st.write("unbestimmt: un, une, des")
        st.write("un garcon, une fille, des enfants")
        st.write("bestimmt: le, la, les, l'")
        st.write("le garcon, la fille, l'ecole")
        st.write("teilungsartikel: du, de la, des")
        st.write("Je veux du pain, de la viande")
        st.write("Nach Verneinung immer de:")
        st.write("J'ai des pommes -> Je n'ai pas de pommes")

    elif "etre" in thema:
        st.subheader("ETRE UND AVOIR")
        st.write("etre = sein: je suis, tu es, il est")
        st.write("nous sommes, vous etes, ils sont")
        st.write("avoir = haben: j'ai, tu as, il a")
        st.write("nous avons, vous avez, ils ont")
        st.write("WANN braucht man sie?")
        st.write("etre fuer Beschreibung, Ort")
        st.write("avoir fuer Besitz, Alter")
        st.write("J'ai 15 ans, nicht Je suis 15!")

    elif "Adjektive" in thema:
        st.subheader("ADJEKTIVE")
        st.write("WIE: Angleichen an Nomen!")
        st.write("maennlich: petit, feminin: petite")
        st.write("Plural +s: petites")
        st.write("Stellung meist nach Nomen:")
        st.write("une voiture rouge")
        st.write("Vor Nomen: bon, grand, petit, beau etc")
        st.write("un grand garcon")
        st.write("Steigerung: plus grand que")

    elif "Verneinung" in thema:
        st.subheader("VERNEINUNG")
        st.write("WIE: ne + Verb + pas")
        st.write("Je ne parle pas")
        st.write("Bei Vokal: n'")
        st.write("Je n'aime pas")
        st.write("Andere: ne plus nicht mehr")
        st.write("ne jamais nie, ne rien nichts")
        st.write("ne personne niemand")
        st.write("ne que nur: Je n'ai que 2 euros")

    elif "Fragen" in thema:
        st.subheader("FRAGEN BILDEN")
        st.write("1. Mit est-ce que: Tu parles? -> Est-ce que tu parles?")
        st.write("2. Inversion: Parles-tu?")
        st.write("3. Mit Fragewort: Ou, Quand, Comment, Pourquoi")
        st.write("Ou vas-tu? Pourquoi tu pleures?")
        st.write("4. Mit que: Que fais-tu? Qu'est-ce que tu fais?")

    st.success("Fertig!")

st.caption("v6.0 ALLES DRIN by HISTORIA12703")
