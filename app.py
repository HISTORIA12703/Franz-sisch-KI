import streamlit as st, requests, urllib.parse, random, time
st.set_page_config(page_title="LernBox Ultimate", page_icon="📚", layout="wide")
st.markdown('<h1 style="text-align:center;color:#2E86AB;">📚 LernBox Ultimate - 80+ Themen + 300 Vokabeln</h1>', unsafe_allow_html=True)

if 'xp' not in st.session_state: st.session_state['xp']=0

VOKABELN = {
"Französisch": {
 "L1 Familie 20": [("la famille","die Familie"),("le père","der Vater"),("la mère","die Mutter"),("le frère","der Bruder"),("la soeur","die Schwester"),("le grand-père","der Opa"),("la grand-mère","die Oma"),("l'enfant","das Kind"),("le bébé","das Baby"),("le cousin","der Cousin"),("la cousine","die Cousine"),("l'oncle","der Onkel"),("la tante","die Tante"),("le mari","der Ehemann"),("la femme","die Ehefrau"),("le pain","das Brot"),("la pomme","der Apfel"),("l'eau","das Wasser"),("la maison","das Haus"),("la porte","die Tür")],
 "L2 Schule 20": [("l'école","die Schule"),("le professeur","der Lehrer"),("l'élève","der Schüler"),("le cours","der Unterricht"),("le livre","das Buch"),("le cahier","das Heft"),("le stylo","der Stift"),("le crayon","der Bleistift"),("la gomme","der Radiergummi"),("la matière","das Fach"),("les devoirs","die Hausaufgaben"),("l'examen","die Prüfung"),("la note","die Note"),("le tableau","die Tafel"),("la règle","das Lineal"),("apprendre","lernen"),("enseigner","lehren"),("lire","lesen"),("écrire","schreiben"),("compter","zählen")],
 "L3 Verben 20": [("aller","gehen"),("venir","kommen"),("faire","machen"),("dire","sagen"),("voir","sehen"),("vouloir","wollen"),("pouvoir","können"),("prendre","nehmen"),("donner","geben"),("manger","essen"),("boire","trinken"),("dormir","schlafen"),("travailler","arbeiten"),("aimer","lieben"),("habiter","wohnen"),("être","sein"),("avoir","haben"),("devenir","werden"),("rester","bleiben"),("trouver","finden")],
 "L4 Alltag 20": [("parler","sprechen"),("écouter","zuhören"),("comprendre","verstehen"),("penser","denken"),("croire","glauben"),("savoir","wissen"),("connaître","kennen"),("le temps","die Zeit"),("la vie","das Leben"),("le jour","der Tag"),("la nuit","die Nacht"),("la table","der Tisch"),("la chaise","der Stuhl"),("la fenêtre","das Fenster"),("la voiture","das Auto"),("le travail","die Arbeit"),("l'argent","das Geld"),("l'heure","die Uhrzeit"),("le monde","die Welt"),("l'ami","der Freund")],
 "L5 Adjektive 20": [("bon","gut"),("mauvais","schlecht"),("grand","groß"),("petit","klein"),("beau","schön"),("nouveau","neu"),("vieux","alt"),("jeune","jung"),("facile","leicht"),("difficile","schwer"),("gentil","nett"),("heureux","glücklich"),("triste","traurig"),("ici","hier"),("là","dort"),("maintenant","jetzt"),("toujours","immer"),("beaucoup","viel"),("très","sehr"),("bien","gut")],
},
"Englisch": {
 "L1 Familie 20": [("family","die Familie"),("father","der Vater"),("mother","die Mutter"),("brother","der Bruder"),("sister","die Schwester"),("grandfather","der Opa"),("grandmother","die Oma"),("child","das Kind"),("baby","das Baby"),("cousin","der Cousin"),("uncle","der Onkel"),("aunt","die Tante"),("husband","der Ehemann"),("wife","die Ehefrau"),("friend","der Freund"),("bread","das Brot"),("apple","der Apfel"),("water","das Wasser"),("house","das Haus"),("door","die Tür")],
 "L2 Schule 20": [("school","die Schule"),("teacher","der Lehrer"),("pupil","der Schüler"),("course","der Kurs"),("book","das Buch"),("exercise book","das Heft"),("pen","der Stift"),("pencil","der Bleistift"),("rubber","der Radiergummi"),("subject","das Fach"),("homework","die Hausaufgaben"),("exam","die Prüfung"),("mark","die Note"),("blackboard","die Tafel"),("ruler","das Lineal"),("to learn","lernen"),("to teach","lehren"),("to read","lesen"),("to write","schreiben"),("to count","zählen")],
 "L3 Verben 20": [("to go","gehen"),("to come","kommen"),("to make","machen"),("to say","sagen"),("to see","sehen"),("to want","wollen"),("can","können"),("to take","nehmen"),("to give","geben"),("to eat","essen"),("to drink","trinken"),("to sleep","schlafen"),("to work","arbeiten"),("to love","lieben"),("to live","wohnen"),("to be","sein"),("to have","haben"),("to become","werden"),("to stay","bleiben"),("to find","finden")],
 "L4 Alltag 20": [("to speak","sprechen"),("to listen","zuhören"),("to understand","verstehen"),("to think","denken"),("to believe","glauben"),("to know","wissen"),("time","die Zeit"),("life","das Leben"),("day","der Tag"),("night","die Nacht"),("table","der Tisch"),("chair","der Stuhl"),("window","das Fenster"),("car","das Auto"),("work","die Arbeit"),("money","das Geld"),("clock","die Uhrzeit"),("world","die Welt"),("city","die Stadt"),("street","die Straße")],
 "L5 Adjektive 20": [("good","gut"),("bad","schlecht"),("big","groß"),("small","klein"),("beautiful","schön"),("new","neu"),("old","alt"),("young","jung"),("easy","leicht"),("difficult","schwer"),("nice","nett"),("happy","glücklich"),("sad","traurig"),("here","hier"),("there","dort"),("now","jetzt"),("always","immer"),("much","viel"),("very","sehr"),("well","gut")],
},
"Spanisch": {
 "L1 Familie 20": [("la familia","die Familie"),("el padre","der Vater"),("la madre","die Mutter"),("el hermano","der Bruder"),("la hermana","die Schwester"),("el abuelo","der Opa"),("la abuela","die Oma"),("el niño","das Kind"),("el bebé","das Baby"),("el primo","der Cousin"),("la prima","die Cousine"),("el tío","der Onkel"),("la tía","die Tante"),("el marido","der Ehemann"),("la mujer","die Ehefrau"),("el pan","das Brot"),("la manzana","der Apfel"),("el agua","das Wasser"),("la casa","das Haus"),("la puerta","die Tür")],
 "L2 Schule 20": [("la escuela","die Schule"),("el profesor","der Lehrer"),("el alumno","der Schüler"),("el curso","der Kurs"),("el libro","das Buch"),("el cuaderno","das Heft"),("el bolígrafo","der Stift"),("el lápiz","der Bleistift"),("la goma","der Radiergummi"),("la materia","das Fach"),("los deberes","die Hausaufgaben"),("el examen","die Prüfung"),("la nota","die Note"),("la pizarra","die Tafel"),("la regla","das Lineal"),("aprender","lernen"),("enseñar","lehren"),("leer","lesen"),("escribir","schreiben"),("contar","zählen")],
 "L3 Verben 20": [("ir","gehen"),("venir","kommen"),("hacer","machen"),("decir","sagen"),("ver","sehen"),("querer","wollen"),("poder","können"),("tomar","nehmen"),("dar","geben"),("comer","essen"),("beber","trinken"),("dormir","schlafen"),("trabajar","arbeiten"),("amar","lieben"),("vivir","wohnen"),("ser","sein perm."),("estar","sein Ort"),("tener","haben"),("haber","haben Hilf"),("necesitar","brauchen")],
 "L4 Alltag 20": [("hablar","sprechen"),("escuchar","zuhören"),("comprender","verstehen"),("pensar","denken"),("creer","glauben"),("saber","wissen"),("conocer","kennen"),("el tiempo","die Zeit"),("la vida","das Leben"),("el día","der Tag"),("la noche","die Nacht"),("la mesa","der Tisch"),("la silla","der Stuhl"),("la ventana","das Fenster"),("el coche","das Auto"),("el trabajo","die Arbeit"),("el dinero","das Geld"),("la hora","die Uhrzeit"),("el mundo","die Welt"),("el amigo","der Freund")],
 "L5 Adjektive 20": [("bueno","gut"),("malo","schlecht"),("grande","groß"),("pequeño","klein"),("hermoso","schön"),("nuevo","neu"),("viejo","alt"),("joven","jung"),("fácil","leicht"),("difícil","schwer"),("amable","nett"),("feliz","glücklich"),("triste","traurig"),("aquí","hier"),("allí","dort"),("ahora","jetzt"),("siempre","immer"),("mucho","viel"),("muy","sehr"),("bien","gut")],
},
}

