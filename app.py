import streamlit as st, requests, urllib.parse, random, time
st.set_page_config(page_title="LernBox Ultimate", page_icon="📚", layout="wide")
st.markdown('<h1 style="text-align:center;color:#2E86AB;">📚 LernBox Ultimate - 80+ Themen</h1>', unsafe_allow_html=True)
if 'xp' not in st.session_state: st.session_state['xp']=0

VOKABELN = {
"Französisch": {"L1 Familie 20": [("la famille","die Familie"),("le père","der Vater"),("la mère","die Mutter"),("le frère","der Bruder"),("la soeur","die Schwester"),("le grand-père","der Opa"),("la grand-mère","die Oma"),("l'enfant","das Kind"),("le bébé","das Baby"),("le cousin","der Cousin"),("la cousine","die Cousine"),("l'oncle","der Onkel"),("la tante","die Tante"),("le mari","der Ehemann"),("la femme","die Ehefrau"),("le pain","das Brot"),("la pomme","der Apfel"),("l'eau","das Wasser"),("la maison","das Haus"),("la porte","die Tür")],"L2 Schule 20": [("l'école","die Schule"),("le professeur","der Lehrer"),("l'élève","der Schüler"),("le cours","der Unterricht"),("le livre","das Buch"),("le cahier","das Heft"),("le stylo","der Stift"),("le crayon","der Bleistift"),("la gomme","der Radiergummi"),("la matière","das Fach"),("les devoirs","die Hausaufgaben"),("l'examen","die Prüfung"),("la note","die Note"),("le tableau","die Tafel"),("la règle","das Lineal"),("apprendre","lernen"),("enseigner","lehren"),("lire","lesen"),("écrire","schreiben"),("compter","zählen")],"L3 Verben 20": [("aller","gehen"),("venir","kommen"),("faire","machen"),("dire","sagen"),("voir","sehen"),("vouloir","wollen"),("pouvoir","können"),("prendre","nehmen"),("donner","geben"),("manger","essen"),("boire","trinken"),("dormir","schlafen"),("travailler","arbeiten"),("aimer","lieben"),("habiter","wohnen"),("être","sein"),("avoir","haben"),("devenir","werden"),("rester","bleiben"),("trouver","finden")],"L4 Alltag 20": [("parler","sprechen"),("écouter","zuhören"),("comprendre","verstehen"),("penser","denken"),("croire","glauben"),("savoir","wissen"),("connaître","kennen"),("le temps","die Zeit"),("la vie","das Leben"),("le jour","der Tag"),("la nuit","die Nacht"),("la table","der Tisch"),("la chaise","der Stuhl"),("la fenêtre","das Fenster"),("la voiture","das Auto"),("le travail","die Arbeit"),("l'argent","das Geld"),("l'heure","die Uhrzeit"),("le monde","die Welt"),("l'ami","der Freund")],"L5 Adjektive 20": [("bon","gut"),("mauvais","schlecht"),("grand","groß"),("petit","klein"),("beau","schön"),("nouveau","neu"),("vieux","alt"),("jeune","jung"),("facile","leicht"),("difficile","schwer"),("gentil","nett"),("heureux","glücklich"),("triste","traurig"),("ici","hier"),("là","dort"),("maintenant","jetzt"),("toujours","immer"),("beaucoup","viel"),("très","sehr"),("bien","gut")]},
"Englisch": {"L1 Familie 20": [("family","die Familie"),("father","der Vater"),("mother","die Mutter"),("brother","der Bruder"),("sister","die Schwester"),("grandfather","der Opa"),("grandmother","die Oma"),("child","das Kind"),("baby","das Baby"),("cousin","der Cousin"),("uncle","der Onkel"),("aunt","die Tante"),("husband","der Ehemann"),("wife","die Ehefrau"),("friend","der Freund"),("bread","das Brot"),("apple","der Apfel"),("water","das Wasser"),("house","das Haus"),("door","die Tür")],"L2 Schule 20": [("school","die Schule"),("teacher","der Lehrer"),("pupil","der Schüler"),("course","der Kurs"),("book","das Buch"),("exercise book","das Heft"),("pen","der Stift"),("pencil","der Bleistift"),("rubber","der Radiergummi"),("subject","das Fach"),("homework","die Hausaufgaben"),("exam","die Prüfung"),("mark","die Note"),("blackboard","die Tafel"),("ruler","das Lineal"),("to learn","lernen"),("to teach","lehren"),("to read","lesen"),("to write","schreiben"),("to count","zählen")],"L3 Verben 20": [("to go","gehen"),("to come","kommen"),("to make","machen"),("to say","sagen"),("to see","sehen"),("to want","wollen"),("can","können"),("to take","nehmen"),("to give","geben"),("to eat","essen"),("to drink","trinken"),("to sleep","schlafen"),("to work","arbeiten"),("to love","lieben"),("to live","wohnen"),("to be","sein"),("to have","haben"),("to become","werden"),("to stay","bleiben"),("to find","finden")],"L4 Alltag 20": [("to speak","sprechen"),("to listen","zuhören"),("to understand","verstehen"),("to think","denken"),("to believe","glauben"),("to know","wissen"),("time","die Zeit"),("life","das Leben"),("day","der Tag"),("night","die Nacht"),("table","der Tisch"),("chair","der Stuhl"),("window","das Fenster"),("car","das Auto"),("work","die Arbeit"),("money","das Geld"),("clock","die Uhrzeit"),("world","die Welt"),("city","die Stadt"),("street","die Straße")],"L5 Adjektive 20": [("good","gut"),("bad","schlecht"),("big","groß"),("small","klein"),("beautiful","schön"),("new","neu"),("old","alt"),("young","jung"),("easy","leicht"),("difficult","schwer"),("nice","nett"),("happy","glücklich"),("sad","traurig"),("here","hier"),("there","dort"),("now","jetzt"),("always","immer"),("much","viel"),("very","sehr"),("well","gut")]},
"Spanisch": {"L1 Familie 20": [("la familia","die Familie"),("el padre","der Vater"),("la madre","die Mutter"),("el hermano","der Bruder"),("la hermana","die Schwester"),("el abuelo","der Opa"),("la abuela","die Oma"),("el niño","das Kind"),("el bebé","das Baby"),("el primo","der Cousin"),("la prima","die Cousine"),("el tío","der Onkel"),("la tía","die Tante"),("el marido","der Ehemann"),("la mujer","die Ehefrau"),("el pan","das Brot"),("la manzana","der Apfel"),("el agua","das Wasser"),("la casa","das Haus"),("la puerta","die Tür")],"L2 Schule 20": [("la escuela","die Schule"),("el profesor","der Lehrer"),("el alumno","der Schüler"),("el curso","der Kurs"),("el libro","das Buch"),("el cuaderno","das Heft"),("el bolígrafo","der Stift"),("el lápiz","der Bleistift"),("la goma","der Radiergummi"),("la materia","das Fach"),("los deberes","die Hausaufgaben"),("el examen","die Prüfung"),("la nota","die Note"),("la pizarra","die Tafel"),("la regla","das Lineal"),("aprender","lernen"),("enseñar","lehren"),("leer","lesen"),("escribir","schreiben"),("contar","zählen")],"L3 Verben 20": [("ir","gehen"),("venir","kommen"),("hacer","machen"),("decir","sagen"),("ver","sehen"),("querer","wollen"),("poder","können"),("tomar","nehmen"),("dar","geben"),("comer","essen"),("beber","trinken"),("dormir","schlafen"),("trabajar","arbeiten"),("amar","lieben"),("vivir","wohnen"),("ser","sein perm."),("estar","sein Ort"),("tener","haben"),("haber","haben Hilf"),("necesitar","brauchen")],"L4 Alltag 20": [("hablar","sprechen"),("escuchar","zuhören"),("comprender","verstehen"),("pensar","denken"),("creer","glauben"),("saber","wissen"),("conocer","kennen"),("el tiempo","die Zeit"),("la vida","das Leben"),("el día","der Tag"),("la noche","die Nacht"),("la mesa","der Tisch"),("la silla","der Stuhl"),("la ventana","das Fenster"),("el coche","das Auto"),("el trabajo","die Arbeit"),("el dinero","das Geld"),("la hora","die Uhrzeit"),("el mundo","die Welt"),("el amigo","der Freund")],"L5 Adjektive 20": [("bueno","gut"),("malo","schlecht"),("grande","groß"),("pequeño","klein"),("hermoso","schön"),("nuevo","neu"),("viejo","alt"),("joven","jung"),("fácil","leicht"),("difícil","schwer"),("amable","nett"),("feliz","glücklich"),("triste","traurig"),("aquí","hier"),("allí","dort"),("ahora","jetzt"),("siempre","immer"),("mucho","viel"),("muy","sehr"),("bien","gut")]},
}

