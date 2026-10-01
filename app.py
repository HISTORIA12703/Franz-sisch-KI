import streamlit as st

st.set_page_config(page_title="Französisch MEGA KI", page_icon="🇫🇷", layout="centered")
st.title("🇫🇷 Französisch MEGA KI")
st.write("Mit richtiger Erklärung - wann und wie!")
st.write("---")

thema = st.selectbox("Was willst du lernen?", [
    "Pronomen - ALLE komplett mit Wann/Wie",
    "Direkte und Indirekte Rede - komplett",
    "Pronoms d'objet - le, la, lui, leur, y, en",
    "COD und COI",
    "Passe compose",
    "Imparfait"
])

if st.button("Erklären lassen"):
    st.write("---")

    if "ALLE komplett" in thema:
        st.subheader("👑 PRONOMEN - Komplett erklärt")
        
        st.write("**WAS IST EIN PRONOMEN?**")
        st.write("Ein Pronomen ersetzt ein Nomen.")
        st.write("Damit du nicht immer wieder sagst: Paul, Paul, Paul")
        st.write("Sondern: Paul -> il, er")
        st.write("---")
        
        st.write("**1. PERSONALPRONOMEN**")
        st.write("WANN: Immer als Subjekt, wer macht was?")
        st.write("je = ich, tu = du, il = er, elle = sie")
        st.write("nous = wir, vous = ihr/Sie, ils/elles = sie Plural")
        st.write("WIE: Am Satzanfang")
        st.write("Beispiel: Je parle, tu parles, il parle")
        st.write("---")
        
        st.write("**2. OBJEKTPRONOMEN - le, la, lui, y, en**")
        st.write("WANN: Wenn du etwas schon kennst und nicht wiederholen willst")
        st.write("WIE: Immer VOR dem Verb! Das ist anders als Deutsch!")
        st.write("")
        st.write("le = ihn/es (männlich)")
        st.write("WANN: Bei COD männlich")
        st.write("Beispiel: Tu vois le film? Oui, je le vois.")
        st.write("")
        st.write("la = sie/es (weiblich)")
        st.write("Beispiel: Tu vois la fille? Oui, je la vois.")
        st.write("Aber: vor Vokal wird la zu l'")
        st.write("J'aime l'ecole -> Je l'aime")
        st.write("")
        st.write("lui = ihm/ihr")
        st.write("WANN: Bei Personen mit a, also COI")
        st.write("Beispiel: Tu parles a Paul? Oui, je lui parle.")
        st.write("")
        st.write("y = dort/hin, daran")
        st.write("WANN: Bei Orten mit a, en, chez und bei a + Sache")
        st.write("Beispiel Ort: Tu vas a Paris? Oui, j'y vais.")
        st.write("Beispiel Sache: Tu penses a l'examen? Oui, j'y pense.")
        st.write("NICHT bei Personen! Bei Personen = lui/leur")
        st.write("")
        st.write("en = davon, welche, etwas davon")
        st.write("WANN: Bei de, du, de la, des und bei Mengen")
        st.write("Beispiel Menge: Tu veux du gateau? Oui, j'en veux 2.")
        st.write("Beispiel de: Tu parles de Paul? Oui, j'en parle.")
        st.write("---")
        
        st.write("**3. POSSESSIVPRONOMEN**")
        st.write("WANN: Wenn du sagen willst wem etwas gehört")
        st.write("mon, ma, mes = mein")
        st.write("ton, ta, tes = dein")
        st.write("son, sa, ses = sein/ihr")
        st.write("le mien = meiner, la mienne = meine")
        st.write("Beispiel: C'est ton livre? Non, c'est le mien!")
        st.write("WICHTIG: ma wird zu mon vor Vokal: mon amie")
        st.write("---")
        
        st.write("**4. RELATIVPRONOMEN - qui, que, ou, dont**")
        st.write("WANN: Wenn du 2 Sätze verbindest")
        st.write("qui = der die das als Subjekt")
        st.write("WANN: Danach kommt ein Verb")
        st.write("Beispiel: L'homme qui parle est mon pere")
        st.write("")
        st.write("que = den, die, das als Objekt")
        st.write("WANN: Danach kommt Subjekt + Verb")
        st.write("Beispiel: Le livre que je lis est super")
        st.write("Vor Vokal: qu'")
        st.write("")
        st.write("ou = wo, in dem")
        st.write("WANN: Bei Ort oder Zeit")
        st.write("Beispiel: La ville ou j'habite / Le jour ou je suis ne")
        st.write("")
        st.write("dont = von dem, über den, dessen")
        st.write("WANN: Wenn im 2. Satz de vorkommt")
        st.write("Beispiel: Le livre dont je parle (parler de)")
        st.write("Beispiel: L'homme dont le pere est mort")
        st.write("---")
        
        st.write("**REIHENFOLGE MERKEN!**")
        st.write("1. me te se nous vous")
        st.write("2. le la les")
        st.write("3. lui leur")
        st.write("4. y")
        st.write("5. en")
        st.write("6. VERB")
        st.write("Beispiel: Il me le donne = Er gibt es mir")

    elif "Indirekte" in thema:
        st.subheader("🗣️ DIREKTE UND INDIREKTE REDE")
        
        st.write("**WAS IST DAS?**")
        st.write("Direkt = Original, mit Gänsefüßchen")
        st.write("Indirekt = Du erzählst was jemand