THEMEN = {
"Französisch Grammatik": {
"LE LA LUI LEUR": {"t":"LE/LA direkt ohne à: Je LE vois Paul. LUI/LEUR indirekt mit à: Je LUI parle à Paul. LEUR plural.","q":[["Je LE vois Paul?","LE direkt","LUI indirekt"],["Je LUI parle à Paul?","LUI mit à","LE ohne à"],["Je LEUR parle à mes parents?","LEUR","LUI"]]},
"Y EN": {"t":"Y=dort Ort: J'Y vais à Paris. EN=davon Zahl: J'EN ai 3. EN=Teil: du pain -> J'EN veux.","q":[["J'Y vais Paris?","Y Ort","EN davon"],["J'EN ai 3?","EN Zahl","Y Ort"]]},
"Reihenfolge": {"t":"me te se nous vous + le la les + lui leur + y + en + VERB: Il ME LE donne.","q":[["Il ME LE donne?","JA richtig","NEIN"]]},
"Passé Composé": {"t":"avoir/être + Partizip. être bei Bewegung und Reflexiv: Je suis allé, Elle s'est lavée.","q":[["J'ai mangé Hilfsverb?","avoir","être"],["Je suis allé?","être Bewegung","avoir"]]},
"Subjonctif": {"t":"Nach il faut que, je veux que, bien que -> Subjonctif: Il faut que tu viennes / fasses.","q":[["Il faut que tu ___?","viennes Subjonctif","viens Indikativ"]]},
"Futur": {"t":"werden + Infinitiv: Je mangerai, Tu iras. Aller + Infinitiv für nah: Je vais manger.","q":[["Je mangerai?","Futur","Passé"]]},
"Imparfait": {"t":"Gewohnheit Vergangenheit: Quand j'étais petit, je jouais. War, hatte, machte regelmäßig.","q":[["Quand j'étais petit je jouais?","Imparfait Gewohnheit","Passé einmalig"]]},
"Conditionnel": {"t":"Würde: Je voudrais, J'aimerais. Wenn...dann: Si j'avais... je ferais.","q":[["Je voudrais?","Conditionnel würde","Futur werde"]]},
},
"Geschichte": {
"Franz. Revolution 1789": {"t":"14.7.1789 Bastille Sturm, 1793 Ludwig XVI geköpft Guillotine, 1799-1815 Napoleon Kaiser 1804, Waterloo 1815.","q":[["Bastille?","14.7.1789","1793"],["Ludwig XVI geköpft?","1793","1789"],["Napoleon Kaiser?","1804","1789"],["Waterloo?","1815","1804"]]},
"Industrialisierung": {"t":"1769 James Watt Dampfmaschine, 1835 erste deutsche Bahn Nürnberg-Fürth, Krupp Stahl, Kinderarbeit, 1871 Hochindustrialisierung.","q":[["Dampfmaschine wer?","James Watt 1769","Stephenson"],["Erste Bahn DE?","1835 Nürnberg-Fürth","1871"]]},
"1848 Revolution": {"t":"Märzrevolution, Paulskirche Frankfurt erste Demokratie Versuch, schwarz-rot-gold, gescheitert, König lehnt Krone ab.","q":[["Paulskirche Jahr?","1848","1789"],["Farben?","schwarz-rot-gold","schwarz-weiß-rot"]]},
"Kaiserreich 1871": {"t":"18.1.1871 Versailles Gründung nach Sieg gegen Frankreich, Wilhelm I Kaiser, Bismarck Kanzler, 3 Kriege, Kolonien.","q":[["Gründung Kaiserreich?","18.1.1871","1848"],["Bismarck war?","Reichskanzler","Kaiser"],["Ort Gründung?","Versailles","Berlin"]]},
"1. Weltkrieg 1914-18": {"t":"28.6.1914 Attentat Sarajevo Franz Ferdinand, Schützengraben, Verdun 1916, USA 1917, 11.11.1918 Ende, 17 Mio Tote, Versailler Vertrag.","q":[["Beginn 1.WK?","1914","1939"],["Attentat wo?","Sarajevo","Berlin"],["Verdun Jahr?","1916","1914"],["Ende?","11.11.1918","8.5.45"]]},
"Weimar 1919-33": {"t":"1919 Verfassung Weimar, 1923 Inflation Geldschein 1 Billion, 1929 Weltwirtschaftskrise, Arbeitslose 6 Mio, 1933 Hitler.","q":[["Verfassung Weimar?","1919","1933"],["Inflation wann?","1923","1929"],["Weltwirtschaftskrise?","1929","1923"]]},
"NS Zeit 1933-45": {"t":"30.1.33 Hitler Macht Machtergreifung, Reichstagsbrand 27.2.33, Ermächtigungsgesetz, Gleichschaltung, Nürnberger Gesetze 1935, Kristallnacht 9.11.38, Holocaust 6 Mio Juden Auschwitz.","q":[["Hitler Macht?","30.1.1933","9.11.38"],["Reichstagsbrand?","27.2.1933","30.1.33"],["Nürnberger Gesetze?","1935","1933"],["Kristallnacht?","9.11.1938","1933"],["Holocaust Opfer?","6 Mio Juden","1 Mio"]]},
"2. Weltkrieg 1939-45": {"t":"1.9.39 Überfall Polen Blitzkrieg, 1941 Russlandfeldzug Barbarossa, Pearl Harbor 7.12.41 USA tritt ein, Stalingrad 42/43 Wende, D-Day 6.6.44 Normandie, Atombombe 6.8.45 Hiroshima, 8.5.45 Kapitulation DE, 2.9.45 Japan, 60 Mio Tote.","q":[["Beginn 2.WK?","1.9.1939","28.6.14"],["Pearl Harbor?","7.12.1941","1.9.39"],["Stalingrad?","1942/43 Wende","1941"],["D-Day?","6.6.1944","1.9.39"],["Atombombe Hiroshima?","6.8.1945","6.6.44"],["Ende DE?","8.5.1945","11.11.18"]]},
"DDR BRD Mauer": {"t":"1949 23.5. BRD Grundgesetz, 7.10. DDR Gründung, 13.8.61 Mauerbau, 1962 Kuba Krise, 1969 Mond, 9.11.89 Mauerfall, 3.10.90 Wiedervereinigung Tag der Einheit, 28 Jahre Mauer, BRD 16 Länder.","q":[["BRD Gründung?","23.5.1949","7.10.49"],["DDR Gründung?","7.10.1949","1949"],["Mauerbau?","13.8.1961","9.11.89"],["Mauerfall?","9.11.1989","13.8.61"],["Wiedervereinigung?","3.10.1990","9.11.89"],["Wie lange Mauer?","28 Jahre","10 Jahre"]]},
"Antike Griechen Römer": {"t":"753 v.Chr. Rom Gründung, 500 v.Chr. Demokratie Athen, 490 Marathon, 336-323 Alexander der Große Weltreich, 44 v.Chr. Caesar ermordet Iden des März, 0 Geburt Jesus, 476 Untergang Westrom.","q":[["Rom Gründung?","753 v.Chr.","44 v.Chr."],["Demokratie Athen?","500 v.Chr.","753 v.Chr."],["Caesar ermordet?","44 v.Chr.","476"],["Westrom Untergang?","476 n.Chr.","44 v.Chr."]]},
"Mittelalter Entdeckungen": {"t":"500-1500 Mittelalter, 800 Karl der Große Kaiser, 1096-1291 Kreuzzüge Jerusalem, 1347 Pest Schwarzer Tod, 1453 Buchdruck Gutenberg, 1492 Kolumbus Amerika, 1517 Luther 95 Thesen Wittenberg Reformation, 1519-22 Magellan Weltumsegelung.","q":[["Karl Kaiser?","800","1492"],["Kreuzzüge Beginn?","1096","800"],["Buchdruck?","1453 Gutenberg","1492"],["Kolumbus?","1492","1517"],["Luther Thesen?","1517","1492"],["Magellan Welt?","1519-22","1492"]]},
"Kalter Krieg": {"t":"1947-1991 USA vs UdSSR, 1949 NATO, 1955 Warschauer Pakt, 1962 Kuba Krise fast Atomkrieg, 1969 Mondlandung USA, 1989 Mauerfall Ende.","q":[["NATO Gründung?","1949","1955"],["Warschauer Pakt?","1955","1949"],["Kuba Krise?","1962","1949"],["Mondlandung?","1969","1962"]]},
"EU heute": {"t":"1957 Römische Verträge EWG, 1993 EU Maastricht, 2002 Euro Bargeld, 27 Länder EU, 2020 Brexit UK raus, Schengen offene Grenzen.","q":[["Römische Verträge?","1957","1993"],["EU Gründung?","1993","1957"],["Euro Bargeld?","2002","1993"],["Brexit?","2020","2002"]]},
},
"Physik": {
"Mechanik": {"t":"v=s/t, 100km/h=27,8m/s, 50km/h=13,9, a=F/m, Freier Fall s=0,5*g*t², g=9,81m/s².","q":[["100km/h=?","27,8 m/s","100 m/s"],["g=?","9,81 m/s²","10 km/h"]]},
"Kraft Newton 3 Gesetze": {"t":"1.Trägheit, 2.F=m*a, 3.Actio=Reactio. 70kg=686N Gewicht (m*g). 1N=1kg*m/s².","q":[["F=?","m*a","m/v"],["70kg Gewicht?","686N","70N"],["Actio=Reactio?","3. Newton","1."]]},
"Strom Ohmsches Gesetz": {"t":"U=R*I, I=U/R, R=U/I. 12V 3Ω=4A. Reihe: R=R1+R2=5Ω. Parallel: 1/R=1/R1+1/R2 -> 2//2=1Ω. P=U*I: 230V*10A=2300W.","q":[["12V 3Ω I=?","4A","36A"],["Reihe 2+3=?","5Ω","1Ω"],["Parallel 2//2=?","1Ω","4Ω"],["230V 10A P=?","2300W","230W"]]},
"Energie Leistung": {"t":"kinetisch 0,5*m*v², potentiell m*g*h, Spann m*g*h, 1kWh=3,6 Mio Joule=3600kJ, Energie bleibt erhalten, Leistung P=E/t Watt.","q":[["0,5*m*v²=?","kinetisch","potentiell"],["m*g*h=?","potentiell","kinetisch"],["1kWh=?","3,6 Mio J","3600 J"]]},
"Optik Licht": {"t":"Reflexion Einfall=Ausfall, Brechung Licht bricht, Linse sammelt, c=300.000km/s=3*10^8m/s schnellste, Lichtjahr 9,46 Billionen km.","q":[["Einfall=Ausfall?","Reflexion","Brechung"],["c=?","300.000 km/s","343 m/s"],["Lichtjahr?","9,46 Billionen km","300.000 km"]]},
"Akustik Wellen": {"t":"Schall 343m/s Luft, v=f*λ, tief=klein f, laut=Amplitude, Ultraschall >20kHz, Infraschall <20Hz.","q":[["Schall Luft?","343 m/s","300.000 km/s"],["v=f*λ?","Welle Formel","Kraft"],["Ultraschall?"," >20kHz","<20Hz"]]},
"Kernphysik": {"t":"E=mc² Einstein, Uran 235 spaltet -> Energie, Kernspaltung Kraftwerk, Fusion Sonne H->He, Halbwertszeit, radioaktiv Alpha Beta Gamma.","q":[["E=mc² wer?","Einstein","Newton"],["Spaltung Uran?","Kernspaltung","Fusion"],["Sonne Energie?","Fusion","Spaltung"]]},
"Druck": {"t":"p=F/A, 1bar=100.000Pa, Luftdruck 1bar, Auftrieb, 10m Wasser=1bar mehr.","q":[["p=?","F/A","m*a"],["1bar=?","100.000 Pa","1 Pa"],["10m Wasser?","+1bar","1bar total"]]},
},
"Mathe": {
"Brüche": {"t":"1/4+2/4=3/4 gleicher Nenner addieren, 1/2*2/3=2/6=1/3, kürzen teilen, Hauptnenner suchen.","q":[["1/4+2/4=?","3/4","3/8"],["1/2=?","0,5","0,2"]]},
"Prozent Dreisatz": {"t":"% = /100, 50%=0,5, 10%=0,1, Dreisatz: 20% von 200=40. Formel W=G*p/100.","q":[["50% von 200=?","100","50"],["20% von 200=?","40","20"]]},
"Pythagoras": {"t":"a²+b²=c² nur rechtwinklig! c Hypotenuse längste gegenüber 90°. 3-4-5 Dreieck: 3²+4²=5²=25.","q":[["a²+b²=?","c²","a²"],["3²+4²=5²?","JA 9+16=25","NEIN"]]},
"Gleichungen": {"t":"2x+4=10 =>2x=6=>x=3. Mitternacht: x=(-b±√(b²-4ac))/2a. pq: x=-p/2±√((p/2)²-q).","q":[["2x+4=10 x=?","3","5"],["Mitternacht Formel?","-b±√.../2a","a²+b²"]]},
"Funktionen": {"t":"Gerade y=mx+b m Steigung b y-Achse, Parabel y=x², Nullstelle y=0, Steigung = Ableitung.","q":[["y=mx+b ist?","Gerade","Parabel"],["m ist?","Steigung","y-Achse"]]},
"Wahrscheinlichkeit": {"t":"P=günstig/möglich, Würfel 6=1/6=16,7%, Münze 50%, 2 Würfel gleiche Zahl 6/36=1/6.","q":[["Würfel 6?","1/6","6/1"],["Münze Kopf?","50%","1/6"]]},
"Geometrie": {"t":"Kreis: U=2πr, A=πr², r Durchmesser/2. Dreieck A=0,5*g*h, Rechteck A=a*b, Quader V=a*b*c.","q":[["Kreis U=?","2πr","πr²"],["Kreis A=?","πr²","2πr"],["Quader V=?","a*b*c","a*b"]]},
"Binom": {"t":"(a+b)²=a²+2ab+b², (a-b)²=a²-2ab+b², (a+b)(a-b)=a²-b².","q":[["(a+b)²=?","a²+2ab+b²","a²+b²"]]},
},
"Biologie": {
"Zelle": {"t":"Tier Zelle, Pflanze Zelle + Chloroplast + Zellwand. Zellkern DNA, Mitochondrien Kraftwerk ATP, Ribosomen Protein Fabrik, Fotosynthese CO2+H2O+ Licht -> Zucker+O2.","q":[["Kraftwerk Zelle?","Mitochondrien","Zellkern"],["Photosynthese wo?","Chloroplast","Mitochondrien"],["Fabrik Protein?","Ribosomen","Kern"]]},
"Genetik Mendel": {"t":"DNA Doppelhelix Watson Crick 1953, Gene, 46 Chromosomen Mensch 23 Paare, Mendel Erbsen 1865 dominant rezessiv, AA Aa aa, 3:1 Verhältnis.","q":[["DNA Form?","Doppelhelix","Einzel"],["Chromosomen Mensch?","46","23"],["Mendel was?","Erbsen","Fliegen"],["Dominant+rezessiv Aa=?","dominant sichtbar","rezessiv"]]},
"Evolution Darwin": {"t":"Darwin 1859 Origin, Selektion Auslese, Mutation zufällig, Survival fittest, Arten entstehen, Mensch Affe gemeinsamer Vorfahr.","q":[["Darwin Jahr Buch?","1859","1492"],["Selektion?","Auslese stärkste","Zufall"],["Mutation?","zufällig","geplant"]]},
"Ökologie": {"t":"Nahrungskette: Produzent Pflanze -> Konsument Tier -> Destruent Pilz Bakterien, Fotosynthese, CO2 Kreislauf, Treibhaus.","q":[["Produzent?","Pflanze","Tier"],["Destruent?","Pilz Bakterien","Pflanze"],["Fotosynthese Produkt?","Zucker+O2","CO2"]]},
"Mensch Körper": {"t":"Herz 4 Kammern 2 Vorhöfe 2 Kammern, Blutkreislauf groß klein, Lunge Alveolen, Gehirn 86 Mrd Neuronen, Verdauung Mund Magen Darm, 206 Knochen.","q":[["Herz Kammern?","4","2"],["Neuronen Gehirn?","86 Mrd","1 Mio"],["Knochen Mensch?","206","500"]]},
"Immunsystem": {"t":"Weiß Blutkörperchen, Antikörper, Impfung trainiert, Bakterien Antibiotika, Virus kein Antibiotika, HIV, Corona.","q":[["Antibiotika gegen?","Bakterien","Virus"],["Impfung macht?","Antikörper Training","krank"]]},
"Atmung Fotosynthese": {"t":"Mensch O2 ein CO2 aus, Pflanze CO2 ein O2 aus Fotosynthese. Zellatmung Zucker+O2->CO2+H2O+Energie.","q":[["Mensch atmet?","O2 ein CO2 aus","CO2 ein O2 aus"],["Pflanze Fotosynthese?","CO2 ein O2 aus","O2 ein CO2 aus"]]},
},
"Chemie": {
"Atome Aufbau": {"t":"Proton + positiv Kern, Neutron neutral Kern, Elektron - Hülle, Ordnungszahl=Protonen=Elektronen, Masse=Proton+Neutron, Isotop gleiche Protonen andere Neutronen.","q":[["Kern besteht aus?","Proton+Neutron","Elektron"],["Ordnungszahl=?","Protonen Zahl","Neutronen"],["Elektron Ladung?","negativ -","positiv +"]]},
"Periodensystem": {"t":"118 Elemente, H Wasserstoff 1 leichtestes, He Helium 2, Li 3, C Kohlenstoff 6 Basis Leben, O Sauerstoff 8 Atmen, Fe Eisen 26, Au Gold 79, U Uran 92 radioaktiv. Metalle links, Nichtmetalle rechts, Edelgase ganz rechts.","q":[["H Ordnungszahl?","1","8"],["O Ordnungszahl?","8","1"],["Au ist?","Gold","Silber"],["Wie viele Elemente?","118","100"]]},
"Bindungen": {"t":"Ionenbindung Metall+Nichtmetall gibt Elektron ab -> Na+ Cl- -> NaCl Salz. Kovalent Nichtmetall+Nichtmetall teilen zB H2O O2. Metallbindung Metalle teilen alle.","q":[["NaCl Bindung?","Ionenbindung","kovalent"],["H2O Bindung?","kovalent teilen","Ionen"],["Metallbindung?","Metalle alle teilen","Metall+Nichtmetall"]]},
"Reaktionen Säure Base": {"t":"Säure pH<7 sauer, Base pH>7 basisch laugig, pH 7 neutral. Säure+Base=Salz+Wasser Neutralisation. Oxidation mit O2 Rost. Reduktion, Redox.","q":[["pH 7?","neutral","sauer"],["pH 2?","sauer","basisch"],["pH 12?","basisch","sauer"],["Säure+Base=?","Salz+Wasser","Säure"]]},
"Organisch": {"t":"Organisch = C-H Kohlenwasserstoff. Methan CH4 Erdgas, Ethan C2H6, Propan C3, Butan C4, Benzin Gemisch, Alkohol OH zB Ethanol C2H5OH, Säure COOH.","q":[["Methan Formel?","CH4","CO2"],["Organisch Basis?","C-H","H2O"],["Ethanol?","C2H5OH Alkohol","CH4"]]},
"Molare Masse": {"t":"Mol 6,022*10^23 Teilchen Avogadro, Molare Masse g/mol: H 1, C 12, O 16, H2O 18g/mol, CO2 44g/mol.","q":[["H2O Molmasse?","18 g/mol","16"],["CO2 Molmasse?","44","18"]]},
},
"Deutsch": {
"Fälle": {"t":"Nominativ Wer? Was? Der Mann. Genitiv Wessen? Des Mannes. Dativ Wem? Dem Mann. Akkusativ Wen? Was? Den Mann.","q":[["Wessen?","Genitiv","Dativ"],["Wem?","Dativ","Akkusativ"],["Wen?","Akkusativ","Nominativ"]]},
"Zeiten": {"t":"Präsens ich gehe, Präteritum ich ging, Perfekt ich bin gegangen, Plusquam ich war gegangen, Futur I ich werde gehen, Futur II ich werde gegangen sein.","q":[["ich ging?","Präteritum","Perfekt"],["ich bin gegangen?","Perfekt","Präteritum"],["ich war gegangen?","Plusquam","Perfekt"]]},
"Satzglieder": {"t":"Subjekt Wer? Prädikat Was tut? Objekt Wen? Wem? Adverbial Wie? Wo? Wann? Warum? Attribut Zusatz.","q":[["Wer?","Subjekt","Objekt"],["Was tut?","Prädikat","Subjekt"],["Wo? Wann?","Adverbial","Objekt"]]},
"Rechtschreibung das dass": {"t":"das Artikel: das Haus. das Relativ: das Haus, das... dass mit ss nach Komma: Ich weiß, dass du kommst. Seid = ihr seid, seit = seit 2020 Zeit.","q":[["das Haus?","Artikel das","dass ss"],["Ich weiß, dass du?","dass ss Konjunktion","das Artikel"],["Ihr seid?","seid mit d","seit mit t"],["Seit 2020?","seit Zeit","seid ihr"]]},
"Komma": {"t":"Komma bei Aufzählung, vor dass weil wenn, bei Infinitiv mit zu, Apposition.","q":[["Komma vor dass?","JA immer","NEIN"]]},
"Literatur": {"t":"Epik erzählend Roman Novelle, Lyrik Gedicht Ballade, Drama Theater Tragödie Komödie, Goethe Faust 1808, Schiller Glocke, Ballade Erlkönig.","q":[["Faust Autor?","Goethe","Schiller"],["Ballade ist?","Gedicht erzählend","Roman"],["Drama ist?","Theaterstück","Gedicht"]]},
"Wortarten": {"t":"Nomen groß: Haus, Verb tun: gehen, Adjektiv wie: schön, Artikel der die das, Pronomen er sie es, Adverb wie: gestern, Präposition vor Nomen: in auf.","q":[["Haus ist?","Nomen","Verb"],["gehen ist?","Verb","Nomen"],["schön ist?","Adjektiv","Nomen"]]},
},
"Geographie": {
"Deutschland": {"t":"16 Bundesländer: BW Bayern Berlin Brandenburg Bremen Hamburg Hessen MV Niedersachsen NRW RLP Saarland Sachsen Sachsen-Anhalt SH Thüringen. Hauptstadt Berlin, 83 Mio Einwohner, Nachbarn 9 Länder: DK PL CZ AT CH FR LU BE NL.","q":[["Wie viele Bundesländer?","16","9"],["Hauptstadt DE?","Berlin","München"],["Nachbarländer?","9","16"],["Einwohner?","83 Mio","50 Mio"]]},
"Europa": {"t":"44 Länder Europa, EU 27 Länder, Europarat, Hauptstadt EU Brüssel, längster Fluss Wolga 3530km, Donau 2850km, Alpen höchster Mont Blanc 4808m, EU Parlament Straßburg Brüssel.","q":[["EU wie viele Länder?","27","44"],["Längster Fluss Europa?","Wolga 3530km","Donau"],["Mont Blanc Höhe?","4808m","8000m"]]},
"Klima Zonen": {"t":"Tropen Äquator 0° heiß feucht Regenwald, Subtropen Wüste, gemäßigt DE 4 Jahreszeiten, subpolar Tundra, polar Eis. Klimawandel CO2 Treibhaus +1,2°C.","q":[["Äquator Klima?","Tropen heiß feucht","polar kalt"],["DE Klimazone?","gemäßigt","Tropen"],["Klimawandel Grund?","CO2 Treibhaus","O2"]]},
"Platten Tektonik": {"t":"7 große Platten bewegen cm pro Jahr, Erdbeben an Plattengrenzen, Vulkane Ring of Fire Pazifik, Kontinentaldrift Wegener, Tsunami, Pangaea früher ein Kontinent.","q":[["Erdbeben Grund?","Platten Tektonik","Wind"],["Ring of Fire?","Vulkane Pazifik","Europa"],["Pangaea war?","ein Kontinent früher","ein Vulkan"]]},
"Welt Kontinente Ozeane": {"t":"7 Kontinente: Asien größter, Afrika, Nordamerika, Südamerika, Antarktis, Europa, Australien. 5 Ozeane: Pazifik größter, Atlantik, Indik, Südlich, Arktisch.","q":[["Größter Kontinent?","Asien","Europa"],["Größter Ozean?","Pazifik","Atlantik"],["Wie viele Kontinente?","7","5"]]},
"Wirtschaft": {"t":"Industrie DE Auto, Dienstleistung, Globalisierung, Entwicklungsländer, Schwellenländer, Öl OPEC, EU Binnenmarkt.","q":[["DE Industrie?","Auto Maschinen","Öl"],["OPEC ist?","Öl Länder","EU"]]},
},
}

