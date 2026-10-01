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
        st.subheader("🎯 OBJEKTE - le, la, lui, leur, y, en")
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
        st.write("REIHENFOLGE: me/te/se/nous/vous + le/la/les + lui/leur + y
