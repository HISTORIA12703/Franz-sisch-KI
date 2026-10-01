import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="Lern App", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title { text-align: center; font-size: 45px; font-weight: bold; color: #2E86AB; }
.search-box { background-color: #f0f7ff; padding: 25px; border-radius: 15px; border: 2px solid #2E86AB; margin-bottom: 20px; }
.stButton > button { width: 100%; background-color: white; color: #2E86AB; border: 2px solid #2E86AB; border-radius: 10px; padding: 12px; font-weight: bold; }
.stButton > button:hover { background-color: #2E86AB; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 Lern App</div>', unsafe_allow_html=True)
st.markdown('<div class="search-box">', unsafe_allow_html=True)
st.markdown("### 🔍 Wonach möchtest du suchen?")
thema = st.text_input("", placeholder="z.B. USA, Atombombe, Football, y en, ser estar, present perfect...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

def suche_wikipedia(thema):
    try:
        headers = {'User-Agent': 'LernApp/1.0'}
        enc = urllib.parse.quote(thema.replace(" ", "_"))
        url = f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc}"
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            if 'extract' in data:
                return {"titel": data.get("title"), "text": data.get("extract"), "link": data.get("content_urls", {}).get("desktop", {}).get("page", "")}
        # Fallback Suche
        search_url = f"https://de.wikipedia.org/w/api.php?action=opensearch&search={thema}&limit=1&namespace=0&format=json"
        r2 = requests.get(search_url, headers=headers, timeout=5)
        if r2.status_code == 200:
            res = r2.json()
            if len(res)>1 and res[1]:
                enc2 = urllib.parse.quote(res[1][0].replace(" ", "_"))
                r3 = requests.get(f"https://de.wikipedia.org/api/rest_v1/page/summary/{enc2}", headers=headers, timeout=5)
                if r3.status_code == 200:
                    d = r3.json()
                    return {"titel": d.get("title"), "text": d.get("extract"), "link": d.get("content_urls", {}).get("desktop", {}).get("page", "")}
    except:
        pass
    return None

# ===== RICHTIGE VOKABELN + GRAMMATIK 100% KORREKT =====
faecher = {
"Französisch - Vokabeln & Grammatik": """
**VOKABELN RICHTIG:**
le pain das Brot, la pomme der Apfel, le livre das Buch, la maison das Haus, l'eau das Wasser, le temps Zeit Wetter, la vie Leben, le monde Welt
aller gehen, venir kommen, faire machen, dire sagen, voir sehen, vouloir wollen, pouvoir können, prendre nehmen, manger essen, boire trinken, dormir schlafen
bon gut, mauvais schlecht, grand groß, petit klein, nouveau neu, vieux alt, beau schön, heureux glücklich
ici hier, là dort, maintenant jetzt, toujours immer, déjà schon, beaucoup viel, très sehr

**GRAMMATIK 100% RICHTIG - LE LA LUI Y EN:**

**LE** = ihn/es männlich COD direkt Objekt Frage Wen?Was? OHNE a vor Nomen
Regel: Je mange LE pain (das Brot) -> Je LE mange (Ich esse es)
Je vois LE film -> Je LE vois Ich sehe ihn
Je connais PAUL -> Je LE connais Ich kenne ihn
MERKE: LE ersetzt LE/la Nomen OHNE à

**LA** = sie/es weiblich COD
Je vois MARIE -> Je LA vois Ich sehe sie
Je mange LA pomme -> Je LA mange Ich esse sie
La remplace weibliches Nomen OHNE à

**LES** = sie Plural COD
Je vois LES enfants -> Je LES vois Ich sehe sie
Je mange LES pommes -> Je LES mange

**LUI** = ihm/ihr COI indirekt Wem? MIT à vor Person!
Regel: Nur bei VERB + À + PERSON
Je parle À Marie (Ich spreche MIT Marie) -> Je LUI parle Ich spreche mit ihr
Je donne le livre À Paul -> Je LUI donne le livre Ich gebe ihm das Buch
Je téléphone À mes parents -> Je LEUR téléphone Moment LEUR Plural!
MERKE: LUI/LEUR nur bei à + PERSON nicht Sache!

**LEUR** = ihnen Plural COI
Je parle AUX enfants (à + les = aux) -> Je LEUR parle
Je donne des bonbons AUX élèves -> Je LEUR donne des bonbons

**Y** = dort/dorthin/daran Ort mit à, chez, dans, sur ODER à + SACHE nicht Person!
Je vais À Paris -> J'Y vais Ich gehe dorthin (Ort)
Je suis CHEZ moi -> J'Y suis Ich bin dort
Je pense À mon examen (SACHE nicht Person) -> J'Y pense Ich denke daran
Je mets le livre DANS le sac -> J'Y mets le livre
Aber: Je pense À Marie (Person) -> Je pense À ELLE nicht Y! Y nur Sache!
Je m'habitue À ce bruit Sache -> Je M'Y habitue

**EN** = davon/dessen Menge mit de/du/des/Zahl/beaucoup
Je veux DU pain (partitiv) -> J'EN veux Ich will davon
J'ai 3 frères Zahl -> J'EN ai 3 Ich habe 3 davon
J'ai BEAUCOUP DE livres -> J'EN ai beaucoup Ich habe viele davon
Je parle DE mon voyage (de + Sache) -> J'EN parle Ich spreche davon
Il vient DE Paris -> Il EN vient Er kommt von dort

**REIHENFOLGE FÜR KLAUSUR - PFLICHT:**
me te se nous vous + le la les + lui leur + y + en + VERB
Beispiele richtig:
Il ME LE donne Er gibt es mir (mir + es)
Il TE LES donne Er gibt sie dir
Je LE LUI donne Ich gebe es ihm
Il Y EN a Es gibt davon
Je M'Y habitue Ich gewöhne mich daran (me + y)
Ne LUI EN parle pas Sprich nicht davon mit ihm (lui + en)

**DIREKTE -> INDIREKTE RICHTIG:**
Direkt: Il dit: "Je suis malade."
Indirekt Präsens Einleitung (Il dit): Il dit qu'il EST malade Zeit BLEIBT!
Direkt: Il dit: "J'ai mangé."
Indirekt: Il dit qu'il A mangé

Vergangenheit Einleitung (Il a dit): Zeiten verschieben!
Présent -> Imparfait: Il a dit qu'il ÉTAIT malade (war)
Passé composé -> Plus-que-parfait: J'ai mangé -> Il a dit qu'il AVAIT mangé (hatte gegessen)
Futur -> Conditionnel présent: J'irai -> Il a dit qu'il IRAIT (würde gehen)

FRAGEN:
Où vas-tu? -> Il a demandé où il ALLAIT (Imparfait)
Que fais-tu? -> Il a demandé CE QUE je faisais ACHTUNG que wird ce que!
Qu'est-ce que tu fais? -> ce que tu faisais
Tu viens? Ja/Nein Frage -> si: Il a demandé SI je venais (ob)

BEFEHL:
Viens! -> Il m'a dit DE VENIR (de + Infinitiv)
Ne viens pas! -> de NE PAS venir
""",

"Spanisch - Vokabeln & Grammatik": """
**VOKABELN RICHTIG:**
el pan Brot, la manzana Apfel, el libro Buch, la casa Haus, el agua Wasser, el tiempo Zeit Wetter, la vida Leben, el mundo Welt
ir gehen, venir kommen, hacer machen, decir sagen, ver sehen, querer wollen, poder können, tomar nehmen, comer essen, beber trinken, dormir schlafen
bueno gut, malo schlecht, grande groß, pequeño klein, nuevo neu, viejo alt, bonito schön, feliz glücklich
aquí hier, allí dort, ahora jetzt, siempre immer, ya schon, mucho viel, muy sehr

**GRAMMATIK 100% RICHTIG:**

**LO LA LES = COD direkt Wen?Was? OHNE a:**
Veo EL LIBRO (das Buch) -> LO veo Ich sehe es (ihn)
Veo LA CASA (das Haus) -> LA veo Ich sehe sie (es)
Veo A JUAN (Person mit a!) -> LO veo trotzdem LO weil direkt! Aber mit a personal!
Veo A MARÍA -> LA veo
Veo LOS libros -> LOS veo
Veo LAS casas -> LAS veo

**LE LES = COI indirekt Wem? MIT a:**
Hablo A JUAN (Ich spreche MIT Juan) -> LE hablo Ich spreche mit ihm
Doy el libro A MARÍA -> LE doy el libro Ich gebe ihr das Buch
Doy libros A LOS NIÑOS -> LES doy libros Ich gebe ihnen Bücher
Hablo A MIS PADRES -> LES hablo

**WICHTIGSTE REGEL SPANISCH - SE LO DOY:**
Du kannst NICHT sagen LE LO DOY! Das ist FALSCH!
Wenn LE/LES (indirekt) + LO/LA (direkt) zusammen kommen, wird LE/LES zu SE!
FALSCH: Le lo doy
RICHTIG: SE LO DOY Ich gebe es ihm

Beispiele richtig:
Le doy el libro + lo = SE LO DOY
Les doy los libros = SE LOS DOY Ich gebe sie ihnen
Me lo da Er gibt es mir (me + lo erlaubt!)
Te lo doy Ich gebe es dir (te + lo erlaubt!)
Nur le/les + lo/la/la wird SE!

**SER vs ESTAR beide SEIN - UNTERSCHIED RICHTIG:**

SER = WAS IST ES? Permanent Definition Identität Eigenschaft Herkunft Material Zeit
Soy Juan Ich bin Juan Name Identität
Soy de Alemania Ich bin aus Deutschland Herkunft
Soy alto Ich bin groß Eigenschaft permanent groß
Es grande Es ist groß
Son las tres Es ist 3 Uhr Zeit SER für Uhrzeit!
Es de madera Es ist aus Holz Material
Es para comer Es ist zum Essen Bestimmung

ESTAR = WO? WIE? GERADE? Ort Zustand Ergebnis gerade dabei
Estoy en casa Ich bin zu Hause ORT wo?
Estoy cansado Ich bin müde ZUSTAND wie? müde krank traurig
Está roto Es ist kaputt Ergebnis Zustand durch Handlung kaputt gegangen
Está sucio Es ist schmutzig
Estoy comiendo Ich esse gerade GERADE DABEI Verlaufsform estar + gerundio!
Estoy leyendo Ich lese gerade
Está leyendo Er liest gerade

Es aburrido Er ist langweilig Charakter langweilig SER
Está aburrido Ihm ist langweilig Zustand gerade langweilig ESTAR
Es bueno Er ist gut Charakter SER vs Está bueno Es schmeckt gut Zustand!

**POR vs PARA beide FÜR:**

POR = Grund Ursache Durch Tausch Dauer Warum? Wodurch? Wie lange?
Gracias POR todo Danke für alles Grund Ursache
Voy POR la calle Ich gehe durch die Straße durch
POR la mañana morgens Zeit am Morgen
POR dos horas für zwei Stunden Dauer wie lange?
Te doy 5 euros POR el libro Ich gebe 5€ für das Buch Tausch gegen
POR qué? Warum? Grund
PORque weil
Paseo POR el parque Spaziere durch den Park

PARA = Ziel Zweck Empfänger Frist Wofür? Wohin? Für wen? Bis wann?
Esto es PARA comer Das ist zum Essen Zweck Wofür?
Este regalo es PARA ti Das Geschenk ist für dich Empfänger für wen?
Voy PARA Madrid Ich fahre nach Madrid Ziel Wohin? Richtung
Para mañana bis morgen Frist bis wann?
Para mí es difícil Für mich ist es schwierig Meinung für wen?
¿Para qué? Wofür? Zweck
Para ser rico Um reich zu sein Ziel
""",

"Englisch - Vokabeln & Grammatik": """
**VOKABELN:**
bread Brot, apple Apfel, book Buch, house Haus, water Wasser, time Zeit, life Leben, world Welt
go gehen, come kommen, make machen, say sagen, see sehen, want wollen, can können, take nehmen, eat essen, drink trinken, sleep schlafen
good gut, bad schlecht, big groß, small klein, new neu, old alt, beautiful schön, happy glücklich
here hier, there dort, now jetzt, always immer, already schon, much viel, very sehr

**GRAMMATIK RICHTIG:**

ZEITEN:
Present Simple I go every day Gewohnheit he goes mit s! Frage Do you go? Does he go? Verneinung I don't go He doesn't go
Past Simple I went gestern einmalig Yesterday I went ed regelmäßig play->played go->went unregelmäßig Frage Did you go? didn't
Present Perfect I have gone Ergebnis jetzt I have eaten I am full have/has + Past Participle 3.Form go->gone eat->eaten Signal already yet just ever never since for since 2010 for 2 years
Past Perfect I had gone Vorvergangenheit Before I came he had left hatte verlassen bevor ich kam
Future will spontan I will help you I think will going to geplant I am going to study morgen fest Present Continuous I am going tomorrow Plan mit Zeit

INDIREKTE:
He says: "I am ill." -> He says he IS ill Zeit BLEIBT bei says Präsens Einleitung!
He said: "I am ill." -> He said he WAS ill Zeit zurück Present->Past
He said: "I have eaten." -> He said he HAD eaten Present Perfect->Past Perfect
He said: "I will go." -> He said he WOULD go will->would can->could

Fragen:
Where are you? -> He asked where I WAS (Rückverschiebung)
What do you do? -> He asked what I DID
Do you come? Ja/Nein -> if/whether: He asked IF I CAME ob

Befehl: Come here! -> He told me TO COME here to + Infinitiv

IF SÄTZE RICHTIG:
Type 0 Naturgesetz If you heat water to 100 it boils If+Present Present immer wahr
Type 1 möglich real If I GO I WILL go If+Present will Future 50% möglich If it rains I will stay
Type 2 irreal jetzt If I WENT I WOULD go If+Past would+Inf unwahrscheinlich If I were you I would go If I had money I would buy
Type 3 irreal Vergangenheit If I HAD GONE I WOULD HAVE GONE If+Past Perfect would have+PP vorbei zu spät If I had studied I would have passed

PASSIVE RICHTIG be + Past Participle:
Active I make a cake -> Passive A cake IS MADE (am/is/are + PP)
Past A cake WAS MADE was/were+PP
Perfect A cake HAS BEEN MADE has been+PP
Future A cake WILL BE MADE will be+PP
Progressive A cake IS BEING MADE is being+PP
Mit by: A cake was made BY ME von mir
""",

"Mathe - Richtig": """
**BRÜCHE 100% RICHTIG:**
1/4 = ein Viertel Kuchen in 4 Teile 1 Teil
Gleicher Nenner: 1/4 + 2/4 = 3/4 Zähler addieren Nenner bleibt!
Ungleicher Nenner: 1/2 + 1/3 Hauptnenner kgV kleinstes gemeinsames Vielfaches von 2 und 3 ist 6
1/2 = 3/6 (mal 3) 1/3=2/6 (mal 2) 3/6+2/6=5/6
Multiplikation: Zähler mal Zähler Nenner mal Nenner 1/2 * 3/4 = 3/8
Division: Mit Kehrwert malnehmen 1/2 : 1/4 = 1/2 * 4/1 = 4/2 = 2 Kehrwert von 1/4 ist 4/1
Prozent: % = /100 20% = 20/100 = 0,2 20% von 50 = 50*0,2=10 Dreisatz 100% = 50 1% =0,5 20%=10

**GLEICHUNGEN RICHTIG - WAAGE:**
Beide Seiten gleich halten!
2x + 4 = 10 | -4 beide Seiten 2x = 6 | :2 beide Seiten x=3 Probe 2*3+4=10 stimmt!
3x - 5 = 10 | +5 3x=15 | :3 x=5
Quadratisch ax²+bx+c=0 Mitternachtsformel x=(-b ± √(b²-4ac))/2a
Beispiel x² -5x +6=0 a=1 b=-5 c=6 D=b²-4ac=25-24=1 x=(5±1)/2 x1=3 x2=2
Diskriminante D>0 2 Lösungen D=0 1 Lösung D<0 keine Lösung
pq Formel x²+px+q=0 x=-p/2 ± √((p/2)²-q)

**GEOMETRIE RICHTIG:**
Pythagoras NUR rechtwinkliges Dreieck 90°! a²+b²=c² c Hypotenuse längste Seite gegenüber 90°
Beispiel 3 4 5 weil 3²+4²=9+16=25=5²
Rechteck A=a*b Fläche U=2a+2b Umfang Quadrat A=a² U=4a
Kreis r Radius d=2r Durchmesser U=2πr A=πr² π=3,14
Quader V=a*b*c Würfel V=a³ Zylinder V=πr²*h Kreis mal Höhe Kugel V=4/3πr³ O=4πr² Oberfläche
Trigonometrie sin=Gegenkathete/Hypotenuse cos=Ankathete/Hyp sin30°=0,5 sin²+cos²=1

**ABLEITUNG RICHTIG:**
Definition f'(x)=lim h->0 (f(x+h)-f(x))/h Steigung Tangente
Potenzregel x^n -> n*x^(n-1) x³->3x² x²->2x x->1 Zahl 5->0
Summenregel (u+v)'=u'+v' Produktregel (u*v)'=u'v+uv' Kettenregel äußere mal innere (x²+1)³ ->3(x²+1)²*2x
Extrempunkte f'(x)=0 f''(x)>0 Tiefpunkt f''<0 Hochpunkt

**INTEGRAL Umkehrung Ableitung:**
∫x^n dx = x^(n+1)/(n+1)+C +C Konstante!
Bestimmtes Integral ∫a^b f(x)dx = F(b)-F(a) Fläche unter Kurve

**WAHRSCHEINLICHKEIT:**
P= günstige / alle Möglichkeiten Würfel P(6)=1/6
UND = multiplizieren ODER = addieren Baumdiagramm Pfad multiplizieren
Binomial P(k)= (n über k)*p^k*(1-p)^(n-k) n Versuche k Treffer p Wahrscheinlichkeit
""",
"Geschichte - Richtig": """
**FRANZÖSISCHE REVOLUTION 1789 RICHTIG:**
WER? 1.Stand Klerus Kirche 1% Bevölkerung 10% Land keine Steuern 2.Stand Adel 2% 20% Land keine Steuern 3.Stand Bürger Bauer 97% zahlt alle Steuern!
WARUM? Absolutismus Ludwig XVI "Ich bin der Staat" Verschwendung Versailles Pleite durch Kriege Amerika 1Mrd Schulden Hunger 1788 schlechte Ernte Brotpreis +65% 70% Lohn nur für Brot Aufklärung Rousseau Volkssouveränität Montesquieu Gewaltenteilung!
WANN? 5.5.1789 Generalstände Einberufung 17.6. 3.Stand Nationalversammlung 20.6. Ballhausschwur nicht auseinander bis Verfassung 14.7. Sturm Bastille Gefängnis Symbol 26.8. Menschenrechte Freiheit Gleichheit Brüderlichkeit Eigentum 1791 Verfassung konstitutionelle Monarchie 1792 Republik 21.1.1793 Ludwig XVI geköpft 1793-94 Schreckensherrschaft Robespierre 40000 Tote Guillotine 1799 Napoleon Putsch Ende!
FOLGEN: Ende Feudalismus Demokratie Menschenrechte Nationalismus Code Napoleon 1804 Gleichheit vor Gesetz!

**INDUSTRIALISIERUNG RICHTIG:**
Ab 1760 England Kohle Eisen Erfindungen James Watt Dampfmaschine 1769 Fabriken statt Handarbeit Manchester 25000->300000 Einwohner 100 Jahre! Arbeiter 16h 6 Tage Kinderarbeit 6 Jahre Slums Krankheiten Marx Engels Manifest 1848 Proletarier aller Länder vereinigt! SPD 1875 Eisenbahn 1835 Nürnberg-Fürth! 2.Phase Elektrizität Chemie!

**1.WELTKRIEG 1914-18 RICHTIG:**
Ursachen Imperialismus Wettrüsten Bündnisse! Auslöser Attentat Sarajevo 28.6.1914 Gavrilo Princip erschießt Franz Ferdinand Thronfolger Österreich! Bündnisse Mittelmächte Deutschland Österreich vs Entente Frankreich Russland England! Schlieffenplan Deutschland durch Belgien schnell Frankreich besiegen! Verlauf Schützengraben Westfront 700km Verdun 1916 700000 Tote Somme Panzer 1916 Osten Russland! USA 1917 Kriegseintritt U-Boot Krieg! Ende 11.11.1918 Waffenstillstand 11 Uhr! Folgen Versailles 28.6.1919 Deutschland allein Schuld Reparationen 132Mrd Goldmark Gebietsverlust 17Mio Tote Weimarer Republik 1919!

**2.WELTKRIEG 1939-45 RICHTIG:**
Ursachen Versailles Weltwirtschaftskrise 1929 Hitler 1933! Beginn 1.9.1939 Überfall Polen Blitzkrieg! Verlauf 1940 Frankreich besetzt 1941 Balkan Russland Unternehmen Barbarossa 22.6.1941 3Mio Soldaten! 7.12.1941 Pearl Harbor Japan USA Krieg! Holocaust 6Mio Juden Auschwitz! Wannsee Konferenz 20.1.1942 Endlösung! Wende Stalingrad Jan 1943 300000 Deutsche eingekesselt D-Day 6.6.1944 Normandie! Ende 8.5.1945 Kapitulation! Atombombe Hiroshima 6.8.1945 Little Boy 140000 Tote Nagasaki 9.8. Fat Man 70000! Folgen 60Mio Tote Deutschland geteilt BRD DDR UN 1945!

**KALTER KRIEG 1947-1990 RICHTIG:**
USA Kapitalismus vs UdSSR Kommunismus! Berlin Blockade 1948-49 Luftbrücke Rosinenbomber NATO 1949 Westen Warschauer Pakt 1955 Osten! Mauer 13.8.1961-9.11.1989 28 Jahre 155km 140 Tote! Kuba Krise 1962 13 Tage fast Atomkrieg! Vietnam 1965-75 USA verliert! Entspannung Brandt Ostpolitik Wandel durch Annäherung Gorbatschow Glasnost Offenheit Perestroika Umbau 1985! Ende Montagsdemos Leipzig Wir sind das Volk Mauerfall 9.11.1989 Einheit 3.10.1990 Kohl!
"""
}

if thema:
    st.write("---")
    st.markdown(f"### Ergebnis für '{thema}':")
    wiki = suche_wikipedia(thema)
    if wiki:
        st.info(f"**🌐 {wiki['titel']} (Wikipedia)**\n\n{wiki['text']}")
        if wiki['link']:
            st.markdown(f"[Mehr bei Wikipedia]({wiki['link']})")
        st.write("---")
    s = thema.lower()
    for name, text in faecher.items():
        if s in name.lower() or s in text.lower() or s.replace("ß","ss") in text.lower().replace("ß","ss"):
            st.markdown(f"**📚 {name}:**")
            st.write(text)
            st.write("---")

st.write("---")
st.markdown("### 📖 Oder wähle ein Fach für Vokabeln + Grammatik richtig:")
cols = st.columns(2)
fach_liste = list(faecher.keys())
for i, fach_name in enumerate(fach_liste):
    col = cols[i % 2]
    if col.button(fach_name, key=fach_name):
        st.session_state['fach'] = fach_name

if 'fach' in st.session_state:
    st.write("---")
    st.markdown(f"## {st.session_state['fach']}")
    st.write(faecher[st.session_state['fach']])
    if st.button("❌ Schließen"):
        del st.session_state['fach']
        st.rerun()

st.caption("app.py - Vokabeln + Grammatik 100% richtig + Suche gefixt")
