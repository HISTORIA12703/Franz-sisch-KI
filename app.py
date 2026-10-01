import streamlit as st
import requests, urllib.parse

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")
st.markdown('<h1 style="text-align:center;color:#2E86AB;">📚 Lern App - Mit Quiz + Suche</h1>', unsafe_allow_html=True)

def wiki(q):
    try:
        enc=urllib.parse.quote(q.replace(" ","_"))
        r=requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers={'User-Agent':'LernApp'}, timeout=3)
        if r.status_code==200:
            return r.json().get("extract","")
    except:
        pass
    return ""

# SEHR VIELE THEMEN + VOKABELN MIT SUCHE
DATEN = {
"Französisch": {
    "Vokabeln Alltag": {"t":"le pain Brot la pomme Apfel le livre Buch la maison Haus l'eau Wasser le temps Zeit la vie Leben le jour Tag la nuit Nacht la table Tisch la chaise Stuhl la porte Tür la fenêtre Fenster aller gehen venir kommen faire machen dire sagen voir sehen vouloir wollen pouvoir können prendre nehmen manger essen boire trinken dormir schlafen travailler arbeiten aimer lieben parler sprechen comprendre verstehen bon gut mauvais schlecht grand groß petit klein beau schön nouveau neu vieux alt jeune jung facile leicht difficile schwer ici hier là dort maintenant jetzt toujours immer beaucoup viel peu wenig très sehr bien gut mal schlecht oui ja non nein merci danke", "q":[["le pain =?","Brot","Apfel"], ["aller =?","gehen","kommen"], ["bon =?","gut","schlecht"], ["ici =?","hier","dort"]]},
    "Vokabeln Schule": {"t":"l'école Schule le professeur Lehrer l'élève Schüler le cours Unterricht le livre Buch le cahier Heft le stylo Stift le crayon Bleistift la matière Fach les devoirs Hausaufgaben l'examen Prüfung la note Note apprendre lernen enseigner lehren lire lesen écrire schreiben compter zählen parler sprechen écouter zuhören réussir bestehen échouer durchfallen", "q":[["l'école =?","Schule","Haus"], ["le professeur =?","Lehrer","Schüler"]]},
    "le la les lui leur": {"t":"LE=ihn/es direkt COD OHNE a Je mange LE pain->Je LE mange Je vois Paul->Je LE vois LA=sie Je vois Marie->Je LA vois LES=sie Plural Je LES vois LUI=ihm/ihr indirekt COI MIT a Person Je parle À Marie->Je LUI parle Je donne À Marie le livre->Je LUI donne LEUR=ihnen Je parle AUX enfants->Je LEUR parle Je LEUR donne", "q":[["Je mange LE pain -> Je __ mange","LE","LUI"], ["Je parle À Marie -> Je __ parle","LUI","LE"], ["AUX enfants -> Je __ parle","LEUR","LUI"], ["Je vois Marie -> Je __ vois","LA","LUI"]]},
    "y en": {"t":"Y=dort/dahin/daran Ort mit à chez dans sur ODER à+SACHE Je vais À Paris->J'Y vais Je suis chez moi->J'Y suis Je pense À mon examen Sache->J'Y pense ABER Person Je pense À Marie->Je pense À ELLE nicht Y! EN=davon/dessen Menge mit de/du/des Zahl Je veux DU pain->J'EN veux J'ai 3 frères Zahl->J'EN ai 3 J'ai beaucoup DE livres->J'EN ai beaucoup J'EN ai besoin", "q":[["Je vais À Paris -> J'__ vais","Y","EN"], ["J'ai 3 frères -> J'__ ai 3","EN","Y"], ["Je veux DU pain -> J'__ veux","EN","Y"]]},
    "Reihenfolge Pronomen": {"t":"PFLICHT Reihenfolge: me te se nous vous + le la les + lui leur + y + en + VERB Il ME LE donne Er gibt es mir Il TE LES donne Je LE LUI donne Ich gebe es ihm Il Y EN a Es gibt davon Je M'Y habitue Ich gewöhne mich daran", "q":[["Il ME LE donne richtig?","JA me+le","NEIN le+me"], ["Was nach le la les?","lui leur","me te"], ["Il Y EN a =?","Es gibt davon","Er ist dort"]]},
    "indirekte Rede": {"t":"Il dit: Je suis malade Direkt Indirekt Il dit qu'il EST malade Präsens bleibt weil Einleitung Präsens! Il a dit: Je suis malade -> Il a dit qu'il ÉTAIT malade Present->Imparfait J'ai mangé->avait mangé Futur->Conditionnel Où vas-tu?->où il allait Que fais-tu?->ce que je faisais Qu'est-ce que->ce que Pourquoi?->pourquoi Viens!->de venir", "q":[["Il dit qu'il EST bleibt weil Präsens Einleitung?","JA bleibt EST","NEIN wird ÉTAIT"], ["Il a dit qu'il ÉTAIT Present->?","Imparfait","Futur"], ["Que fais-tu? -> __ faisais","ce que","que"]]},
    "Zeiten Verben": {"t":"Passé composé 14 Verben mit être aller venir arriver partir entrer sortir monter descendre rester tomber naître mourir devenir revenir + reflexiv je suis allé(e) Imparfait je parlais Hintergrund Gewohnheit Futur je parlerai Conditionnel je parlerais würde Plus-que j'avais parlé Vorvergangenheit", "q":[["je suis allé =?","Passé composé mit être","Imparfait"], ["je parlais =?","Imparfait Hintergrund","Futur"], ["je parlerais =?","Conditionnel würde","Passé"]]},
    "Subjonctif": {"t":"Subjonctif nach il faut que je veux que bien que pour que avant que il est important que Formen que je sois que j'aie que je fasse que j'aille que je puisse que je veuille que je sache Indicativ nach je pense que, Subjonctif nach je ne pense pas que", "q":[["Nach il faut que kommt?","Subjonctif","Indicativ"], ["que je sois =?","Subjonctif être","Indicativ"]]},
},
"Spanisch": {
    "Vokabeln Alltag": {"t":"el pan Brot la manzana Apfel el libro Buch la casa Haus el agua Wasser el tiempo Zeit la vida Leben el día Tag la noche Nacht la mesa Tisch la silla Stuhl la puerta Tür la ventana Fenster ir gehen venir kommen hacer machen decir sagen ver sehen querer wollen poder können tomar nehmen comer essen beber trinken dormir schlafen trabajar arbeiten amar lieben hablar sprechen comprender verstehen bueno bueno malo schlecht grande grande pequeño klein hermoso schön nuevo neu viejo alt joven jung fácil leicht difícil schwer aquí hier allí dort ahora jetzt siempre immer mucho mucho poco wenig muy sehr bien gut mal schlecht sí ja no nein gracias danke", "q":[["el pan =?","Brot","Apfel"], ["ir =?","gehen","kommen"], ["bueno =?","gut","schlecht"]]},
    "Vokabeln Schule": {"t":"la escuela Schule el profesor Lehrer el alumno Schüler el curso Kurs el libro Buch el cuaderno Heft el bolígrafo Stift el lápiz Bleistift la materia Fach los deberes Hausaufgaben el examen Prüfung la nota Note aprender lernen enseñar lehren leer lesen escribir schreiben contar zählen hablar sprechen escuchar zuhören aprobar bestehen suspender durchfallen", "q":[["la escuela =?","Schule","Haus"], ["el profesor =?","Lehrer","Schüler"]]},
    "lo la le les": {"t":"LO=ihn direkt OHNE a Veo EL LIBRO->LO veo LA=sie Veo LA CASA->LA veo LOS LAS Plural LE=ihm indirekt MIT a Hablo A JUAN->LE hablo Doy libro A MARÍA->LE doy LES=ihnen A LOS NIÑOS->LES doy", "q":[["Veo EL LIBRO -> __ veo","LO","LE"], ["Hablo A JUAN -> __ hablo","LE","LO"]]},
    "se lo doy WICHTIG": {"t":"WICHTIGSTE REGEL: Du kannst NICHT Le lo doy sagen! FALSCH! Wenn LE/LES + LO/LA LOS LAS zusammen kommen wird LE/LES zu SE! Le doy el libro + lo = SE LO DOY Les doy los libros = SE LOS DOY Me lo da Te lo doy erlaubt! Nur le/les+lo/la wird SE!", "q":[["Le lo doy ist?","FALSCH","RICHTIG"], ["Richtig?","SE LO DOY","LE LO DOY"], ["Les doy los libros ->?","SE LOS DOY","LES LOS DOY"]]},
    "ser estar": {"t":"SER=WAS IST permanent Identität Eigenschaft Herkunft Material Zeit Soy Juan Name Soy de Alemania Herkunft Soy alto Eigenschaft Son las tres Uhrzeit Es de madera Material ESTAR=WO?WIE?GERADE? Estoy en casa Ort Estoy cansado Zustand Está roto Ergebnis kaputt Estoy comiendo gerade estar+gerundio Es aburrido Charakter vs Está aburrido ihm ist langweilig gerade!", "q":[["Soy alto =?","SER permanent","ESTAR Zustand"], ["Estoy en casa =?","ESTAR Ort","SER"], ["Estoy cansado =?","ESTAR Zustand","SER"], ["Son las tres =?","SER Zeit","ESTAR"]]},
    "por para": {"t":"POR=Grund Ursache Durch Tausch Dauer Warum?Wodurch? Gracias POR todo Grund Voy POR la calle durch POR dos horas Dauer 5€ POR libro Tausch PARA=Ziel Zweck Empfänger Frist Wofür? Esto es PARA comer Zweck PARA ti für dich Empfänger Voy PARA Madrid Ziel Para mañana bis morgen Frist", "q":[["Gracias ___ todo Grund","POR","PARA"], ["Esto es ___ comer Zweck","PARA","POR"], ["Voy ___ Madrid Ziel","PARA","POR"], ["POR dos horas =?","Dauer","Ziel"]]},
    "Zeiten": {"t":"yo hablo Present yo hablé Pretérito yo hablaba Imperfecto hablaré Futur hablaría Condicional he hablado Perfect había hablado Pluscuam Subjuntivo haya hable", "q":[["yo hablo =?","Present","Past"], ["he hablado =?","Perfect","Futur"]]},
},
"Italienisch": {
    "Vokabeln Alltag": {"t":"il pane Brot la mela Apfel il libro Buch la casa Haus l'acqua Wasser il tempo Zeit la vita Leben il giorno Tag la notte Nacht il tavolo Tisch la sedia Stuhl la porta Tür la finestra Fenster andare gehen venire kommen fare machen dire sagen vedere sehen volere wollen potere können prendere nehmen mangiare essen bere trinken dormire schlafen lavorare arbeiten amare lieben parlare sprechen capire verstehen buono gut cattivo schlecht grande groß piccolo klein bello schön nuovo neu vecchio alt giovane jung facile leicht difficile schwer qui hier là dort ora jetzt sempre immer molto viel poco wenig molto sehr bene gut male schlecht sì ja no nein grazie danke", "q":[["il pane =?","Brot","Apfel"], ["andare =?","gehen","kommen"]]},
    "Vokabeln Schule": {"t":"la scuola Schule il professore Lehrer l'alunno Schüler il corso Kurs il libro Buch il quaderno Heft la penna Stift la matita Bleistift la materia Fach i compiti Hausaufgaben l'esame Prüfung il voto Note imparare lernen insegnare lehren leggere lesen scrivere schreiben contare zählen parlare sprechen ascoltare zuhören superare bestehen bocciare durchfallen", "q":[["la scuola =?","Schule","Haus"]]},
    "lo la gli li le ci ne": {"t":"LO=ihn masc Vedo IL LIBRO->LO vedo LA=sie fem Vedo LA CASA->LA vedo LI=masc Plural Vedo I LIBRI->LI vedo LE=fem Plural Vedo LE CASE->LE vedo GLI=ihm/ihr/ihnen MIT a Parlo A GIOVANNI->GLI parlo Parlo AI bambini->GLI parlo CI=y dort/daran Ort Sache Vado A Parigi->CI vado CI penso daran Sache NE=en davon de Zahl Voglio DEL pane->NE voglio Ho 3 fratelli Zahl->NE ho 3 NE ho molti", "q":[["Vedo IL LIBRO -> __ vedo","LO","GLI"], ["Parlo A GIOVANNI -> __ parlo","GLI","LO"], ["Vado A Parigi -> __ vado","CI","NE"], ["Voglio DEL pane -> __ voglio","NE","CI"]]},
    "essere stare glielo": {"t":"GLIELO=gli+lo zusammen wie SE LO DOY Glielo do Ich gebe es ihm Glielo dico Ich sage es ihm Me lo da Te lo do Ce lo ha ESSERE=WAS IST permanent Sono Giovanni Name Sono di Germania Herkunft Sono alto Eigenschaft Sono le 3 Uhrzeit! STARE=WO?WIE?GERADE? Sto a casa Ort Sto male krank Zustand Sta rotto kaputt Ergebnis Sto mangiando gerade stare+gerundio Sto leggendo", "q":[["Glielo do =?","Ich gebe es ihm","Ich bin dort"], ["Sono Giovanni =?","ESSERE","STARE"], ["Sto a casa =?","STARE Ort","ESSERE"], ["Sto mangiando =?","gerade stare+gerundio","permanent"]]},
    "Zeiten": {"t":"io parlo Present ho parlato Passato prossimo parlavo Imperfetto parlerò Futuro parlerei Condizionale congiuntivo che io parli", "q":[["io parlo =?","Present","Past"], ["ho parlato =?","Passato prossimo","Present"]]},
},
"Latein": {
    "Vokabeln Alltag": {"t":"panis Brot malum Apfel liber Buch casa Haus aqua Wasser tempus Zeit vita Leben dies Tag nox Nacht mensa Tisch sella Stuhl porta Tür fenestra Fenster ire gehen venire kommen facere machen dicere sagen videre sehen velle wollen posse können capere nehmen edere essen bibere trinken dormire schlafen laborare arbeiten amare lieben loqui sprechen intellegere verstehen bonus gut malus schlecht magnus groß parvus klein pulcher schön novus neu vetus alt iuvenis jung facilis leicht difficilis schwer hic hier illic dort nunc jetzt semper immer multus viel parvus wenig valde sehr bene gut male schlecht ita ja non nein gratias danke ego ich tu du is ea id er sie es nos wir vos ihr", "q":[["panis =?","Brot","Apfel"], ["ire =?","gehen","kommen"], ["ego =?","ich","du"]]},
    "Kasus": {"t":"Nominativ Wer?Was? Subjekt puella Mädchen Puella videt Das Mädchen sieht Genitiv Wessen? puellae des Mädchens Filius puellae Sohn des Mädchens Dativ Wem? puellae dem Mädchen Do librum puellae Ich gebe dem Mädchen Buch Akkusativ Wen?Was? puellam das Mädchen Video puellam Ich sehe Mädchen Ablativ Womit?Wo?Wann? cum puella mit Mädchen in villa in Villa Ablativus absolutus", "q":[["Wer?Was? =?","Nominativ","Genitiv"], ["Wessen? =?","Genitiv","Nominativ"], ["puellam =?","Akkusativ","Nominativ"]]},
    "Deklinationen 1-5": {"t":"1.a Dekl puella puellae puellae puellam puella Gen puellae 2.o servus Gen servi bellum Gen belli 3.konsonantisch rex Gen regis corpus Gen corporis caput Gen capitis 4.u fructus Gen fructus 5.e res Gen rei dies Tag Gen diei", "q":[["puella Gen?","puellae","puellam"], ["servus Gen?","servi","servus"], ["rex Gen?","regis","rex"], ["fructus Gen?","fructus","fructi"]]},
    "AcI": {"t":"AcI Akkusativ mit Infinitiv nach sagen denken wissen Dico eum venire Ich sage dass er kommt wörtlich Ich sage ihn zu kommen eum Akk venire Inf Präsens Dico eum venisse dass er gekommen ist Perfekt Inf Dico eum venturum esse dass er kommen wird Futur Scio eam venire Ich weiß dass sie kommt", "q":[["Dico eum venire =?","Ich sage dass er kommt","Ich komme"], ["eum im AcI =?","Akkusativ","Nominativ"]]},
    "Gerundium Partizip": {"t":"Gerundium Verbalsubstantiv amandum das Lieben Gen amandi Dat amando Akk amandum Abl amando Ad amandum Zum Lieben Causa amandi Wegen des Liebens Partizipien PPA amans liebend Präsens Aktiv amans puella liebendes Mädchen PPP amatus geliebt worden Perfekt Passiv amata puella geliebtes Mädchen PFA amaturus im Begriff zu lieben Futur Aktiv", "q":[["amans =?","liebend PPA","geliebt"], ["amatus =?","geliebt worden PPP","liebend"], ["Ad amandum =?","Zum Lieben","des Liebens"]]},
    "Konjugationen": {"t":"amo amare amavi amatum lieben moneo monere monui monitum mahnen lego legere legi lectum lesen audio audire audivi auditum hören sum esse fui sein eo ire ii itum gehen fero ferre tuli latum tragen volo velle volui wollen", "q":[["amo amare =?","lieben","mahnen"], ["sum esse fui =?","sein","gehen"]]},
},
"Physik": {
    "Mechanik Grundlagen": {"t":"Bewegung Ort Geschwindigkeit v=s/t m/s 100km/h=27,8m/s Beschleunigung a=v/t m/s² Freier Fall s=0,5*g*t² g=9,81 2s Fall 19,6m v=g*t 2s 19,6m/s Wurf", "q":[["v=s/t v=?","Geschwindigkeit","Strecke"], ["100km/h =? m/s","27,8","100"], ["Freier Fall s=?","0,5*g*t²","g*t"]]},
    "Newton Gesetze": {"t":"Newton1 Trägheit ohne Kraft bleibt Körper in Ruhe oder gleichförmig geradeaus Newton2 F=m*a 1N=1kg*1m/s² Kraft=Masse*Beschleunigung Beispiel 2kg*3m/s²=6N Gewicht Fg=m*g 70kg*9,81=686N a=F/m Newton3 Actio=Reactio Kräfte paarweise Wand drückt dich zurück wie du Wand Rakete stößt Gas nach unten Gas stößt Rakete nach oben", "q":[["Newton2 F=?","m*a","m*g"], ["Gewicht Fg=?","m*g","m*a"], ["Newton3?","Actio=Reactio","F=m*a"], ["70kg Gewicht?","686N","70N"]]},
    "Energie Leistung": {"t":"Energie Erhaltung bleibt erhalten wird nur umgewandelt nie vernichtet Formen kinetisch Bewegung 0,5*m*v² Auto 1000kg 20m/s 200000J potentiell Höhe m*g*h 70kg 10m 6867J Wärme Licht elektrisch chemisch Leistung P=E/t Watt Joule/Sekunde kW kWh 1kWh=3,6Mio J 100W Lampe 10h 1kWh", "q":[["Kinetisch?","0,5*m*v²","m*g*h"], ["Potentiell?","m*g*h","0,5*m*v²"], ["1kWh =?","3,6 Mio J","1000 J"]]},
    "Stromkreis": {"t":"Strom Elektronen fließen U Volt Spannung Druck I Ampere Menge pro Zeit R Ohm Widerstand Hindernis Ohmsches Gesetz R=U/I I=U/R U=R*I Beispiel 12V 3Ω I=4A Reihe Rges=R1+R2 2+3=5Ω Spannung teilt sich Parallel 1/R=1/R1+1/R2 2Ω//2Ω=1Ω Strom teilt sich Leistung P=U*I 230V*10A=2300W Energie kWh Gefahren 50mA gefährlich Steckdose 230V", "q":[["R=U/I R=?","U/I","U*I"], ["12V 3Ω I=?","4A","36A"], ["Reihe 2+3=?","5Ω","1,2Ω"], ["Parallel 2//2=?","1Ω","4Ω"], ["230V*10A=?","2300W","23W"]]},
    "Optik": {"t":"Licht 300000km/s Reflexion Einfallswinkel=Ausfallswinkel Spiegel Brechung Übergang Luft Glas Wasser Stab knickt Prisma weiß in Farben Regenbogen Linse Sammellinse brennt Brennpunkt Brennweite f=1/D Dioptrien Auge Linse Netzhaut kurzsichtig - weit+ Farben rot 700nm blau 400nm Laser gebündelt monochromatisch", "q":[["Einfall=Ausfall =?","Reflexion","Brechung"], ["Weiß durch Prisma?","Farben Regenbogen","weiß bleibt"]]},
    "Kern Atom": {"t":"Atom Kern Proton+ Neutron Hülle Elektron Kernspaltung Uran235 Neutron spaltet setzt Energie frei E=mc² 1g Uran=3 Tonnen Kohle Kettenreaktion moderiert Kraftwerk unkontrolliert Bombe Fusion Sonne Wasserstoff zu Helium 15Mio Grad Alpha Beta Gamma Strahlung Halbwertszeit", "q":[["Brennstoff Kern?","Uran235","Eisen"], ["E=mc² =?","Masse=Energie","F=m*a"]]},
},
"Mathe": {
    "Brüche Prozent": {"t":"1/4+2/4=3/4 1/2+1/3=5/6 Multi 1/2*3/4=3/8 Divi Kehrwert 1/2:1/4=2 Prozent %= /100 Dreisatz 100%=50 1%=0,5 20%=10 Zins Z=K*p/100", "q":[["1/4+2/4=?","3/4","3/8"], ["1/2:1/4=?","2","1/8"], ["20% von 50=?","10","20"]]},
    "Gleichungen": {"t":"Waage beide Seiten gleich 2x+4=10 x=3 Mitternacht x=(-b±√(b²-4ac))/2a pq x=-p/2±√((p/2)²-q) D>0 2 Lösungen D=0 1 D<0 keine Lineare Systeme Einsetzen Gleichsetzen", "q":[["2x+4=10 x=?","3","5"], ["Mitternacht Formel?","(-b±√)/2a","a+b"]]},
    "Geometrie": {"t":"Pythagoras a²+b²=c² nur 90° 3²+4²=5² Rechteck a*b Umfang 2a+2b Kreis Umfang 2πr Fläche πr² Quader Volumen a*b*c Würfel a³ Zylinder πr²*h Kugel 4/3πr³ Oberfläche 4πr² sin=GK/Hyp cos=AK/Hyp tan=GK/AK sin²+cos²=1", "q":[["a²+b²=?","c²","a²"], ["Kreis Umfang?","2πr","πr²"], ["sin=?","GK/Hyp","AK/Hyp"]]},
    "Ableitung Integral": {"t":"x^n->n*x^(n-1) x³->3x² Konstante 0 Produkt u'v+uv' Kettenregel innere*äußere f'=0 Extrem Hoch Tief f''>0 Tief f''<0 Hoch Integral ∫x^n=x^(n+1)/(n+1)+C Fläche F(b)-F(a) Hauptsatz", "q":[["x³ abgeleitet?","3x²","x²"], ["f'=0 =?","Extrem","Nullstelle"]]},
    "Wahrscheinlichkeit": {"t":"P=günstige/alle Würfel P(6)=1/6 Laplace UND multi ODER add Baum Pfad multi Summe add Erwartung n*p Binomial (n über k)*p^k*(1-p)^(n-k) Normal Glocke", "q":[["P(6) Würfel=?","1/6","1/3"], ["UND im Baum?","multi","add"]]},
},
"Geschichte": {
    "französische revolution": {"t":"1789 1.Stand 1% 10% Land keine Steuern 2.Stand 2% 20% keine Steuern 3.Stand 97% zahlt alles Ludwig XVI pleite Hunger Aufklärung Rousseau 14.7. Bastille 26.8. Menschenrechte 21.1.93 Ludwig geköpft Robespierre 40k 1799 Napoleon Ende", "q":[["Wann Bastille?","14.7.1789","1789"], ["3.Stand %?","97%","1%"], ["Ludwig geköpft?","21.1.93","1789"]]},
    "industrialisierung": {"t":"1760 England Kohle Eisen Watt Dampfmaschine 1769 Fabriken Manchester 25k->300k 16h Arbeit Kinderarbeit 1848 Marx Kommunistisches Manifest SPD 1875 Eisenbahn 1835 Nürnberg Fürth Krupp Thyssen", "q":[["Wann Dampfmaschine?","1769","1789"], ["Manchester 25k->?","300k","25k"]]},
    "1 weltkrieg": {"t":"1914-18 Imperialismus Kolonien Wettrüsten Sarajevo 28.6.14 Princip Franz Ferdinand Mittelmächte DE Ö vs Entente FR RU EN Schlieffenplan Belgien Schützengraben 700km Verdun 700k Somme Tank Giftgas 11.11.18 Waffenstillstand Versailles 28.6.19 132Mrd Reparationen 17Mio Tote", "q":[["Auslöser 1.WK?","Sarajevo 28.6.14","Bastille"], ["Waffenstillstand?","11.11.18","28.6.19"], ["Tote?","17 Mio","1 Mio"]]},
    "2 weltkrieg": {"t":"1939-45 Versailles Krise Weltwirtschaft Hitler 30.1.33 Diktator 1.9.39 Polen Blitzkrieg 1940 Frankreich 22.6.41 Russland 7.12.41 Pearl Harbor USA Holocaust 6Mio Auschwitz Wannsee 20.1.42 Stalingrad Winter 1943 Wende D-Day 6.6.44 8.5.45 Kapitulation Hiroshima 6.8.45 140k Nagasaki 70k 60Mio Tote UNO", "q":[["Beginn 2.WK?","1.9.39 Polen","1914"], ["Holocaust wie viele?","6 Mio Juden","1 Mio"], ["Hiroshima wann?","6.8.45","1940"]]},
    "kalter krieg mauer": {"t":"1947-90 USA vs UdSSR Kapitalismus vs Kommunismus Berlin Blockade 48-49 Luftbrücke Rosinenbomber NATO 49 Warschauer Pakt 55 Mauer 13.8.61-9.11.89 28J 155km 140 Tote Kuba 62 fast Atomkrieg Vietnam 65-75 Brandt Ostpolitik Gorbatschow Glasnost Perestroika Montagsdemos 9.11.89 Fall 3.10.90 Einheit BRD 23.5.49 DDR 7.10.49", "q":[["Mauer wann gebaut?","13.8.61","9.11.89"], ["Wie lange Mauer?","28 Jahre","10 Jahre"], ["Einheit wann?","3.10.90","9.11.89"]]},
    "usa": {"t":"1776 4.7. Unabhängigkeit 13 Kolonien England Washington 1.Präsident 1861-65 Bürgerkrieg Nord vs Süd Lincoln Sklaverei Ende 50 Staaten 340Mio Weltmacht", "q":[["USA Unabhängigkeit?","1776","1789"]]},
    "hitler ns": {"t":"Hitler 20.4.1889 Braunau WWI Gefreiter 1923 Putsch Knast Mein Kampf 30.1.33 Kanzler 1933 Ermächtigung Diktator Juden Boykott Nürnberger Gesetze 1935 Kristallnacht 9.11.38 KZ Holocaust 6Mio 2.WK 1939-45 Selbstmord 30.4.45 Bunker", "q":[["Hitler Kanzler wann?","30.1.33","1945"], ["Kristallnacht wann?","9.11.38","1933"]]},
},
"Geographie": {
    "Plattentektonik": {"t":"Erde Schichten Kruste 5-70km dünn Mantel 2900km flüssig fest Kern 3500km Eisen 5000° Platten 5cm/Jahr wie Fingernagel divergent auseinander Rücken Island wächst konvergent zusammen Himalaya Anden Subduktion Ozean unter Kontinent Erdbeben Vulkan transform aneinander vorbei San Andreas Erdbeben Richter log10 6 ist 10x5 Tsunami Hotspot Hawaii Mantelplume Ring of Fire Pazifik", "q":[["Platten wie schnell?","5cm/Jahr","5m/Jahr"], ["Himalaya entsteht durch?","Kollision Kontinent Kontinent","Auseinander"], ["Richter ist?","log10","linear"]]},
    "Klima Wetter": {"t":"Wetter täglich kurzfristig Klima 30J Durchschnitt Klimazonen Polar -40 Eis Gemäßigt 4 Jahreszeiten Westeuropa Golfstrom Subtropen warm trocken Mittelmeer Tropen heiß feucht Regenwald Wüste 50°C Tag -10°C Nacht Temperaturumkehr Klimawandel Treibhaus CO2 280->420 +50% Methan +1,2°C Meer +20cm Gletscher -50% Extremwetter Dürre Flut Kipppunkte", "q":[["Klima ist?","30 Jahre Durchschnitt","heute Regen"], ["CO2 früher heute?","280->420 ppm","gleich"], ["Anstieg Temperatur?","+1,2°C","+5°C"]]},
    "Bevölkerung": {"t":"8Mrd 2026 Wachstum 2,5Mrd 1950 8Mrd 2026 10Mrd 2058 Demografischer Übergang 5 Phasen hohe Geburt Tod->niedrig Migration Push Krieg Armut Pull Arbeit Geld Urbanisierung 1900 10% Stadt 2026 56% Megacity 10Mio+ Tokio 37Mio Lagos Slums", "q":[["Wie viele 2026?","8 Mrd","5 Mrd"], ["Urbanisierung heute?","56% Stadt","10%"]]},
},
"Biologie": {
    "Zelle": {"t":"Prokaryot kein Kern Bakterien 1μm Eukaryot mit Kern Pflanze Tier 10-100μm Membran Doppellipid selektiv Kern Chef 46 DNA Doppelhelix Nucleolus Ribosomen bauen Ribosomen Arbeiter Protein bauen Mitochondrien Kraftwerk 1000 pro Zelle Doppelmembran eigene DNA ATP Zucker+O2->CO2+H2O+36 ATP ER Straße Transport Golgi Post verpackt Lysosom Müll Verdaung", "q":[["Kraftwerk?","Mitochondrien","Kern"], ["Mito macht?","ATP Energie","DNA"], ["46 Chromosomen?","46","23"]]},
    "Fotosynthese Zellatmung": {"t":"Pflanze Zellwand Zellulose stützt Chloroplast Solar Doppelmembran eigene DNA Chlorophyll grün absorbiert rot blau reflektiert grün Thylakoid Stapel Grana Vakuole 90% Wasserspeicher Fotosynthese 6CO2+6H2O+Licht->C6H12O6+6O2 Lichtreaktion 2H2O->O2+4H++4e- O2 kommt aus Wasser! Calvin CO2+RuBP->Zucker Nur 1-2% effizient Zellatmung umgekehrt C6H12O6+6O2->6CO2+6H2O+36 ATP im Mito", "q":[["Fotosynthese Formel?","6CO2+6H2O->Zucker+O2","Zucker+O2->CO2+H2O"], ["O2 kommt aus?","Wasser H2O","CO2"], ["Wo Fotosynthese?","Chloroplast","Mito"], ["Wo Zellatmung?","Mitochondrien","Chloroplast"]]},
    "Genetik Evolution": {"t":"DNA Doppelhelix Watson Crick 1953 A-T 2 Bindungen C-G 3 Gen Abschnitt DNA für Protein Chromosom 46 23 Paar Mitose 1->2 identisch Wachstum Wundheilung Meiose 1->4 halb 23 Geschlecht Crossing Over Bunt Mendel 1865 Erbsen dominant rezessiv 3:1 AA Aa aa Mutation Strahlung Fehler Mukoviszidose Evolution Darwin 1859 Entstehung der Arten Selektion stärkste überlebt Fossilien Archaeopteryx Urvogel Homologie gleiche Knochen DNA Mensch Schimpanse 98% gleich 6Mio Jahre getrennt", "q":[["A paart mit?","T","C"], ["46 Chromosomen Mensch?","46","23"], ["Mitose 1->?","2 identisch","4 halb"], ["Mendel Verhältnis?","3:1","1:1"], ["Mensch Schimpanse DNA?","98%","50%"]]},
},
"Chemie": {
    "Atombau PSE": {"t":"Atom Kern Proton+ 1u positiv Neutron 1u neutral Hülle Elektron 1/1836 negativ fast nichts Ordnungszahl=Protonen=Elektronen PSE nach Protonen sortiert Gruppen gleiche Valenzelektronen Gruppe1 Alkali 1 Valenz will weg +1 heftig Wasser Gruppe2 Erdalkali 2 Gruppe17 Halogen 7 will 1 -1 giftig Gruppe18 Edelgase 8 voll stabil leuchtet Periode Schalen Isotope gleiche Protonen andere Neutronen C12 C14 radioaktiv 5730 Jahre Alter", "q":[["Proton Ladung?","positiv +","negativ -"], ["Elektron Masse?","1/1836 viel kleiner","gleich"], ["Gruppe1 Valenz?","1","7"], ["Gruppe18 warum stabil?","8 voll","1"]]},
    "Bindungen": {"t":"Oktettregel 8 wollen voll stabil Ionenbindung Metall gibt Elektron ab wird + Nichtmetall nimmt wird - Metall+Nichtmetall Na+ Cl- NaCl Salz Gitter hoch 800°C spröde leitet flüssig/wässrig nicht fest Kovalente teilen Elektronen Nichtmetall+Nichtmetall H2O O2 CO2 niedrig Schmelz Metallbindung Metallgitter Elektronengas frei beweglich leitet Strom Wärme glänzt verformbar Legierung", "q":[["NaCl ist?","Ionen Metall+Nichtmetall","Kovalent"], ["Salz Schmelz?","hoch 800°C","niedrig"], ["Metall leitet weil?","Elektronengas frei","Gitter"]]},
    "Säuren Basen pH": {"t":"Brönsted Säure gibt H+ Proton ab Base nimmt H+ auf Starke Säure voll dissoziiert HCl->H++Cl- H2SO4 HNO3 Starke Base NaOH KOH schwache teilweise CH3COOH pH=-log[H+] 0-6 sauer 7 neutral 8-14 basisch pH1 Magen sauer pH7 Wasser neutral pH14 Natronlauge basisch Indikator Lackmus rot sauer blau basisch Phenolphthalein farblos sauer pink basisch Neutralisation Säure+Base->Salz+Wasser H++OH-->H2O Titration", "q":[["pH1 =?","sauer","basisch"], ["pH7 =?","neutral","sauer"], ["pH14 =?","basisch","sauer"], ["Säure gibt ab?","H+ Proton","OH-"], ["Neutralisation ->?","Salz+Wasser","nur Wasser"], ["Starke Säure?","HCl H2SO4 HNO3","CH3COOH"]]},
    "Redox": {"t":"Oxidation e- abgeben Oxidationszahl steigt Reduktion e- aufnehmen Zahl sinkt OIL RIG Oxidation Is Loss Reduction Is Gain Redox beide gleichzeitig Rost Fe->Fe3++3e- Oxidation Fe gibt e- ab O2+4e-->2O2- Reduktion O2 nimmt e- auf Gesamt 4Fe+3O2->2Fe2O3 Verbrennung C+O2->CO2 Oxidationsmittel nimmt e- auf wird selbst reduziert Reduktionsmittel gibt e- ab wird oxidiert Reihe", "q":[["Oxidation =?","e- abgeben","e- aufnehmen"], ["Reduktion =?","e- aufnehmen","e- abgeben"], ["Rost Fe+O2->?","Fe2O3","Fe"], ["Oxidationsmittel wird?","reduziert","oxidiert"]]},
},
"Deutsch": {
    "Grammatik": {"t":"Kasus Nominativ Wer? Der Mann Genitiv Wessen? des Mannes Dativ Wem? dem Mann Akkusativ Wen? den Mann Nebensatz Verb am Ende dass er kommt weil er krank ist Konjunktiv I indirekte Rede er sei er habe er solle Wenn I=Indikativ gleich dann II er hätte Konjunktiv II irreal wäre hätte würde wenn ich Zeit hätte käme ich", "q":[["Wessen? =?","Genitiv","Nominativ"], ["Nebensatz Verb wo?","am Ende","am Anfang"], ["er sei =?","Konjunktiv I","Konjunktiv II"]]},
    "Literatur": {"t":"Epik erzählt Roman Novelle Fabel Lyrik Gedicht Sonett Ballade Dramatik Theater Akt Szene Klassik Goethe Schiller Aufklärung Faust Werther Romantik Gefühl Sturm Drang Naturalismus", "q":[["Faust von?","Goethe","Schiller"]]},
},
"Englisch": {
    "Vokabeln": {"t":"bread Brot apple Apfel book Buch house Haus water Wasser time Zeit life Leben day Tag night Nacht table Tisch chair Stuhl door Tür window Fenster go gehen come kommen make machen say sagen see sehen want wollen can können take nehmen eat essen drink trinken sleep schlafen work arbeiten love lieben speak sprechen understand verstehen good gut bad schlecht big groß small klein beautiful schön new neu old alt young jung easy leicht difficult schwer here hier there dort now jetzt always immer much viel little wenig very sehr good gut bad schlecht yes ja no nein thanks danke", "q":[["bread =?","Brot","Apfel"], ["go =?","gehen","kommen"]]},
    "Zeiten": {"t":"Present I go he goes Do/Does Past I went Did you? Present Perfect I have gone have+PP since for already yet ever never Past Perfect I had gone Vorvergangenheit Future will spontan going to geplant will going to", "q":[["He __ every day","goes","go"], ["I have gone =?","Present Perfect","Past"], ["Signal already yet =?","Perfect","Past"]]},
    "if Sätze": {"t":"Type0 Naturgesetz If you heat water to 100 it boils Present Present Type1 möglich If I GO I WILL go Present will Type2 irreal jetzt If I WENT I WOULD go Past would If I were you Type3 irreal vorbei If I HAD GONE I WOULD HAVE GONE PastPerfect would have", "q":[["If I GO I __ go Type1","WILL","WOULD"], ["If I WENT I __ go Type2","WOULD","WILL"], ["If I HAD GONE I __ HAVE Type3","WOULD","WILL"]]},
    "Passive": {"t":"be+Past Participle Active I make a cake -> A cake IS MADE am/is/are+PP Past WAS MADE Perfect HAS BEEN MADE Future WILL BE MADE mit BY von mir", "q":[["A cake IS MADE =?","Passive","Active"], ["IS MADE be+?","PP Past Participle","Present"]]},
},
}

