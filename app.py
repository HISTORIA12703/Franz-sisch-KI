import streamlit as st, requests, urllib.parse, random, time
st.set_page_config(page_title="LernBox Pro - Alle Fächer", page_icon="📚", layout="wide")

st.markdown("""
<style>
.stButton>button {width:100%;border-radius:12px;height:3em;font-weight:bold;white-space:normal;}
.vok-card {background:#f0f8ff;padding:10px;border-radius:10px;margin:4px 0;border-left:4px solid #2E86AB;}
.test-card {background:#fff8e1;padding:15px;border-radius:12px;border:3px solid #ff9800;margin-top:10px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center;color:#2E86AB;">📚 LernBox Pro - 50+ Themen 🚀</h1>', unsafe_allow_html=True)

@st.cache_data(ttl=3600)
def wiki(q):
    try:
        enc=urllib.parse.quote(q.replace(" ","_"))
        r=requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers={'User-Agent':'LernBox'}, timeout=3)
        if r.status_code==200:
            j=r.json()
            if j.get("extract"): return j.get("extract")[:500], j.get("content_urls",{}).get("desktop",{}).get("page","")
    except: pass
    return "",""

# VOKABELN 20 PRO LEKTION
VOKABELN = {
"Französisch": {
    "L1 Familie 20": [("la famille","die Familie"),("le père","der Vater"),("la mère","die Mutter"),("le frère","der Bruder"),("la soeur","die Schwester"),("le grand-père","der Opa"),("la grand-mère","die Oma"),("l'enfant","das Kind"),("le bébé","das Baby"),("le cousin","der Cousin"),("la cousine","die Cousine"),("l'oncle","der Onkel"),("la tante","die Tante"),("le mari","der Ehemann"),("la femme","die Ehefrau"),("le pain","das Brot"),("la pomme","der Apfel"),("l'eau","das Wasser"),("la maison","das Haus"),("la porte","die Tür")],
    "L2 Schule 20": [("l'école","die Schule"),("le professeur","der Lehrer"),("l'élève","der Schüler"),("le cours","der Unterricht"),("le livre","das Buch"),("le cahier","das Heft"),("le stylo","der Stift"),("le crayon","der Bleistift"),("la gomme","der Radiergummi"),("la matière","das Fach"),("les devoirs","die Hausaufgaben"),("l'examen","die Prüfung"),("la note","die Note"),("le tableau","die Tafel"),("la règle","das Lineal"),("apprendre","lernen"),("enseigner","lehren"),("lire","lesen"),("écrire","schreiben"),("compter","zählen")],
    "L3 Verben 20": [("aller","gehen"),("venir","kommen"),("faire","machen"),("dire","sagen"),("voir","sehen"),("vouloir","wollen"),("pouvoir","können"),("prendre","nehmen"),("donner","geben"),("manger","essen"),("boire","trinken"),("dormir","schlafen"),("travailler","arbeiten"),("aimer","lieben"),("habiter","wohnen"),("être","sein"),("avoir","haben"),("devenir","werden"),("rester","bleiben"),("trouver","finden")],
    "L4 Alltag 20": [("parler","sprechen"),("écouter","zuhören"),("comprendre","verstehen"),("penser","denken"),("croire","glauben"),("savoir","wissen"),("connaître","kennen"),("le temps","die Zeit"),("la vie","das Leben"),("le jour","der Tag"),("la nuit","die Nacht"),("la table","der Tisch"),("la chaise","der Stuhl"),("la fenêtre","das Fenster"),("la voiture","das Auto"),("le travail","die Arbeit"),("l'argent","das Geld"),("l'heure","die Uhrzeit"),("le monde","die Welt"),("l'ami","der Freund")],
    "L5 Adjektive 20": [("bon","gut"),("mauvais","schlecht"),("grand","groß"),("petit","klein"),("beau","schön"),("nouveau","neu"),("vieux","alt"),("jeune","jung"),("facile","leicht"),("difficile","schwer"),("gentil","nett"),("heureux","glücklich"),("triste","traurig"),("ici","hier"),("là","dort"),("maintenant","jetzt"),("toujours","immer"),("beaucoup","viel"),("très","sehr"),("bien","gut")],
},
"Spanisch": {
    "L1 Familie 20": [("la familia","die Familie"),("el padre","der Vater"),("la madre","die Mutter"),("el hermano","der Bruder"),("la hermana","die Schwester"),("el abuelo","der Opa"),("la abuela","die Oma"),("el niño","das Kind"),("el bebé","das Baby"),("el primo","der Cousin"),("la prima","die Cousine"),("el tío","der Onkel"),("la tía","die Tante"),("el marido","der Ehemann"),("la mujer","die Ehefrau"),("el pan","das Brot"),("la manzana","der Apfel"),("el agua","das Wasser"),("la casa","das Haus"),("la puerta","die Tür")],
    "L2 Schule 20": [("la escuela","die Schule"),("el profesor","der Lehrer"),("el alumno","der Schüler"),("el curso","der Kurs"),("el libro","das Buch"),("el cuaderno","das Heft"),("el bolígrafo","der Stift"),("el lápiz","der Bleistift"),("la goma","der Radiergummi"),("la materia","das Fach"),("los deberes","die Hausaufgaben"),("el examen","die Prüfung"),("la nota","die Note"),("la pizarra","die Tafel"),("la regla","das Lineal"),("aprender","lernen"),("enseñar","lehren"),("leer","lesen"),("escribir","schreiben"),("contar","zählen")],
    "L3 Verben 20": [("ir","gehen"),("venir","kommen"),("hacer","machen"),("decir","sagen"),("ver","sehen"),("querer","wollen"),("poder","können"),("tomar","nehmen"),("dar","geben"),("comer","essen"),("beber","trinken"),("dormir","schlafen"),("trabajar","arbeiten"),("amar","lieben"),("vivir","wohnen/leben"),("ser","sein permanent"),("estar","sein Ort/Zustand"),("tener","haben"),("haber","haben Hilfsverb"),("necesitar","brauchen")],
    "L4 Alltag 20": [("hablar","sprechen"),("escuchar","zuhören"),("comprender","verstehen"),("pensar","denken"),("creer","glauben"),("saber","wissen"),("conocer","kennen"),("el tiempo","die Zeit"),("la vida","das Leben"),("el día","der Tag"),("la noche","die Nacht"),("la mesa","der Tisch"),("la silla","der Stuhl"),("la ventana","das Fenster"),("el coche","das Auto"),("el trabajo","die Arbeit"),("el dinero","das Geld"),("la hora","die Uhrzeit"),("el mundo","die Welt"),("el amigo","der Freund")],
    "L5 Adjektive 20": [("bueno","gut"),("malo","schlecht"),("grande","groß"),("pequeño","klein"),("hermoso","schön"),("nuevo","neu"),("viejo","alt"),("joven","jung"),("fácil","leicht"),("difícil","schwer"),("amable","nett"),("feliz","glücklich"),("triste","traurig"),("aquí","hier"),("allí","dort"),("ahora","jetzt"),("siempre","immer"),("mucho","viel"),("muy","sehr"),("bien","gut")],
},
"Englisch": {
    "L1 Familie 20": [("family","die Familie"),("father","der Vater"),("mother","die Mutter"),("brother","der Bruder"),("sister","die Schwester"),("grandfather","der Opa"),("grandmother","die Oma"),("child","das Kind"),("baby","das Baby"),("cousin","der Cousin"),("uncle","der Onkel"),("aunt","die Tante"),("husband","der Ehemann"),("wife","die Ehefrau"),("friend","der Freund"),("bread","das Brot"),("apple","der Apfel"),("water","das Wasser"),("house","das Haus"),("door","die Tür")],
    "L2 Schule 20": [("school","die Schule"),("teacher","der Lehrer"),("pupil","der Schüler"),("course","der Kurs"),("book","das Buch"),("exercise book","das Heft"),("pen","der Stift"),("pencil","der Bleistift"),("rubber","der Radiergummi"),("subject","das Fach"),("homework","die Hausaufgaben"),("exam","die Prüfung"),("mark","die Note"),("blackboard","die Tafel"),("ruler","das Lineal"),("to learn","lernen"),("to teach","lehren"),("to read","lesen"),("to write","schreiben"),("to count","zählen")],
    "L3 Verben 20": [("to go","gehen"),("to come","kommen"),("to make","machen"),("to say","sagen"),("to see","sehen"),("to want","wollen"),("can","können"),("to take","nehmen"),("to give","geben"),("to eat","essen"),("to drink","trinken"),("to sleep","schlafen"),("to work","arbeiten"),("to love","lieben"),("to live","wohnen/leben"),("to be","sein"),("to have","haben"),("to become","werden"),("to stay","bleiben"),("to find","finden")],
    "L4 Alltag 20": [("to speak","sprechen"),("to listen","zuhören"),("to understand","verstehen"),("to think","denken"),("to believe","glauben"),("to know","wissen"),("time","die Zeit"),("life","das Leben"),("day","der Tag"),("night","die Nacht"),("table","der Tisch"),("chair","der Stuhl"),("window","das Fenster"),("car","das Auto"),("work","die Arbeit"),("money","das Geld"),("clock","die Uhrzeit"),("world","die Welt"),("city","die Stadt"),("street","die Straße")],
    "L5 Adjektive 20": [("good","gut"),("bad","schlecht"),("big","groß"),("small","klein"),("beautiful","schön"),("new","neu"),("old","alt"),("young","jung"),("easy","leicht"),("difficult","schwer"),("nice","nett"),("happy","glücklich"),("sad","traurig"),("here","hier"),("there","dort"),("now","jetzt"),("always","immer"),("much","viel"),("very","sehr"),("well","gut")],
},
}

THEMEN = {
"Französisch": {
    "LE LA LUI LEUR": {"t":"LE/LA direkt ohne à: Je LE vois / LUI/LEUR indirekt mit à: Je LUI parle à Paul","q":[["Je LE vois Paul?","LE direkt","LUI indirekt"],["Je LUI parle?","LUI mit à","LE ohne à"],["Je LEUR parle?","LEUR plural","LUI singular"]]},
    "Y EN": {"t":"Y=dort Ort: J'Y vais / EN=davon Zahl: J'EN ai 3 + Teil: du pain -> EN","q":[["J'Y vais Paris?","Y Ort","EN davon"],["J'EN ai 3?","EN Zahl","Y Ort"],["Du pain -> J'EN veux?","EN","Y"]]},
    "Reihenfolge Pronomen": {"t":"me te se nous vous + le la les + lui leur + y + en + Verb","q":[["Il ME LE donne richtig?","JA","NEIN"],["Il LE LUI donne?","JA le+lui","NEIN lui+le"]]},
    "Passé Composé": {"t":"avoir/être + Partizip: J'ai mangé, Je suis allé. être bei Bewegung","q":[["J'ai mangé Hilfsverb?","avoir","être"],["Je suis allé?","être Bewegung","avoir"]]},
    "Subjonctif": {"t":"Nach il faut que, je veux que, bien que -> Subjonctif: Il faut que tu viennes","q":[["Il faut que tu ___?","viennes Subjonctif","viens Indikativ"]]},
},
"Spanisch": {
    "SE LO DOY": {"t":"LE+LO = SE LO DOY! Nie Le lo! Les+los=SE LOS","q":[["Le lo doy richtig?","FALSCH Le lo geht nicht","RICHTIG"],["SE LO DOY?","JA richtig","NEIN"],["Les+los?","SE LOS","Les los"]]},
    "SER ESTAR": {"t":"SER permanent: Soy Juan, Es grande / ESTAR Ort Zustand: Estoy en casa, estoy cansado","q":[["Soy Juan?","SER permanent","ESTAR Zustand"],["Estoy en casa?","ESTAR Ort","SER"],["Estoy cansado müde?","ESTAR Zustand","SER"]]},
    "POR PARA": {"t":"POR Grund Durch Dank: Gracias POR, por la mañana / PARA Ziel Zweck: Para comer, para ti","q":[["Gracias POR?","POR Grund","PARA Ziel"],["Para comer Zweck?","PARA","POR"],["Por la mañana?","POR Zeit","PARA"]]},
    "Pretérito Indefinido": {"t":"Einmalige Vergangenheit: Ayer comí, fui, hablé","q":[["Ayer comí Zeit?","Indefinido einmalig","Imperfecto gewohnt"]]},
    "Subjuntivo": {"t":"Nach quiero que, es importante que -> Subjuntivo","q":[["Quiero que vengas?","Subjuntivo","Indicativo"]]},
},
"Geschichte": {
    "Französische Revolution": {"t":"14.7.1789 Bastille, 1793 Ludwig XVI geköpft, 1799-1815 Napoleon","q":[["Bastille?","14.7.1789","1793"],["Ludwig geköpft?","1793","1789"],["Napoleon Kaiser?","1804","1789"]]},
    "Industrialisierung": {"t":"1769 Watt Dampfmaschine, 1835 erste deutsche Bahn Nürnberg-Fürth, 1871 Krupp","q":[["Dampfmaschine?","Watt 1769","1835"],["Erste Bahn DE?","1835 Nürnberg-Fürth","1871"]]},
    "Kaiserreich 1871-1918": {"t":"18.1.1871 Gründung Versailles, Wilhelm I, Bismarck Kanzler, 3 Kriege","q":[["Gründung Kaiserreich?","18.1.1871","1848"],["Bismarck war?","Kanzler","Kaiser"]]},
    "1. Weltkrieg": {"t":"28.6.1914 Sarajevo Franz Ferdinand, 1914-18 Schützengraben, 11.11.18 Waffenstillstand","q":[["Beginn?","1914","1939"],["Sarajevo Attentat?","28.6.1914","1.9.39"],["Ende?","11.11.1918","8.5.45"]]},
    "Weimar 1919-33": {"t":"1919 Verfassung, 1923 Inflation, 1929 Weltwirtschaftskrise, 1933 Hitler","q":[["Verfassung Weimar?","1919","1933"],["Inflation?","1923","1929"]]},
    "NS & 2.WK": {"t":"30.1.33 Hitler Macht, Reichstagsbrand 1933, 1.9.39 Polen, D-Day 6.6.44, 8.5.45 Ende, Holocaust 6 Mio","q":[["Hitler Macht?","30.1.1933","1.9.39"],["Beginn 2.WK?","1.9.1939","1914"],["D-Day?","6.6.1944","1.9.39"],["Ende 2.WK?","8.5.1945","1918"],["Holocaust Opfer?","6 Mio Juden","1 Mio"]]},
    "DDR BRD Mauer": {"t":"1949 BRD DDR, 13.8.61 Mauerbau, 9.11.89 Mauerfall, 3.10.90 Wiedervereinigung, 28 Jahre Mauer","q":[["Mauerbau?","13.8.1961","9.11.89"],["Mauerfall?","9.11.1989","13.8.61"],["Wiedervereinigung?","3.10.1990","9.11.89"],["Wie lange Mauer?","28 Jahre","10 Jahre"],["BRD DDR Gründung?","1949","1945"]]},
    "Antike": {"t":"753 v.Chr. Rom Gründung, 500 v.Chr. Demokratie Athen, 44 v.Chr. Caesar ermordet, 476 Untergang Westrom","q":[["Rom Gründung?","753 v.Chr.","44 v.Chr."],["Caesar tot?","44 v.Chr.","476"]]},
    "Mittelalter Entdeckungen": {"t":"800 Karl Kaiser, 1096 Kreuzzüge, 1492 Kolumbus Amerika, 1517 Luther 95 Thesen, 1519 Magellan Welt","q":[["Kolumbus?","1492","1517"],["Luther?","1517","1492"],["Karl Kaiser?","800","1492"],["Kreuzzüge Beginn?","1096","1492"]]},
},
"Physik": {
    "Mechanik": {"t":"v=s/t, 100km/h=27,8m/s, a=F/m, Freier Fall s=0,5*g*t² g=9,81","q":[["100km/h=?","27,8 m/s","100 m/s"],["Freier Fall Formel?","0,5*g*t²","v=s/t"],["g=?","9,81","10"]]},
    "Kraft Newton": {"t":"F=m*a, 70kg=686N Gewicht, Actio=Reactio, Trägheit","q":[["F=?","m*a","m*g"],["70kg Gewicht?","686N","70N"],["Actio=Reactio?","3.Newton","1.Newton"]]},
    "Strom": {"t":"R=U/I, I=U/R, 12V 3Ω=4A, Reihe R1+R2, Parallel 1/R=1/R1+1/R2, P=U*I 230V*10A=2300W","q":[["12V 3Ω I=?","4A","36A"],["Reihe 2+3Ω=?","5Ω","1Ω"],["Parallel 2//2=?","1Ω","4Ω"],["P bei 230V 10A?","2300W","230W"]]},
    "Energie": {"t":"kinetisch 0,5*m*v², potentiell m*g*h, 1kWh=3,6Mio Joule, Energieerhaltung","q":[["0,5*m*v²=?","kinetisch","potentiell"],["m*g*h=?","potentiell","kinetisch"],["1kWh=?","3,6 Mio J","3600 J"]]},
    "Optik": {"t":"Einfall=Ausfall Reflexion, Brechung, Linse, Licht c=300.000km/s","q":[["Einfall=Ausfall?","Reflexion","Brechung"],["Licht c=?","300.000 km/s","300 km/s"]]},
    "Kernphysik": {"t":"E=mc², Uran 235 spaltet, Kernspaltung, Fusion Sonne, Halbwertszeit","q":[["E=mc² wer?","Einstein","Newton"],["Uran spaltet?","Kernspaltung","Fusion"]]},
    "Wellen": {"t":"v=f*λ, Schall 343m/s Luft, Licht Welle+Teilchen","q":[["Schall Luft?","343 m/s","300.000 km/s"],["v=f*λ?","Wellenformel","Kraft"]]},
},
"Mathe": {
    "Brüche": {"t":"1/4+2/4=3/4, 1/2=0,5, Hauptnenner, kürzen","q":[["1/4+2/4=?","3/4","3/8"],["1/2=?","0,5","0,2"]]},
    "Prozent": {"t":"% = /100, 50%=0,5, Dreisatz","q":[["50% von 200=?","100","50"],["20%=?","0,2","20"]]},
    "Pythagoras": {"t":"a²+b²=c² rechtwinklig, c Hypotenuse","q":[["a²+b²=?","c²","a²"],["c ist?","Hypotenuse","Kathete"]]},
    "Gleichungen": {"t":"2x+4=10 => x=3, Mitternachtsformel x=-b±√(b²-4ac)/2a","q":[["2x+4=10 x=?","3","5"],["Mitternacht?","-b±√...","a²+b²"]]},
    "Funktionen": {"t":"y=mx+b Gerade, Parabel y=x², Steigung m","q":[["y=mx+b ist?","Gerade","Parabel"]]},
    "Wahrscheinlich": {"t":"P= günstig/möglich, Würfel 1/6, 50% Münze","q":[["Würfel 6?","1/6","6/1"],["Münze Kopf?","50%","1/6"]]},
},
"Biologie": {
    "Zelle": {"t":"Tier/Pflanze Zelle, Zellkern, Mitochondrien Kraftwerk, Photosynthese Chloroplast","q":[["Kraftwerk Zelle?","Mitochondrien","Zellkern"],["Photosynthese wo?","Chloroplast","Mitochondrien"]]},
    "Genetik": {"t":"DNA Doppelhelix, Gene, Mendel Erbsen, dominant rezessiv, 46 Chromosomen Mensch","q":[["DNA Form?","Doppelhelix","Einzel"],["Chromosomen Mensch?","46","23"],["Mendel was?","Erbsen","Fliegen"]]},
    "Evolution": {"t":"Darwin 1859, Selektion, Survival of fittest, Mutation","q":[["Darwin Jahr?","1859","1492"],["Selektion?","Auslese","Mutation"]]},
    "Ökologie": {"t":"Nahrungskette, Produzent Konsument, Fotosynthese CO2+Wasser->Zucker+O2","q":[["Fotosynthese Produkt?","Zucker+O2","CO2"],["Produzent?","Pflanze","Tier"]]},
    "Mensch": {"t":"Herz 4 Kammern, Blutkreislauf, Lunge, Gehirn 86Mrd Neuronen","q":[["Herz Kammern?","4","2"],["Neuronen?","86 Mrd","1 Mio"]]},
},
"Chemie": {
    "Atome": {"t":"Proton+ Neutron Kern, Elektron Hülle, Ordnungszahl=Protonen, Periodensystem","q":[["Kern besteht aus?","Proton+Neutron","Elektron"],["Ordnungszahl=?","Protonen","Neutronen"]]},
    "Periodensystem": {"t":"118 Elemente, H Wasserstoff 1, O Sauerstoff 8, Metalle links, Nichtmetalle rechts","q":[["H Ordnungszahl?","1","8"],["Wie viele Elemente?","118","100"]]},
    "Bindungen": {"t":"Ionen Metall+Nichtmetall, kovalent Nichtmetall+Nichtmetall teilen Elektronen, Metallbindung","q":[["Ionenbindung?","Metall+Nichtmetall","Nichtmetall+Nichtmetall"]]},
    "Reaktionen": {"t":"Säure+Base=Salz+Wasser, pH 0-14 sauer 7 neutral 14 basisch, Oxidation","q":[["pH 7?","neutral","sauer"],["Säure+Base=?","Salz+Wasser","Säure"]]},
    "Organisch": {"t":"C-H Kohlenwasserstoff, Methan CH4, Ethan, Benzin, Alkohol OH","q":[["Methan?","CH4","CO2"],["Organisch Basis?","C-H","H2O"]]},
},
"Deutsch": {
    "Grammatik Fälle": {"t":"Nom Wer? Gen Wessen? Dat Wem? Akk Wen? Der des dem den","q":[["Wessen?","Genitiv","Dativ"],["Wem?","Dativ","Akkusativ"]]},
    "Zeiten": {"t":"Präsens ich gehe, Präteritum ich ging, Perfekt ich bin gegangen, Plusquam ich war gegangen, Futur ich werde gehen","q":[["ich ging?","Präteritum","Perfekt"],["ich bin gegangen?","Perfekt","Präteritum"]]},
    "Satzglieder": {"t":"Subjekt Wer? Prädikat Was tut? Objekt Wen? Wem? Adverbial Wie Wo Wann?","q":[["Wer?","Subjekt","Objekt"],["Was tut?","Prädikat","Subjekt"]]},
    "Rechtschreibung": {"t":"das/dass: das Haus, ich weiß, dass... Seid ihr? Seit 2020. Groß klein Nomen groß","q":[["das Haus?","Artikel das","dass mit ss"],["Ich weiß, dass?","dass ss","das s"]]},
    "Literatur": {"t":"Ballade, Drama, Epik, Lyrik, Goethe Faust, Schiller Glocke","q":[["Faust wer?","Goethe","Schiller"],["Drama ist?","Theaterstück","Gedicht"]]},
},
"Geographie": {
    "Deutschland": {"t":"16 Bundesländer, Hauptstadt Berlin, 83 Mio, Nachbarn 9 Länder","q":[["Wie viele Bundesländer?","16","9"],["Hauptstadt?","Berlin","München"],["Nachbarn?","9 Länder","16"]]},
    "Europa": {"t":"44 Länder, EU 27, Europarat, Alpen, Donau 2850km","q":[["EU wie viele?","27","44"],["Donau Länge?","2850km","1000km"]]},
    "Klima": {"t":"Tropen Äquator heiß feucht, Subtropen, gemäßigt DE, polar kalt, Klimawandel CO2","q":[["Äquator Klima?","Tropen heiß feucht","polar"],["Klimawandel Grund?","CO2","O2"]]},
    "Platten": {"t":"Tektonik Platten bewegen, Erdbeben, Vulkane Ring of Fire, Kontinentaldrift","q":[["Erdbeben Grund?","Platten Tektonik","Wind"],["Ring of Fire?","Vulkane Pazifik","Europa"]]},
},
}

# SUCHE
st.markdown("### 🔍 Suche - Alles durchsuchen")
s_glob = st.text_input("", placeholder="z.B. Mauer, pain, Newton, Photosynthese, 1914, dass...", label_visibility="collapsed")
if s_glob:
    s_low=s_glob.lower()
    txt,link=wiki(s_glob)
    if txt:
        with st.expander(f"🌐 Wikipedia: {s_glob}", expanded=True):
            st.write(txt)
            if link: st.markdown(f"[Wikipedia]({link})")
    count=0
    for fach in VOKABELN:
        for lek,lst in VOKABELN[fach].items():
            for f,d in lst:
                if s_low in f.lower() or s_low in d.lower():
                    st.markdown(f'<div class="vok-card"><b>{fach} {lek}:</b> {f} = {d}</div>', unsafe_allow_html=True)
                    count+=1
    for fach,themen in THEMEN.items():
        for tname,data in themen.items():
            if s_low in tname.lower() or s_low in data["t"].lower():
                with st.expander(f"📖 {fach}: {tname}"):
                    st.info(data["t"])
                    count+=1
    if count==0: st.warning(f"Nichts für '{s_glob}'")

st.write("---")
if 'xp' not in st.session_state: st.session_state['xp']=0
st.progress(min(st.session_state['xp']/200,1.0), text=f"⭐ XP: {st.session_state['xp']} - Level {st.session_state['xp']//50+1}")

st.markdown("### 📚 Alle Fächer")
cols=st.columns(4)
alle=list(VOKABELN.keys())+["Geschichte","Physik","Mathe","Biologie","Chemie","Deutsch","Geographie"]
alle=list(dict.fromkeys(alle))
for i,fach in enumerate(alle):
    if cols[i%4].button(fach, key=f"f_{fach}"):
        st.session_state['fach']=fach
        for k in ['lek','thema','vok_idx']: st.session_state.pop(k,None)

if 'fach' in st.session_state:
    fach=st.session_state['fach']
    st.write("---")
    st.markdown(f"## 📖 {fach}")
    fs=st.text_input(f"🔍 In {fach} filtern", placeholder="", key=f"fs_{fach}")

    if fach in VOKABELN:
        leks=list(VOKABELN[fach].keys())
        if fs:
            fs_low=fs.lower()
            leks=[l for l in leks if fs_low in l.lower() or any(fs_low in f.lower() or fs_low in d.lower() for f,d in VOKABELN[fach][l])]
        lc=st.columns(5)
        for j,lek in enumerate(leks):
            if lc[j%5].button(lek, key=f"lek_{fach}_{lek}"):
                st.session_state['lek']=lek; st.session_state['vok_test']=False
        if 'lek' in st.session_state and st.session_state['lek'] in VOKABELN[fach]:
            lek=st.session_state['lek']; lst=VOKABELN[fach][lek]
            if fs:
                fs_low=fs.lower(); lst=[(f,d) for f,d in lst if fs_low in f.lower() or fs_low in d.lower()]
            with st.expander(f"📝 {lek} - {len(lst)} Vokabeln", expanded=True):
                for f,d in lst:
                    st.markdown(f'<div class="vok-card"><b>{f}</b> = {d}</div>', unsafe_allow_html=True)
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Test {lek}")
            if st.button(f"▶️ 20 Fragen Test", key=f"t20_{fach}_{lek}", use_container_width=True):
                st.session_state['vok_test']=True; st.session_state['vok_fragen']=random.sample(lst, min(20,len(lst))); st.session_state['vok_idx']=0; st.session_state['vok_score']=0
            if st.session_state.get('vok_test'):
                fragen=st.session_state.get('vok_fragen',[]); idx=st.session_state.get('vok_idx',0); score=st.session_state.get('vok_score',0)
                if idx < len(fragen):
                    st.progress(idx/len(fragen), text=f"{idx+1}/{len(fragen)} Score {score}")
                    orig_f, orig_d = fragen[idx]
                    # Richtung abwechselnd
                    if idx%2==0:
                        st.markdown(f"### Was heißt **{orig_f}**?")
                        falsche=[d for _,d in lst if d!=orig_d]; opts=[orig_d]+random.sample(falsche, min(3,len(falsche))); random.shuffle(opts); correct=orig_d
                    else:
                        st.markdown(f"### Wie heißt **{orig_d}** auf {fach}?")
                        falsche=[f for f,_ in lst if f!=orig_f]; opts=[orig_f]+random.sample(falsche, min(3,len(falsche))); random.shuffle(opts); correct=orig_f
                    c1,c2=st.columns(2)
                    for i,opt in enumerate(opts):
                        if c1.button(opt, key=f"a1_{fach}_{lek}_{idx}_{i}") if i<2 else c2.button(opt, key=f"a2_{fach}_{lek}_{idx}_{i}"):
                            if opt==correct:
                                st.success(f"✅ {orig_f} = {orig_d} 🎉"); st.balloons(); st.session_state['vok_score']=score+1; st.session_state['xp']+=5
                            else:
                                st.error(f"❌ Richtig: {orig_f} = {orig_d}")
                            st.session_state['vok_idx']=idx+1; time.sleep(0.8); st.rerun()
                else:
                    st.markdown(f"### 🏁 {score}/{len(fragen)}")
                    if score==len(fragen): st.balloons(); st.snow(); st.success("🌟 PERFEKT! +20 XP"); st.session_state['xp']+=20
                    elif score>=len(fragen)*0.8: st.success(f"🎉 {score}/{len(fragen)} +10 XP"); st.balloons(); st.session_state['xp']+=10
                    else: st.warning(f"{score}/{len(fragen)}")
                    if st.button("🔄 Nochmal", key=f"again_{fach}_{lek}"): st.session_state['vok_fragen']=random.sample(lst, min(20,len(lst))); st.session_state['vok_idx']=0; st.session_state['vok_score']=0; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button(f"🔥 GESAMTTEST {fach} 100 - 20 Fragen", key=f"ges_{fach}", use_container_width=True):
                alle_v=[]
                for l in VOKABELN[fach].values(): alle_v.extend(l)
                st.session_state['lek']="GESAMTTEST 100"; st.session_state['vok_test']=True; st.session_state['vok_fragen']=random.sample(alle_v,20); st.session_state['vok_idx']=0; st.session_state['vok_score']=0; st.rerun()

    if fach in THEMEN:
        th=THEMEN[fach]
        if fs:
            fs_low=fs.lower(); th={k:v for k,v in th.items() if fs_low in k.lower() or fs_low in v["t"].lower()}
        st.markdown(f"### 📖 {fach} - {len(th)} Themen")
        tc=st.columns(3)
        for j,tname in enumerate(th.keys()):
            if tc[j%3].button(tname, key=f"th_{fach}_{tname}"):
                st.session_state['thema']=tname
        if 'thema' in st.session_state and st.session_state['thema'] in th:
            tname=st.session_state['thema']; d=th[tname]
            st.write("---")
            st.info(f"**{tname}:** {d['t']}")
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Test {tname} - {len(d['q'])} Fragen")
            for qi,(fr,ri,fa) in enumerate(d["q"]):
                st.write(f"**{qi+1}. {fr}**")
                if f"done_{fach}_{tname}_{qi}" not in st.session_state:
                    c1,c2=st.columns(2)
                    if c1.button(ri, key=f"q1_{fach}_{tname}_{qi}", use_container_width=True):
                        st.session_state[f"done_{fach}_{tname}_{qi}"]=True; st.session_state[f"res_{fach}_{tname}_{qi}"]=True; st.session_state['xp']+=3; st.rerun()
                    if c2.button(fa, key=f"q2_{fach}_{tname}_{qi}", use_container_width=True):
                        st.session_state[f"done_{fach}_{tname}_{qi}"]=True; st.session_state[f"res_{fach}_{tname}_{qi}"]=False; st.rerun()
                else:
                    if st.session_state.get(f"res_{fach}_{tname}_{qi}"):
                        st.success(f"✅ {ri} 🎉")
                    else:
                        st.error(f"❌ Richtig: {ri}")
            st.markdown('</div>', unsafe_allow_html=True)

    if st.button("❌ Schließen", use_container_width=True):
        for k in list(st.session_state.keys()):
            if k!='xp': del st.session_state[k]
        st.rerun()
