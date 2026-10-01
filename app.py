import streamlit as st
import requests, urllib.parse, random

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 36px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 12px; border-radius: 10px; border: 2px solid #2E86AB; margin: 8px 0; }
.quiz-box { background-color: #fff8e1; padding: 15px; border-radius: 10px; border: 3px solid #ff9800; margin: 12px 0; }
.chat-box { background-color: #e8f5e9; padding: 15px; border-radius: 10px; border: 2px solid #4caf50; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 8px; min-height: 36px; font-size: 12px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App</div>', unsafe_allow_html=True)

# TABS: Lernen + Chatbot
tab1, tab2 = st.tabs(["📖 Lernen + Quiz + Suche", "🤖 Chatbot"])

def wiki_suche(thema):
    try:
        enc = urllib.parse.quote(thema.replace(" ", "_"))
        r = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}", headers={'User-Agent':'LernApp'}, timeout=4)
        if r.status_code==200 and 'extract' in r.json():
            d=r.json()
            return d.get("extract","")
    except:
        pass
    return ""

# ALLE 12 FÄCHER MIT VIELEN THEMEN + QUIZ
alle_faecher = {
"Französisch": {
    "Vokabeln": {"t": "le pain Brot la pomme Apfel le livre Buch la maison Haus l'eau Wasser aller gehen venir kommen faire machen dire sagen voir sehen vouloir wollen pouvoir können manger essen boire trinken bon gut grand groß petit klein beau schön ici hier maintenant jetzt toujours immer", "q": [("le pain =?", "Brot", "Apfel"), ("aller =?", "gehen", "kommen"), ("bon =?", "gut", "schlecht")]},
    "le la les lui leur": {"t": "LE=ihn/es direkt COD OHNE a Je mange LE pain->Je LE mange Je vois Paul->Je LE vois LA=sie Je vois Marie->Je LA vois LES=sie Plural Je LES vois LUI=ihm/ihr indirekt COI MIT a Person Je parle À Marie->Je LUI parle LEUR=ihnen Je parle AUX enfants->Je LEUR parle", "q": [("Je mange LE pain -> Je __ mange", "LE", "LUI"), ("Je parle À Marie -> Je __ parle", "LUI", "LE"), ("Je parle AUX enfants -> __ parle", "LEUR", "LUI"), ("Je vois Marie -> Je __ vois", "LA", "LUI")]},
    "y en": {"t": "Y=dort/dahin/daran Ort mit à chez dans sur ODER à+SACHE Je vais À Paris->J'Y vais Je suis chez moi->J'Y suis Je pense À mon examen Sache->J'Y pense ABER Person Je pense À Marie->Je pense À ELLE nicht Y! EN=davon/dessen Menge mit de/du/des Zahl Je veux DU pain->J'EN veux J'ai 3 frères Zahl->J'EN ai 3 J'ai beaucoup DE livres->J'EN ai beaucoup", "q": [("Je vais À Paris -> J'__ vais", "Y", "EN"), ("J'ai 3 frères -> J'__ ai 3", "EN", "Y"), ("Je veux DU pain -> J'__ veux", "EN", "Y")]},
    "Reihenfolge": {"t": "PFLICHT: me te se nous vous + le la les + lui leur + y + en + VERB Il ME LE donne Er gibt es mir Il TE LES donne Je LE LUI donne Ich gebe es ihm Il Y EN a Es gibt davon Je M'Y habitue", "q": [("Il ME LE donne = richtige Reihenfolge?", "JA me+le", "NEIN le+me"), ("Was kommt nach le la les?", "lui leur", "me te")]},
    "indirekte Rede": {"t": "Il dit: Je suis malade Direkt Indirekt Il dit qu'il EST malade Präsens bleibt weil Einleitung Präsens! Il a dit: Je suis malade -> Il a dit qu'il ÉTAIT malade Present->Imparfait J'ai mangé->avait mangé Futur->Conditionnel Où vas-tu?->où il allait Que fais-tu?->ce que je faisais Viens!->de venir", "q": [("Il dit qu'il EST malade Einleitung Präsens Zeit?", "bleibt EST", "wird ÉTAIT"), ("Il a dit qu'il ÉTAIT malade Present->?", "Imparfait", "Futur"), ("Que fais-tu? -> __ faisais", "ce que", "que")]},
    "Zeiten": {"t": "Passé composé 14 Verben mit être aller venir arriver partir entrer sortir monter descendre rester tomber naître mourir devenir revenir + reflexiv je suis allé(e) Imparfait je parlais Hintergrund Futur je parlerai Conditionnel je parlerais Plus-que j'avais parlé", "q": [("je suis allé =?", "Passé composé mit être", "Imparfait"), ("je parlais =?", "Imparfait", "Futur"), ("je parlerais =?", "Conditionnel würde", "Passé")]},
},
"Spanisch": {
    "Vokabeln": {"t": "el pan Brot la manzana Apfel el libro Buch la casa Haus el agua Wasser ir gehen venir kommen hacer machen decir sagen ver sehen querer wollen poder können comer essen beber trinken dormir schlafen bueno malo grande pequeño aquí allí ahora siempre mucho muy", "q": [("el pan =?", "Brot", "Apfel"), ("ir =?", "gehen", "kommen"), ("la casa =?", "Haus", "Brot")]},
    "lo la le les": {"t": "LO=ihn direkt OHNE a Veo EL LIBRO->LO veo LA=sie Veo LA CASA->LA veo LOS LAS LE=ihm indirekt MIT a Hablo A JUAN->LE hablo Doy libro A MARÍA->LE doy LES=ihnen A LOS NIÑOS->LES doy", "q": [("Veo EL LIBRO -> __ veo", "LO", "LE"), ("Hablo A JUAN -> __ hablo", "LE", "LO")]},
    "se lo doy": {"t": "WICHTIGSTE REGEL: Du kannst NICHT Le lo doy sagen! FALSCH! Wenn LE/LES + LO/LA LA LOS LAS zusammen kommen wird LE/LES zu SE! Le doy el libro + lo = SE LO DOY Les doy los libros = SE LOS DOY Me lo da Te lo doy erlaubt! Nur le/les+lo/la wird SE!", "q": [("Le lo doy ist?", "FALSCH", "RICHTIG"), ("Richtig?", "SE LO DOY", "LE LO DOY"), ("Les doy los libros ->?", "SE LOS DOY", "LES LOS DOY")]},
    "ser estar": {"t": "SER=WAS IST permanent Identität Eigenschaft Herkunft Material Zeit Soy Juan Name Soy de Alemania Herkunft Soy alto Eigenschaft Son las tres Uhrzeit Es de madera Material ESTAR=WO?WIE?GERADE? Estoy en casa Ort Estoy cansado Zustand Está roto Ergebnis kaputt Estoy comiendo gerade estar+gerundio Es aburrido Charakter vs Está aburrido ihm ist langweilig gerade!", "q": [("Soy alto =?", "SER permanent", "ESTAR Zustand"), ("Estoy en casa =?", "ESTAR Ort", "SER"), ("Estoy cansado =?", "ESTAR Zustand", "SER"), ("Son las tres =?", "SER Zeit", "ESTAR")]},
    "por para": {"t": "POR=Grund Ursache Durch Tausch Dauer Warum?Wodurch? Gracias POR todo Grund Voy POR la calle durch POR dos horas Dauer 5€ POR libro Tausch PARA=Ziel Zweck Empfänger Frist Wofür? Esto es PARA comer Zweck PARA ti für dich Empfänger Voy PARA Madrid Ziel Para mañana bis morgen Frist", "q": [("Gracias ___ todo Grund", "POR", "PARA"), ("Esto es ___ comer Zweck", "PARA", "POR"), ("Voy ___ Madrid Ziel", "PARA", "POR"), ("POR dos horas =?", "Dauer", "Ziel")]},
    "Zeiten": {"t": "yo hablo Present yo hablé Pretérito yo hablaba Imperfecto hablaré Futur hablaría Condicional he hablado Perfect había hablado Pluscuam", "q": [("yo hablo =?", "Present", "Past"), ("he hablado =?", "Perfect", "Futur")]},
},
"Englisch": {
    "Vokabeln": {"t": "bread Brot apple Apfel book Buch house Haus water Wasser go come make say see want can take eat drink sleep good bad big small new old beautiful happy here there now always already much very", "q": [("bread =?", "Brot", "Apfel"), ("go =?", "gehen", "kommen")]},
    "Zeiten": {"t": "Present I go he goes Do you? Does he? Past I went Did you? Perfect I have gone have+PP since for already yet ever never Past Perfect I had gone Vorvergangenheit Future will spontan going to geplant", "q": [("He __ every day he goes mit s", "goes", "go"), ("I have gone =?", "Present Perfect", "Past"), ("Signal already yet =?", "Perfect", "Past")]},
    "if Sätze": {"t": "Type0 Natur If you heat water to 100 it boils Present Present Type1 möglich If I GO I WILL go Present will Type2 irreal jetzt If I WENT I WOULD go Past would If I were you Type3 irreal vorbei If I HAD GONE I WOULD HAVE GONE PastPerfect would have", "q": [("If I GO I __ go Type1", "WILL", "WOULD"), ("If I WENT I __ go Type2", "WOULD", "WILL"), ("If I HAD GONE I __ HAVE GONE Type3", "WOULD", "WILL")]},
    "Passive": {"t": "be+Past Participle Active I make a cake -> A cake IS MADE am/is/are+PP Past WAS MADE Perfect HAS BEEN MADE Future WILL BE MADE mit BY von mir", "q": [("A cake IS MADE =?", "Passive Present", "Active"), ("IS MADE be+?", "PP Past Participle", "Present")]},
    "indirekte Rede": {"t": "He says I am ill -> He says he IS ill bleibt He said I am ill -> He said he WAS ill Present->Past Where are you?->where I WAS Do you come?->if I came Come!->to come", "q": [("He says he IS ill Zeit bleibt weil says Present?", "JA bleibt IS", "NEIN WAS")]},
},
"Italienisch": {
    "Vokabeln": {"t": "il pane Brot la mela Apfel il libro Buch la casa Haus l'acqua Wasser andare gehen venire kommen fare machen dire sagen vedere sehen volere wollen potere können mangiare essen bere trinken dormire schlafen buono cattivo grande piccolo qui là ora sempre molto bene", "q": [("il pane =?", "Brot", "Apfel"), ("andare =?", "gehen", "kommen"), ("la casa =?", "Haus", "Brot")]},
    "lo la gli li": {"t": "LO=ihn masc Vedo IL LIBRO->LO vedo LA=sie fem Vedo LA CASA->LA vedo LI=masc Plural Vedo I LIBRI->LI vedo LE=fem Plural Vedo LE CASE->LE vedo GLI=ihm/ihr/ihnen MIT a Parlo A GIOVANNI->GLI parlo Parlo AI bambini->GLI parlo", "q": [("Vedo IL LIBRO -> __ vedo", "LO", "GLI"), ("Parlo A GIOVANNI -> __ parlo", "GLI", "LO"), ("Vedo I LIBRI masc Plural -> __ vedo", "LI", "LO")]},
    "ci ne": {"t": "CI=y dort/daran Ort Sache Vado A Parigi->CI vado Vado A CASA->CI vado CI penso daran Sache NE=en davon de Zahl Voglio DEL pane->NE voglio Ho 3 fratelli Zahl->NE ho 3 NE ho molti", "q": [("Vado A Parigi -> __ vado", "CI", "NE"), ("Voglio DEL pane -> __ voglio", "NE", "CI"), ("Ho 3 fratelli -> __ ho 3", "NE", "CI")]},
    "glielo essere stare": {"t": "GLIELO=gli+lo zusammen wie SE LO DOY Glielo do Ich gebe es ihm Glielo dico Ich sage es ihm Me lo da Te lo do Ce lo ha ESSERE=WAS IST permanent Sono Giovanni Sono di Germania Sono alto Sono le 3 Uhrzeit STARE=WO?WIE?GERADE? Sto a casa Ort Sto male krank Zustand Sta rotto kaputt Ergebnis Sto mangiando gerade stare+gerundio", "q": [("Glielo do =?", "Ich gebe es ihm", "Ich bin dort"), ("Sono Giovanni = ESSERE oder STARE?", "ESSERE", "STARE"), ("Sto a casa =?", "STARE Ort", "ESSERE"), ("Sto mangiando = gerade?", "JA stare+gerundio", "NEIN")]},
    "Zeiten": {"t": "io parlo Present ho parlato Passato prossimo parlavo Imperfetto parlerò Futuro parlerei Condizionale", "q": [("io parlo =?", "Present", "Past"), ("ho parlato =?", "Passato prossimo", "Present")]},
},
"Latein": {
    "Vokabeln": {"t": "panis Brot malum Apfel liber Buch casa Haus aqua Wasser ire gehen facere machen dicere sagen videre sehen velle wollen posse können bonus gut malus schlecht magnus groß parvus klein hic hier nunc jetzt ego ich tu du is ea id er sie es nos wir", "q": [("panis =?", "Brot", "Apfel"), ("ire =?", "gehen", "kommen"), ("ego =?", "ich", "du")]},
    "Kasus": {"t": "Nominativ Wer?Was? puella Subjekt Genitiv Wessen? puellae des Mädchens Dativ Wem? puellae dem Mädchen Akkusativ Wen?Was? puellam das Mädchen Ablativ Womit?Wo?Wann? cum puella mit Mädchen in villa", "q": [("Wer?Was? =?", "Nominativ", "Genitiv"), ("Wessen? =?", "Genitiv", "Nominativ"), ("puellam =?", "Akkusativ", "Nominativ")]},
    "Deklinationen": {"t": "1.a puella Gen puellae 2.o servus Gen servi bellum Gen belli 3.rex Gen regis corpus Gen corporis 4.u fructus Gen fructus 5.e res Gen rei", "q": [("puella Gen?", "puellae", "puellam"), ("servus Gen?", "servi", "servus"), ("rex Gen?", "regis", "rex")]},
    "AcI": {"t": "AcI Akkusativ mit Infinitiv nach sagen denken Dico eum venire Ich sage dass er kommt eum Akk venire Inf Dico eum venisse dass er gekommen ist Dico eum venturum esse dass er kommen wird", "q": [("Dico eum venire =?", "Ich sage dass er kommt", "Ich komme"), ("eum im AcI =?", "Akkusativ", "Nominativ")]},
    "Gerundium Partizip": {"t": "Gerundium amandum das Lieben Ad amandum Zum Lieben PPA amans liebend PPP amatus geliebt worden PFA amaturus im Begriff zu lieben", "q": [("amans =?", "liebend PPA", "geliebt"), ("amatus =?", "geliebt PPP", "liebend"), ("Ad amandum =?", "Zum Lieben", "des Liebens")]},
},
"Deutsch": {
    "Konjunktiv": {"t": "Konjunktiv I indirekte Rede er sei er habe er solle Wenn I=Indikativ gleich dann II er hätte Konjunktiv II irreal wäre hätte würde wenn ich Zeit hätte käme ich", "q": [("er sei =?", "Konjunktiv I indirekte", "Konjunktiv II"), ("wenn ich Zeit hätte =?", "Konjunktiv II irreal", "Konjunktiv I")]},
    "Kasus": {"t": "Nominativ Wer? Der Mann Genitiv Wessen? des Mannes Dativ Wem? dem Mann Akkusativ Wen? den Mann Nebensatz Verb am Ende dass er kommt", "q": [("Wessen? =?", "Genitiv", "Nominativ"), ("Nebensatz Verb wo?", "am Ende", "am Anfang")]},
},
"Mathe": {
    "Brüche Prozent": {"t": "1/4+2/4=3/4 1/2+1/3=5/6 Multi 1/2*3/4=3/8 Divi Kehrwert 1/2:1/4=2 Prozent %= /100 Dreisatz 100%=50 1%=0,5 20%=10", "q": [("1/4+2/4=?", "3/4", "3/8"), ("1/2:1/4=?", "2", "1/8"), ("20% von 50=?", "10", "20")]},
    "Gleichungen": {"t": "Waage beide Seiten gleich 2x+4=10 x=3 Mitternacht x=(-b±√(b²-4ac))/2a pq x=-p/2±√((p/2)²-q) D>0 2 Lösungen D=0 1 D<0 keine", "q": [("2x+4=10 x=?", "3", "5"), ("Mitternacht Formel?", "(-b±√...)/2a", "a+b")]},
    "Geometrie": {"t": "Pythagoras a²+b²=c² nur 90° 3²+4²=5² Rechteck a*b Kreis 2πr πr² Quader a*b*c Würfel a³ Zylinder πr²*h Kugel 4/3πr³ sin=GK/Hyp cos=AK/Hyp tan=GK/AK sin²+cos²=1", "q": [("a²+b²=?", "c²", "a²"), ("3 4 5 weil?", "9+16=25", "3+4=5"), ("Kreis Umfang?", "2πr", "πr²")]},
    "Ableitung Integral": {"t": "x^n->n*x^(n-1) x³->3x² Produkt u'v+uv' Kette f'=0 Extrem Hoch Tief Integral ∫x^n=x^(n+1)/(n+1)+C Fläche F(b)-F(a)", "q": [("x³ abgeleitet?", "3x²", "x²"), ("f'=0 bedeutet?", "Extrem", "Nullstelle")]},
    "Wahrscheinlichkeit": {"t": "P=günstige/alle Würfel P(6)=1/6 UND multi ODER add Baum Pfad multi Binomial (n über k)*p^k*(1-p)^(n-k)", "q": [("P(6) Würfel=?", "1/6", "1/3"), ("UND im Baum?", "multi", "add")]},
},
"Geschichte": {
    "französische revolution": {"t": "1789 1.Stand 1% 10% Land keine Steuern 2.Stand 2% 20% keine Steuern 3.Stand 97% zahlt alles Ludwig XVI pleite Hunger Aufklärung Rousseau 14.7. Bastille 26.8. Menschenrechte 21.1.93 Ludwig geköpft Robespierre 40k 1799 Napoleon", "q": [("Wann Bastille?", "14.7.1789", "1789"), ("3.Stand wie viel %?", "97%", "1%"), ("Wer geköpft 21.1.93?", "Ludwig XVI", "Napoleon")]},
    "industrialisierung": {"t": "1760 England Kohle Eisen Watt Dampfmaschine 1769 Fabriken Manchester 25k->300k 16h Kinderarbeit Marx 1848 SPD 1875 Eisenbahn 1835", "q": [("Wann Dampfmaschine Watt?", "1769", "1789"), ("Manchester 25k->?", "300k", "25k")]},
    "1 weltkrieg": {"t": "1914-18 Imperialismus Sarajevo 28.6.14 Princip Franz Ferdinand Mittelmächte DE Ö vs Entente FR RU EN Schlieffenplan Belgien Schützengraben 700km Verdun 700k 11.11.18 Waffenstillstand Versailles 28.6.19 132Mrd 17Mio Tote", "q": [("Auslöser 1.WK?", "Sarajevo 28.6.14", "Bastille"), ("Wann Waffenstillstand?", "11.11.18", "28.6.19"), ("Wie viele Tote?", "17 Mio", "1 Mio")]},
    "2 weltkrieg": {"t": "1939-45 Versailles Krise Hitler 33 1.9.39 Polen Blitzkrieg 1940 Frankreich 22.6.41 Russland 7.12.41 Pearl Harbor Holocaust 6Mio Auschwitz Wannsee 20.1.42 Stalingrad D-Day 6.6.44 8.5.45 Hiroshima 6.8.45 140k Nagasaki 70k 60Mio Tote", "q": [("Beginn 2.WK?", "1.9.39 Polen", "1940"), ("Holocaust wie viele?", "6 Mio Juden", "1 Mio"), ("Hiroshima wann?", "6.8.45", "1940")]},
    "kalter krieg mauer": {"t": "1947-90 USA vs UdSSR Berlin Blockade 48-49 Luftbrücke NATO 49 Warschauer Pakt 55 Mauer 13.8.61-9.11.89 28J 155km 140 Tote Kuba 62 Vietnam 65-75 Brandt Ostpolitik Gorbatschow Montagsdemos 9.11.89 Fall 3.10.90 Einheit BRD 23.5.49 DDR 7.10.49", "q": [("Mauer wann gebaut?", "13.8.61", "9.11.89"), ("Wie lange Mauer?", "28 Jahre", "10 Jahre"), ("Wann Einheit?", "3.10.90", "9.11.89")]},
    "usa hitler": {"t": "USA 1776 Unabhängigkeit 13 Kolonien Washington 1861-65 Bürgerkrieg Lincoln Sklaverei Ende 340Mio Hitler 1889-1945 Braunau NSDAP 1933 Diktator 2.WK Holocaust Selbstmord 30.4.45", "q": [("USA Unabhängigkeit?", "1776", "1789"), ("Hitler Machtergreifung?", "30.1.33", "1945")]},
},
"Geographie": {
    "Plattentektonik": {"t": "Kruste 5-70km Mantel 2900km Kern 5000° 5cm/Jahr divergent Rücken Island wächst konvergent Himalaya Anden Subduktion Erdbeben Vulkan transform San Andreas Richter log10 Tsunami Hotspot Hawaii Ring of Fire", "q": [("Platten wie schnell?", "5cm/Jahr", "5m/Jahr"), ("Himalaya entsteht durch?", "Kollision Kontinent Kontinent", "Auseinander"), ("Richter Skala ist?", "log10", "linear")]},
    "Klima": {"t": "Wetter täglich Klima 30J Durchschnitt Zonen Polar -40 Eis Gemäßigt 4 Jahreszeiten Subtropen warm trocken Tropen heiß feucht Wüste 50°C Tag -10°C Nacht Klimawandel CO2 280->420 +50% +1,2°C Meer +20cm Gletscher Extremwetter", "q": [("Klima ist?", "30 Jahre Durchschnitt", "heute Regen"), ("CO2 früher heute?", "280->420 ppm", "gleich"), ("Temperaturanstieg?", "+1,2°C", "+5°C")]},
    "Bevölkerung": {"t": "8Mrd 2026 Demografischer Übergang 5 Phasen Migration Push Krieg Armut Pull Arbeit Urbanisierung 1900 10% Stadt 2026 56% Megacity 10Mio+ Tokio 37Mio", "q": [("Wie viele Menschen 2026?", "8 Mrd", "5 Mrd"), ("Urbanisierung heute?", "56% Stadt", "10%")]},
},
"Biologie": {
    "Zelle": {"t": "Prokaryot kein Kern 1μm Eukaryot mit Kern 10-100μm Membran Doppellipid Kern Chef 46 DNA Nucleolus Ribosomen Arbeiter Protein Mitochondrien Kraftwerk 1000 Doppelmembran eigene DNA ATP Zucker+O2->CO2+H2O+36 ATP ER Straße Golgi Post Lysosom Müll", "q": [("Kraftwerk?", "Mitochondrien", "Kern"), ("Mitochondrien macht?", "ATP Energie", "DNA"), ("Wie viele Chromosomen?", "46", "23")]},
    "Fotosynthese": {"t": "Pflanze Zellwand Zellulose Chloroplast Solar Doppelmembran eigene DNA Chlorophyll grün absorbiert rot blau reflektiert grün Thylakoid Grana Vakuole 90% Fotosynthese 6CO2+6H2O+Licht->Zucker+O2 Licht 2H2O->O2+4H++4e- O2 aus Wasser Calvin CO2+RuBP->Zucker Nur 1-2%", "q": [("Formel Fotosynthese?", "6CO2+6H2O->Zucker+O2", "Zucker+O2->CO2+H2O"), ("O2 kommt aus?", "Wasser H2O", "CO2"), ("Chlorophyll Farbe?", "grün", "rot")]},
    "Genetik": {"t": "DNA Doppelhelix Watson Crick 1953 A-T 2 C-G 3 Gen Abschnitt Chromosom 46 23 Paar Mitose 1->2 identisch Wachstum Meiose 1->4 halb 23 Crossing Over Mendel 1865 dominant rezessiv 3:1 Mutation Strahlung Mukoviszidose Evolution Darwin 1859 Selektion Fossilien Archaeopteryx Homologie DNA Mensch Schimpanse 98% 6Mio getrennt", "q": [("A paart mit?", "T", "C"), ("46 Chromosomen Mensch?", "46", "23"), ("Mendel Verhältnis?", "3:1", "1:1"), ("Mensch Schimpanse DNA?", "98%", "50%")]},
},
"Physik": {
    "Mechanik": {"t": "v=s/t 100km/h=27,8m/s a=v/t Freier Fall s=0,5*g*t² g=9,81 2s 19,6m v=g*t 2s 19,6m/s", "q": [("100km/h =?", "27,8 m/s", "100 m/s"), ("Freier Fall s=?", "0,5*g*t²", "g*t")]},
    "Newton": {"t": "Newton1 ohne Kraft Ruhe gleichförmig Newton2 F=m*a 1N=1kg*1m/s² 2kg*3=6N Gewicht m*g 70kg=686N Newton3 Actio=Reactio Wand drückt dich Rakete Gas unten Rakete oben", "q": [("F=m*a F=?", "m*a", "m*g"), ("70kg Gewicht?", "686N", "70N"), ("Actio=Reactio =?", "Newton3", "Newton2")]},
    "Energie": {"t": "Energie bleibt erhalten umgewandelt Kinetisch 0,5*m*v² 1000kg 20m/s 200kJ Potentiell m*g*h 70kg 10m 6867J Leistung P=E/t Watt kW kWh 1kWh=3,6Mio J", "q": [("0,5*m*v² =?", "kinetisch", "potentiell"), ("m*g*h =?", "potentiell", "kinetisch"), ("1kWh =?", "3,6 Mio J", "1000 J")]},
    "Strom": {"t": "U Volt Druck I Ampere Menge R Ohm Hindernis R=U/I 12V 3Ω I=4A Reihe Rges=R1+R2 2+3=5Ω Parallel 1/R=1/R1+1/R2 2//2=1Ω P=U*I 230V 10A 2300W kWh 50mA gefährlich", "q": [("R=U/I?", "U/I", "U*I"), ("12V 3Ω I=?", "4A", "36A"), ("Reihe 2+3=?", "5Ω", "1Ω"), ("Parallel 2//2=?", "1Ω", "4Ω"), ("P=U*I 230V 10A=?", "2300W", "23W")]},
    "Optik": {"t": "Reflexion Einfall=Ausfall Brechung Wasser Stab knick Linse sammelt Brennpunkt f=1/D Auge kurz weitsichtig Farben 400-700nm Prisma Regenbogen Laser gebündelt", "q": [("Einfall=Ausfall =?", "Reflexion", "Brechung"), ("Weiß durch Prisma?", "Farben Regenbogen", "weiß bleibt"), ("400-700nm ist?", "Licht Farben", "Strom")]},
    "Kern": {"t": "Uran235 Spaltung Neutron E=mc² 1g Uran=3 Tonnen Kohle Kettenreaktion Kraftwerk moderiert Bombe unkontrolliert Fusion Sonne H->He 15Mio Grad Alpha Beta Gamma Halbwertszeit", "q": [("Brennstoff Kern?", "Uran235", "Eisen"), ("E=mc² bedeutet?", "Masse=Energie", "F=m*a"), ("Fusion wo?", "Sonne", "Kraftwerk")]},
},
"Chemie": {
    "Atombau": {"t": "Kern Proton+ 1u positiv Neutron 1u neutral Hülle Elektron 1/1836 negativ Ordnungszahl=Protonen PSE nach Protonen Gruppen gleiche Valenz Gruppe1 Alkali 1 will weg +1 Gruppe17 Halogen 7 will 1 -1 Gruppe18 Edelgase 8 voll stabil Isotope C12 C14 5730 Jahre", "q": [("Proton Ladung?", "positiv +", "negativ -"), ("Elektron Masse?", "1/1836 viel kleiner", "gleich"), ("Gruppe1 hat wie viele Valenz?", "1", "7")]},
    "Bindungen": {"t": "Oktett 8 wollen voll Ionen Metall gibt Nichtmetall nimmt Metall+Nichtmetall Na+ Cl- NaCl Salz Gitter hoch 800°C spröde leitet flüssig Kovalent teilen Nichtmetall+Nichtmetall H2O niedrig Metall Elektronengas leitet glänzt", "q": [("NaCl ist?", "Ionen Metall+Nichtmetall", "Kovalent"), ("Salz Schmelz?", "hoch 800°C", "niedrig"), ("Metall leitet weil?", "Elektronengas frei", "Gitter")]},
    "Säuren Basen": {"t": "Brönsted Säure gibt H+ ab Base nimmt H+ Starke voll HCl->H++Cl- schwache teilweise pH=-log[H+] 0-6 sauer 7 neutral 8-14 basisch pH1 Magen pH7 Wasser pH14 Natronlauge Lackmus rot sauer blau basisch Phenol farblos sauer pink basisch HCl H2SO4 HNO3 stark NaOH stark Neutralisation Säure+Base->Salz+Wasser H++OH-->H2O", "q": [("pH1 =?", "sauer", "basisch"), ("pH7 =?", "neutral", "sauer"), ("pH14 =?", "basisch", "sauer"), ("Säure gibt ab?", "H+ Proton", "OH-"), ("Neutralisation Säure+Base->?", "Salz+Wasser", "nur Wasser")]},
    "Redox": {"t": "Oxidation e- abgeben Zahl steigt Reduktion e- aufnehmen sinkt OIL RIG Rost Fe->Fe3++3e- Oxidation O2+4e-->2O2- Reduktion 4Fe+3O2->2Fe2O3 Verbrennung C+O2->CO2 Oxidationsmittel nimmt e- auf wird reduziert Reduktionsmittel gibt e- ab wird oxidiert", "q": [("Oxidation =?", "e- abgeben", "e- aufnehmen"), ("Reduktion =?", "e- aufnehmen", "e- abgeben"), ("Rost Fe+O2->?", "Fe2O3", "Fe")]},
},
}

with tab1:
    st.markdown('<div class="search-box">', unsafe_allow_html=True)
    st.write("🔍 Suche in allen Fächern + Internet")
    thema = st.text_input("", placeholder="", label_visibility="collapsed", key="haupt2")
    st.markdown('</div>', unsafe_allow_html=True)

    if thema:
        st.write(f"**Fakten für '{thema}':**")
        wiki = wiki_suche(thema)
        if wiki:
            st.info(f"🌐 Wikipedia: {wiki[:500]}...")
        s=thema.lower()
        for fach, unter in alle_faecher.items():
            for u_name, u_data in unter.items():
                if s in u_name.lower() or s in u_data["t"].lower():
                    st.write(f"**{fach} - {u_name}:** {u_data['t'][:200]}...")

    st.write("---")
    st.markdown("### 📖 Alle 12 Fächer - Klicken für Themen + Quiz")

    cols = st.columns(3)
    for i, fach_name in enumerate(alle_faecher.keys()):
        if cols[i % 3].button(fach_name, key=f"btn_{fach_name}"):
            st.session_state['fach'] = fach_name
            st.session_state.pop('unter', None)

    if 'fach' in st.session_state:
        fach = st.session_state['fach']
        st.write("---")
        st.markdown(f"## 📚 {fach}")

        sub_suche = st.text_input(f"In {fach} suchen:", placeholder="", key=f"sub_{fach}")

        unter_dict = alle_faecher[fach]
        show_dict = unter_dict
        if sub_suche:
            ss=sub_suche.lower()
            show_dict = {k:v for k,v in unter_dict.items() if ss in k.lower() or ss in v["t"].lower()}

        u_cols = st.columns(2)
        for j, u_name in enumerate(show_dict.keys()):
            if u_cols[j % 2].button(u_name, key=f"u_{fach}_{u_name}"):
                st.session_state['unter'] = u_name

        if 'unter' in st.session_state and st.session_state['unter'] in unter_dict:
            u = st.session_state['unter']
            data = unter_dict[u]
            st.write("---")
            st.markdown(f"### {u}")
            st.write(data["t"])
            wiki_extra = wiki_suche(f"{u} {fach}")
            if wiki_extra:
                st.caption(f"🌐 Wikipedia: {wiki_extra[:300]}...")

            # QUIZ FIX IMMER SICHTBAR
            st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Quiz zu {u}")

            for qi, (frage, richtig, falsch) in enumerate(data["q"]):
                st.markdown(f"**{qi+1}. {frage}**")
                # Radio mit Key
                key = f"quiz_{fach}_{u}_{qi}"
                if key not in st.session_state:
                    st.session_state[key] = "--- Wählen ---"
                auswahl = st.radio("Wähle", ["--- Wählen ---", richtig, falsch], key=key, label_visibility="collapsed", horizontal=True)
                if auswahl!= "--- Wählen ---":
                    if auswahl == richtig:
                        st.success(f"✅ Richtig! {richtig}")
                    else:
                        st.error(f"❌ Falsch! Richtig: {richtig}")
            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("❌ Fach schließen"):
            for k in ['fach','unter']:
                st.session_state.pop(k, None)
            st.rerun()

with tab2:
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    st.markdown("### 🤖 Chatbot - Frag mich alles zum Lernen!")
    st.markdown("Ich helfe dir bei allen Fächern: Französisch le la lui, Spanisch ser estar, Mathe, Geschichte, Bio, Physik, Chemie... Schreib einfach!")
    st.markdown('</div>', unsafe_allow_html=True)

    if 'chat' not in st.session_state:
        st.session_state['chat'] = [{"role":"assistant","content":"Hey! Ich bin dein Lern-Chatbot 📚 Frag mich z.B. 'Erklär mir le la lui' oder 'Was ist ser estar?' oder 'Erklär Fotosynthese'"}]

    for msg in st.session_state['chat']:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    frage = st.chat_input("Frag mich was... z.B. le la lui erklären")

    if frage:
        st.session_state['chat'].append({"role":"user","content":frage})
        with st.chat_message("user"):
            st.write(frage)

        # BOT ANTWORT LOGIK
        f = frage.lower()
        antwort = ""

        # Suche in allen Fächern
        for fach, unter in alle_faecher.items():
            for u_name, u_data in unter.items():
                if u_name.lower() in f or any(w in f for w in u_name.lower().split()):
                    antwort = f"**{fach} - {u_name}:**\n\n{u_data['t']}\n\nWillst du ein Quiz dazu machen? Geh zu Lernen Tab und klick auf {u_name}!"
                    break
            if antwort:
                break

        if not antwort:
            if "le" in f and "lui" in f or "le la" in f:
                antwort = alle_faecher["Französisch"]["le la les lui leur"]["t"] + "\n\nBeispiel: Je mange LE pain -> Je LE mange (direkt ohne a) / Je parle À Marie -> Je LUI parle (mit a Person!)"
            elif "y" in f and "en" in f:
                antwort = alle_faecher["Französisch"]["y en"]["t"]
            elif "ser" in f and "estar" in f:
                antwort = alle_faecher["Spanisch"]["ser estar"]["t"]
            elif "se lo" in f:
                antwort = alle_faecher["Spanisch"]["se lo doy"]["t"]
            elif "por para" in f or "por" in f:
                antwort = alle_faecher["Spanisch"]["por para"]["t"]
            elif "fotosynthese" in f or "fotosyn" in f:
                antwort = alle_faecher["Biologie"]["Fotosynthese"]["t"]
            elif "mito" in f or "zelle" in f:
                antwort = alle_faecher["Biologie"]["Zelle"]["t"]
            elif "pythagoras" in f:
                antwort = alle_faecher["Mathe"]["Geometrie"]["t"]
            elif "newton" in f or "f=m" in f:
                antwort = alle_faecher["Physik"]["Newton"]["t"]
            elif "strom" in f or "ohm" in f:
                antwort = alle_faecher["Physik"]["Strom"]["t"]
            elif "ph " in f or "säure" in f:
                antwort = alle_faecher["Chemie"]["Säuren Basen"]["t"]
            else:
                # Wikipedia fallback
                wiki = wiki_suche(frage)
                if wiki:
                    antwort = f"🌐 Aus Wikipedia:\n\n{wiki}\n\nFrag mich noch was dazu!"
                else:
                    antwort = f"Zu '{frage}' hab ich lokal: Schau im Lernen Tab bei allen Fächern! Oder frag genauer z.B. 'le la lui', 'ser estar', 'Fotosynthese', 'Newton', 'pH', 'Pythagoras', 'Mauer', 'Französische Revolution' - ich erkläre alles!"

        with st.chat_message("assistant"):
            st.write(antwort)
        st.session_state['chat'].append({"role":"assistant","content":antwort})
        st.rerun()
