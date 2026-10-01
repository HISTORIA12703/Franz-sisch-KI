import streamlit as st, requests, urllib.parse, random, time

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")
st.markdown('<h1 style="text-align:center;color:#2E86AB;">📚 Lern App - 20 pro Lektion + Tests 🎉</h1>', unsafe_allow_html=True)

def wiki(q):
    try:
        enc=urllib.parse.quote(q.replace(" ","_"))
        r=requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers={'User-Agent':'LernApp'}, timeout=3)
        if r.status_code==200: return r.json().get("extract","")
    except: pass
    return ""

# 100 VOKABELN = 5 LEKTIONEN À 20 PRO SPRACHE
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
    "L3 Verben 20": [("ir","gehen"),("venir","kommen"),("hacer","machen"),("decir","sagen"),("ver","sehen"),("querer","wollen"),("poder","können"),("tomar","nehmen"),("dar","geben"),("comer","essen"),("beber","trinken"),("dormir","schlafen"),("trabajar","arbeiten"),("amar","lieben"),("vivir","wohnen/leben"),("ser","sein permanent"),("estar","sein Ort/Zustand"),("tener","haben"),("haber","haben Hilfsverb"),("hacer","machen")],
    "L4 Alltag 20": [("hablar","sprechen"),("escuchar","zuhören"),("comprender","verstehen"),("pensar","denken"),("creer","glauben"),("saber","wissen"),("conocer","kennen"),("el tiempo","die Zeit"),("la vida","das Leben"),("el día","der Tag"),("la noche","die Nacht"),("la mesa","der Tisch"),("la silla","der Stuhl"),("la ventana","das Fenster"),("el coche","das Auto"),("el trabajo","die Arbeit"),("el dinero","das Geld"),("la hora","die Uhrzeit"),("el mundo","die Welt"),("el amigo","der Freund")],
    "L5 Adjektive 20": [("bueno","gut"),("malo","schlecht"),("grande","groß"),("pequeño","klein"),("hermoso","schön"),("nuevo","neu"),("viejo","alt"),("joven","jung"),("fácil","leicht"),("difícil","schwer"),("amable","nett"),("feliz","glücklich"),("triste","traurig"),("aquí","hier"),("allí","dort"),("ahora","jetzt"),("siempre","immer"),("mucho","viel"),("muy","sehr"),("bien","gut")],
},
"Italienisch": {
    "L1 Familie 20": [("la famiglia","die Familie"),("il padre","der Vater"),("la madre","die Mutter"),("il fratello","der Bruder"),("la sorella","die Schwester"),("il nonno","der Opa"),("la nonna","die Oma"),("il bambino","das Kind"),("il bebè","das Baby"),("il cugino","der Cousin"),("la cugina","die Cousine"),("lo zio","der Onkel"),("la zia","die Tante"),("il marito","der Ehemann"),("la moglie","die Ehefrau"),("il pane","das Brot"),("la mela","der Apfel"),("l'acqua","das Wasser"),("la casa","das Haus"),("la porta","die Tür")],
    "L2 Schule 20": [("la scuola","die Schule"),("il professore","der Lehrer"),("l'alunno","der Schüler"),("il corso","der Kurs"),("il libro","das Buch"),("il quaderno","das Heft"),("la penna","der Stift"),("la matita","der Bleistift"),("la gomma","der Radiergummi"),("la materia","das Fach"),("i compiti","die Hausaufgaben"),("l'esame","die Prüfung"),("il voto","die Note"),("la lavagna","die Tafel"),("il righello","das Lineal"),("imparare","lernen"),("insegnare","lehren"),("leggere","lesen"),("scrivere","schreiben"),("contare","zählen")],
    "L3 Verben 20": [("andare","gehen"),("venire","kommen"),("fare","machen"),("dire","sagen"),("vedere","sehen"),("volere","wollen"),("potere","können"),("prendere","nehmen"),("dare","geben"),("mangiare","essen"),("bere","trinken"),("dormire","schlafen"),("lavorare","arbeiten"),("amare","lieben"),("abitare","wohnen"),("essere","sein permanent"),("stare","sein Ort/Zustand"),("avere","haben"),("diventare","werden"),("restare","bleiben")],
    "L4 Alltag 20": [("parlare","sprechen"),("ascoltare","zuhören"),("capire","verstehen"),("pensare","denken"),("credere","glauben"),("sapere","wissen"),("conoscere","kennen"),("il tempo","die Zeit"),("la vita","das Leben"),("il giorno","der Tag"),("la notte","die Nacht"),("il tavolo","der Tisch"),("la sedia","der Stuhl"),("la finestra","das Fenster"),("la macchina","das Auto"),("il lavoro","die Arbeit"),("i soldi","das Geld"),("l'ora","die Uhrzeit"),("il mondo","die Welt"),("l'amico","der Freund")],
    "L5 Adjektive 20": [("buono","gut"),("cattivo","schlecht"),("grande","groß"),("piccolo","klein"),("bello","schön"),("nuovo","neu"),("vecchio","alt"),("giovane","jung"),("facile","leicht"),("difficile","schwer"),("gentile","nett"),("felice","glücklich"),("triste","traurig"),("qui","hier"),("là","dort"),("ora","jetzt"),("sempre","immer"),("molto","viel"),("molto","sehr"),("bene","gut")],
},
"Latein": {
    "L1 Familie 20": [("familia","die Familie"),("pater","der Vater"),("mater","die Mutter"),("frater","der Bruder"),("soror","die Schwester"),("avus","der Opa"),("avia","die Oma"),("liberi","die Kinder"),("infans","das Baby"),("consobrinus","der Cousin"),("consobrina","die Cousine"),("avunculus","der Onkel"),("amita","die Tante"),("maritus","der Ehemann"),("uxor","die Ehefrau"),("panis","das Brot"),("malum","der Apfel"),("aqua","das Wasser"),("casa","das Haus"),("porta","die Tür")],
    "L2 Schule 20": [("schola","die Schule"),("magister","der Lehrer"),("discipulus","der Schüler"),("cursus","der Kurs"),("liber","das Buch"),("tabula","die Tafel"),("stilus","der Stift"),("materia","das Fach"),("pensum","die Hausaufgabe"),("examen","die Prüfung"),("nota","die Note"),("regula","das Lineal"),("gummi","der Radiergummi"),("discere","lernen"),("docere","lehren"),("legere","lesen"),("scribere","schreiben"),("numerare","zählen"),("loqui","sprechen"),("audire","zuhören")],
    "L3 Verben 20": [("ire","gehen"),("venire","kommen"),("facere","machen"),("dicere","sagen"),("videre","sehen"),("velle","wollen"),("posse","können"),("capere","nehmen"),("dare","geben"),("edere","essen"),("bibere","trinken"),("dormire","schlafen"),("laborare","arbeiten"),("amare","lieben"),("habitare","wohnen"),("esse","sein"),("habere","haben"),("fieri","werden"),("manere","bleiben"),("invenire","finden")],
    "L4 Alltag 20": [("intellegere","verstehen"),("putare","denken"),("credere","glauben"),("scire","wissen"),("noscere","kennen"),("tempus","die Zeit"),("vita","das Leben"),("dies","der Tag"),("nox","die Nacht"),("mensa","der Tisch"),("sella","der Stuhl"),("fenestra","das Fenster"),("currus","das Auto/Wagen"),("labor","die Arbeit"),("pecunia","das Geld"),("hora","die Uhrzeit"),("mundus","die Welt"),("amicus","der Freund"),("domus","das Haus"),("urbs","die Stadt")],
    "L5 Adjektive 20": [("bonus","gut"),("malus","schlecht"),("magnus","groß"),("parvus","klein"),("pulcher","schön"),("novus","neu"),("vetus","alt"),("iuvenis","jung"),("facilis","leicht"),("difficilis","schwer"),("benignus","nett"),("felix","glücklich"),("tristis","traurig"),("hic","hier"),("illic","dort"),("nunc","jetzt"),("semper","immer"),("multus","viel"),("valde","sehr"),("bene","gut")],
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
"Französisch": {"le la lui leur": {"t":"LE direkt LUI indirekt mit a","q":[["Je LE mange","LE direkt","LUI indirekt"],["Je LUI parle","LUI mit a","LE ohne a"],["Je LEUR parle","LEUR","LUI"],["Je LES vois","LES","LEUR"],["Je LA vois","LA","LUI"],["Je LE vois Paul","LE","LUI"]]},"y en": {"t":"Y dort Ort EN davon Zahl","q":[["J'Y vais Paris","Y","EN"],["J'EN ai 3 Zahl","EN","Y"],["J'EN veux du pain","EN","Y"]]},"Reihenfolge": {"t":"me te se nous vous + le la les + lui leur + y + en + Verb","q":[["Il ME LE donne","JA","NEIN"]]},"indirekte Rede": {"t":"Il dit qu'il EST bleibt Präsens Il a dit qu'il ÉTAIT Present->Imparfait","q":[["Il dit qu'il EST bleibt?","JA Präsens bleibt","NEIN wird ÉTAIT"]]}},
"Spanisch": {"se lo doy SE": {"t":"LE+LO=SE LO DOY nie Le lo!","q":[["Le lo doy?","FALSCH","RICHTIG"],["SE LO DOY richtig?","JA","NEIN"],["SE LOS DOY?","Les+los=SE LOS","Les los"]]},"ser estar": {"t":"SER permanent ESTAR Ort Zustand gerade","q":[["Soy Juan","SER","ESTAR"],["Estoy en casa Ort","ESTAR","SER"],["Estoy cansado Zustand","ESTAR","SER"],["Son las 3 Zeit","SER","ESTAR"]]},"por para": {"t":"POR Grund Durch Dauer PARA Ziel Zweck","q":[["Gracias POR","POR Grund","PARA Ziel"],["Para comer Zweck","PARA","POR"]]}},
"Italienisch": {"lo gli ci ne": {"t":"LO ihn Vedo LIBRO->LO GLI ihm Parlo GIOVANNI->GLI CI dort Vado Parigi->CI NE davon Voglio pane->NE","q":[["Vedo IL LIBRO -> __","LO","GLI"],["Parlo A GIOVANNI -> __","GLI","LO"],["Vado A Parigi -> __","CI","NE"],["Voglio DEL pane -> __","NE","CI"]]},"essere stare glielo": {"t":"Glielo do=ich gebe es ihm Sono Giovanni permanent Sto a casa Ort Sto mangiando gerade","q":[["Glielo do=?","ich gebe es ihm","ich bin dort"],["Sono Giovanni=?","ESSERE","STARE"],["Sto a casa=?","STARE Ort","ESSERE"]]}},
"Latein": {"Kasus 5": {"t":"Nom Wer? Gen Wessen? Dat Wem? Akk Wen? Abl Womit?","q":[["Wessen?","Genitiv","Nominativ"],["puellam?","Akkusativ","Nominativ"],["cum puella?","Ablativ","Akkusativ"]]},"Deklinationen 1-5": {"t":"1.a puella puellae 2.o servus servi 3.rex regis 4.u fructus 5.e res rei","q":[["puella Gen?","puellae","puellam"],["rex Gen?","regis","rex"]]},"AcI Gerundium": {"t":"Dico eum venire Ich sage dass er kommt amans liebend amatus geliebt","q":[["Dico eum venire=?","Ich sage dass er kommt","Ich komme"]]}},
"Physik": {"Mechanik": {"t":"v=s/t 100km/h=27,8m/s Freier Fall s=0,5*g*t²","q":[["100km/h=?","27,8 m/s","100 m/s"]]},"Newton": {"t":"F=m*a 70kg=686N Actio=Reactio","q":[["F=?","m*a","m*g"],["70kg Gewicht?","686N","70N"]]},"Strom": {"t":"R=U/I 12V 3Ω 4A Reihe 2+3=5Ω Parallel 2//2=1Ω P=U*I 2300W","q":[["12V 3Ω I=?","4A","36A"],["Reihe 2+3=?","5Ω","1Ω"],["Parallel 2//2=?","1Ω","4Ω"]]},"Energie Optik Kern": {"t":"0,5*m*v² kinetisch m*g*h potentiell Einfall=Ausfall E=mc² Uran","q":[["0,5*m*v²=?","kinetisch","potentiell"],["Einfall=Ausfall=?","Reflexion","Brechung"]]}},
"Mathe": {"Brüche Prozent": {"t":"1/4+2/4=3/4 %= /100","q":[["1/4+2/4=?","3/4","3/8"]]},"Pythagoras": {"t":"a²+b²=c²","q":[["a²+b²=?","c²","a²"]]},"Gleichungen": {"t":"2x+4=10 x=3 Mitternacht","q":[["2x+4=10 x=?","3","5"]]}},
"Geschichte": {"franz rev": {"t":"1789 Bastille 14.7. 1793 Ludwig geköpft","q":[["Bastille wann?","14.7.1789","1789"]]},"1WK 2WK Mauer": {"t":"1914-18 Sarajevo 1939-45 Holocaust 6Mio Mauer 13.8.61-9.11.89 28J 3.10.90","q":[["Mauerbau?","13.8.61","1989"],["Mauer wie lange?","28J","10J"],["Beginn 2WK?","1.9.39","1914"]]}},
}