# SUCHE OBEN
st.markdown("### 🔍 Suche in allen Fächern + Wikipedia")
suche = st.text_input("", placeholder="", key="suche")

if suche:
    s=suche.lower()
    w=wiki(suche)
    if w:
        st.info(f"🌐 Wikipedia: {w[:500]}...")
    st.markdown("**Treffer in deinen Fächern:**")
    for fach, themen in DATEN.items():
        for tname, tdata in themen.items():
            if s in tname.lower() or s in tdata["t"].lower():
                st.write(f"**{fach} - {tname}:** {tdata['t'][:150]}...")

st.write("---")
st.markdown("### 📖 Alle Fächer - Klick für Themen")

# FÄCHER MIT SUCHE
cols = st.columns(3)
for i, fach in enumerate(DATEN.keys()):
    if cols[i%3].button(fach, key=f"fach_{fach}"):
        st.session_state['fach']=fach
        st.session_state.pop('unter',None)

if 'fach' in st.session_state:
    fach=st.session_state['fach']
    st.write("---")
    st.markdown(f"## 📚 {fach}")

    # SUCHE IM FACH - LEERE LEISTE
    fach_suche = st.text_input(f"🔍 In {fach} suchen + Vokabeln suchen", placeholder="", key=f"fachsuche_{fach}")

    themen_dict = DATEN[fach]
    if fach_suche:
        fs=fach_suche.lower()
        themen_dict = {k:v for k,v in themen_dict.items() if fs in k.lower() or fs in v["t"].lower()}

    # Unterthemen Buttons
    u_cols = st.columns(2)
    for j, (tname, tdata) in enumerate(themen_dict.items()):
        if u_cols[j%2].button(tname, key=f"unter_{fach}_{tname}"):
            st.session_state['unter']=tname

    # Zeige Thema + Quiz
    if 'unter' in st.session_state and st.session_state['unter'] in DATEN[fach]:
        u=st.session_state['unter']
        d=DATEN[fach][u]
        st.write("---")
        st.markdown(f"### {u}")
        st.write(d["t"])

        # Wikipedia extra
        w2=wiki(f"{u} {fach}")
        if w2:
            st.caption(f"🌐 Wikipedia: {w2[:300]}...")

        # QUIZ - IMMER SICHTBAR GELB!
        st.markdown('<div style="background:#fff8e1;padding:15px;border:3px solid #ff9800;border-radius:12px;margin:15px 0;">', unsafe_allow_html=True)
        st.markdown(f"#### 🎯 Quiz zu {u} - {len(d['q'])} Fragen")
        for qi, (frage, richtig, falsch) in enumerate(d["q"]):
            st.markdown(f"**{qi+1}. {frage}**")
            key=f"quiz_{fach}_{u}_{qi}"
            ans = st.radio("", ["--- Wählen ---", richtig, falsch], key=key, label_visibility="collapsed")
            if ans!="--- Wählen ---":
                if ans==richtig:
                    st.success(f"✅ Richtig! {richtig}")
                else:
                    st.error(f"❌ Falsch! Richtig: {richtig}")
            st.write("")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("❌ Fach schließen"):
        for k in ['fach','unter']:
            st.session_state.pop(k,None)
        st.rerun()

st.caption("Mit Vokabel-Suche + Fach-Suche + Quizze + mehr Themen Physik Italienisch Spanisch Latein")
