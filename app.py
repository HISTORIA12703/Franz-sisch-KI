import streamlit as st

st.set_page_config(page_title="Franzoesisch KI", page_icon="🇫🇷")
st.title("🇫🇷 Franzoesisch MEGA KI")
st.write("Version 5.0 - Final")
st.write("---")

thema = st.selectbox("Was willst du lernen?", [
    "Pronomen - ALLE",
    "Direkte und Indirekte Rede",
    "le, la, lui, leur, y, en",
    "COD und COI",
    "Passe compose",
    "Imparfait"
])

if st.button("Erklaeren lassen"):
    st.write("---")

    if "Pronomen" in thema:
        st.subheader("PRONOMEN - ALLE")
        
        st.write("WAS IST DAS?")
        st.write("Pronomen ersetzt Nomen.")
        st.write("Statt immer Paul zu sagen -> il")
        st.write("")
        
        st.write("1. PERSONAL")
        st.write("je ich, tu du, il er")
        st.write("elle sie, nous wir")
        st.write("vous ihr, ils sie")
        st.write("WANN: Als Subjekt")
        st.write("Beispiel: Je parle")
        st.write("")
        
        st.write("2. OBJEKT - le la lui y en")
        st.write("WANN: Wenn bekannt, nicht wiederholen")
        st.write("WIE: Immer VOR dem Verb!")
        st.write("")
        st.write("le = ihn (maennlich)")
        st.write("Tu vois le film? Je le vois")
        st.write("la = sie (weiblich)")
        st.write("Tu vois la fille? Je la vois")
        st.write("Vor Vokal: l'")
        st.write("lui = ihm/ihr bei Person mit a")
        st.write("Tu parles a Paul? Je lui parle")
        st.write("leur = ihnen")
        st.write("y = dort, bei Ort mit a")
        st.write("Tu vas a Paris? J'y vais")
        st.write("en = davon, bei de und Menge")
        st.write("Tu veux du gateau? J'en veux")
        st.write("")
        
        st.write("3. POSSESSIV")
        st.write("mon ma mes = mein")
        st.write("ton ta tes = dein")
        st.write("son sa ses = sein/ihr")
        st.write("le mien = meiner")
        st.write("Beispiel: C'est le mien!")
        st.write("")
        
        st.write("4. RELATIV")
        st.write("qui = der als Subjekt")
        st.write("Danach kommt Verb")
        st.write("L'homme qui parle")
        st.write("")
        st.write("que = den als Objekt")
        st.write("Danach Subjekt+Verb")
        st.write("Le livre que je lis")
        st.write("")
        st.write("ou = wo")
        st.write("La ville ou j'habite")
        st.write("")
        st.write("dont = von dem, dessen")
        st.write("Le livre dont je parle")
        st.write("")
        
        st.write("5. DEMONSTRATIV")
        st.write("celui = dieser")
        st.write("celle, ceux, celles")
        st.write("celui-ci = dieser hier")
        st.write("")
        
        st.write("REIHENFOLGE:")
        st.write("me te se nous vous")
        st.write("+ le la les")
        st.write("+ lui leur")
        st.write("+ y + en + VERB")
        st.write("Beispiel: Il me le donne")

    elif "Direkte" in thema:
        st.subheader("DIREKTE UND INDIREKTE REDE")
        
        st.write("WAS IST DAS?")
        st.write("Direkt = genau zitieren")
        st.write("Indirekt = weitererzaehlen")
        st.write("")
        
        st.write("DIREKT:")
        st.write("Il dit: Je suis malade")
        st.write("Mit Doppelpunkt und :")
        st.write("")
        
        st.write("INDIREKT - Praesens:")
        st.write("WANN: il dit = Zeit bleibt")
        st.write("WIE: que + Pronomen aendern")
        st.write("je -> il, mon -> son")
        st.write("Il dit qu'il est malade")
        st.write("")
        
        st.write("INDIREKT - Vergangenheit:")
        st.write("WANN: il a dit = Zeit aendern!")
        st.write("")
        st.write("Present -> Imparfait")
        st.write("Je suis fatigue")
        st.write("-> Il a dit qu'il etait fatigue")
        st.write("")
        st.write("Passe compose -> Plus-que-parfait")
        st.write("J'ai mange")
        st.write("-> Il avait mange")
        st.write("")
        st.write("Futur -> Conditionnel")
        st.write("Je viendrai")
        st.write("-> Il viendrait")
        st.write("")
        
        st.write("FRAGEN:")
        st.write("Ou vas-tu? -> ou je vais")
        st.write("Que fais-tu? -> ce que je fais")
        st.write("Viens-tu? -> si je viens")
        st.write("si = ob")
        st.write("")
        
        st.write("BEFEHLE:")
        st.write("Viens! -> de venir")
        st.write("Ne pars pas! -> de ne pas partir")

    else:
        st.subheader(thema)
        st.write("Erklaerung zu:")
        st.write(thema)

    st.success("Fertig!")

st.caption("by HISTORIA12703 - v5 Final")
