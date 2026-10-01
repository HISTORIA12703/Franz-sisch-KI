import streamlit as st

st.set_page_config(page_title="Französisch KI", page_icon="🇫🇷", layout="centered")
st.title("🇫🇷 Französisch KI")
st.markdown("### Deine ausführliche Grammatik-Erklärung")
st.write("---")

thema = st.selectbox(
    "Welches Thema brauchst du?",
    ["Passé composé", "Imparfait", "Articles", "être und avoir", "Verneinung", "Futur", "Fragen"]
)

if st.button("Ausführlich erklären lassen"):
    st.write("---")
    
    if thema == "Passé composé":
        st.subheader("📚 Das Passé composé - MEGA ausführlich")
        st.markdown("""
        **1. Was ist das?** Die wichtigste Vergangenheit. Wie Deutsch "Ich HABE gegessen".

        **2. Formel:** **avoir oder être im Präsens + Participe passé**

        **3. avoir oder être?**
        - **90% mit AVOIR:** manger, faire, voir
        - **Nur 14 mit ÊTRE:** aller, venir, arriver, partir, entrer, sortir, monter, rester, tomber, naître, mourir...

        **4. Participe passé bilden:**
        - -er -> -é: mangé
        - -ir -> -i: fini
        - -re -> -u: vendu
        - Unregelmäßig: fait, pris, vu, été, eu

        **5. Beispiele:**
        J'ai mangé une pizza.
        Je suis allé au cinéma.

        **ACHTUNG:** Bei être angleichen! Elle est allée.
        """)

    elif thema == "Articles":
        st.subheader("📚 Les Articles")
        st.markdown("""
        **le** männlich: le garçon
        **la** weiblich: la fille
        **l'** vor Vokal: l'école
        **les** Plural für alle
        
        **un** männlich, **une** weiblich, **des** Plural
        
        **Merksatz:** Lerne immer LA table, nicht nur table!
        """)

    else:
        st.subheader(f"📚 {thema}")
        st.info("Ausführliche Erklärung kommt noch! Sag mir welches du brauchst!")

    st.success("Fertig!")
