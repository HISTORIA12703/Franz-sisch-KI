import streamlit as st

st.set_page_config(page_title="5 Sprachen KI", page_icon="🌍")
st.title("🌍 5 SPRACHEN MEGA KI")
st.write("Alle mit voller Grammatik + Vokabeln")
st.write("---")

sprache = st.selectbox("1. Sprache:", [
    "Französisch",
    "Latein",
    "Spanisch - VOLL",
    "Italienisch - VOLL",
    "Deutsch"
])

if "Französisch" in sprache:
    thema = st.selectbox("2. Thema:", [
        "Pronomen ALLE",
        "Direkte und Indirekte Rede",
        "le la lui y en",
        "Zeiten Futur Passe Imparfait",
        "VOKABELN",
        "Basics Articles etre"
    ])
elif "Spanisch" in sprache or "Italienisch" in sprache:
    thema = st.selectbox("2. Thema:", [
        "Pronomen ALLE mit Wann/Wie",
        "Direkte und Indirekte Rede",
        "Objektpronomen lo le ci ne",
        "Zeiten - Futur Vergangenheit Subjuntivo",
        "Ser Estar / Essere Avere + Por Para",
        "VOKABELN TOP 100",
        "Basics Artikel Verneinung"
    ])
else:
    thema = st.selectbox("2. Thema:", [
        "Pronomen",
        "Direkte und Indirekte Rede",
        "Grammatik Basics",
        "VOKABELN"
    ])