# Suche global
s_glob = st.text_input("🔍 Suche Vokabeln + Bedeutung + Themen", placeholder="")
if s_glob:
    s=s_glob.lower()
    w=wiki(s_glob)
    if w: st.info(f"🌐 {w[:400]}...")
    for fach in VOKABELN:
        for lek, lst in VOKABELN[fach].items():
            for f,d in lst:
                if s in f.lower() or s in d.lower():
                    st.write(f"**{fach} {lek}:** {f} = {d}")

st.write("---")
st.markdown("### 📖 Fächer wählen")
cols=st.columns(4)
faecher=list(VOKABELN.keys())+list(THEMEN.keys())
# uniq
seen=[]
faecher_u=[]
for f in faecher:
    if f not in seen:
        faecher_u.append(f); seen.append(f)
faecher_u=list(VOKABELN.keys())+["Physik","Mathe","Geschichte"]

for i,fach in enumerate(faecher_u):
    if cols[i%4].button(fach, key=f"f_{fach}"):
        st.session_state['fach']=fach
        st.session_state.pop('lek',None); st.session_state.pop('thema',None)

if 'fach' in st.session_state:
    fach=st.session_state['fach']
    st.write("---")
    st.markdown(f"## 📚 {fach}")

    fs = st.text_input(f"🔍 In {fach} suchen", placeholder="", key=f"fs_{fach}")

    if fach in VOKABELN:
        st.markdown(f"### 📝 Vokabeln - 5 Lektionen à 20 = 100 Vokabeln")
        leks=list(VOKABELN[fach].keys())
        if fs:
            leks=[l for l in leks if fs.lower() in l.lower() or any(fs.lower() in f.lower() or fs.lower() in d.lower() for f,d in VOKABELN[fach][l])]

        lc=st.columns(3)
        for j,lek in enumerate(leks):
            if lc[j%3].button(lek, key=f"lek_{fach}_{lek}"):
                st.session_state['lek']=lek
                st.session_state['vok_test']=False

        if 'lek' in st.session_state and st.session_state['lek'] in VOKABELN[fach]:
            lek=st.session_state['lek']
            lst=VOKABELN[fach][lek]
            if fs:
                lst=[(f,d) for f,d in lst if fs.lower() in f.lower() or fs.lower() in d.lower()]

            st.write("---")
            st.markdown(f"### {lek} - {len(lst)} Vokabeln mit Bedeutung")
            # Tabelle
            for f,d in lst:
                c1,c2=st.columns([1,1])
                c1.write(f"**{f}**"); c2.write(f"= {d}")

            st.write("---")
            st.markdown('<div style="background:#fff8e1;padding:15px;border:3px solid #ff9800;border-radius:12px;">', unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Vokabel-Test {lek} - 20 Fragen möglich")

            if st.button(f"🎯 Test starten {lek}", key=f"start_{fach}_{lek}"):
                st.session_state['vok_test']=True
                st.session_state['vok_fragen']=random.sample(lst, min(20, len(lst)))
                st.session_state['vok_idx']=0; st.session_state['vok_score']=0

            if st.session_state.get('vok_test'):
                fragen=st.session_state.get('vok_fragen',[])
                idx=st.session_state.get('vok_idx',0)
                score=st.session_state.get('vok_score',0)
                if idx < len(fragen):
                    fremd,deutsch=fragen[idx]
                    # Richtung zufällig
                    if random.random()>0.5:
                        st.write(f"**{idx+1}/{len(fragen)}: Was heißt '{fremd}'?**")
                        falsche=[d for _,d in lst if d!=deutsch]
                        opts=[deutsch]+random.sample(falsche, min(3,len(falsche)))
                        random.shuffle(opts); opts=["---"]+opts
                        ans=st.radio("", opts, key=f"vq_{fach}_{lek}_{idx}", label_visibility="collapsed")
                        if ans!="---":
                            if ans==deutsch:
                                st.success(f"✅ {fremd} = {deutsch} 🎉"); st.balloons()
                                st.session_state['vok_score']=score+1
                            else:
                                st.error(f"❌ Richtig: {fremd} = {deutsch}")
                            st.session_state['vok_idx']=idx+1; time.sleep(0.7); st.rerun()
                    else:
                        st.write(f"**{idx+1}/{len(fragen)}: Wie heißt '{deutsch}' auf {fach}?**")
                        falsche=[f for f,_ in lst if f!=fremd]
                        opts=[fremd]+random.sample(falsche, min(3,len(falsche)))
                        random.shuffle(opts); opts=["---"]+opts
                        ans=st.radio("", opts, key=f"vq2_{fach}_{lek}_{idx}", label_visibility="collapsed")
                        if ans!="---":
                            if ans==fremd:
                                st.success(f"✅ {deutsch} = {fremd} 🎉"); st.balloons()
                                st.session_state['vok_score']=score+1
                            else:
                                st.error(f"❌ Richtig: {deutsch} = {fremd}")
                            st.session_state['vok_idx']=idx+1; time.sleep(0.7); st.rerun()
                else:
                    st.markdown(f"### 🏆 {score}/{len(fragen)}")
                    if score==len(fragen): st.balloons(); st.snow(); st.success("🌟 PERFEKT! Alle 20 richtig!")
                    elif score>=16: st.balloons(); st.success(f"🎉 Sehr gut {score}/20!")
                    else: st.warning(f"{score}/20 - nochmal üben!")
                    if st.button("🔄 Nochmal", key=f"again_{fach}_{lek}"):
                        st.session_state['vok_fragen']=random.sample(lst, min(20,len(lst))); st.session_state['vok_idx']=0; st.session_state['vok_score']=0; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

            # GESAMTTEST 100 Vokabeln
            st.write("---")
            if st.button(f"🏆 GESAMTTEST {fach} - 100 Vokabeln - 20 Fragen", key=f"gesamt_{fach}"):
                alle=[]
                for l in VOKABELN[fach].values(): alle.extend(l)
                st.session_state['lek']=f"GESAMTTEST {fach}"
                st.session_state['vok_test']=True
                st.session_state['vok_fragen']=random.sample(alle, 20)
                st.session_state['vok_idx']=0; st.session_state['vok_score']=0
                st.rerun()

    # Grammatik Themen + Tests
    if fach in THEMEN or fach in ["Physik","Mathe","Geschichte"]:
        th=THEMEN.get(fach, {})
        if fach=="Physik": th=THEMEN["Physik"]
        if fach=="Mathe": th=THEMEN["Mathe"]
        if fach=="Geschichte": th=THEMEN["Geschichte"]
        if fs and th:
            th={k:v for k,v in th.items() if fs.lower() in k.lower() or fs.lower() in v["t"].lower()}

        st.markdown(f"### 📖 Mehr Themen - {fach} mit Tests")
        tc=st.columns(2)
        for j, tname in enumerate(th.keys()):
            if tc[j%2].button(tname, key=f"th_{fach}_{tname}"):
                st.session_state['thema']=tname

        if 'thema' in st.session_state and st.session_state['thema'] in th:
            tname=st.session_state['thema']; d=th[tname]
            st.write("---")
            st.markdown(f"### {tname}")
            st.info(d["t"])
            st.markdown('<div style="background:#e3f2fd;padding:15px;border:3px solid #2196f3;border-radius:12px;">', unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Test zu {tname} - {len(d['q'])} Fragen")
            score_key=f"score_{fach}_{tname}"
            if score_key not in st.session_state: st.session_state[score_key]=0
            for qi,(fr,ri,fa) in enumerate(d["q"]):
                st.write(f"**{qi+1}. {fr}**")
                ans=st.radio("", ["---", ri, fa], key=f"tq_{fach}_{tname}_{qi}", label_visibility="collapsed")
                if ans!="---":
                    if ans==ri:
                        st.success(f"✅ Richtig! {ri} 🎉")
                        if f"done_{fach}_{tname}_{qi}" not in st.session_state:
                            st.balloons(); st.session_state[f"done_{fach}_{tname}_{qi}"]=True
                            st.session_state[score_key]+=1
                    else:
                        st.error(f"❌ Richtig: {ri}")
            st.write(f"**Score: {st.session_state.get(score_key,0)}/{len(d['q'])}**")
            st.markdown('</div>', unsafe_allow_html=True)

    if st.button("❌ Schließen"):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
