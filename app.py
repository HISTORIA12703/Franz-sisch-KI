import streamlit as st

st.set_page_config(page_title="Alle Fächer Ultra Lang", page_icon="📚", layout="wide")
st.title("📚 v28 - ALLE FÄCHER ULTRA LANG - KOMPLETT")
st.subheader("Französisch | Spanisch | Englisch | Italienisch | Latein | Deutsch | Mathe | Geschichte | Geo | Bio | Physik | Chemie")
st.write("---")

# SUCHE
suche = st.text_input("🔍 SUCHE - Gib Thema ein (z.B. y en, Se lo doy, If Sätze, Fotosynthese, Ableitung, Revolution, Atombau):", "")

# DATENBANK - ALLE FÄCHER ULTRA LANG
faecher = {

"Französisch": """
**PRONOMEN LE LA LUI Y EN - ULTRA AUSFÜHRLICH:**

LE=IHN männlich COD Wen?Was? OHNE a: Je mange LE pain -> Je LE mange. WANN? Kein a dahinter! Frage Wen?Was?

LA=SIE weiblich COD: Je vois MARIE -> Je LA vois. Je mange LA pomme -> Je LA mange.

LES=SIE Plural COD: Je vois LES pommes -> Je LES vois.

LUI=IHM IHR COI Wem? MIT a: Je parle À MARIE -> Je LUI parle. Je donne le livre À PAUL -> Je LUI donne. WANN? Mit à vor Person!

LEUR=IHNEN COI Plural: Je parle AUX enfants -> Je LEUR parle.

Y=DORT DORTHIN DARAN Ort mit à chez dans: Je vais À PARIS -> J'Y vais. Je pense À l'examen (Sache) -> J'Y pense. WANN? Ort oder à+Sache nicht Person!

EN=DAVON Menge mit de du des Zahl: Je veux DU pain -> J'EN veux. J'ai 2 pommes -> J'EN ai 2. Je parle DE mon voyage -> J'EN parle. WANN? de/du/des/Zahl!

REIHENFOLGE: me te se nous vous + le la les + lui leur + y + en + VERB. Il ME LE donne, Il Y EN a, Je M'Y habitue.

POSSESSIV: mon ma mes mein ton ta tes dein son sa ses sein notre nos unser. Le mien meiner C'est le mien gehört mir.

RELATIV: qui der Subjekt L'homme QUI parle, que den Objekt Le livre QUE je lis, où wo La ville OÙ j'habite, dont von dem L'homme DONT je parle parler DE.

DIREKTE INDIREKTE REDE:
Direkt Il dit: "Je suis malade."
Indirekt Il dit qu'il est malade Zeit BLEIBT bei Präsens Einleitung.
Il a dit qu'il était malade Zeit ÄNDERN Present->Imparfait J'ai mangé->avait mangé Futur->Conditionnel J'irai->irait.
Fragen Où vas-tu?->où il allait, Que fais-tu?->ce qu'il faisait que->ce que! JaNein Tu viens?->si il venait ob.
Befehl Viens!->de venir.

ZEITEN: Passé composé avoir/etre+Partizip 14 Verben mit etre aller venir partir arriver naître mourir entrer sortir monter descendre rester tomber retourner + angleichen Elle est allée. Imparfait je parlais Gewohnheit Quand j'étais petit je jouais. Futur parlerai serai aurai irai ferai proche Je vais manger Futur antérieur J'aurai fini.
""",

"Spanisch": """
**SE LO DOY REGEL - ULTRA AUSFÜHRLICH:**

LO LA = Wen?Was? direkt OHNE a: Veo EL LIBRO -> LO veo. Veo LA CASA -> LA veo.

LE LES = Wem? MIT a: Hablo A JUAN -> LE hablo. Doy el libro A MARIA -> LE doy.

VERBOTEN LE LO! Le lo doy FALSCH! RICHTIG SE LO DOY! Wenn le/les + lo/la zusammen -> le/les wird SE! Spurious se! Me lo da erlaubt nur le+lo verboten!

SER vs ESTAR:
SER permanent WAS IST: Soy Juan Identität, Soy de Alemania Herkunft, Soy alto groß Eigenschaft, Es grande, Son las 3 Uhrzeit, Es de madera Material. Merke WAS IST ES?
ESTAR Ort Zustand gerade: Estoy en casa Ort, Estoy cansado müde Zustand, Está roto kaputt Ergebnis, Estoy comiendo esse gerade Verlaufsform! Merke Ort+Zustand+gerade!

POR vs PARA:
POR Grund Durch Tausch Dauer: Gracias POR todo Grund, Voy POR la calle durch, POR la mañana morgens, POR 2 horas Dauer, Te doy 5€ POR el libro Tausch.
PARA Ziel Zweck Empfänger Frist: Esto es PARA comer zum Essen Zweck, Para ti für dich Empfänger, Voy PARA Madrid nach Madrid Ziel, Para mañana bis morgen Frist, Para mi es difícil für mich Meinung.
TRICK POR=Warum? Wodurch? PARA=Wofür? Wohin? Für wen?

Y EN gibt es nicht: J'y vais=Voy allí, J'en veux=Quiero de ello.

Indirekte Rede: Dice que está enfermo bleibt, Dijo que estaba enfermo ändert Present->Imperfecto Futuro->Condicional.
""",

"Englisch": """
**ENGLISCH ULTRA AUSFÜHRLICH:**

PRONOMEN: I you he she it we they, me him her us them, my your his her our their, mine yours his hers ours theirs, myself yourself himself.

ZEITEN 12:
Present Simple I go Gewohnheit I go every day he she it goes mit s Do you go? Does he go? don't doesn't Signal every day always.
Past Simple I went einmalig Yesterday I went regelmäßige ed unregelmäßige went had Did you go? didn't Signal yesterday ago.
Present Perfect I have gone Ergebnis jetzt I have eaten I am full have has + PP 3.Form go went gone Signal already yet just ever never since for.
Past Perfect I had gone Vorvergangenheit Before I came he had left.
Future will spontan I will go I think will, going to geplant I am going to go, Present Continuous Plan I am going tomorrow.

INDIREKTE REDE:
He says: "I am ill." -> He says he IS ill Zeit BLEIBT bei says Präsens.
He said: "I am ill." -> He said he WAS ill Zeit ZURÜCK Present->Past Past->Past Perfect will->would can->could.
Fragen Where are you?->where he WAS, What do you do?->what he DID, Do you come?->if he CAME ob.
Befehl Come!->to come.

IF SÄTZE:
Type0 Naturgesetz If you heat water to 100 it boils If+Present Present.
Type1 möglich If I GO I WILL go If+Present will.
Type2 irreal jetzt If I WENT I WOULD go If+Past would+Inf If I were you.
Type3 irreal vorbei If I HAD GONE I WOULD HAVE GONE If+Past Perfect would have+PP.

PASSIVE be+PP: Active I make a cake -> Passive A cake IS MADE am is are+PP Past was were+PP Perfect has been+PP Future will be+PP Progressive is being+PP. By Agens The book was written BY Shakespeare.
""",

"Italienisch": """
**ITALIENISCH ULTRA:**

CI NE = Y EN Gleiches System! Ci vado=J'y vais dort, Ne voglio=J'en veux davon.

PRONOMEN lo la li le direkt Lo vedo, indirekt gli ihm ihnen le ihr Gli parlo, Kombination gli+lo=glielo Glielo do gebe es ihm! Me lo da Ce ne sono Es gibt davon.

ESSERE vs STARE: Essere permanent Sono tedesco È grande, Stare Ort Zustand gerade Sto a casa Ort Sto male Zustand Sto mangiando esse gerade Verlaufsform Sto per mangiare gleich essen.

ARTIKEL al del nel: a+il=al de+il=del in+il=nel su+il=sul il lo la i gli le un uno una lo vor s+Konsonant lo studente.

Zeiten Futur parlerò avrò sarò andrò farò, Passato ho parlato sono andato 14 Verben wie Französisch, Imperfetto parlavo.
""",

"Latein": """
**LATEIN ULTRA:**

PRONOMEN ego ich tu du is ea id er sie es hic dieser ille jener ipse selbst qui quae quod der die das.

KASUS 5 Fälle: Nominativ wer? Puella Mädchen, Genitiv wessen? Puellae des Mädchens, Dativ wem? Puellae dem Mädchen, Akkusativ wen? Puellam das Mädchen, Ablativ womit? wo? Puella mit Mädchen. Deklinationen 1. a puella 2. o servus dominus 3. kons. rex regis 4. u fructus 5. e res rei.

AcI Accusativus cum Infinitivo nach sagen denken wissen: Dico eum venire Ich sage dass er kommt wörtlich Ich sage ihn kommen. Oratio obliqua indirekte Rede mit Konjunktiv.

Gerundium -ung amandum das Lieben, PPA Partizip Präsens Aktiv -nd amans liebend, PPP -t amatus geliebt worden.

Zeiten Präsens amo Imperfekt amabam Perfekt amavi Plusquam amaveram Futur amabo Konjunktiv amem amer.
""",

"Deutsch": """
**DEUTSCH ULTRA:**

PRONOMEN ich du er sie es wir ihr sie mich dich ihn sich mein dein sein unser euer ihr der die das welcher.

KONJUNKTIV I INDIREKTE REDE: Direkt Er sagt: "Ich bin krank." -> Indirekt Er sagt er SEI krank. Bildung ich sei du seiest er sei wir seien ihr seiet sie seien. haben er habe du habest, sein er sei, werden er werde, können er könne sollen er solle. Wenn Konjunktiv I = Indikativ dann Konjunktiv II Ersatz: sie haben -> sie hätten (statt haben weil gleich). Sie sagt sie HÄTTEN kein Geld.

KASUS: Nominativ wer? Der Mann, Genitiv wessen? Des Mannes, Dativ wem? Dem Mann, Akkusativ wen? Den Mann. Adjektiv stark dieser gute Mann schwach der gute Mann gemischt ein guter Mann. Nebensatz weil dass obwohl wenn Verb am Ende Ich weiß dass er kommt.

ZEITEN: Präsens ich gehe, Perfekt ich bin gegangen ich habe gesehen, Präteritum ich ging ich sah Erzählung, Plusquamperfekt ich war gegangen hatte gesehen Vorvergangenheit, Futur I ich werde gehen, Futur II ich werde gegangen sein.
""",

"Mathe": """
**MATHE ULTRA LANG AUSFÜHRLICH:**

BRÜCHE: Zähler oben wie viele Teile Nenner unten wie groß 1/4 ein Viertel von Kuchen. Gleicher Nenner addieren 1/4+2/4=3/4 Zähler addieren Nenner bleibt! Ungleich Hauptnenner kgV! 1/2+1/3 kgV 6 1/2=3/6 mal3 1/3=2/6 mal2 =5/6. Multi Zähler*Zähler Nenner*Nenner 1/2*3/4=3/8. Divi mit Kehrwert mal! 1/2:1/4=1/2*4/1=2. Prozent %= /100 20%=0,2 20% von 50=50*0,2=10. Dreisatz 100%=50 20%=x x=50*20/100=10. Potenz 2^3=2*2*2=8 2^0=1! Wurzel √9=3 weil 3*3=9.

GLEICHUNGEN WAAGE: 2x+4=10 Was stört? +4 weg -4 BEIDE Seiten 2x=6 :2 x=3 Probe 2*3+4=10. Quadratisch ax²+bx+c=0 Mitternacht x=(-b±√(b²-4ac))/2a D=b²-4ac D>0 2 Lösungen D=0 1 D<0 keine. Beispiel x²-5x+6=0 a1 b-5 c6 D25-24=1 x=(5±1)/2 x3 x2. pq x²+px+q=0 x=-p/2±√((p/2)²-q) Beispiel x²+4x+3=0 x=-2±√(4-3)=-2±1 -1 -3. Faktorisieren (x-2)(x-3)=0 x2 oder3.

GEOMETRIE: Pythagoras NUR rechtwinklig a²+b²=c² c Hypotenuse längste gegenüber 90°! 3 4 5 weil 9+16=25. Rechteck A=a*b U=2a+2b Quadrat a² U=4a Dreieck A=g*h/2 g Grund h Höhe! Kreis U=2πr A=πr² r Radius d=2r. Quader V=a*b*c Würfel a³ Zylinder V=πr²*h Kugel V=4/3πr³ O=4πr².

TRIGO: sin=GK/Hyp Gegenkathete Hypotenuse cos=AK/Hyp Ankathete tan=GK/AK=sin/cos Merke GAGA Hühnerhof AG! sin30=0,5 sin²+cos²=1 360°=2π 180°=π.

ABLEITUNG: Steigung f'(x)=lim h->0 (f(x+h)-f(x))/h Potenzregel x^n->n*x^(n-1) x³->3x² x²->2x x->1 5->0! Summe (u+v)'=u'+v' Produkt (u*v)'=u'v+uv' Kette f(g) -> f'(g)*g' äußere mal innere (x²+1)³->3(x²+1)²*2x! Extrem f'=0 f''>0 Tief f''<0 Hoch! Integral Umkehrung ∫x^n=x^(n+1)/(n+1)+C ∫3x²=x³+C weil (x³)'=3x²! Bestimmt ∫a^b=F(b)-F(a) Fläche! Beispiel Fläche x² 0 bis2 F=x³/3 8/3-0=8/3.

WAHRSCHEINLICHKEIT: Laplace P=Ereignis/alle Würfel 1/6. UND multiplizieren ODER addieren! Baum Pfad multiplizieren! Binomial P(k)=(n über k)*p^k*(1-p)^(n-k) n Versuche k Treffer p Wahrscheinlichkeit! Erwartung E=n*p Durchschnitt Summe/Anzahl.
""",

"Geschichte": """
**GESCHICHTE ULTRA LANG:**

FRANZÖSISCHE REVOLUTION 1789-1799 5W:

WER? 1.Stand Klerus 1% 10% Land kein Steuern! 2.Stand Adel 2% 20% Land kein Steuern! 3.Stand 97% Bürger Bauern Handwerker zahlt ALLE Steuern Zehnt Frondienst!

WARUM 4 Ursachen: 1.Absolutismus Ludwig XVI L'état c'est moi alle Macht! 2.Pleite Kriege 7jährig Amerika teures Versailles 1Mrd Schulden! 3.Hunger 1788 schlechte Ernte Hagel Brot +65% Lohn 70% für Brot! 4.Aufklärung Rousseau Volkssouveränität Montesquieu Gewaltenteilung Locke Menschenrechte!

WANN: 5.5.1789 Generalstände wegen Steuern! 17.6. 3.Stand Nationalversammlung! Ballhausschwur 20.6. Wir gehen nicht vor Verfassung! 14.7.1789 Sturm Bastille Symbol! 26.8. Menschenrechte Freiheit Gleichheit Brüderlichkeit! 1791 Verfassung! 1792 Republik! 21.1.1793 Ludwig geköpft Guillotine! 1793-94 Schreckensherrschaft Robespierre 40000! 1799 Napoleon 18.Brumaire Putsch Konsul Kaiser Ende!

FOLGEN Ende Feudalismus Menschenrechte Nationalismus Code Napoleon!

INDUSTRIALISIERUNG 1760-1900: England 1760 Kohle Eisen Kolonien! Watt Dampfmaschine 1769! Spinning Jenny! Fabriken! Städte Manchester 25k->300k! Arbeiter arm 16h Kinderarbeit! Marx Engels Manifest 1848! SPD 1875! Eisenbahn 1835 Deutschland!

1.WK 1914-18: Sarajevo 28.6.1914 Princip Franz Ferdinand! Bündnisse! Schlieffenplan durch Belgien! Schützengraben 700km Verdun 1916 700k Tote Somme Giftgas Panzer! 11.11.1918 Waffenstillstand! Versailles 28.6.1919 Deutschland Schuld Reparationen 132Mrd! 17Mio Tote Weimar!

2.WK 1939-45: 1.9.1939 Polen Blitzkrieg! 1940 Frankreich! 1941 Russland Barbarossa 22.6.! Pearl Harbor 7.12.1941 USA! Holocaust 6Mio Juden Auschwitz 1,1Mio Wannsee 20.1.1942 Endlösung Heydrich! Wende Stalingrad Jan43 300k! D-Day 6.6.1944 Normandie! 8.5.45 Kapitulation! Hiroshima 6.8. 140k Nagasaki 9.8. 70k! 60Mio Tote geteilt UN!

KALTER KRIEG 1947-90: USA Kapitalismus vs UdSSR Kommunismus! Berlin Blockade 48-49 Luftbrücke! NATO49 Warschauer Pakt55! Mauer 13.8.61-9.11.89 28J 140 Tote! Kuba62 13 Tage fast Atomkrieg! Vietnam65-75! Gorbatschow Glasnost Perestroika 89! Montagsdemos Leipzig Wir sind das Volk! Mauerfall 9.11.89! 3.10.90 Einheit Kohl!

BRD DDR: BRD 23.5.49 Grundgesetz Bonn Adenauer CDU Westintegration Wirtschaftswunder Brandt SPD Ostpolitik Kniefall Warschau! DDR 7.10.49 Ost Berlin SED Sozialismus Planwirtschaft Stasi 91k+173k IM Mangel Mauer 61 Flucht! Montagsdemos 89!
""",

"Geographie": """
**GEOGRAPHIE ULTRA LANG:**

PLATTENTEKTONIK: Erde Schichten Kruste 5-70km dünn Mantel 2900km heiß zäh Kern flüssig außen fest innen 5000°! Platten 7 große + kleine bewegen 5cm/Jahr wie Fingernagel! 3 Grenzen: divergent auseinander Mittelozeanischer Rücken Island wächst Magma neu! konvergent zusammen Subduktion eine unter andere Anden Himalaya entsteht weil Indien gegen Eurasien! Erdbeben Vulkan! transform vorbei San Andreas Kalifornien!

ERDBEBEN: Hypozentrum unten Epizentrum oben an Oberfläche! Richter Skala log10! Seismograph! Tsunami bei Meer!

VULKAN: Hotspot Hawaii mitten Platte! Ring of Fire Pazifik! Schildvulkan flach Hawaii Lava flüssig, Schichtvulkan steil Vesuv explosiv!

KLIMA: Wetter täglich kurzfristig Klima 30 Jahre Durchschnitt! Klimazonen Polar kalt -40 Gemäßigt 4 Jahreszeiten Mitteleuropa Subtropen warm trocken Mittelmeer Tropen heiß feucht Regenwald Wüste! Klimawandel natürlich + Mensch! CO2 280ppm 1850 ->420ppm 2026 +50%! Temperatur +1,2°C seit 1850! Treibhaus CO2 CH4! Folgen Meer +20cm Extremwetter!

BEVÖLKERUNG: 8Mrd 2026! Demografischer Übergang 5 Phasen hohe Geburt Tod -> niedrige! Entwicklungsländer Phase2 viele Kinder! Deutschland Phase5 wenig Kinder alt! Migration Push Pull Push Krieg Armut Pull Arbeit! Urbanisierung Landflucht Megacity 10Mio+!

GLOBALISIERUNG: Welt vernetzt Handel Internet Container 1960! Lieferketten! Gewinner Firmen billig Verlierer Arbeiter! Corona zeigt Abhängigkeit!
""",

"Biologie": """
**BIOLOGIE ULTRA LANG:**

ZELLE KLEINSTE LEBENDE EINHEIT FABRIK:

Prokaryot Bakterien einfach kein Kern DNA frei im Zytoplasma klein 1μm keine Organellen nur Ribosomen!

Eukaryot Tier Pflanze Mensch mit Kern größer 10-100μm mit Organellen!

TIERZELLE FABRIK VERGLEICH: Zellmembran=Fabrikzaun Doppellipidschicht Phospholipide schützt kontrolliert rein raus selektiv permeabel! Zytoplasma=Gel Flüssigkeit 70% Wasser da schwimmen Organellen! Zellkern=Chef Büro Steuerzentrale Doppelmembran Poren enthält DNA Chromosomen 46 beim Mensch macht mRNA! Nucleolus macht Ribosomen! Mitochondrien=KRAFTWERK 1000 pro Zelle macht ATP Energie durch Zellatmung Zucker+O2->CO2+H2O+36 ATP! Doppelmembran eigene DNA! Deshalb Sauerstoff nötig! Warum? Endosymbiontentheorie waren mal Bakterien! Ribosomen=Arbeiter Baut Proteine aus Aminosäuren Translation mRNA->Protein! ER=Transportstraße Netzwerk rau mit Ribosomen macht Proteine glatt ohne macht Lipide! Golgi=Verpackung Versand Modifiziert Proteine Vesikel! Lysosom=Müllverbrennung Verdaut Müll mit Enzymen pH5 sauer!

PFLANZE EXTRA: Zellwand=Betonmauer aus Zellulose stabiler als Membran Holz! Chloroplasten=Solaranlage Fotosynthese 6CO2+6H2O+Licht->C6H12O6+6O2 Macht Zucker aus Licht Grün Chlorophyll a b! Doppelmembran eigene DNA! Vakuole=Wassersack groß 90% Zelle speichert Wasser Zucker Gift Druck Turgor hält Pflanze aufrecht! Wenn kein Wasser welk!

FOTOSYNTHESE: Ort Chloroplast Thylakoidmembran Grana! Lichtreaktion Photon schlägt Elektron aus P680 Wasser Spaltung 2H2O->O2+4H++4e- O2 kommt aus Wasser nicht CO2 Beweis O18! Elektronentransport macht ATP! Dunkelreaktion Calvin Zyklus im Stroma CO2+RuBP->Zucker braucht ATP NADPH! Warum nur 1-2% Effizienz? Nur 45% Licht PAR Reflexion Photorespiration RuBisCO verwechselt CO2 mit O2 20% Verlust Atmung 50%!

ZELLATMUNG: Umgekehrt Zucker+O2->CO2+H2O+Energie Ort Mitochondrien! Glykolyse im Zytoplasma Citratzyklus Matrix Atmungskette Membran! 36 ATP pro Zucker!

GENETIK: DNA Doppelhelix Watson Crick 1953 A-T 2 Bindungen C-G 3 Bindungen! Gen Abschnitt DNA für Protein! Chromosom DNA verpackt Mensch 46 23 von Mama 23 von Papa 22 Autosomen + XY! Mitose Zellteilung 1->2 identisch Wachstum! Meiose Keimzellen 1->4 mit halb 23! Mendel Erbsen dominant groß rezessiv klein 3:1! Mutation Veränderung DNA durch Strahlung!

EVOLUTION: Darwin 1859 natürliche Selektion Survival of fittest Wer angepasst überlebt! Beweise Fossilien Archaeopteryx, Homologie Hand Wal Fledermaus gleicher Knochen, DNA Mensch Affe 98% gleich! Mensch Affe 6Mio Jahre getrennt!

MENSCH: Herz 4 Kammern 2 Vorhöfe 2 Kammern Blutkreislauf Lunge->Herz->Körper->Herz->Lunge! Blut AB0 A Antigen B Antikörper etc! Gehirn Großhirn Denken Kleinhirn Bewegung Hirnstamm Atmung! Lunge Alveolen Gasaustausch! Niere filtert Blut Urin! Immun weiße Blutkörperchen Antikörper Impfung!
""",

"Physik": """
**PHYSIK ULTRA LANG:**

MECHANIK NEWTON 3 GESETZE:

Newton1 Trägheit Ohne Kraft bleibt Körper in Ruhe oder gleichförmiger Bewegung! Beispiel Buch liegt bleibt liegen bis du schiebst! Weltraum ohne Reibung fliegt ewig!

Newton2 F=m*a Kraft=Masse*Beschleunigung! Was ist Kraft? Newton N! 1N=1kg*1m/s²! Beispiel 2kg Masse mit 3m/s² beschleunigen F=2*3=6N! Gewicht F=m*g g=9,81m/s² Erdanziehung! 70kg Mensch Gewicht 70*9,81=686N! Beschleunigung a=F/m!

Newton3 Actio=Reactio Kraft=Gegenkraft! Du drückst Wand Wand drückt dich! Rakete stößt Gas nach unten Gas stößt Rakete nach oben!

GRÖSSEN: Weg s Meter m Zeit t Sekunde s Geschwindigkeit v=s/t m/s km/h 100km/h=27,8m/s! Beschleunigung a=v/t m/s²! Freier Fall g=9,81! Fall Weg s=0,5*g*t²! Beispiel Fall 2s s=0,5*9,81*4=19,6m!

ENERGIE: Energie bleibt erhalten nur umgewandelt! Formen Kinetisch Bewegung 0,5*m*v² Beispiel Auto 1000kg 20m/s E=0,5*1000*400=200000J! Potentiell Höhe m*g*h Beispiel 70kg 10m hoch E=70*9,81*10=6867J! Wärme Licht elektrisch chemisch! Leistung P=E/t Watt W 1kW=1000W! kWh Kilowattstunde Energie 1kWh=3,6Mio J! Beispiel 100W Lampe 10h 1kWh!

STROM: Strom Elektronen fließen! Spannung U Volt V Druck! Stromstärke I Ampere A Menge! Widerstand R Ohm Ω Hindernis! Ohmsches Gesetz R=U/I U=R*I I=U/R! Beispiel 12V Batterie 3Ω Widerstand I=12/3=4A! Reihe hintereinander Rges=R1+R2 Beispiel 2Ω+3Ω=5Ω! Parallel nebeneinander 1/Rges=1/R1+1/R2 Beispiel 2Ω parallel 2Ω 1/R=1/2+1/2=1 R=1Ω! Leistung P=U*I Watt! Beispiel 230V 10A P=2300W! Stromzähler kWh!

OPTIK: Licht gerade Strahl! Reflexion Einfallswinkel=Ausfallswinkel Spiegel! Brechung Wasser bricht Licht Stab im Wasser knick! Linse sammelt! Sammellinse Brennpunkt! Auge Linse Netzhaut! Kurz weitsichtig Brille! Farben weiß alle Farben Prisma Regenbogen! Laser gebündelt!
""",

"Chemie": """
**CHEMIE ULTRA LANG:**

ATOMBAU: Atom kleinste Einheit unteilbar früher gedacht! Besteht aus Kern Proton+ Neutron Hülle Elektron! Proton positiv +1 1u Masse Kern! Neutron neutral 0 1u! Elektron negativ -1 fast keine Masse 1/1836! Ordnungszahl=Protonenzahl! Element durch Protonenzahl! PSE Periodensystem geordnet nach Protonenzahl! Gruppen Spalten gleiche Valenzelektronen! Gruppe1 Alkali 1 Valenzelektron will weg gibt +1! Gruppe17 Halogene 7 Valenzelektronen will 1 haben -1! Gruppe18 Edelgase 8 voll stabil! Periode Zeile! Isotope gleiche Protonen andere Neutronen C12 6Prot6Neut C14 6Prot8Neut radioaktiv!

BINDUNGEN: Warum binden? Oktettregel 8 Valenzelektronen wollen alle voll wie Edelgase stabil! 3 Arten: Ionenbindung Metall gibt Elektron an Nichtmetall ab Metall wird + Nichtmetall - ziehen sich an Salz! Beispiel Na gibt 1e- an Cl Na+ Cl- NaCl Kochsalz! Kovalent Atome teilen Elektronen beide haben 8! Beispiel H2O O teilt mit 2 H! Metallbindung Metalle Elektronengas frei beweglich leitet Strom verformbar! Eigenschaften Ionen Salz hoch Schmelz spröde leitet flüssig! Kovalent Molekül niedrig Schmelz! Metall leitet glänzt!

SÄUREN BASEN pH: Säure gibt H+ Proton ab nach Brönsted! Base nimmt H+ auf! Starke Säure vollständig dissoziiert HCl->H++Cl-! Schwache Säure teilweise Essigsäure! pH=-log[H+]! pH 0-14! 0-6 sauer 7 neutral 8-14 basisch alkalisch! pH1 stark sauer Magensäure pH7 neutral Wasser pH14 stark basisch Natronlauge! Indikator Lackmus rot sauer blau basisch Phenolphthalein farblos sauer pink basisch! Starke Säuren HCl Salzsäure H2SO4 Schwefelsäure HNO3 Salpetersäure! Starke Basen NaOH Natronlauge KOH! Neutralisation Säure+Base->Salz+Wasser! Beispiel HCl+NaOH->NaCl+H2O Kochsalz+Wasser! H+ + OH- -> H2O!

REDOX: Oxidation Elektronen abgeben Oxidationszahl steigt! Reduktion Elektronen aufnehmen Zahl sinkt! Merke OIL RIG Oxidation Is Loss Reduction Is Gain! Beispiel Rost Fe->Fe3+ +3e- Oxidation Fe gibt ab! O2+4e-->2O2- Reduktion O nimmt auf! Redox zusammen! Rost Fe+O2->Fe2O3! Verbrennung C+O2->CO2!
"""
}

# ANZEIGE
if suche:
    s = suche.lower()
    gefunden = False
    for name, text in faecher.items():
        if s in name.lower() or s in text.lower():
            st.markdown(f"## 📚 {name}")
            st.write(text)
            st.write("---")
            gefunden = True
    if not gefunden:
        st.error(f"Nichts für '{suche}' gefunden - versuche y en, Se lo doy, If Sätze, Fotosynthese, Revolution, Pythagoras, Ableitung")
else:
    auswahl = st.selectbox("📚 FACH WÄHLEN - VOLLSTÄNDIG:", list(faecher.keys()))
    st.markdown(f"## {auswahl}")
    st.write(faecher[auswahl])

st.success("✅ v28 - Alle 12 Fächer ultra lang + Suche - Nicht gekürzt!")
st.caption("Französisch Spanisch Englisch Italienisch Latein Deutsch Mathe Geschichte Geo Bio Physik Chemie - Alles maximum!")
