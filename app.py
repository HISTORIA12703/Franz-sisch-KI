import streamlit as st

st.set_page_config(page_title="Französisch MEGA KI", page_icon="🇫🇷", layout="centered")
st.title("🇫🇷 Französisch MEGA KI")
st.write("Die ganze Grammatik ausführlich!")
st.write("---")

thema = st.selectbox("Was willst du lernen?", [
    "Pronoms d'objet - le, la, lui, leur, y, en",
    "Pronomen - ALLE Pronomen komplett",
    "Direkte und Indirekte Rede",
    "COD und COI",
    "Passe compose",
    "Imparfait",
    "Articles",
    "etre und avoir",
    "Adjektive",
    "Verneinung",
    "Futur",
    "Fragen bilden"
])

if st.button("Erklären lassen"):
    st.write("---")

    if "objet" in thema:
        st.subheader("OBJEKTE - le, la, lui, leur, y, en")
        st.write("A) COD - Wen? Was? -> le, la, les")
        st.write("Je vois le garcon -> Je le vois.")
        st.write("Stellung: VOR dem Verb!")
        st.write("")
        st.write("B) COI - Wem? -> lui, leur")
        st.write("Je parle a Paul -> Je lui parle.")
        st.write("")
        st.write("C) y - Ort mit a")
        st.write("Tu vas a Paris? -> Oui, j'y vais.")
        st.write("")
        st.write("D) en - von, davon, Menge mit de")
        st.write("Tu veux du gateau? -> Oui, j'en veux.")
        st.write("")
        st.write("REIHENFOLGE:")
        st.write("me te se nous vous + le la les + lui leur + y + en + VERB")

    elif "ALLE Pronomen" in thema:
        st.subheader("PRONOMEN - ALLE im Überblick")
        st.write("1. PERSONAL: je, tu, il, elle, nous, vous, ils, elles")
        st.write("2. POSSESSIV: mon ma mes / ton ta tes / son sa ses")
        st.write("   le mien, la mienne, les miens")
        st.write("3. DEMONSTRATIV: celui, celle, ceux, celles")
        st.write("   celui-ci = dieser hier")
        st.write("4. RELATIV: qui, que, ou, dont")
        st.write("   qui = der (Subjekt)")
        st.write("   que = den (Objekt)")
        st.write("   ou = wo")
        st.write("   dont = von dem")
        st.write("5. FRAGE: qui, que, quoi, lequel")
        st.write("6. BETONT: moi, toi, lui, elle, nous, vous, eux")

    elif "Direkte" in thema:
        st.subheader("DIREKTE und INDIREKTE REDE")
        st.write("A) DIREKT: Il dit: Je suis fatigue.")
        st.write("B) INDIREKT: Il dit qu'il est fatigue.")
        st.write("")
        st.write("WICHTIGE AENDERUNGEN:")
        st.write("Pronomen: je -> il, mon -> son")
        st.write("")
        st.write("Zeiten wenn Hauptsatz Vergangenheit:")
        st.write("Present -> Imparfait")
        st.write("  Je suis malade -> il etait malade")
        st.write("Passe compose -> Plus-que-parfait")
        st.write("  J'ai mange -> il avait mange")
        st.write("Futur -> Conditionnel")
        st.write("  Je viendrai -> il viendrait")
        st.write("")
        st.write("Fragen:")
        st.write("Ou vas-tu? -> ou je vais")
        st.write("Que fais-tu? -> ce que je fais")
        st.write("Viens-tu? -> si je viens")
        st.write("")
        st.write("Befehl:")
        st.write("Viens! -> de venir")

    elif "COD" in thema:
        st.subheader("COD vs COI")
        st.write("COD ohne a: Je la mange")
        st.write("COI mit a: Je lui parle")

    elif "Passe" in thema:
        st.subheader("Passe compose")
        st.write("Formel: avoir/etre + Partizip")
        st.write("etre fuer 14 Verben: aller, venir, partir, etc.")
        st.write("Bei etre angleichen: Elle est allee")

    else:
        st.subheader(thema)
        st.write("Erklaerung zu diesem Thema")
        st.write("Mit Regeln und Beispielen")

    st.success("Fertig! Noch ein Thema?")

st.caption("Version 3.1 FIXED - by HISTORIA12703")
