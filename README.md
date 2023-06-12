# PAOvaj kod implementira algoritam najkraćeg puta (Dijkstra algoritam) na usmerenom grafu. Evo šta se dešava u ovom kodu:

Definišu se dve klase: Vertex (čvor) i Edge (grana). Vertex klasa predstavlja čvor grafa sa svojim podacima, kao što su prethodnik (p), udaljenost (d) i ime (name). Edge klasa predstavlja granu grafa sa poljima src (polazni čvor), dst (odredišni čvor) i w (težina grane).

Definiše se klasa Graph (graf) koja sadrži listu čvorova (V) i listu grana (E). Konstruktor klase Graph inicijalizuje listu čvorova i listu grana.

Metoda ShortestPath prima dva čvora nodeA i nodeB i izračunava najkraći put između njih koristeći Dijkstra algoritam. Prvo se poziva metoda dijkstra koja izračunava najkraće puteve od nodeA do svih ostalih čvorova u grafu. Zatim se poziva metoda print_path koja konstruiše i štampa najkraći put od nodeA do nodeB. Uz to, ispisuje se i ukupna dužina najkraćeg puta.

Metoda getAdj vraća listu susednih čvorova za dati čvor v tako što prolazi kroz listu grana i proverava da li je čvor v početak grane.

Metoda getWeight vraća težinu grane između čvorova s (polazni) i d (odredišni) tako što prolazi kroz listu grana i traži grane koje odgovaraju polaznom i odredišnom čvoru.

Metoda relax ažurira udaljenost i prethodnika čvora v ako je put preko čvora u kraći od trenutnog najkraćeg puta do v.

Metoda initSingleSrc inicijalizuje udaljenosti svih čvorova na beskonačno (inf) osim početnog čvora s, čija se udaljenost postavlja na 0.

Metoda extractMin pronalazi čvor sa najmanjom udaljenošću iz liste čvorova Q.

Metoda dijkstra izračunava najkraće puteve od početnog čvora s do svih ostalih čvorova u grafu. Inicijalizuje se udaljenost svih čvorova, a zatim se dok ima neobeleženih čvorova bira čvor sa najmanjom udaljenošću, ažuriraju se udaljenosti susednih čvorova i čvor se premešta iz liste neobeleženih u listu obeleženih čvorova.

Metoda print_path rekonstruiše najkraći put od čvora s do čvora v koristeći prethodnike čvorova. Počevši od ciljnog čvora v, prelazi se kroz prethodnike sve dok se ne stigne do početnog čvora s. Na taj način se konstruiše lista čvorova koja predstavlja najkraći put. Lista se vraća i štampa se u metodi ShortestPath.

Kreiraju se instance čvorova vA, vB, vC, vD, vE, vF i grana ab, ad, ae, bc, cf, de, ec, fe, koje predstavljaju graf sa šest čvorova i osam grana.

Kreira se instanca grafa G koja sadrži sve čvorove i grane.

Ispisuje se sadržaj grafa G.

Poziva se metoda ShortestPath nad instancom grafa G sa početnim čvorom vA i ciljnim čvorom vE, što rezultira pronalaženjem najkraćeg puta između ova dva čvora i ispisivanjem putanje i ukupne dužine puta.
