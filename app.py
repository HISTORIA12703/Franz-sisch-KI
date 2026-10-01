import streamlit as st

st.set_page_config(page_title="Französisch Ki", page_icon="🇫🇷")
st.title("🇫🇷 Französisch Ki")
st.write("Deine KI für Grammatik!")

thema = st.selectbox("Wähle ein Thema:", ["Passé composé", "Imparfait", "Articles le/la", "être / avoir", "Futur"])

if st.button("Erklären"):
    st.subheader(f"Thema: {thema}")
    st.write(f"Hier kommt die ausführliche Erklärung zu {thema}...")
    st.markdown("""
    **1. Regel:** Ganz einfach erklärt
    **2. Beispiel:** Je suis allé...
    **3. Merksatz:** So merkst du es dir!
    """)
import streamlit as st

st.set_page_config(page_title="Französisch KI", page_icon="🇫🇷", layout="centered")
st.title("🇫🇷 Französisch KI")
st.markdown("### Deine ausführliche Grammatik-Erklärung")
st.write("---")

thema = st.selectbox(
    "Welches Thema brauchst du?",
    ["Passé composé", "Imparfait", "Imparfait vs Passé composé", "Articles (le, la, un, une)", "être und avoir", "Verneinung (ne...pas)", "Futur simple", "Fragen bilden"]
)

