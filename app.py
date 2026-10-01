import streamlit as st

st.set_page_config(page_title="Französisch MEGA KI", page_icon="🇫🇷", layout="centered")
st.title("🇫🇷 Französisch MEGA KI")
st.markdown("**Die ganze Grammatik - ausführlich erklärt!**")
st.write("---")

thema = st.selectbox("Was willst du lernen?", [
    "--- WÄHLE THEMA ---",
    "1. Pronoms d'objet (le, la, lui, leur, y, en) - OBJEKTE",
    "2. COD & COI - Objekte",
    "3. Passé composé",
    "4. Imparfait",
    "5. Imparfait vs Passé composé",
    "6. Articles (le, la, un, une, du, de la)",
    "7. être & avoir komplett",
    "8. Pronomen (je, me, moi, etc.)",
    "9. Adjektive - Angleichung",
    "10. Verneinung (ne...pas, plus, jamais)",
    "11. Futur simple & proche",
    "12. Plus-que-parfait",
    "13. Subjonctif",
    "14. Fragen bilden",
    "15. Relativpronomen (qui, que, où)"
])

if st.button("🚀 Ausführlich erklären"):
    st.write("---")
    
    if "Objekte" in thema or "1." in thema:
        st.subheader("🎯 OBJEKTE - Pronoms d'objet (WICHTIG!)")
        st.markdown("""
        **Das vermissen 90% der Schüler!**

        **A) COD - Akkusativ (WEN? WAS?)**
        Ersetzt das direkte Objekt.
        - **le** ihn/es
