import streamlit as st

st.set_page_config(page_title="Französisch MEGA KI", page_icon="🇫🇷", layout="centered")
st.title("🇫🇷 Französisch MEGA KI")
st.write("Die ganze Grammatik ausführlich!")
st.write("---")

thema = st.selectbox("Was willst du lernen?", [
    "Pronoms d'objet - le, la, lui, leur, y, en",
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
        st.subheader("🎯 OBJEKTE - le, la, lui, leur, y, en")
        st.write("Das wichtigste Thema!")
        st.write("")
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
        st.write("REIHENFOLGE: me/te/se/nous/vous + le/la/les + lui/leur + y + en + VERB")
        st.write("ACHTUNG: La pizza? Je l'ai mangee. -> Bei COD vor Verb angleichen!")

    elif "COD" in thema:
        st.subheader("COD vs COI")
        st.write("COD = direkt, ohne a")
        st.write("Je mange une pomme -> Je la mange")
        st.write("")
        st.write("COI = mit a")
        st.write("Je parle a Marie -> Je lui parle")

    elif "Passe" in thema:
        st.subheader("Passe compose")
        st.write("Formel: avoir/etre + Partizip")
        st.write("avoir fuer 90%")
        st.write("etre fuer 14 Verben: aller, venir, arriver, partir, entrer, sortir, monter, descendre, rester, tomber, naitre, mourir, retourner, passer")
        st.write("Partizip: manger -> mange, finir -> fini, vendre -> vendu")
        st.write("Achtung bei etre immer angleichen: Elle est allee")

    else:
        st.subheader(thema)
        st.write(f"Hier kommt die ausführliche Erklärung zu {thema}")
        st.write("Mit Regeln, Beispielen und typischen Fehlern.")

    st.success("Fertig! Noch ein Thema?")

st.caption("Version 2.1 FIXED - by HISTORIA12703")