if st.button("Erklären"):
    st.write("---")

    # FRANZÖSISCH - DEIN ALTER CODE
    if sprache == "Französisch":
        if "Pronomen" in thema:
            st.write("je tu il elle nous vous ils")
            st.write("le la lui y en VOR Verb! Je le vois!")
            st.write("Reihenfolge me le lui y en + VERB")
            st.write("mon ma mes, le mien, qui que ou dont")
        elif "Direkte" in thema:
            st.write("Il dit: Je suis malade")
            st.write("Il dit qu'il est malade")
            st.write("il a dit-> Present->Imparfait, Futur->Conditionnel")
            st.write("Ou->ou, Que->ce que, JaNein->si, Befehl de+Inf")
        elif "le, la" in thema:
            st.write("le la COD, lui leur COI, y Ort, en Menge")
        elif "Zeiten" in thema:
            st.write("Futur proche Je vais manger")
            st.write("Futur simple parlerai serai aurai irai")
            st.write("Passe J'ai mange, Imparfait Je parlais")
        elif "VOKABELN" in thema:
            st.write("bonjour merci oui non, homme femme garcon fille")
            st.write("etre avoir faire aller vouloir dire voir")
            st.write("ecole livre professeur, pain eau manger boire")
            st.write("mais parce que tres beaucoup deja toujours")
        else:
            st.write("un une des, le la les, ne pas, Est-ce que")

    # SPANISCH VOLL
    elif "Spanisch" in sprache:
        if "Pronomen" in thema:
            st.subheader("SPANISCH PRONOMEN VOLL")
            st.write("WAS: Ersetzt Nomen")
            st.write("Personal: yo tu el ella nosotros vosotros ellos")
            st.write("Objekt direkt: me te lo la nos os los las")
            st.write("WANN: Wen? Was? Ohne a")
            st.write("Lo veo = Ich sehe ihn (Film)")
            st.write("La veo = Ich sehe sie")
            st.write("Objekt indirekt: me te le nos os les")
            st.write("WANN: Wem? Mit a bei Person")
            st.write("Le hablo = Ich spreche mit ihm")
            st.write("Les doy = Ich gebe ihnen")
            st.write("WICHTIG: le wird zu se vor lo!")
            st.write("Le lo doy -> Se lo doy = Ich gebe es ihm")
            st.write("Reihenfolge: me te se lo le + VERB")
            st.write("Me lo da, Te lo digo")
            st.write("Possessiv: mi tu su nuestro vuestro su")
            st.write("mi libro, mis libros")
            st.write("Relativ: que der, quien wer, donde wo")
            st.write("cuyo dessen: el hombre cuyo libro")

        elif "Direkte" in thema:
            st.subheader("INDIREKTE REDE SPANISCH")
            st.write("Direkt: Dice: Estoy enfermo")
            st.write("Indirekt Praesens: Dice que esta enfermo")
            st.write("Zeit bleibt bei dice!")
            st.write("Indirekt Vergangenheit: Dijo que...")
            st.write("WANN Zeit ändern:")
            st.write("Presente->Imperfecto: estoy->estaba")
            st.write("Indefinido->Pluscuamperfecto: fui->habia sido")
            st.write("Futuro->Condicional: ire->iria")
            st.write("Fragen: Donde vas?->donde iba")
            st.write("Que haces?->lo que hacia")
            st.write("Vienes?->si venia")
            st.write("Befehl: Ven!->que viniera / de venir")
            st.write("Me dice que venga = Er sagt ich soll kommen")

        elif "Objektpronomen" in thema:
            st.subheader("lo le la - UNTERSCHIED!")
            st.write("lo = ihn/es direkt")
            st.write("Veo el libro->Lo veo")
            st.write("le = ihm indirekt")
            st.write("Hablo a Juan->Le hablo")
            st.write("Aber Achtung: In Spanien oft le fuer Person!")
            st.write("Le vi a Juan = Ich sah Juan (leismo)")
            st.write("Regel Schule: lo fuer Sache, le fuer Person mit a")
            st.write("y/en gibt es NICHT! Stattdessen:")
            st.write("y -> alli, ahi: Vas a Paris? Voy alli")
            st.write("en -> de ello: Hablas de Juan? Hablo de el")

        elif "Zeiten" in thema:
            st.subheader("ZEITEN SPANISCH VOLL")
            st.write("Futur: Infinitiv+Endung e as a emos eis an")
            st.write("hablar->hablare hablaras hablara")
            st.write("comer->comere, vivir->vivire")
            st.write("Irregular: tener->tendre, hacer->hare")
            st.write("decir->dire, venir->vendre, poder->podre")
            st.write("Futur nah: ir a + Inf: Voy a comer")
            st.write("Preterito Indefinido: hable hablaste hablo")
            st.write("Imperfecto: hablaba hablabas hablaba")
            st.write("Unterschied: Indefinido einmalig, Imperf immer")
            st.write("Ayer llovio (einmal), Cuando era nino llovia (immer)")
            st.write("Perfekt: he hablado, Plusquam: habia hablado")
            st.write("Subjuntivo: quiero que hables!")
            st.write("WANN: Wunsch, Zweifel, nach que, Emotion")

        elif "Ser Estar" in thema:
            st.subheader("SER vs ESTAR + POR PARA")
            st.write("SER = was etwas IST permanent")
            st.write("Soy aleman, Es grande, Son las 3")
            st.write("ESTAR = wo/wie etwas IST Zustand/Ort")
            st.write("Estoy cansado, Estoy en casa, Esta roto")
            st.write("Trick: ESTAR Ort und Zustand!")
            st.write("POR = durch, wegen, für Zeit, Tausch")
            st.write("Gracias por todo, Por la mañana")
            st.write("PARA = für Zweck, Ziel, Empfänger")
            st.write("Esto es para ti, Para comer, Para mañana")

        elif "VOKABELN" in thema:
            st.write("hola gracias si no, hombre mujer chico chica")
            st.write("ser estar tener hacer ir querer poder decir ver")
            st.write("escuela libro pan agua comer beber")
            st.write("pero porque muy mucho ya siempre con sin para")

        else:
            st.write("un una unos unas, el la los las")
            st.write("no hablo, no nunca, no nada")

    # ITALIENISCH VOLL
    elif "Italienisch" in sprache:
        if "Pronomen" in thema:
            st.subheader("ITALIENISCH PRONOMEN VOLL")
            st.write("Personal: io tu lui lei noi voi loro")
            st.write("Direkt: mi ti lo la ci vi li le")
            st.write("lo=ihn, la=sie, li=sie m Plural, le=sie f Plural")
            st.write("Lo vedo = Ich sehe ihn")
            st.write("Indirekt: mi ti gli le ci vi gli")
            st.write("gli=ihm, le=ihr, gli=ihnen (alle!)")
            st.write("Le parlo = Ich spreche mit ihr")
            st.write("Gli parlo = Ich spreche mit ihm/ihnen")
            st.write("gli + lo -> glielo! Glielo do = Ich gebe es ihm")
            st.write("WICHTIG: ci und ne wie y und en!")
            st.write("ci = dort, hier, daran (wie y)")
            st.write("Vado a Roma->Ci vado = Ich gehe dorthin")
            st.write("Ci penso = Ich denke daran")
            st.write("ne = davon, welche (wie en)")
            st.write("Vuoi del pane? Ne voglio due = Ich will 2 davon")
            st.write("Ne parlo = Ich spreche davon")
            st.write("Reihenfolge: mi lo gli ci ne + VERB")
            st.write("Me lo da, Ce ne sono due")
            st.write("Possessiv: mio tuo suo nostro vostro loro")
            st.write("Relativ: che, cui, dove, il cui dessen")

        elif "Direkte" in thema:
            st.subheader("INDIREKTE REDE ITALIENISCH")
            st.write("Direkt: Dice: Sono malato")
            st.write("Indirekt: Dice che e malato")
            st.write("Zeit bleibt bei dice presente")
            st.write("Bei ha detto: Zeit ändern!")
            st.write("Presente->Imperfetto: sono->era")
            st.write("Passato->Trapassato: ho fatto->avevo fatto")
            st.write("Futuro->Condizionale: verro->sarebbe venuto")
            st.write("Fragen: Dove vai?->dove andavo")
            st.write("Che fai?->cio che facevo")
            st.write("Vieni?->se venivo")
            st.write("Befehl: Vieni!->di venire / che venisse")

        elif "Objektpronomen" in thema:
            st.subheader("ci ne - WIE y en!")
            st.write("Franz y = Ital ci = Span alli")
            st.write("Franz en = Ital ne")
            st.write("Gleiches System! Nur anderes Wort!")
            st.write("Franz J'y vais = Ital Ci vado = Span Voy alli")
            st.write("Franz J'en veux 2 = Ital Ne voglio 2")
            st.write("Franz J'en parle = Ital Ne parlo")
            st.write("Das musst du für Prüfung wissen!")

        elif "Zeiten" in thema:
            st.subheader("ZEITEN ITALIENISCH VOLL")
            st.write("Futur: Inf ohne e + o ai a emo ete anno")
            st.write("parlare->parlero parlerai parlera")
            st.write("avere->avro, essere->saro, andare->andro")
            st.write("fare->faro, venire->verro, vedere->vedro")
            st.write("Futur nah: stare per + Inf: Sto per mangiare")
            st.write("Passato prossimo: ho parlato, sono andato")
            st.write("14 Verben mit essere wie Franz etre!")
            st.write("andare venire entrare uscire restare etc")
            st.write("Imperfetto: parlavo parlavi parlava")
            st.write("Perf=einmalig, Imperf=immer wie Span/Franz")
            st.write("Ieri ha piovuto, Da bambino pioveva sempre")
            st.write("Trapassato: avevo parlato")
            st.write("Congiuntivo: voglio che tu parli!")

        elif "Ser Estar" in thema:
            st.subheader("ESSERE vs STARE + ARTIKEL")
            st.write("ESSERE = sein permanent wie ser")
            st.write("Sono tedesco, E grande")
            st.write("STARE = Ort, Zustand, gerade dabei wie estar")
            st.write("Sto a casa, Sto male, Sto mangiando=Ich esse gerade")
            st.write("Artikel: il lo la i gli le, un uno una")
            st.write("il libro, lo studente, l'amico, la casa")
            st.write("Preposizioni articolate: al, del, nel, sul = a+il etc")

        elif "VOKABELN" in thema:
            st.write("ciao grazie si no, uomo donna ragazzo ragazza")
            st.write("essere avere fare andare volere potere dire vedere")
            st.write("scuola libro pane acqua mangiare bere")
            st.write("ma perche molto gia sempre con senza per, ci ne!")

        else:
            st.write("il la lo, un una, non parlo, non mai niente")

    # LATEIN / DEUTSCH KURZ
    elif sprache == "Latein":
        if "VOKABELN" in thema:
            st.write("esse habere dicere facere videre audire ire venire")
            st.write("homo vir femina rex populus urbs bellum amicus")
        else:
            st.write("Latein: AcI, Kasus, Deklinationen, Konjunktionen")

    elif sprache == "Deutsch":
        if "VOKABELN" in thema:
            st.write("behaupten aeussern vermuten hervorragend")
            st.write("Meiner Meinung nach, Im Gegensatz zu")
        else:
            st.write("Konjunktiv I: er sei habe solle, Nebensatz Verb Ende")

    st.success("Fertig!")

st.caption("v10.0 VOLL - Franz Latein Span Ital Deutsch")