THEMEN = {
"Geschichte": {
"Franz. Revolution 1789": {"t":"14.7.1789 Bastille, 1793 Ludwig XVI geköpft, 1804 Napoleon Kaiser, 1815 Waterloo.","q":[["Bastille?","14.7.1789","1793"],["Ludwig geköpft?","1793","1789"]]},
"Industrialisierung": {"t":"1769 Watt Dampfmaschine, 1835 erste Bahn Nürnberg-Fürth.","q":[["Dampfmaschine?","Watt 1769","1835"],["Erste Bahn?","1835","1871"]]},
"Kaiserreich 1871": {"t":"18.1.1871 Versailles, Wilhelm I, Bismarck.","q":[["Gründung?","18.1.1871","1848"]]},
"1. WK 1914-18": {"t":"28.6.1914 Sarajevo Franz Ferdinand, 11.11.1918 Ende.","q":[["Beginn 1.WK?","1914","1939"],["Ende?","11.11.1918","8.5.45"]]},
"Weimar 1919-33": {"t":"1919 Verfassung, 1923 Inflation, 1929 Krise.","q":[["Weimar Verfassung?","1919","1933"]]},
"NS 1933-45": {"t":"30.1.33 Hitler Macht, Holocaust 6 Mio, 1935 Nürnberger, 1938 Kristallnacht.","q":[["Hitler Macht?","30.1.1933","1938"],["Holocaust?","6 Mio Juden","1 Mio"]]},
"2. WK 1939-45": {"t":"1.9.39 Polen, D-Day 6.6.44, 8.5.45 Ende DE, 60 Mio Tote.","q":[["Beginn 2.WK?","1.9.1939","1914"],["D-Day?","6.6.1944","1.9.39"],["Ende?","8.5.1945","1918"]]},
"Mauer 1961-89": {"t":"13.8.61 Mauerbau, 9.11.89 Mauerfall, 3.10.90 Wiedervereinigung, 28 Jahre.","q":[["Mauerbau?","13.8.1961","9.11.89"],["Mauerfall?","9.11.1989","1961"],["Wiedervereinigung?","3.10.1990","1989"]]},
"Antike": {"t":"753 v.Chr. Rom, 500 v.Chr. Demokratie Athen, 44 v.Chr. Caesar tot, 476 Untergang Westrom.","q":[["Rom Gründung?","753 v.Chr.","44 v.Chr."],["Caesar tot?","44 v.Chr.","476"]]},
"Mittelalter": {"t":"800 Karl Kaiser, 1096 Kreuzzüge, 1492 Kolumbus, 1517 Luther.","q":[["Kolumbus?","1492","1517"],["Luther?","1517","1492"],["Karl Kaiser?","800","1492"]]},
"Kalter Krieg": {"t":"1949 NATO, 1955 Warschauer Pakt, 1962 Kuba Krise, 1969 Mond.","q":[["NATO?","1949","1955"],["Kuba Krise?","1962","1949"]]},
"EU": {"t":"1957 Römische, 1993 EU, 2002 Euro, 27 Länder.","q":[["Euro Bargeld?","2002","1993"],["EU Länder?","27","44"]]},
},
"Physik": {
"Mechanik": {"t":"v=s/t, 100km/h=27,8m/s, g=9,81, Freier Fall s=0,5*g*t².","q":[["100km/h=?","27,8 m/s","100 m/s"]]},
"Newton": {"t":"F=m*a, 70kg=686N, Actio=Reactio.","q":[["F=?","m*a","m/v"],["70kg=?","686N","70N"]]},
"Strom": {"t":"R=U/I, 12V 3Ω=4A, Reihe 2+3=5Ω, Parallel 2//2=1Ω, P=U*I.","q":[["12V 3Ω I=?","4A","36A"],["Reihe 2+3=?","5Ω","1Ω"],["Parallel 2//2=?","1Ω","4Ω"]]},
"Energie": {"t":"kinetisch 0,5*m*v², potentiell m*g*h, 1kWh=3,6 Mio J.","q":[["0,5*m*v²=?","kinetisch","potentiell"]]},
"Optik": {"t":"Einfall=Ausfall Reflexion, c=300.000km/s.","q":[["Einfall=Ausfall?","Reflexion","Brechung"]]},
"Kern": {"t":"E=mc², Uran Spaltung, Sonne Fusion.","q":[["E=mc² wer?","Einstein","Newton"]]},
},
"Mathe": {
"Brüche": {"t":"1/4+2/4=3/4, 1/2=0,5.","q":[["1/4+2/4=?","3/4","3/8"]]},
"Prozent": {"t":"50%=0,5, 20% von 200=40.","q":[["50% von 200=?","100","50"]]},
"Pythagoras": {"t":"a²+b²=c², 3-4-5 Dreieck.","q":[["a²+b²=?","c²","a²"]]},
"Gleichungen": {"t":"2x+4=10 => x=3, Mitternacht -b±√.","q":[["2x+4=10?","3","5"]]},
"Funktionen": {"t":"y=mx+b Gerade.","q":[["y=mx+b ist?","Gerade","Parabel"]]},
"Wahrscheinlichkeit": {"t":"P=günstig/möglich, Würfel 1/6.","q":[["Würfel 6?","1/6","6/1"]]},
"Geometrie": {"t":"Kreis U=2πr A=πr², Quader V=a*b*c.","q":[["Kreis U=?","2πr","πr²"]]},
"Binom": {"t":"(a+b)²=a²+2ab+b².","q":[["(a+b)²=?","a²+2ab+b²","a²+b²"]]},
},
"Biologie": {
"Zelle": {"t":"Mitochondrien Kraftwerk, Chloroplast Fotosynthese, Fotosynthese CO2+H2O->Zucker+O2.","q":[["Kraftwerk?","Mitochondrien","Kern"]]},
"Genetik": {"t":"DNA Doppelhelix, 46 Chromosomen, Mendel Erbsen.","q":[["DNA?","Doppelhelix","Einzel"],["Chromosomen?","46","23"]]},
"Evolution": {"t":"Darwin 1859, Selektion.","q":[["Darwin?","1859","1492"]]},
"Ökologie": {"t":"Produzent Pflanze, Destruent Pilz.","q":[["Produzent?","Pflanze","Tier"]]},
"Mensch": {"t":"Herz 4 Kammern, 86 Mrd Neuronen, 206 Knochen.","q":[["Herz Kammern?","4","2"]]},
"Immun": {"t":"Antibiotika Bakterien, Impfung Antikörper.","q":[["Antibiotika gegen?","Bakterien","Virus"]]},
},
"Chemie": {
"Atome": {"t":"Proton+ Neutron Kern, Elektron Hülle, Ordnungszahl=Protonen.","q":[["Kern?","Proton+Neutron","Elektron"]]},
"Periodensystem": {"t":"118 Elemente, H 1, O 8, Au Gold 79.","q":[["H?","1","8"],["Au?","Gold","Silber"]]},
"Bindungen": {"t":"Ionen Metall+Nichtmetall NaCl, kovalent H2O teilen.","q":[["NaCl?","Ionen","kovalent"]]},
"Säure Base": {"t":"pH 7 neutral <7 sauer >7 basisch, Säure+Base=Salz+Wasser.","q":[["pH 7?","neutral","sauer"]]},
"Organisch": {"t":"C-H Basis, CH4 Methan, C2H5OH Alkohol.","q":[["Methan?","CH4","CO2"]]},
},
"Deutsch": {
"Fälle": {"t":"Wer? Nom, Wessen? Gen, Wem? Dat, Wen? Akk.","q":[["Wessen?","Genitiv","Dativ"]]},
"Zeiten": {"t":"ich ging Präteritum, ich bin gegangen Perfekt.","q":[["ich ging?","Präteritum","Perfekt"]]},
"Satzglieder": {"t":"Wer? Subjekt, Was tut? Prädikat, Wo? Adverbial.","q":[["Wer?","Subjekt","Objekt"]]},
"das dass": {"t":"das Haus Artikel, dass mit ss nach Komma: ich weiß, dass... seid ihr vs seit 2020.","q":[["das Haus?","Artikel das","dass ss"],["Ich weiß, dass?","dass ss","das"]]},
"Literatur": {"t":"Faust Goethe, Drama Theater, Ballade Gedicht.","q":[["Faust?","Goethe","Schiller"]]},
},
"Geographie": {
"Deutschland": {"t":"16 Bundesländer, Berlin Hauptstadt, 83 Mio, 9 Nachbarn.","q":[["Bundesländer?","16","9"]]},
"Europa": {"t":"EU 27, Wolga längst 3530km, Mont Blanc 4808m.","q":[["EU?","27","44"]]},
"Klima": {"t":"Tropen Äquator heiß, gemäßigt DE, polar kalt, CO2 Treibhaus.","q":[["Äquator?","Tropen","polar"]]},
"Platten": {"t":"Platten bewegen, Erdbeben Grenze, Ring of Fire Pazifik.","q":[["Erdbeben?","Platten","Wind"]]},
"Kontinente": {"t":"7 Kontinente Asien größter, 5 Ozeane Pazifik größter.","q":[["Größter Kontinent?","Asien","Europa"]]},
},
"Französisch Grammatik": {
"LE LUI": {"t":"LE direkt ohne à, LUI indirekt mit à: Je LUI parle à Paul.","q":[["Je LE vois?","LE direkt","LUI"]]},
"Y EN": {"t":"Y Ort J'Y vais, EN Zahl J'EN ai 3 + Teil du pain.","q":[["J'Y vais Paris?","Y Ort","EN"]]},
"Passé": {"t":"avoir/être + Partizip.","q":[["J'ai mangé?","avoir","être"]]},
},
}