# UI
c1,c2=st.columns([4,1])
with c1:
    suche=st.text_input("", placeholder="🔍 Suche: Mauer, pain, Newton, dass, DNA, 1914...", label_visibility="collapsed")
with c2:
    st.metric("⭐ XP", st.session_state['xp'])

if suche:
    s=suche.lower()
    count=0
    for fach in VOKABELN:
        for lek,lst in VOKABELN[fach].items():
            for f,d in lst:
                if s in f.lower() or s in d.lower():
                    st.info(f"{fach} {lek}: {f} = {d}")
                    count+=1
                    if count>20: break
    for fach,themen in THEMEN.items():
        for tname,data in themen.items():
            if s in tname.lower() or s in data["t"].lower():
                with st.expander(f"📖 {fach}: {tname} - gefunden!", expanded=True):
                    st.info(data["t"])
                count+=1
    if count==0:
        try:
            enc=urllib.parse.quote(suche)
            r=requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", timeout=3)
            if r.status_code==200:
                st.info(r.json().get("extract","")[:500])
        except: pass
        st.warning(f"Nichts für '{suche}'")

st.write("---")
st.progress(min(st.session_state['xp']/300,1.0), text=f"Level {st.session_state['xp']//50+1} - {st.session_state['xp']} XP bis 300")

