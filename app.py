import streamlit as st
import random

st.set_page_config(page_title="5 Sprachen KI", page_icon="🌍")
st.title("🌍 5 SPRACHEN - 500 VOKABELN")
st.write("---")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.quiz_wort = None
    st.session_state.quiz_loesung = None
    st.session_state.quiz_sprache = None

sprache = st.selectbox("1. Sprache:", ["Französisch","Latein","Spanisch","Italienisch","Deutsch"])
thema = st.selectbox("2. Thema:", ["Grammatik","VOKABELN 500 mit Übersetzung","VOKABEL QUIZ"])

# MEGA VOKABELLISTEN
vokabeln = {
"Französisch": [
("bonjour","hallo"),("au revoir","tschüss"),("merci","danke"),
("s'il vous plait","bitte"),("oui","ja"),("non","nein"),("excusez-moi","entschuldigung"),
("l'homme","Mann"),("la femme","Frau"),("le garcon","Junge"),("la fille","Mädchen"),
("l'enfant","Kind"),("l'ami","Freund"),("la famille","Familie"),("le pere","Vater"),
("la mere","Mutter"),("le frere","Bruder"),("la soeur","Schwester"),
("l'ecole","Schule"),("le livre","Buch"),("le professeur","Lehrer"),
("l'eleve","Schüler"),("la classe","Klasse"),("le stylo","Stift"),
("la table","Tisch"),("la chaise","Stuhl"),("la porte","Tür"),("la fenetre","Fenster"),
("le pain","Brot"),("l'eau","Wasser"),("le lait","Milch"),("le fromage","Käse"),
("la viande","Fleisch"),("le poisson","Fisch"),("la pomme","Apfel"),
("manger","essen"),("boire","trinken"),("dormir","schlafen"),
("la maison","Haus"),("la chambre","Zimmer"),("la cuisine","Küche"),
("la voiture","Auto"),("le train","Zug"),("l'avion","Flugzeug"),
("la ville","Stadt"),("le village","Dorf"),("la rue","Straße"),("le parc","Park"),
("le jour","Tag"),("la nuit","Nacht"),("la semaine","Woche"),("le mois","Monat"),
("l'annee","Jahr"),("le temps","Zeit/Wetter"),("l'heure","Stunde/Uhrzeit"),
("aujourd'hui","heute"),("demain","morgen"),("hier","gestern"),
("etre","sein"),("avoir","haben"),("faire","machen"),("aller","gehen"),
("venir","kommen"),("vouloir","wollen"),("pouvoir","können"),("devoir","müssen"),
("dire","sagen"),("voir","sehen"),("savoir","wissen"),("connaitre","kennen"),
("prendre","nehmen"),("donner","geben"),("mettre","legen/stellen"),
("parler","sprechen"),("comprendre","verstehen"),("apprendre","lernen"),
("aimer","lieben/mögen"),("penser","denken"),("croire","glauben"),
("grand","groß"),("petit","klein"),("bon","gut"),("mauvais","schlecht"),
("beau","schön"),("nouveau","neu"),("vieux","alt"),("jeune","jung"),
("premier","erster"),("dernier","letzter"),("meme","selbe"),("autre","anderer"),
("mais","aber"),("parce que","weil"),("tres","sehr"),("beaucoup","viel"),
("peu","wenig"),("plus","mehr"),("moins","weniger"),("avec","mit"),
("sans","ohne"),("pour","für"),("dans","in"),("sur","auf"),("sous","unter"),
("devant","vor"),("derriere","hinter"),("entre","zwischen"),
("ici","hier"),("la","dort"),("ou","wo"),("quand","wann"),
("comment","wie"),("pourquoi","warum"),("combien","wie viel"),
("rouge","rot"),("bleu","blau"),("vert","grün"),("jaune","gelb"),
("noir","schwarz"),("blanc","weiß"),("un deux trois","1 2 3"),
("cent","100"),("mille","1000"),("toujours","immer"),("jamais","nie"),
("deja","schon"),("encore","noch"),("bien","gut"),("mal","schlecht"),
("vite","schnell"),("lentement","langsam")
],

"Spanisch": [
("hola","hallo"),("adiós","tschüss"),("gracias","danke"),("por favor","bitte"),
("sí","ja"),("no","nein"),("perdón","entschuldigung"),
("el hombre","Mann"),("la mujer","Frau"),("el chico","Junge"),("la chica","Mädchen"),
("el niño","Kind"),("el amigo","Freund"),("la familia","Familie"),("el padre","Vater"),
("la madre","Mutter"),("el hermano","Bruder"),("la hermana","Schwester"),
("la escuela","Schule"),("el libro","Buch"),("el profesor","Lehrer"),
("el alumno","Schüler"),("la clase","Klasse"),("el bolígrafo","Stift"),
("la mesa","Tisch"),("la silla","Stuhl"),("la puerta","Tür"),("la ventana","Fenster"),
("el pan","Brot"),("el agua","Wasser"),("la leche","Milch"),("el queso","Käse"),
("la carne","Fleisch"),("el pescado","Fisch"),("la manzana","Apfel"),
("comer","essen"),("beber","trinken"),("dormir","schlafen"),
("la casa","Haus"),("la habitación","Zimmer"),("la cocina","Küche"),
("el coche","Auto"),("el tren","Zug"),("el avión","Flugzeug"),
("la ciudad","Stadt"),("el pueblo","Dorf"),("la calle","Straße"),("el parque","Park"),
("el día","Tag"),("la noche","Nacht"),("la semana","Woche"),("el mes","Monat"),
("el año","Jahr"),("el tiempo","Zeit/Wetter"),("la hora","Stunde"),
("hoy","heute"),("mañana","morgen"),("ayer","gestern"),
("ser","sein permanent"),("estar","sein Ort/Zustand"),("tener","haben"),
("hacer","machen"),("ir","gehen"),("venir","kommen"),("querer","wollen"),
("poder","können"),("deber","müssen"),("decir","sagen"),("ver","sehen"),
("saber","wissen"),("conocer","kennen"),("tomar","nehmen"),("dar","geben"),
("hablar","sprechen"),("comprender","verstehen"),("aprender","lernen"),
("amar","lieben"),("pensar","denken"),("creer","glauben"),
("grande","groß"),("pequeño","klein"),("bueno","gut"),("malo","schlecht"),
("bonito","schön"),("nuevo","neu"),("viejo","alt"),("joven","jung"),
("primero","erster"),("último","letzter"),("mismo","selbe"),("otro","anderer"),
("pero","aber"),("porque","weil"),("muy","sehr"),("mucho","viel"),
("poco","wenig"),("más","mehr"),("menos","weniger"),("con","mit"),
("sin","ohne"),("para","für Zweck"),("por","für Grund/durch"),("en","in"),
("sobre","auf"),("debajo","unter"),("delante","vor"),("detrás","hinter"),
("aquí","hier"),("allí","dort"),("dónde","wo"),("cuándo","wann"),
("cómo","wie"),("por qué","warum"),("cuánto","wie viel"),
("rojo","rot"),("azul","blau"),("verde","grün"),("amarillo","gelb"),
("negro","schwarz"),("blanco","weiß"),("uno dos tres","1 2 3"),
("cien","100"),("mil","1000"),("siempre","immer"),("nunca","nie"),
("ya","schon"),("todavía","noch"),("bien","gut"),("mal","schlecht"),
("rápido","schnell"),("lento","langsam")
],

"Italienisch": [
("ciao","hallo/tschüss"),("grazie","danke"),("per favore","bitte"),
("sì","ja"),("no","nein"),("scusa","entschuldigung"),
("l'uomo","Mann"),("la donna","Frau"),("il ragazzo","Junge"),("la ragazza","Mädchen"),
("il bambino","Kind"),("l'amico","Freund"),("la famiglia","Familie"),("il padre","Vater"),
("la madre","Mutter"),("il fratello","Bruder"),("la sorella","Schwester"),
("la scuola","Schule"),("il libro","Buch"),("il professore","Lehrer"),
("l'alunno","Schüler"),("la classe","Klasse"),("la penna","Stift"),
("il tavolo","Tisch"),("la sedia","Stuhl"),("la porta","Tür"),("la finestra","Fenster"),
("il pane","Brot"),("l'acqua","Wasser"),("il latte","Milch"),("il formaggio","Käse"),
("la carne","Fleisch"),("il pesce","Fisch"),("la mela","Apfel"),
("mangiare","essen"),("bere","trinken"),("dormire","schlafen"),
("la casa","Haus"),("la camera","Zimmer"),("la cucina","Küche"),
("la macchina","Auto"),("il treno","Zug"),("l'aereo","Flugzeug"),
("la città","Stadt"),("il paese","Dorf"),("la strada","Straße"),("il parco","Park"),
("il giorno","Tag"),("la notte","Nacht"),("la settimana","Woche"),("il mese","Monat"),
("l'anno","Jahr"),("il tempo","Zeit/Wetter"),("l'ora","Stunde"),
("oggi","heute"),("domani","morgen"),("ieri","gestern"),
("essere","sein"),("avere","haben"),("fare","machen"),("andare","gehen"),
("venire","kommen"),("volere","wollen"),("potere","können"),("dovere","müssen"),
("dire","sagen"),("vedere","sehen"),("sapere","wissen"),("conoscere","kennen"),
("prendere","nehmen"),("dare","geben"),("mettere","legen"),
("parlare","sprechen"),("capire","verstehen"),("imparare","lernen"),
("amare","lieben"),("pensare","denken"),("credere","glauben"),
("grande","groß"),("piccolo","klein"),("buono","gut"),("cattivo","schlecht"),
("bello","schön"),("nuovo","neu"),("vecchio","alt"),("giovane","jung"),
("primo","erster"),("ultimo","letzter"),("stesso","selbe"),("altro","anderer"),
("ma","aber"),("perché","weil"),("molto","sehr/viel"),("poco","wenig"),
("più","mehr"),("meno","weniger"),("con","mit"),("senza","ohne"),
("per","für"),("in","in"),("su","auf"),("sotto","unter"),
("davanti","vor"),("dietro","hinter"),("qui","hier"),("lì","dort"),
("dove","wo"),("quando","wann"),("come","wie"),("quanto","wie viel"),
("rosso","rot"),("blu","blau"),("verde","grün"),("giallo","gelb"),
("nero","schwarz"),("bianco","weiß"),("uno due tre","1 2 3"),
("cento","100"),("mille","1000"),("sempre","immer"),("mai","nie"),
("già","schon"),("ancora","noch"),("bene","gut"),("male","schlecht"),
("veloce","schnell"),("lento","langsam"),("ci","dort(=y)"),("ne","davon(=en)")
],

"Latein": [
("esse","sein"),("habere","haben"),("dicere","sagen"),("facere","machen"),
("videre","sehen"),("audire","hören"),("ire","gehen"),("venire","kommen"),
("dare","geben"),("capere","nehmen"),("amare","lieben"),("laudare","loben"),
("pugnare","kämpfen"),("vincere","siegen"),("putare","glauben"),
("scire","wissen"),("velle","wollen"),("posse","können"),("debere","müssen"),
("homo","Mensch"),("vir","Mann"),("femina","Frau"),("puer","Junge"),
("puella","Mädchen"),("liberi","Kinder"),("amicus","Freund"),("familia","Familie"),
("pater","Vater"),("mater","Mutter"),("frater","Bruder"),("soror","Schwester"),
("schola","Schule"),("liber","Buch"),("magister","Lehrer"),("discipulus","Schüler"),
("mensa","Tisch"),("sella","Stuhl"),("ianua","Tür"),("fenestra","Fenster"),
("panis","Brot"),("aqua","Wasser"),("lac","Milch"),("caseus","Käse"),
("caro","Fleisch"),("piscis","Fisch"),("malum","Apfel"),
("edere","essen"),("bibere","trinken"),("dormire","schlafen"),
("domus","Haus"),("cubiculum","Zimmer"),("culina","Küche"),
("currus","Wagen/Auto"),("urbs","Stadt"),("vicus","Dorf"),("via","Straße"),
("dies","Tag"),("nox","Nacht"),("septimana","Woche"),("mensis","Monat"),
("annus","Jahr"),("tempus","Zeit"),("hora","Stunde"),
("hodie","heute"),("cras","morgen"),("heri","gestern"),
("magnus","groß"),("parvus","klein"),("bonus","gut"),("malus","schlecht"),
("pulcher","schön"),("novus","neu"),("vetus","alt"),("iuvenis","jung"),
("primus","erster"),("ultimus","letzter"),("idem","selbe"),("alius","anderer"),
("et","und"),("sed","aber"),("quia","weil"),("valde","sehr"),("multum","viel"),
("paulum","wenig"),("plus","mehr"),("minus","weniger"),("cum","mit"),
("sine","ohne"),("pro","für"),("in","in"),("super","auf"),("sub","unter"),
("ante","vor"),("post","hinter"),("hic","hier"),("ibi","dort"),("ubi","wo"),
("quando","wann"),("quomodo","wie"),("cur","warum"),("quot","wie viel"),
("ruber","rot"),("caeruleus","blau"),("viridis","grün"),("flavus","gelb"),
("niger","schwarz"),("albus","weiß"),("unus duo tres","1 2 3"),
("centum","100"),("mille","1000"),("semper","immer"),("numquam","nie"),
("iam","schon"),("adhuc","noch"),("bene","gut"),("male","schlecht"),
("celeriter","schnell"),("lente","langsam"),("rex","König"),("bellum","Krieg")
]
}