if st.button("Ausführlich erklären lassen"):
    st.write("---")
    
    if thema == "Passé composé":
        st.subheader("📚 Das Passé composé - MEGA ausführlich")
        st.markdown("""
        **1. Was ist das überhaupt?**
        Das Passé composé ist die wichtigste Vergangenheit im Französischen. Auf Deutsch ist das wie "Ich HABE gegessen" oder "Ich BIN gegangen". Man benutzt es für abgeschlossene Handlungen.

        **2. Wie bildet man es? Formel:**
        **avoir oder être im Präsens + Participe passé (Vergangenheitsform)**

        **3. Wann nehme ich avoir und wann être?**
        - **90% aller Verben mit AVOIR:** manger, faire, voir, prendre...
        - **Nur 14 Verben mit ÊTRE:** aller, venir, arriver, partir, entrer, sortir, monter, descendre, rester, tomber, naître, mourir, retourner, passer. Merksatz: Haus der Verben!

        **4. Wie bilde ich das Participe passé?**
        - Verben auf -er -> -é: manger -> mangé, parler -> parlé
        - Verben auf -ir -> -i: finir -> fini, choisir -> choisi
        - Verben auf -re -> -u: vendre -> vendu
        - UNREGELMÄSSIG musst du lernen: faire -> fait, prendre -> pris, voir -> vu, être -> été, avoir -> eu

        **5. Beispielsätze mit avoir:**
        J'ai mangé une pizza. (Ich habe eine Pizza gegessen)
        Tu as fait tes devoirs. (Du hast deine Hausaufgaben gemacht)
        Il a vu un film. (Er hat einen Film gesehen)

        **6. Beispielsätze mit être + WICHTIGE REGEL:**
        Je suis allé(e) au cinéma. (Ich bin ins Kino gegangen)
        Elle est venue hier. (Sie ist gestern gekommen)
        **ACHTUNG:** Bei être musst du das Partizip angleichen! Wenn die Person weiblich ist, kommt ein -e dran. Im Plural ein -s. Elle est allée, Ils sont allés.

        **7. Signalwörter:**
        hier (gestern), hier soir (gestern Abend), la semaine dernière (letzte Woche), en 2020

        **8. Übung für dich:**
        Übersetze: Wir haben Französisch gelernt.
        Lösung: Nous avons appris le français.
        """)

    elif thema == "Articles (le, la, un, une)":
        st.subheader("📚 Les Articles - Die Artikel")
        st.markdown("""
        **1. Grundidee:**
        Im Französischen ist JEDES Nomen männlich oder weiblich. Es gibt kein "es". Du MUSST den Artikel mitlernen.

        **2. Bestimmte Artikel (der, die, das):**
        - **le** männlich: le garçon, le livre, le chien
        - **la** weiblich: la fille, la table, la maison
        - **l'** vor Vokal egal ob m/w: l'école, l'ami, l'histoire
        - **les** Plural für alle: les garçons, les filles

        **3. Unbestimmte Artikel (ein, eine):**
        - **un** männlich: un garçon (ein Junge)
        - **une** weiblich: une fille (ein Mädchen)
        - **des** Plural: des livres (Bücher / einige Bücher)

        **4. Der Teilungsartikel (ganz wichtig!):**
        Im Französischen sagt man nicht "Ich esse Brot" sondern "Ich esse VON DEM Brot"
        - du pain, de la viande, des pâtes
        - Je mange du pain.
import streamlit as st

st.set_page_config(page_title="Französisch KI", page_icon="🇫🇷", layout="centered")
st.title("🇫🇷 Französisch KI")
st.markdown("### Deine ausführliche Grammatik-Erklärung")
st.write("---")

thema = st.selectbox(
    "Welches Thema brauchst du?",
    ["Passé composé", "Imparfait", "Imparfait vs Passé composé", "Articles (le, la, un, une)", "être und avoir", "Verneinung (ne...pas)", "Futur simple", "Fragen bilden"]
)

if st.button("Ausführlich erklären lassen"):
    st.write("---")
    
    if thema == "Passé composé":
        st.subheader("📚 Das Passé composé - MEGA ausführlich")
        st.markdown("""
        **1. Was ist das überhaupt?**
        Das Passé composé ist die wichtigste Vergangenheit im Französischen. Auf Deutsch ist das wie "Ich HABE gegessen" oder "Ich BIN gegangen". Man benutzt es für abgeschlossene Handlungen.

        **2. Wie bildet man es? Formel:**
        **avoir oder être im Präsens + Participe passé (Vergangenheitsform)**

        **3. Wann nehme ich avoir und wann être?**
        - **90% aller Verben mit AVOIR:** manger, faire, voir, prendre...
        - **Nur 14 Verben mit ÊTRE:** aller, venir, arriver, partir, entrer, sortir, monter, descendre, rester, tomber, naître, mourir, retourner, passer. Merksatz: Haus der Verben!

        **4. Wie bilde ich das Participe passé?**
        - Verben auf -er -> -é: manger -> mangé, parler -> parlé
        - Verben auf -ir -> -i: finir -> fini, choisir -> choisi
        - Verben auf -re -> -u: vendre -> vendu
        - UNREGELMÄSSIG musst du lernen: faire -> fait, prendre -> pris, voir -> vu, être -> été, avoir -> eu

        **5. Beispielsätze mit avoir:**
        J'ai mangé une pizza. (Ich habe eine Pizza gegessen)
        Tu as fait tes devoirs. (Du hast deine Hausaufgaben gemacht)
        Il a vu un film. (Er hat einen Film gesehen)

        **6. Beispielsätze mit être + WICHTIGE REGEL:**
        Je suis allé(e) au cinéma. (Ich bin ins Kino gegangen)
        Elle est venue hier. (Sie ist gestern gekommen)
        **ACHTUNG:** Bei être musst du das Partizip angleichen! Wenn die Person weiblich ist, kommt ein -e dran. Im Plural ein -s. Elle est allée, Ils sont allés.

        **7. Signalwörter:**
        hier (gestern), hier soir (gestern Abend), la semaine dernière (letzte Woche), en 2020

        **8. Übung für dich:**
        Übersetze: Wir haben Französisch gelernt.
        Lösung: Nous avons appris le français.
        """)

    elif thema == "Articles (le, la, un, une)":
        st.subheader("📚 Les Articles - Die Artikel")
        st.markdown("""
        **1. Grundidee:**
        Im Französischen ist JEDES Nomen männlich oder weiblich. Es gibt kein "es". Du MUSST den Artikel mitlernen.

        **2. Bestimmte Artikel (der, die, das):**
        - **le** männlich: le garçon, le livre, le chien
        - **la** weiblich: la fille, la table, la maison
        - **l'** vor Vokal egal ob m/w: l'école, l'ami, l'histoire
        - **les** Plural für alle: les garçons, les filles

        **3. Unbestimmte Artikel (ein, eine):**
        - **un** männlich: un garçon (ein Junge)
        - **une** weiblich: une fille (ein Mädchen)
        - **des** Plural: des livres (Bücher / einige Bücher)

        **4. Der Teilungsartikel (ganz wichtig!):**
        Im Französischen sagt man nicht "Ich esse Brot" sondern "Ich esse VON DEM Brot"
        - du pain, de la viande, des pâtes
        - Je mange du pain.


