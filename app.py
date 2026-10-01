import streamlit as st, requests, urllib.parse, random, time
from datetime import datetime

st.set_page_config(page_title="LernBox - 100 Vokabeln + Tests", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")

# CSS BESSER
st.markdown("""
<style>
.stButton>button {width:100%;border-radius:12px;height:3em;font-weight:bold;}
div[data-testid="stExpander"] {border-radius:12px;}
.vok-card {background:#f0f8ff;padding:12px;border-radius:10px;margin:5px 0;border-left:4px solid #2E86AB;}
.test-card {background:#fff8e1;padding:15px;border-radius:12px;border:3px solid #ff9800;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center;color:#2E86AB;">📚 LernBox - Alles Besser 🚀</h1>', unsafe_allow_html=True)

@st.cache_data(ttl=3600)
def wiki_suche(q):
    try:
        enc=urllib.parse.quote(q.replace(" ","_"))
        for lang in ["de","en"]:
            r=requests.get(f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{enc}", headers={'User-Agent':'LernBox/1.0'}, timeout=3)
            if r.status_code==200:
                j=r.json()
                ext=j.get("extract","")
                if ext and len(ext)>20:
                    return ext[:600], j.get("content_urls",{}).get("desktop",{}).get("page","")
        # Opensearch fallback
        r=requests.get(f"https://de.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(q)}&limit=3&format=json", timeout=3)
        if r.status_code==200:
            data=r.json()
            if len(data)>1 and data[1]:
                return f"Meintest du: {', '.join(data[1][:3])}", ""
    except: pass
    return "", ""

# 5 LEKTIONEN À 20 = 100 VOKABELN PRO SPRACHE
VOKABELN = {
"Französisch": {
    "L1 Familie & Essen 20": [("la famille","die Familie"),("le père","der Vater"),("la mère","die Mutter"),("le frère","der Bruder"),("la soeur","die Schwester"),("le grand-père","der Opa"),("la grand-mère","die Oma"),("l'enfant","das Kind"),("le bébé","das Baby"),("le cousin","der Cousin"),("la cousine","die Cousine"),("l'oncle","der Onkel"),("la tante","die Tante"),("le mari","der Ehemann"),("la femme","die Ehefrau"),("le pain","das Brot"),("la pomme","der Apfel"),("l'eau","das Wasser"),("la maison","das Haus"),("la porte","die Tür")],
    "L2 Schule 20": [("l'école","die Schule"),("le professeur","der Lehrer"),("l'élève","der Schüler"),("le cours","der Unterricht"),("le livre","das Buch"),("le cahier","das Heft"),("le stylo","der Stift"),("le crayon","der Bleistift"),("la gomme","der Radiergummi"),("la matière","das Fach"),("les devoirs","die Hausaufgaben"),("l'examen","die Prüfung"),("la note","die Note"),("le tableau","die Tafel"),("la règle","das Lineal"),("apprendre","lernen"),("enseigner","lehren"),("lire","lesen"),("écrire","schreiben"),("compter","zählen")],
    "L3 Verben Top 20": [("aller","gehen"),("venir","kommen"),("faire","machen"),("dire","sagen"),("voir","sehen"),("vouloir","wollen"),("pouvoir","können"),("prendre","nehmen"),("donner","geben"),("manger","essen"),("boire","trinken"),("dormir","schlafen"),("travailler","arbeiten"),("aimer","lieben"),("habiter","wohnen"),("être","sein"),("avoir","haben"),("devenir","werden"),("rester","bleiben"),("trouver","finden")],
    "L4 Alltag 20": [("parler","sprechen"),("écouter","zuhören"),("comprendre","verstehen"),("penser","denken"),("croire","glauben"),("savoir","wissen"),("connaître","kennen"),("le temps","die Zeit"),("la vie","das Leben"),("le jour","der Tag"),("la nuit","die Nacht"),("la table","der Tisch"),("la chaise","der Stuhl"),("la fenêtre","das Fenster"),("la voiture","das Auto"),("le travail","die Arbeit"),("l'argent","das Geld"),("l'heure","die Uhrzeit"),("le monde","die Welt"),("l'ami","der Freund")],
    "L5 Adjektive 20": [("bon","gut"),("mauvais","schlecht"),("grand","groß"),("petit","klein"),("beau","schön"),("nouveau","neu"),("vieux","alt"),("jeune","jung"),("facile","leicht"),("difficile","schwer"),("gentil","nett"),("heureux","glücklich"),("triste","traurig"),("ici","hier"),("là","dort"),("maintenant","jetzt"),("toujours","immer"),("beaucoup","viel"),("très","sehr"),("bien","gut")],
},
"Spanisch": {
    "L1 Familie & Essen 20": [("la familia","die Familie"),("el padre","der Vater"),("la madre","die Mutter"),("el hermano","der Bruder"),("la hermana","die Schwester"),("el abuelo","der Opa"),("la abuela","die Oma"),("el niño","das Kind"),("el bebé","das Baby"),("el primo","der Cousin"),("la prima","die Cousine"),("el tío","der Onkel"),("la tía","die Tante"),("el marido","der Ehemann"),("la mujer","die Ehefrau"),("el pan","das Brot"),("la manzana","der Apfel"),("el agua","das Wasser"),("la casa","das Haus"),("la puerta","die Tür")],
    "L2 Schule 20": [("la escuela","die Schule"),("el profesor","der Lehrer"),("el alumno","der Schüler"),("el curso","der Kurs"),("el libro","das Buch"),("el cuaderno","das Heft"),("el bolígrafo","der Stift"),("el lápiz","der Bleistift"),("la goma","der Radiergummi"),("la materia","das Fach"),("los deberes","die Hausaufgaben"),("el examen","die Prüfung"),("la nota","die Note"),("la pizarra","die Tafel"),("la regla","das Lineal"),("aprender","lernen"),("enseñar","lehren"),("leer","lesen"),("escribir","schreiben"),("contar","zählen")],
    "L3 Verben Top 20": [("ir","gehen"),("venir","kommen"),("hacer","machen"),("decir","sagen"),("ver","sehen"),("querer","wollen"),("poder","können"),("tomar","nehmen"),("dar","geben"),("comer","essen"),("beber","trinken"),("dormir","schlafen"),("trabajar","arbeiten"),("amar","lieben"),("vivir","wohnen/leben"),("ser","sein permanent"),("estar","sein Ort/Zustand"),("tener","haben"),("haber","haben Hilfsverb"),("necesitar","brauchen")],
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
    "LE LA LUI LEUR": {"t":"LE/LA direkt ohne a: Je LE vois Paul / LUI/LEUR indirekt mit a: Je LUI parle à Paul","q":[["Je LE mange LE oder LUI?","LE direkt","LUI indirekt"],["Je LUI parle à Paul?","LUI mit à","LE ohne à"],["Je LEUR parle à mes parents?","LEUR","LUI"]]},
    "Y EN": {"t":"Y=dort Ort J'Y vais à Paris / EN=davon Zahl J'EN ai 3 + unbestimmt J'EN veux du pain","q":[["J'Y vais à Paris?","Y Ort","EN davon"],["J'EN ai 3 Zahl?","EN Zahl","Y Ort"]]},
    "Reihenfolge Pronomen": {"t":"me te se nous vous + le la les + lui leur + y + en + Verb: Il ME LE donne","q":[["Il ME LE donne richtig?","JA","NEIN"]]},
    "Indirekte Rede": {"t":"Il dit qu'il EST bleibt Präsens / Il a dit qu'il ÉTAIT Present->Imparfait","q":[["Il dit qu'il EST bleibt?","JA","NEIN"]]},
},
"Geschichte": {
    "Französische Revolution 1789": {"t":"14.7.1789 Bastille, 1793 Ludwig XVI geköpft, 1799 Napoleon","q":[["Bastille?","14.7.1789","1793"]]},
    "1. WK 1914-18": {"t":"28.6.1914 Sarajevo Attentat Franz Ferdinand, Schützengraben, 11.11.1918 Ende","q":[["Beginn 1.WK?","1914","1939"],["Sarajevo?","1914","1939"]]},
    "2. WK 1939-45": {"t":"1.9.39 Polen, 1941 Russlandfeldzug, D-Day 6.6.44 Normandie, 8.5.45 Kapitulation","q":[["Beginn 2.WK?","1.9.1939","1914"],["D-Day?","6.6.1944","1.9.39"],["Ende?","8.5.1945","1918"]]},
    "Mauer 1961-89": {"t":"13.8.61 Mauerbau, 9.11.89 Mauerfall, 3.10.90 Wiedervereinigung, 28 Jahre","q":[["Mauerbau?","13.8.1961","9.11.89"],["Mauerfall?","9.11.1989","13.8.61"],["Wiedervereinigung?","3.10.1990","9.11.89"],["Wie lange Mauer?","28 Jahre","10 Jahre"]]},
    "Holocaust": {"t":"6 Mio Juden ermordet, Auschwitz, 27.1.45 Befreiung","q":[["6 Mio?","Juden","Soldaten"],["Befreiung Auschwitz?","27.1.45","8.5.45"]]},
    "Antike": {"t":"753 v.Chr. Rom Gründung, 500 v.Chr. Demokratie Athen, Caesar 44 v.Chr. ermordet","q":[["Rom Gründung?","753 v.Chr.","44 v.Chr."],["Caesar tot?","44 v.Chr.","753"]]},
    "Mittelalter & Entdeckungen": {"t":"800 Karl der Große Kaiser, 1492 Kolumbus Amerika, 1517 Luther 95 Thesen","q":[["Kolumbus?","1492","1517"],["Luther?","1517","1492"],["Karl Kaiser?","800","1492"]]},
},
"Physik": {
    "Mechanik": {"t":"v=s/t 100km/h=27,8m/s Freier Fall s=0,5*g*t² 70kg=686N","q":[["100km/h=?","27,8 m/s","100 m/s"],["70kg Gewicht?","686N","70N"]]},
    "Strom": {"t":"R=U/I 12V 3Ω=4A Reihe 2+3=5Ω Parallel 2//2=1Ω P=U*I","q":[["12V 3Ω I=?","4A","36A"],["Reihe 2+3=?","5Ω","1Ω"],["Parallel 2//2=?","1Ω","4Ω"]]},
    "Energie": {"t":"kinetisch 0,5*m*v² potentiell m*g*h 1kWh=3,6 Mio Joule","q":[["0,5*m*v²=?","kinetisch","potentiell"]]},
},
}

# --- BESSERE SUCHE GLOBAL ---
st.markdown("### 🔍 Super Suche - Vokabeln + Themen + Wikipedia")
col_s1, col_s2 = st.columns([4,1])
with col_s1:
    s_glob = st.text_input("", placeholder="Tipp: Mauer, pain, gehen, Newton, 1914, Brot...", label_visibility="collapsed", key="glob")
with col_s2:
    such_typ = st.selectbox("", ["Alles","Vokabeln","Geschichte","Physik"], label_visibility="collapsed")

if s_glob:
    s_low=s_glob.lower()
    # Wiki
    txt, link = wiki_suche(s_glob)
    if txt:
        with st.expander(f"🌐 Wikipedia: {s_glob}", expanded=True):
            st.write(txt)
            if link: st.markdown(f"[Mehr auf Wikipedia]({link})")

    # Suche
    gefunden=0
    # Vokabeln
    if such_typ in ["Alles","Vokabeln"]:
        for fach, leks in VOKABELN.items():
            for lek, lst in leks.items():
                for fremd, deutsch in lst:
                    if s_low in fremd.lower() or s_low in deutsch.lower() or s_low in lek.lower() or s_low in fach.lower():
                        st.markdown(f'<div class="vok-card"><b>{fach} {lek}:</b> {fremd} = {deutsch}</div>', unsafe_allow_html=True)
                        gefunden+=1
                        if gefunden>30: break
    # Themen
    if such_typ in ["Alles","Geschichte","Physik"]:
        for fach, themen in THEMEN.items():
            if such_typ!="Alles" and fach!=such_typ: continue
            for tname, data in themen.items():
                if s_low in tname.lower() or s_low in data["t"].lower():
                    with st.expander(f"📖 {fach}: {tname}"):
                        st.info(data["t"])
                        gefunden+=1
    if gefunden==0:
        st.warning(f"Nichts für '{s_glob}' - versuch anderes Wort!")

st.write("---")

# Fächer
st.markdown("### 📚 Fächer - 20 pro Lektion")
# Fortschritt
if 'xp' not in st.session_state: st.session_state['xp']=0
st.progress(min(st.session_state['xp']/100,1.0), text=f"⭐ XP: {st.session_state['xp']} / 100 bis Level Up")

cols=st.columns(4)
alle_faecher=list(VOKABELN.keys())+["Geschichte","Physik"]
for i,fach in enumerate(alle_faecher):
    if cols[i%4].button(f"📖 {fach}", key=f"fach_{fach}", use_container_width=True):
        st.session_state['fach']=fach
        for k in ['lek','thema','vok_idx']: st.session_state.pop(k,None)

if 'fach' in st.session_state:
    fach=st.session_state['fach']
    st.write("---")
    st.markdown(f"## {fach}")

    # In-Fach Suche
    fs=st.text_input(f"🔍 In {fach} suchen", placeholder="z.B. Brot, gehen, 1961...", key=f"fs_{fach}")

    if fach in VOKABELN:
        leks=list(VOKABELN[fach].keys())
        if fs:
            fs_low=fs.lower()
            leks=[l for l in leks if fs_low in l.lower() or any(fs_low in f.lower() or fs_low in d.lower() for f,d in VOKABELN[fach][l])]

        lc=st.columns(5)
        for j,lek in enumerate(leks):
            if lc[j%5].button(lek, key=f"lekb_{fach}_{lek}", use_container_width=True):
                st.session_state['lek']=lek
                st.session_state['vok_test']=False

        if 'lek' in st.session_state and st.session_state['lek'] in VOKABELN[fach]:
            lek=st.session_state['lek']
            lst=VOKABELN[fach][lek]
            if fs:
                fs_low=fs.lower()
                lst=[(f,d) for f,d in lst if fs_low in f.lower() or fs_low in d.lower()]

            st.write("---")
            with st.expander(f"📝 {lek} - {len(lst)} Vokabeln", expanded=True):
                for fremd,deutsch in lst:
                    st.markdown(f'<div class="vok-card"><b>{fremd}</b> = {deutsch}</div>', unsafe_allow_html=True)

            # TEST
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Test {lek}")

            c1,c2=st.columns(2)
            if c1.button(f"▶️ 10 Fragen Test", key=f"test10_{fach}_{lek}", use_container_width=True):
                st.session_state['vok_test']=True
                st.session_state['vok_fragen']=random.sample(lst, min(10,len(lst)))
                st.session_state['vok_idx']=0; st.session_state['vok_score']=0; st.session_state['modus']="10"

            if c2.button(f"🏆 20 Fragen Härtetest", key=f"test20_{fach}_{lek}", use_container_width=True):
                st.session_state['vok_test']=True
                st.session_state['vok_fragen']=random.sample(lst, min(20,len(lst)))
                st.session_state['vok_idx']=0; st.session_state['vok_score']=0; st.session_state['modus']="20"

            if st.session_state.get('vok_test'):
                fragen=st.session_state.get('vok_fragen',[])
                idx=st.session_state.get('vok_idx',0)
                score=st.session_state.get('vok_score',0)

                if idx < len(fragen):
                    st.progress((idx)/len(fragen), text=f"Frage {idx+1}/{len(fragen)} - Score {score}")
                    fremd,deutsch=fragen[idx]
                    # Abwechselnd
                    richtung = idx%2==0 # True Fremd->Deutsch
                    if richtung:
                        st.markdown(f"### Was heißt **{fremd}**?")
                        falsche=[d for _,d in lst if d!=deutsch]
                        opts=[deutsch]+random.sample(falsche, min(3,len(falsche)))
                        random.shuffle(opts)
                    else:
                        st.markdown(f"### Wie heißt **{deutsch}** auf {fach}?")
                        falsche=[f for f,_ in lst if f!=fremd]
                        opts=[fremd]+random.sample(falsche, min(3,len(falsche)))
                        random.shuffle(opts)
                        deutsch_tmp=fremd; fremd=deutsch; deutsch=deutsch_tmp # swap für check
                        # eigentlich für check merken
                        # Wir speichern original
                        orig_fremd, orig_deutsch = fragen[idx]

                    # Buttons statt Radio -> besser
                    cols_ans=st.columns(2)
                    for i,opt in enumerate(opts):
                        if cols_ans[i%2].button(opt, key=f"ans_{fach}_{lek}_{idx}_{i}", use_container_width=True):
                            # Check
                            if richtung:
                                richtig = (opt == deutsch)
                                correct_text = deutsch
                            else:
                                orig_fremd, orig_deutsch = fragen[idx]
                                richtig = (opt == orig_fremd)
                                correct_text = orig_fremd

                            if richtig:
                                st.success(f"✅ Richtig! {fragen[idx][0]} = {fragen[idx][1]} 🎉")
                                st.balloons()
                                st.session_state['vok_score']=score+1
                                st.session_state['xp']+=5
                            else:
                                st.error(f"❌ Falsch! Richtig: {fragen[idx][0]} = {fragen[idx][1]}")
                            st.session_state['vok_idx']=idx+1
                            time.sleep(0.9)
                            st.rerun()
                else:
                    total=len(fragen)
                    st.markdown(f"### 🏁 Fertig! {score}/{total}")
                    if score==total:
                        st.balloons(); st.snow()
                        st.success(f"🌟 PERFEKT! {score}/{total} - +20 XP!")
                        st.session_state['xp']+=20
                    elif score>=total*0.8:
                        st.success(f"🎉 Sehr stark! {score}/{total} - +10 XP!")
                        st.balloons()
                        st.session_state['xp']+=10
                    elif score>=total*0.5:
                        st.warning(f"👍 Gut! {score}/{total} - +5 XP")
                        st.session_state['xp']+=5
                    else:
                        st.error(f"💪 Üben! {score}/{total}")

                    if st.button("🔄 Nochmal", key=f"again_{fach}_{lek}", use_container_width=True):
                        st.session_state['vok_fragen']=random.sample(lst, min(len(fragen),len(lst)))
                        st.session_state['vok_idx']=0; st.session_state['vok_score']=0
                        st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

            # Gesamttest
            if st.button(f"🔥 GESAMTTEST {fach} 100 Vokabeln - 20 Fragen", key=f"gesamt_{fach}", use_container_width=True):
                alle=[]
                for l in VOKABELN[fach].values(): alle.extend(l)
                st.session_state['lek']="GESAMTTEST 100"
                st.session_state['vok_test']=True
                st.session_state['vok_fragen']=random.sample(alle, 20)
                st.session_state['vok_idx']=0; st.session_state['vok_score']=0
                st.rerun()

    # Themen Fächer
    if fach in THEMEN:
        th=THEMEN[fach]
        if fs:
            fs_low=fs.lower()
            th={k:v for k,v in th.items() if fs_low in k.lower() or fs_low in v["t"].lower()}

        st.markdown(f"### 📖 Themen {fach} - {len(th)} Stück")
        tc=st.columns(3)
        for j,tname in enumerate(th.keys()):
            if tc[j%3].button(tname, key=f"thb_{fach}_{tname}", use_container_width=True):
                st.session_state['thema']=tname

        if 'thema' in st.session_state and st.session_state['thema'] in th:
            tname=st.session_state['thema']; d=th[tname]
            st.write("---")
            st.info(f"**{tname}:** {d['t']}")
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Test {tname}")
            for qi,(fr,ri,fa) in enumerate(d["q"]):
                st.write(f"**{qi+1}. {fr}**")
                # Buttons
                c1,c2=st.columns(2)
                if f"done_{fach}_{tname}_{qi}" not in st.session_state:
                    if c1.button(ri, key=f"tq1_{fach}_{tname}_{qi}", use_container_width=True):
                        st.session_state[f"done_{fach}_{tname}_{qi}"]=True
                        st.session_state[f"res_{fach}_{tname}_{qi}"]=True
                        st.session_state['xp']+=3
                        st.rerun()
                    if c2.button(fa, key=f"tq2_{fach}_{tname}_{qi}", use_container_width=True):
                        st.session_state[f"done_{fach}_{tname}_{qi}"]=True
                        st.session_state[f"res_{fach}_{tname}_{qi}"]=False
                        st.rerun()
                else:
                    if st.session_state.get(f"res_{fach}_{tname}_{qi}"):
                        st.success(f"✅ Richtig! {ri} 🎉")
                    else:
                        st.error(f"❌ Richtig wäre: {ri}")
            st.markdown('</div>', unsafe_allow_html=True)

    if st.button("❌ Schließen", use_container_width=True):
        for k in list(st.session_state.keys()):
            if k not in ['xp']: del st.session_state[k]
        st.rerun()