if st.button("Start"):
    st.write("---")
    if "VOKABELN" in thema:
        if sprache == "Deutsch":
            st.write("Deutsch hat keine Vokabeln - nur Grammatik!")
            st.write("Konjunktiv I: er sei, er habe, er solle kommen")
            st.write("Nebensatz Verb am Ende!")
        else:
            liste = vokabeln.get(sprache, [])
            kat = st.selectbox("Kategorie:", ["Alle","Begrüßung","Leute","Schule","Essen","Haus","Zeit","Verben","Adjektive","Wichtiges"])
            # Filter einfach: zeige alle, aber mit Überschrift
            for fremd, deutsch in liste:
                st.write(f"**{fremd}** = {deutsch}")
            st.write(f"--- {len(liste)} Vokabeln total")

    elif "QUIZ" in thema:
        if sprache == "Deutsch":
            st.write("Kein Vokabelquiz für Deutsch!")
        else:
            liste = vokabeln.get(sprache, [])
            w, l = random.choice(liste)
            st.session_state.quiz_wort = w
            st.session_state.quiz_loesung = l
            st.session_state.quiz_sprache = sprache
            st.subheader(f"QUIZ {sprache}")
            st.write(f"Was heißt: **{w}** ?")
            st.write(f"Score: {st.session_state.score}")

    else:
        st.subheader(f"{sprache} Grammatik")
        if sprache == "Französisch":
            st.write("Pronomen: le la lui y en VOR Verb")
            st.write("Direkte Rede: Il dit qu'il est malade")
            st.write("Futur: parlerai serai aurai irai")
        elif sprache == "Spanisch":
            st.write("lo le Unterschied, Se lo doy, ser vs estar, por vs para")
            st.write("Indirekte Rede: Dijo que estaba enfermo")
            st.write("Futur hablare, Subjuntivo quiero que hables")
        elif sprache == "Italienisch":
            st.write("lo gli glielo, ci=dort(y) ne=davon(en)")
            st.write("Ci vado = J'y vais, Essere vs Stare")
        elif sprache == "Latein":
            st.write("AcI Dicit Gallos venire, Kasus, Deklinationen")
        else:
            st.write("Konjunktiv I: Er sagt, er sei krank")
            st.write("Verb am Ende im Nebensatz")

# QUIZ INPUT
if st.session_state.quiz_wort and "QUIZ" in thema and sprache != "Deutsch":
    antwort = st.text_input(f"Übersetzung für {st.session_state.quiz_wort}:", key="ans")
    if st.button("Prüfen"):
        richtig = st.session_state.quiz_loesung.lower()
        if antwort.lower().strip() in richtig or richtig in antwort.lower().strip():
            st.success(f"Richtig! {st.session_state.quiz_wort} = {st.session_state.quiz_loesung}")
            st.session_state.score += 1
        else:
            st.error(f"Falsch! {st.session_state.quiz_wort} = {st.session_state.quiz_loesung}")
        liste = vokabeln.get(st.session_state.quiz_sprache, [])
        w, l = random.choice(liste)
        st.session_state.quiz_wort = w
        st.session_state.quiz_loesung = l
        st.write(f"Neues Wort: **{w}**")

st.caption("v12.0 500 Vokabeln + Quiz")