# UI
suche=st.text_input("🔍 Suche", placeholder="Mauer, pain, Newton, DNA, 1914...")
if suche:
 s=suche.lower()
 for fach in VOKABELN:
  for lek,lst in VOKABELN[fach].items():
   for f,d in lst:
    if s in f.lower() or s in d.lower(): st.info(f"{fach} {lek}: {f} = {d}")
 for fach,themen in THEMEN.items():
  for tname,data in themen.items():
   if s in tname.lower() or s in data["t"].lower():
    with st.expander(f"{fach}: {tname} gefunden!", expanded=True): st.info(data["t"])

st.write("---")
st.progress(min(st.session_state['xp']/300,1.0), text=f"⭐ {st.session_state['xp']} XP - Level {st.session_state['xp']//50+1}")

st.markdown("### 📚 Fächer")
cols=st.columns(4)
fach_list=list(VOKABELN.keys())+list(THEMEN.keys())
fach_list=list(dict.fromkeys(fach_list))
for i,fach in enumerate(fach_list):
 if cols[i%4].button(fach, key=f"fb_{fach}", use_container_width=True): st.session_state['fach']=fach

if 'fach' in st.session_state:
 fach=st.session_state['fach']
 st.write("---")
 st.markdown(f"## {fach}")

 if fach in VOKABELN:
  for lek,lst in VOKABELN[fach].items():
   with st.expander(f"📝 {lek} - {len(lst)} Vokabeln"):
    for f,d in lst: st.write(f"**{f}** = {d}")
    if st.button(f"▶️ Test {lek}", key=f"t_{fach}_{lek}", use_container_width=True):
     st.session_state['q']=random.sample(lst,20); st.session_state['qi']=0; st.session_state['qs']=0

 if fach in THEMEN:
  st.markdown(f"### 📖 {len(THEMEN[fach])} Themen:")
  for tname,data in THEMEN[fach].items():
   with st.expander(f"📚 {tname}", expanded=True):
    st.info(data["t"])
    for idx,(fr,ri,fa) in enumerate(data["q"]):
     st.write(f"**{idx+1}. {fr}**")
     k=f"{fach}_{tname}_{idx}"
     if f"d_{k}" not in st.session_state:
      c1,c2=st.columns(2)
      if c1.button(ri, key=f"r_{k}", use_container_width=True): st.session_state[f"d_{k}"]=True; st.session_state[f"o_{k}"]=True; st.session_state['xp']+=3; st.rerun()
      if c2.button(fa, key=f"f_{k}", use_container_width=True): st.session_state[f"d_{k}"]=True; st.session_state[f"o_{k}"]=False; st.rerun()
     else:
      if st.session_state.get(f"o_{k}"): st.success(f"✅ {ri} 🎉")
      else: st.error(f"❌ Richtig: {ri}")

 if 'q' in st.session_state:
  qs=st.session_state['q']; qi=st.session_state['qi']; sc=st.session_state['qs']
  if qi < len(qs):
   st.markdown("---")
   st.markdown(f"### 🎯 Frage {qi+1}/{len(qs)} Score {sc}")
   st.progress(qi/len(qs))
   f,d=qs[qi]
   if qi%2==0:
    st.markdown(f"## Was heißt **{f}**?")
    allv=[];
    for v in VOKABELN[st.session_state.get('fach','Französisch')].values(): allv.extend(v)
    opts=[d]+random.sample([x[1] for x in allv if x[1]!=d],3); random.shuffle(opts); corr=d; orig=f"**{f}** = {d}"
   else:
    st.markdown(f"## Wie heißt **{d}**?")
    allv=[];
    for v in VOKABELN[st.session_state.get('fach','Französisch')].values(): allv.extend(v)
    opts=[f]+random.sample([x[0] for x in allv if x[0]!=f],3); random.shuffle(opts); corr=f; orig=f"**{f}** = {d}"
   c1,c2=st.columns(2)
   for i,o in enumerate(opts):
    if (c1.button(o, key=f"an_{qi}_{i}") if i<2 else c2.button(o, key=f"an_{qi}_{i}")):
     if o==corr: st.success(f"✅ {orig}"); st.balloons(); st.session_state['qs']=sc+1; st.session_state['xp']+=5
     else: st.error(f"❌ {orig}")
     st.session_state['qi']=qi+1; time.sleep(1); st.rerun()
  else:
   st.markdown(f"## 🏁 {sc}/{len(qs)}")
   if sc==len(qs): st.balloons(); st.snow(); st.success("🌟 PERFEKT! +20 XP"); st.session_state['xp']+=20
   elif sc>=len(qs)*0.8: st.success(f"🎉 {sc}/{len(qs)} +10 XP"); st.session_state['xp']+=10
   else: st.warning(f"{sc}/{len(qs)}")
   if st.button("🔄 Nochmal"): st.session_state['q']=random.sample(qs,20); st.session_state['qi']=0; st.session_state['qs']=0; st.rerun()
   if st.button("❌ Schließen"): del st.session_state['q']; st.rerun()

 if st.button("⬅️ Zurück"):
  for k in list(st.session_state.keys()):
   if k!='xp': del st.session_state[k]
  st.rerun()