st.markdown("### 📚 Klick ein Fach - Themen kommen SOFORT!")
fach_list=list(VOKABELN.keys())+list(THEMEN.keys())
fach_list=list(dict.fromkeys(fach_list))
cols=st.columns(4)
for i,fach in enumerate(fach_list):
    emoji="🗣️" if fach in VOKABELN else "📖"
    if cols[i%4].button(f"{emoji} {fach}", key=f"fach_{fach}", use_container_width=True):
        st.session_state['fach']=fach

if 'fach' in st.session_state:
    fach=st.session_state['fach']
    st.write("---")
    st.markdown(f"## {fach}")

    # VOKABELN TEIL
    if fach in VOKABELN:
        for lek,lst in VOKABELN[fach].items():
            with st.expander(f"📝 {lek} - {len(lst)} Vokabeln - klicken zum Lernen", expanded=False):
                for f,d in lst:
                    st.write(f"**{f}** = {d}")
                if st.button(f"▶️ Test {lek} 20 Fragen", key=f"test_{fach}_{lek}", use_container_width=True):
                    st.session_state['test_fach']=fach
                    st.session_state['test_lek']=lek
                    st.session_state['test_fragen']=random.sample(lst, min(20,len(lst)))
                    st.session_state['test_idx']=0
                    st.session_state['test_score']=0
                    st.rerun()

    # THEMEN TEIL - KOMMT SOFORT!!!
    if fach in THEMEN:
        st.markdown(f"### 📖 {fach} - {len(THEMEN[fach])} Themen SOFORT da:")
        for tname,data in THEMEN[fach].items():
            with st.expander(f"📚 {tname}", expanded=True):
                st.info(data["t"])
                st.markdown("**🎯 Testfragen:**")
                for qi,(frage,richtig,falsch) in enumerate(data["q"]):
                    st.write(f"**{qi+1}. {frage}**")
                    key_base=f"{fach}_{tname}_{qi}"
                    if f"done_{key_base}" not in st.session_state:
                        c1,c2=st.columns(2)
                        if c1.button(f"✅ {richtig}", key=f"r_{key_base}", use_container_width=True):
                            st.session_state[f"done_{key_base}"]=True
                            st.session_state[f"ok_{key_base}"]=True
                            st.session_state['xp']+=3
                            st.rerun()
                        if c2.button(f"❌ {falsch}", key=f"f_{key_base}", use_container_width=True):
                            st.session_state[f"done_{key_base}"]=True
                            st.session_state[f"ok_{key_base}"]=False
                            st.rerun()
                    else:
                        if st.session_state.get(f"ok_{key_base}"):
                            st.success(f"✅ Richtig! {richtig} 🎉")
                        else:
                            st.error(f"❌ Richtig wäre: {richtig}")

    # TEST MODAL FÜR VOKABELN
    if 'test_fragen' in st.session_state:
        fragen=st.session_state['test_fragen']
        idx=st.session_state['test_idx']
        score=st.session_state['test_score']
        if idx < len(fragen):
            st.markdown("---")
            st.markdown(f"### 🎯 Test {st.session_state.get('test_lek','')} - Frage {idx+1}/{len(fragen)} Score {score}")
            st.progress(idx/len(fragen))
            f_orig,d_orig=fragen[idx]
            # Abwechselnd
            if idx%2==0:
                st.markdown(f"## Was heißt **{f_orig}**?")
                # Finde alle falsche
                all_lst=[]
                for l in VOKABELN[st.session_state['test_fach']].values(): all_lst.extend(l)
                falsche=[d for _,d in all_lst if d!=d_orig]
                opts=[d_orig]+random.sample(falsche, min(3,len(falsche)))
                random.shuffle(opts)
                correct=d_orig
            else:
                st.markdown(f"## Wie heißt **{d_orig}**?")
                all_lst=[]
                for l in VOKABELN[st.session_state['test_fach']].values(): all_lst.extend(l)
                falsche=[f for f,_ in all_lst if f!=f_orig]
                opts=[f_orig]+random.sample(falsche, min(3,len(falsche)))
                random.shuffle(opts)
                correct=f_orig

            cols=st.columns(2)
            for i,opt in enumerate(opts):
                if cols[i%2].button(opt, key=f"ans_{idx}_{i}", use_container_width=True):
                    if opt==correct:
                        st.success(f"✅ {f_orig} = {d_orig} 🎉"); st.balloons(); st.session_state['test_score']=score+1; st.session_state['xp']+=5
                    else:
                        st.error(f"❌ Richtig: {f_orig} = {d_orig}")
                    st.session_state['test_idx']=idx+1
                    time.sleep(1)
                    st.rerun()
        else:
            st.markdown(f"## 🏁 Fertig! {score}/{len(fragen)}")
            if score==len(fragen): st.balloons(); st.snow(); st.success("🌟 PERFEKT! +20 XP"); st.session_state['xp']+=20
            elif score>=len(fragen)*0.8: st.success(f"🎉 Stark {score}/{len(fragen)} +10 XP"); st.balloons(); st.session_state['xp']+=10
            else: st.warning(f"{score}/{len(fragen)} weiter üben")
            if st.button("🔄 Nochmal", use_container_width=True):
                del st.session_state['test_fragen']
                st.rerun()
            if st.button("❌ Test schließen", use_container_width=True):
                for k in list(st.session_state.keys()):
                    if k.startswith("test_"): del st.session_state[k]
                st.rerun()

    if st.button("⬅️ Fach schließen", use_container_width=True):
        for k in list(st.session_state.keys()):
            if k!='xp': del st.session_state[k]
        st.rerun()
