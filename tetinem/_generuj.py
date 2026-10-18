# Generátor jazykových verzí stránky aplikace TETÍNEM.
# Spuštění: python3 tetinem/_generuj.py  (z kořene repozitáře red-apps)
# Česká verze je index.html, ostatní en.html, de.html, es.html, pl.html, fr.html, uk.html.
import html, os

LANGS = [('cs', '🇨🇿', 'Čeština', 'index.html'), ('en', '🇬🇧', 'English', 'en.html'), ('de', '🇩🇪', 'Deutsch', 'de.html'),
         ('es', '🇪🇸', 'Español', 'es.html'), ('pl', '🇵🇱', 'Polski', 'pl.html'), ('fr', '🇫🇷', 'Français', 'fr.html'),
         ('uk', '🇺🇦', 'Українська', 'uk.html')]
SHOTS = ['tetinem-1.jpg', 'tetinem-2.jpg', 'tetinem-3.jpg', 'tetinem-4.jpg', 'tetinem-5.jpg', 'tetinem-6.jpg',
         'tetinem-diplom.jpg', 'tetinem-pohlednice.jpg']
MAIL = '<a href="mailto:redapps.support@gmail.com">redapps.support@gmail.com</a>'

T = {}

T['cs'] = dict(
    title='TETÍNEM — Průvodce a příběhy obce Tetín',
    desc='Turistický průvodce obcí Tetín s mapou, trasami, příběhy a pověstmi. Audioprůvodce, který začne vyprávět sám, jakmile dojdete k zajímavému místu. Česky, anglicky, německy, španělsky, polsky, francouzsky a ukrajinsky.',
    nav_apps='Aplikace', nav_support='Podpora', nav_privacy='Soukromí', country='Česká republika',
    sub='Průvodce a příběhy obce Tetín',
    lead='Turistický průvodce jedním z nejstarších míst české historie. Mapa s místy a trasami, příběhy a pověsti ke čtení i poslechu a audioprůvodce, který začne vyprávět sám, jakmile k místu dojdete. Česky, anglicky, německy, španělsky, polsky, francouzsky a ukrajinsky.',
    status_b='V testování',
    status=f'Na iPhonu běží veřejné testování přes TestFlight, verze pro Android čeká na schválení v Google Play. Napište na {MAIL}, jestli chcete aplikaci vyzkoušet nebo vědět, až bude ke stažení.',
    pros=[('Průvodce, který vypráví sám', 'Schovejte telefon do kapsy a vyrazte. Jakmile dojdete k zajímavému místu, průvodce začne vyprávět jeho příběh — i se zamčeným telefonem.'),
          ('Příběhy na starém papíře', 'Příběhy, pověsti a zajímavosti o kněžně Tetě, svaté Ludmile a tetínském hradu. Ke čtení i k poslechu, v sedmi jazycích.'),
          ('Funguje i bez signálu', 'V údolí a pod skalami signál bývá slabý. Průvodce si stáhnete předem a příběhy, fotky i trasy máte v telefonu.'),
          ('Hra a diplom pro děti', 'U devíti míst čeká otázka. Za správnou odpověď zazní znělka a do sbírky přibude razítko. Kdo nasbírá všechna, dostane diplom se svým jménem.')],
    features_h='Co aplikace umí',
    features=['Interaktivní mapa s místy, filtry a vrstvami, které jde zapínat a vypínat',
              'Turistické podklady Mapy.com — turistická, základní a letecká mapa',
              'Naučné trasy z GPX s vaší polohou a ukazatelem, kolik už máte ušlo',
              'U tras piktogramy a filtr: s kočárkem, s vozíkem, se psem, schody, náročnost terénu',
              'Pěší navigace k místu přímo v aplikaci, s hlasovými pokyny k odbočení — i se zamčeným telefonem',
              'Příběhy, pověsti a zajímavosti — samostatně i u konkrétních míst',
              'Audioprůvodce s nahrávkami, případně předčítání hlasem telefonu',
              'Režim procházky: příběh se spustí sám, když dojdete k místu',
              'QR kódy na cedulích u míst — naskenujete a příběh hned hraje',
              'U muzea, kostelů a restaurací „Otevřeno do…“ nebo „Zavřeno“ podle otevírací doby',
              'Tipy pro turisty: kde se najíst, parkování, WC, jak se k nám dostat',
              'Průvodcovská služba a kontakty s tlačítky Zavolat a E-mail',
              'Hra pro děti: u každého místa otázka, za správnou odpověď znělka a razítko do sbírky',
              'Diplom tetínského objevitele se jménem dítěte za všechna razítka — uložit nebo poslat',
              'Pohlednice „Pozdravy z Tetína“: vlastní fotka v rámečku se svatou Ludmilou, svatým Václavem a kněžnou Tetou',
              '„Tenkrát a dnes“ — stará pohlednice a dnešní pohled pod jedním posuvníkem',
              'Hotový plán výletu na půl dne s obědem a vyhlídkami, který můžete ohodnotit hvězdičkami',
              'Kalendář akcí — pouť, koncerty, výstavy',
              'Upozornění od obce přímo na úvodní obrazovce — třeba na kluzké vyhlídky nebo zavřený kostel',
              'Pošlete vlastní fotku z výletu, po schválení ji uvidí ostatní; nevhodnou fotku jde nahlásit',
              'Offline režim — příběhy, fotky a nahrávky stažené předem',
              'Sedm jazyků — čeština, angličtina, němčina, španělština, polština, francouzština a ukrajinština — přepnete vlaječkou',
              'Překlady do cizích jazyků vznikají pomocí umělé inteligence (DeepL) a aplikace na to u textů upozorňuje; nový obsah z obce se do všech jazyků přeloží sám',
              'Obsah průběžně doplňují lidé z obce přes webovou administraci, bez nové verze aplikace'],
    gallery_h='Jak to vypadá',
    shots=['Úvodní obrazovka', 'Mapa míst a tras', 'Příběhy a pověsti', 'Audioprůvodce', 'Hra pro děti',
           'Výlet na půl dne', 'Diplom za všechna razítka', 'Pohlednice z výletu'],
    shots_note='',
    privacy_h='Bezpečnost a soukromí',
    privacy='Aplikace nevyžaduje registraci, neobsahuje reklamu a nesleduje vás – sbírá jen anonymní denní součty (kolikrát se spustila a co se v ní otevíralo). Poloha se zpracovává jen v telefonu; pro výpočet pěší trasy se výchozí bod a cíl pošlou mapové službě. Obsah průvodce se stahuje z našeho serveru v EU. Pokud sami pošlete fotku, uloží se tam a před zveřejněním ji schvaluje správce. Hodnocení výletu a nahlášení fotky jsou anonymní — aplikace k nim posílá jen náhodné číslo instalace, aby šlo hlasovat jen jednou. Diplom a pohlednice se vytvářejí přímo v telefonu a nikam se neposílají, dokud je sami nesdílíte.',
    policy='Zásady ochrany osobních údajů',
    req='iOS a Android · příběhy a fotky lze stáhnout pro použití bez signálu',
    ai_note='',
    lang_label='Jazyk stránky',
)

T['en'] = dict(
    title='TETÍNEM — Guide & stories of Tetín',
    desc='A visitor guide to the village of Tetín with a map, routes, stories and legends. An audio guide that starts talking by itself when you reach an interesting place. In Czech, English, German, Spanish, Polish, French and Ukrainian.',
    nav_apps='Apps', nav_support='Support', nav_privacy='Privacy', country='Czech Republic',
    sub='Guide & stories of the village of Tetín',
    lead='A visitor guide to one of the oldest places in Czech history. A map with places and routes, stories and legends to read or listen to, and an audio guide that starts talking by itself as soon as you reach a place. In Czech, English, German, Spanish, Polish, French and Ukrainian.',
    status_b='In testing',
    status=f'Public testing is running on iPhone via TestFlight; the Android version is awaiting approval on Google Play. Write to {MAIL} if you would like to try the app or be told when it is available.',
    pros=[('A guide that tells the story itself', 'Put your phone in your pocket and go. When you reach an interesting place, the guide starts telling its story — even with the phone locked.'),
          ('Stories on old paper', 'Stories, legends and curiosities about Princess Teta, Saint Ludmila and Tetín Castle. To read or listen to, in seven languages.'),
          ('Works without signal', 'The signal is often weak in the valley and below the cliffs. Download the guide in advance and keep the stories, photos and routes on your phone.'),
          ('A game and a diploma for kids', 'A question waits at nine places. A correct answer plays a jingle and adds a stamp to the collection. Collect them all and get a diploma with your name.')],
    features_h='What the app can do',
    features=['Interactive map with places, filters and layers you can switch on and off',
              'Mapy.com base maps — hiking, standard and aerial',
              'Nature trails from GPX with your position and how far you have walked',
              'Route pictograms and filters: pushchair, wheelchair, dogs, steps, terrain difficulty',
              'Walking navigation to a place right in the app, with spoken turn-by-turn directions — even with the phone locked',
              'Stories, legends and curiosities — on their own and for each place',
              'Audio guide with recordings, or read aloud by the phone’s voice',
              'Walk mode: a story starts by itself when you reach a place',
              'QR codes on signs at each place — scan and the story plays right away',
              '“Open until…” or “Closed” for the museum, churches and restaurants based on opening hours',
              'Tips for visitors: where to eat, parking, toilets, how to get here',
              'Guided tours and contacts with Call and E-mail buttons',
              'Kids’ game: a question at each place, a jingle and a stamp for every correct answer',
              'Tetín Explorer diploma with the child’s name for all stamps — save or share',
              '“Greetings from Tetín” postcard: your own photo in a frame with Saint Ludmila, Saint Wenceslas and Princess Teta',
              '“Then and now” — an old postcard and today’s view under one slider',
              'A ready-made half-day trip with lunch and viewpoints that you can rate with stars',
              'Events calendar — pilgrimage, concerts, exhibitions',
              'Notices from the village right on the home screen — e.g. slippery viewpoints or a closed church',
              'Send your own photo from the trip; once approved, others will see it; inappropriate photos can be reported',
              'Offline mode — stories, photos and recordings downloaded in advance',
              'Seven languages — Czech, English, German, Spanish, Polish, French and Ukrainian — switch with a flag',
              'Translations are made with artificial intelligence (DeepL) and the app says so next to the texts; new content from the village is translated into all languages automatically',
              'Content is continuously added by people from the village through a web admin, without a new app version'],
    gallery_h='What it looks like',
    shots=['Home screen', 'Map of places and routes', 'Stories and legends', 'Audio guide', 'Kids’ game',
           'Half-day trip', 'Diploma for all stamps', 'Postcard from the trip'],
    shots_note='Screenshots show the Czech version of the app.',
    privacy_h='Security and privacy',
    privacy='The app requires no registration, contains no ads and does not track you – it only collects anonymous daily totals (how many times it was opened and what was viewed). Your location is processed only on the phone; to calculate a walking route, the start and destination are sent to the map service. The guide content is downloaded from our server in the EU. If you send a photo yourself, it is stored there and approved by an administrator before publication. Trip ratings and photo reports are anonymous — the app only sends a random installation number so that each person can vote once. The diploma and postcard are created on the phone and are not sent anywhere unless you share them.',
    policy='Privacy policy (Czech / English)',
    req='iOS and Android · stories and photos can be downloaded for use without signal',
    ai_note='This page was translated with the help of AI.',
    lang_label='Page language',
)

T['de'] = dict(
    title='TETÍNEM — Reiseführer & Geschichten aus Tetín',
    desc='Ein Reiseführer für das Dorf Tetín mit Karte, Routen, Geschichten und Sagen. Ein Audioguide, der von selbst zu erzählen beginnt, sobald Sie einen interessanten Ort erreichen. Auf Tschechisch, Englisch, Deutsch, Spanisch, Polnisch, Französisch und Ukrainisch.',
    nav_apps='Apps', nav_support='Support', nav_privacy='Datenschutz', country='Tschechische Republik',
    sub='Reiseführer & Geschichten aus Tetín',
    lead='Ein Reiseführer zu einem der ältesten Orte der tschechischen Geschichte. Eine Karte mit Orten und Routen, Geschichten und Sagen zum Lesen und Hören und ein Audioguide, der von selbst zu erzählen beginnt, sobald Sie einen Ort erreichen. Auf Tschechisch, Englisch, Deutsch, Spanisch, Polnisch, Französisch und Ukrainisch.',
    status_b='Im Test',
    status=f'Auf dem iPhone läuft ein öffentlicher Test über TestFlight, die Android-Version wartet auf die Freigabe bei Google Play. Schreiben Sie an {MAIL}, wenn Sie die App ausprobieren oder erfahren möchten, wann sie verfügbar ist.',
    pros=[('Ein Reiseführer, der selbst erzählt', 'Stecken Sie das Handy in die Tasche und gehen Sie los. Sobald Sie einen interessanten Ort erreichen, erzählt der Guide seine Geschichte — auch bei gesperrtem Handy.'),
          ('Geschichten auf altem Papier', 'Geschichten, Sagen und Wissenswertes über Fürstin Teta, die heilige Ludmila und die Burg Tetín. Zum Lesen und Hören, in sieben Sprachen.'),
          ('Funktioniert auch ohne Empfang', 'Im Tal und unter den Felsen ist der Empfang oft schwach. Laden Sie den Guide vorab herunter – Geschichten, Fotos und Routen haben Sie dann auf dem Handy.'),
          ('Spiel und Urkunde für Kinder', 'An neun Orten wartet eine Frage. Für die richtige Antwort ertönt eine Melodie und ein Stempel kommt in die Sammlung. Wer alle sammelt, bekommt eine Urkunde mit seinem Namen.')],
    features_h='Was die App kann',
    features=['Interaktive Karte mit Orten, Filtern und ein- und ausschaltbaren Ebenen',
              'Kartengrundlagen von Mapy.com — Wander-, Standard- und Luftbildkarte',
              'Lehrpfade aus GPX mit Ihrer Position und Anzeige, wie weit Sie schon gegangen sind',
              'Piktogramme und Filter bei den Routen: Kinderwagen, Rollstuhl, Hunde, Stufen, Schwierigkeit',
              'Fußgängernavigation zum Ort direkt in der App, mit Sprachansagen zum Abbiegen — auch bei gesperrtem Handy',
              'Geschichten, Sagen und Wissenswertes — einzeln und bei den einzelnen Orten',
              'Audioguide mit Aufnahmen oder Vorlesen durch die Stimme des Handys',
              'Spaziermodus: Die Geschichte startet von selbst, wenn Sie den Ort erreichen',
              'QR-Codes auf Schildern an den Orten — scannen und die Geschichte läuft sofort',
              '„Geöffnet bis…“ oder „Geschlossen“ bei Museum, Kirchen und Restaurants nach Öffnungszeiten',
              'Tipps für Besucher: Essen, Parken, WC, Anreise',
              'Führungen und Kontakte mit den Tasten Anrufen und E-Mail',
              'Kinderspiel: an jedem Ort eine Frage, für die richtige Antwort Melodie und Stempel',
              'Urkunde des Tetín-Entdeckers mit dem Namen des Kindes für alle Stempel — speichern oder teilen',
              'Postkarte „Grüße aus Tetín“: eigenes Foto im Rahmen mit der heiligen Ludmila, dem heiligen Wenzel und Fürstin Teta',
              '„Damals und heute“ — alte Postkarte und heutiger Blick unter einem Schieberegler',
              'Fertiger Halbtagesausflug mit Mittagessen und Aussichtspunkten, den Sie mit Sternen bewerten können',
              'Veranstaltungskalender — Wallfahrt, Konzerte, Ausstellungen',
              'Hinweise der Gemeinde direkt auf dem Startbildschirm — etwa rutschige Aussichtspunkte oder eine geschlossene Kirche',
              'Schicken Sie Ihr eigenes Ausflugsfoto; nach der Freigabe sehen es auch andere; unpassende Fotos können gemeldet werden',
              'Offline-Modus — Geschichten, Fotos und Aufnahmen vorab heruntergeladen',
              'Sieben Sprachen — Tschechisch, Englisch, Deutsch, Spanisch, Polnisch, Französisch und Ukrainisch — per Flagge umschalten',
              'Übersetzungen entstehen mit künstlicher Intelligenz (DeepL), und die App weist bei den Texten darauf hin; neue Inhalte der Gemeinde werden automatisch in alle Sprachen übersetzt',
              'Die Inhalte ergänzen Menschen aus dem Dorf laufend über eine Web-Verwaltung, ohne neue App-Version'],
    gallery_h='So sieht es aus',
    shots=['Startbildschirm', 'Karte der Orte und Routen', 'Geschichten und Sagen', 'Audioguide', 'Kinderspiel',
           'Halbtagesausflug', 'Urkunde für alle Stempel', 'Postkarte vom Ausflug'],
    shots_note='Die Bildschirmfotos zeigen die tschechische Version der App.',
    privacy_h='Sicherheit und Datenschutz',
    privacy='Die App erfordert keine Registrierung, enthält keine Werbung und verfolgt Sie nicht – sie erfasst nur anonyme Tagessummen (wie oft sie geöffnet und was angesehen wurde). Ihr Standort wird nur auf dem Handy verarbeitet; zur Berechnung einer Fußroute werden Start und Ziel an den Kartendienst gesendet. Die Inhalte werden von unserem Server in der EU geladen. Wenn Sie selbst ein Foto senden, wird es dort gespeichert und vor der Veröffentlichung von einem Administrator freigegeben. Bewertungen und Fotomeldungen sind anonym — die App sendet nur eine zufällige Installationsnummer, damit jede Person nur einmal abstimmen kann. Urkunde und Postkarte entstehen direkt auf dem Handy und werden nirgendwohin gesendet, solange Sie sie nicht teilen.',
    policy='Datenschutzerklärung (Tschechisch / Englisch)',
    req='iOS und Android · Geschichten und Fotos lassen sich für die Nutzung ohne Empfang herunterladen',
    ai_note='Diese Seite wurde mit Hilfe von KI übersetzt.',
    lang_label='Sprache der Seite',
)

T['es'] = dict(
    title='TETÍNEM — Guía e historias de Tetín',
    desc='Una guía turística del pueblo de Tetín con mapa, rutas, historias y leyendas. Una audioguía que empieza a narrar sola en cuanto llegas a un lugar interesante. En checo, inglés, alemán, español, polaco, francés y ucraniano.',
    nav_apps='Aplicaciones', nav_support='Soporte', nav_privacy='Privacidad', country='República Checa',
    sub='Guía e historias del pueblo de Tetín',
    lead='Una guía turística de uno de los lugares más antiguos de la historia checa. Un mapa con lugares y rutas, historias y leyendas para leer o escuchar y una audioguía que empieza a narrar sola en cuanto llegas a un lugar. En checo, inglés, alemán, español, polaco, francés y ucraniano.',
    status_b='En pruebas',
    status=f'En iPhone hay una prueba pública a través de TestFlight; la versión para Android espera la aprobación en Google Play. Escribe a {MAIL} si quieres probar la aplicación o saber cuándo estará disponible.',
    pros=[('Una guía que narra sola', 'Guarda el móvil en el bolsillo y ponte en marcha. Al llegar a un lugar interesante, la guía empieza a contar su historia, incluso con el móvil bloqueado.'),
          ('Historias en papel antiguo', 'Historias, leyendas y curiosidades sobre la princesa Teta, santa Ludmila y el castillo de Tetín. Para leer o escuchar, en siete idiomas.'),
          ('Funciona sin cobertura', 'En el valle y bajo las rocas la cobertura suele ser débil. Descarga la guía con antelación y tendrás historias, fotos y rutas en el móvil.'),
          ('Juego y diploma para niños', 'En nueve lugares espera una pregunta. Cada respuesta correcta suena con una melodía y suma un sello a la colección. Quien los reúna todos recibe un diploma con su nombre.')],
    features_h='Qué ofrece la aplicación',
    features=['Mapa interactivo con lugares, filtros y capas que se pueden activar y desactivar',
              'Mapas base de Mapy.com: senderismo, básico y aéreo',
              'Rutas didácticas desde GPX con tu posición y la distancia recorrida',
              'Pictogramas y filtros en las rutas: carrito, silla de ruedas, perros, escaleras, dificultad',
              'Navegación a pie hasta el lugar dentro de la aplicación, con indicaciones de voz para cada giro, incluso con el móvil bloqueado',
              'Historias, leyendas y curiosidades, sueltas y junto a cada lugar',
              'Audioguía con grabaciones o lectura con la voz del móvil',
              'Modo paseo: la historia empieza sola al llegar al lugar',
              'Códigos QR en los carteles de cada lugar: escanea y la historia suena al instante',
              '«Abierto hasta…» o «Cerrado» en el museo, las iglesias y los restaurantes según el horario',
              'Consejos para visitantes: dónde comer, aparcamiento, aseos, cómo llegar',
              'Visitas guiadas y contactos con botones de Llamar y Correo',
              'Juego para niños: una pregunta en cada lugar, melodía y sello por cada respuesta correcta',
              'Diploma de explorador de Tetín con el nombre del niño por todos los sellos: guardar o compartir',
              'Postal «Saludos desde Tetín»: tu propia foto en un marco con santa Ludmila, san Wenceslao y la princesa Teta',
              '«Antes y ahora»: una postal antigua y la vista actual bajo un mismo deslizador',
              'Una excursión de medio día ya preparada, con comida y miradores, que puedes valorar con estrellas',
              'Calendario de eventos: romería, conciertos, exposiciones',
              'Avisos del ayuntamiento en la pantalla de inicio, por ejemplo miradores resbaladizos o una iglesia cerrada',
              'Envía tu propia foto de la excursión; tras aprobarla la verán los demás; las fotos inapropiadas se pueden denunciar',
              'Modo sin conexión: historias, fotos y grabaciones descargadas de antemano',
              'Siete idiomas: checo, inglés, alemán, español, polaco, francés y ucraniano; se cambian con una bandera',
              'Las traducciones se hacen con inteligencia artificial (DeepL) y la aplicación lo indica junto a los textos; el nuevo contenido del pueblo se traduce automáticamente a todos los idiomas',
              'Los vecinos del pueblo amplían el contenido continuamente desde una administración web, sin nueva versión de la aplicación'],
    gallery_h='Así se ve',
    shots=['Pantalla de inicio', 'Mapa de lugares y rutas', 'Historias y leyendas', 'Audioguía', 'Juego para niños',
           'Excursión de medio día', 'Diploma por todos los sellos', 'Postal de la excursión'],
    shots_note='Las capturas muestran la versión checa de la aplicación.',
    privacy_h='Seguridad y privacidad',
    privacy='La aplicación no requiere registro, no contiene anuncios y no te rastrea: solo recoge totales diarios anónimos (cuántas veces se abrió y qué se consultó). Tu ubicación se procesa solo en el móvil; para calcular una ruta a pie se envían el origen y el destino al servicio de mapas. El contenido de la guía se descarga de nuestro servidor en la UE. Si envías una foto, se guarda allí y un administrador la aprueba antes de publicarla. Las valoraciones y denuncias de fotos son anónimas: la aplicación solo envía un número de instalación aleatorio para que cada persona vote una sola vez. El diploma y la postal se crean en el móvil y no se envían a ningún sitio salvo que los compartas.',
    policy='Política de privacidad (checo / inglés)',
    req='iOS y Android · las historias y fotos se pueden descargar para usarlas sin cobertura',
    ai_note='Esta página se ha traducido con ayuda de IA.',
    lang_label='Idioma de la página',
)

T['pl'] = dict(
    title='TETÍNEM — Przewodnik i opowieści z Tetína',
    desc='Przewodnik turystyczny po wsi Tetín z mapą, trasami, opowieściami i legendami. Audioprzewodnik, który sam zaczyna opowiadać, gdy dojdziesz do ciekawego miejsca. Po czesku, angielsku, niemiecku, hiszpańsku, polsku, francusku i ukraińsku.',
    nav_apps='Aplikacje', nav_support='Pomoc', nav_privacy='Prywatność', country='Republika Czeska',
    sub='Przewodnik i opowieści wsi Tetín',
    lead='Przewodnik turystyczny po jednym z najstarszych miejsc czeskiej historii. Mapa z miejscami i trasami, opowieści i legendy do czytania i słuchania oraz audioprzewodnik, który sam zaczyna opowiadać, gdy dojdziesz na miejsce. Po czesku, angielsku, niemiecku, hiszpańsku, polsku, francusku i ukraińsku.',
    status_b='W testach',
    status=f'Na iPhonie trwają publiczne testy przez TestFlight, wersja na Androida czeka na zatwierdzenie w Google Play. Napisz na {MAIL}, jeśli chcesz wypróbować aplikację lub dowiedzieć się, kiedy będzie dostępna.',
    pros=[('Przewodnik, który sam opowiada', 'Schowaj telefon do kieszeni i ruszaj. Gdy dojdziesz do ciekawego miejsca, przewodnik zacznie opowiadać jego historię — nawet przy zablokowanym telefonie.'),
          ('Opowieści na starym papierze', 'Opowieści, legendy i ciekawostki o księżnej Tecie, świętej Ludmile i zamku Tetín. Do czytania i słuchania, w siedmiu językach.'),
          ('Działa bez zasięgu', 'W dolinie i pod skałami zasięg bywa słaby. Pobierz przewodnik wcześniej, a opowieści, zdjęcia i trasy będziesz mieć w telefonie.'),
          ('Gra i dyplom dla dzieci', 'W dziewięciu miejscach czeka pytanie. Za dobrą odpowiedź rozlega się melodyjka, a do kolekcji trafia pieczątka. Kto zbierze wszystkie, dostanie dyplom ze swoim imieniem.')],
    features_h='Co potrafi aplikacja',
    features=['Interaktywna mapa z miejscami, filtrami i warstwami, które można włączać i wyłączać',
              'Podkłady Mapy.com — turystyczny, podstawowy i lotniczy',
              'Ścieżki edukacyjne z GPX z twoją pozycją i informacją, ile już przeszedłeś',
              'Piktogramy i filtr tras: wózek dziecięcy, wózek inwalidzki, psy, schody, trudność terenu',
              'Nawigacja piesza do miejsca w aplikacji, z głosowymi wskazówkami skrętu — także przy zablokowanym telefonie',
              'Opowieści, legendy i ciekawostki — osobno i przy konkretnych miejscach',
              'Audioprzewodnik z nagraniami lub czytanie głosem telefonu',
              'Tryb spaceru: opowieść uruchamia się sama, gdy dojdziesz na miejsce',
              'Kody QR na tablicach przy miejscach — zeskanuj, a opowieść od razu gra',
              '„Otwarte do…” lub „Zamknięte” przy muzeum, kościołach i restauracjach według godzin otwarcia',
              'Porady dla turystów: gdzie zjeść, parking, WC, jak dojechać',
              'Usługi przewodnickie i kontakty z przyciskami Zadzwoń i E-mail',
              'Gra dla dzieci: przy każdym miejscu pytanie, za dobrą odpowiedź melodyjka i pieczątka',
              'Dyplom odkrywcy Tetína z imieniem dziecka za wszystkie pieczątki — zapisz lub wyślij',
              'Pocztówka „Pozdrowienia z Tetína”: własne zdjęcie w ramce ze świętą Ludmiłą, świętym Wacławem i księżną Tetą',
              '„Dawniej i dziś” — stara pocztówka i dzisiejszy widok pod jednym suwakiem',
              'Gotowy plan wycieczki na pół dnia z obiadem i punktami widokowymi, który można ocenić gwiazdkami',
              'Kalendarz wydarzeń — odpust, koncerty, wystawy',
              'Komunikaty gminy na ekranie głównym — np. o śliskich punktach widokowych lub zamkniętym kościele',
              'Wyślij własne zdjęcie z wycieczki; po zatwierdzeniu zobaczą je inni; nieodpowiednie zdjęcie można zgłosić',
              'Tryb offline — opowieści, zdjęcia i nagrania pobrane wcześniej',
              'Siedem języków — czeski, angielski, niemiecki, hiszpański, polski, francuski i ukraiński — przełączane flagą',
              'Tłumaczenia powstają przy pomocy sztucznej inteligencji (DeepL), a aplikacja informuje o tym przy tekstach; nowe treści od gminy tłumaczą się na wszystkie języki automatycznie',
              'Treści na bieżąco uzupełniają mieszkańcy przez administrację internetową, bez nowej wersji aplikacji'],
    gallery_h='Jak to wygląda',
    shots=['Ekran główny', 'Mapa miejsc i tras', 'Opowieści i legendy', 'Audioprzewodnik', 'Gra dla dzieci',
           'Wycieczka na pół dnia', 'Dyplom za wszystkie pieczątki', 'Pocztówka z wycieczki'],
    shots_note='Zrzuty ekranu pokazują czeską wersję aplikacji.',
    privacy_h='Bezpieczeństwo i prywatność',
    privacy='Aplikacja nie wymaga rejestracji, nie zawiera reklam i cię nie śledzi – zbiera tylko anonimowe dzienne sumy (ile razy została uruchomiona i co w niej otwierano). Lokalizacja jest przetwarzana tylko w telefonie; do wyznaczenia trasy pieszej punkt początkowy i cel wysyłane są do usługi map. Treść przewodnika jest pobierana z naszego serwera w UE. Jeśli sam wyślesz zdjęcie, zostanie tam zapisane, a przed publikacją zatwierdzi je administrator. Oceny wycieczki i zgłoszenia zdjęć są anonimowe — aplikacja wysyła tylko losowy numer instalacji, aby każdy mógł zagłosować raz. Dyplom i pocztówka powstają w telefonie i nigdzie nie są wysyłane, dopóki sam ich nie udostępnisz.',
    policy='Polityka prywatności (po czesku / angielsku)',
    req='iOS i Android · opowieści i zdjęcia można pobrać do użytku bez zasięgu',
    ai_note='Ta strona została przetłumaczona przy pomocy AI.',
    lang_label='Język strony',
)

T['fr'] = dict(
    title='TETÍNEM — Guide et histoires de Tetín',
    desc='Un guide touristique du village de Tetín avec carte, itinéraires, histoires et légendes. Un audioguide qui commence à raconter tout seul dès que vous arrivez à un lieu intéressant. En tchèque, anglais, allemand, espagnol, polonais, français et ukrainien.',
    nav_apps='Applications', nav_support='Assistance', nav_privacy='Confidentialité', country='République tchèque',
    sub='Guide et histoires du village de Tetín',
    lead='Un guide touristique de l’un des plus anciens lieux de l’histoire tchèque. Une carte avec des lieux et des itinéraires, des histoires et légendes à lire ou à écouter et un audioguide qui commence à raconter tout seul dès que vous arrivez sur place. En tchèque, anglais, allemand, espagnol, polonais, français et ukrainien.',
    status_b='En test',
    status=f'Un test public est en cours sur iPhone via TestFlight ; la version Android attend la validation sur Google Play. Écrivez à {MAIL} si vous souhaitez essayer l’application ou être prévenu de sa sortie.',
    pros=[('Un guide qui raconte tout seul', 'Mettez votre téléphone dans la poche et partez. Dès que vous arrivez à un lieu intéressant, le guide raconte son histoire — même téléphone verrouillé.'),
          ('Des histoires sur du vieux papier', 'Histoires, légendes et curiosités sur la princesse Teta, sainte Ludmila et le château de Tetín. À lire ou à écouter, en sept langues.'),
          ('Fonctionne sans réseau', 'Dans la vallée et sous les rochers, le réseau est souvent faible. Téléchargez le guide à l’avance : histoires, photos et itinéraires restent dans votre téléphone.'),
          ('Un jeu et un diplôme pour les enfants', 'Une question attend à neuf endroits. Chaque bonne réponse déclenche une petite mélodie et ajoute un tampon à la collection. Qui les réunit tous reçoit un diplôme à son nom.')],
    features_h='Ce que fait l’application',
    features=['Carte interactive avec lieux, filtres et calques activables',
              'Fonds de carte Mapy.com — randonnée, standard et aérien',
              'Sentiers découverte au format GPX avec votre position et la distance parcourue',
              'Pictogrammes et filtres des itinéraires : poussette, fauteuil roulant, chiens, marches, difficulté',
              'Navigation piétonne vers le lieu dans l’application, avec instructions vocales à chaque virage — même téléphone verrouillé',
              'Histoires, légendes et curiosités — seules ou rattachées à chaque lieu',
              'Audioguide avec enregistrements ou lecture par la voix du téléphone',
              'Mode promenade : l’histoire démarre toute seule quand vous arrivez sur place',
              'Codes QR sur les panneaux des lieux — scannez et l’histoire démarre aussitôt',
              '« Ouvert jusqu’à… » ou « Fermé » pour le musée, les églises et les restaurants selon les horaires',
              'Conseils aux visiteurs : où manger, parking, toilettes, comment venir',
              'Visites guidées et contacts avec boutons Appeler et E-mail',
              'Jeu pour enfants : une question à chaque lieu, une mélodie et un tampon pour chaque bonne réponse',
              'Diplôme d’explorateur de Tetín au nom de l’enfant pour tous les tampons — à enregistrer ou partager',
              'Carte postale « Bons baisers de Tetín » : votre photo dans un cadre avec sainte Ludmila, saint Venceslas et la princesse Teta',
              '« Autrefois et aujourd’hui » — une ancienne carte postale et la vue actuelle sous un même curseur',
              'Une excursion d’une demi-journée toute prête, avec déjeuner et points de vue, à noter avec des étoiles',
              'Agenda des événements — pèlerinage, concerts, expositions',
              'Avis de la commune directement sur l’écran d’accueil — par exemple points de vue glissants ou église fermée',
              'Envoyez votre propre photo d’excursion ; une fois validée, les autres la verront ; une photo inappropriée peut être signalée',
              'Mode hors ligne — histoires, photos et enregistrements téléchargés à l’avance',
              'Sept langues — tchèque, anglais, allemand, espagnol, polonais, français et ukrainien — changement par drapeau',
              'Les traductions sont réalisées avec l’intelligence artificielle (DeepL) et l’application le signale près des textes ; les nouveaux contenus de la commune sont traduits automatiquement dans toutes les langues',
              'Les habitants enrichissent le contenu en continu via une administration web, sans nouvelle version de l’application'],
    gallery_h='À quoi ça ressemble',
    shots=['Écran d’accueil', 'Carte des lieux et itinéraires', 'Histoires et légendes', 'Audioguide', 'Jeu pour enfants',
           'Excursion d’une demi-journée', 'Diplôme pour tous les tampons', 'Carte postale de l’excursion'],
    shots_note='Les captures d’écran montrent la version tchèque de l’application.',
    privacy_h='Sécurité et confidentialité',
    privacy='L’application ne demande aucune inscription, ne contient pas de publicité et ne vous suit pas – elle ne collecte que des totaux quotidiens anonymes (nombre d’ouvertures et contenus consultés). Votre position est traitée uniquement sur le téléphone ; pour calculer un itinéraire à pied, le départ et l’arrivée sont envoyés au service de cartographie. Le contenu du guide est téléchargé depuis notre serveur situé dans l’UE. Si vous envoyez vous-même une photo, elle y est stockée et validée par un administrateur avant publication. Les notes et signalements de photos sont anonymes — l’application n’envoie qu’un numéro d’installation aléatoire pour que chacun ne vote qu’une fois. Le diplôme et la carte postale sont créés sur le téléphone et ne sont envoyés nulle part tant que vous ne les partagez pas.',
    policy='Politique de confidentialité (tchèque / anglais)',
    req='iOS et Android · histoires et photos téléchargeables pour une utilisation sans réseau',
    ai_note='Cette page a été traduite avec l’aide de l’IA.',
    lang_label='Langue de la page',
)

T['uk'] = dict(
    title='TETÍNEM — Путівник та історії Тетіна',
    desc='Туристичний путівник селом Тетін із мапою, маршрутами, історіями та легендами. Аудіогід, який сам починає розповідати, щойно ви дійдете до цікавого місця. Чеською, англійською, німецькою, іспанською, польською, французькою та українською.',
    nav_apps='Застосунки', nav_support='Підтримка', nav_privacy='Конфіденційність', country='Чеська Республіка',
    sub='Путівник та історії села Тетін',
    lead='Туристичний путівник одним із найдавніших місць чеської історії. Мапа з місцями та маршрутами, історії й легенди для читання та прослуховування і аудіогід, який сам починає розповідати, щойно ви дійдете до місця. Чеською, англійською, німецькою, іспанською, польською, французькою та українською.',
    status_b='Тестування',
    status=f'На iPhone триває публічне тестування через TestFlight, версія для Android чекає на схвалення в Google Play. Напишіть на {MAIL}, якщо хочете випробувати застосунок або дізнатися, коли він буде доступний.',
    pros=[('Гід, який розповідає сам', 'Покладіть телефон у кишеню й вирушайте. Щойно ви дійдете до цікавого місця, гід почне розповідати його історію — навіть із заблокованим телефоном.'),
          ('Історії на старому папері', 'Історії, легенди й цікавинки про княгиню Тету, святу Людмилу та Тетінський замок. Для читання й прослуховування, сімома мовами.'),
          ('Працює без зв’язку', 'У долині й під скелями зв’язок буває слабким. Завантажте путівник заздалегідь — історії, фото й маршрути будуть у телефоні.'),
          ('Гра й диплом для дітей', 'У дев’яти місцях чекає запитання. За правильну відповідь лунає мелодія, а до колекції додається печатка. Хто збере всі, отримає диплом зі своїм ім’ям.')],
    features_h='Що вміє застосунок',
    features=['Інтерактивна мапа з місцями, фільтрами та шарами, які можна вмикати й вимикати',
              'Підкладки Mapy.com — туристична, звичайна й супутникова',
              'Навчальні стежки з GPX із вашим місцезнаходженням і пройденою відстанню',
              'Піктограми й фільтр маршрутів: дитячий візок, інвалідний візок, собаки, сходи, складність',
              'Піша навігація до місця просто в застосунку, з голосовими підказками на поворотах — навіть із заблокованим телефоном',
              'Історії, легенди й цікавинки — окремо та біля конкретних місць',
              'Аудіогід із записами або читанням голосом телефона',
              'Режим прогулянки: історія вмикається сама, коли ви доходите до місця',
              'QR-коди на табличках біля місць — скануєте, і історія одразу звучить',
              '«Відчинено до…» або «Зачинено» біля музею, костелів і ресторанів за годинами роботи',
              'Поради для туристів: де поїсти, паркування, туалети, як дістатися',
              'Екскурсійні послуги й контакти з кнопками «Подзвонити» та «Ел. пошта»',
              'Гра для дітей: біля кожного місця запитання, за правильну відповідь мелодія й печатка',
              'Диплом дослідника Тетіна з ім’ям дитини за всі печатки — зберегти або надіслати',
              'Листівка «Вітання з Тетіна»: власне фото в рамці зі святою Людмилою, святим Вацлавом і княгинею Тетою',
              '«Тоді й тепер» — стара листівка й сучасний вигляд під одним повзунком',
              'Готовий план прогулянки на пів дня з обідом і оглядовими майданчиками, який можна оцінити зірками',
              'Календар подій — проща, концерти, виставки',
              'Повідомлення від громади просто на головному екрані — наприклад, про слизькі оглядові майданчики чи зачинений костел',
              'Надішліть власне фото з прогулянки; після схвалення його побачать інші; неприйнятне фото можна поскаржити',
              'Офлайн-режим — історії, фото й записи, завантажені заздалегідь',
              'Сім мов — чеська, англійська, німецька, іспанська, польська, французька та українська — перемикаються прапорцем',
              'Переклади створюються за допомогою штучного інтелекту (DeepL), і застосунок повідомляє про це біля текстів; новий вміст від громади перекладається на всі мови автоматично',
              'Вміст постійно доповнюють мешканці села через вебадміністрування, без нової версії застосунку'],
    gallery_h='Як це виглядає',
    shots=['Головний екран', 'Мапа місць і маршрутів', 'Історії та легенди', 'Аудіогід', 'Гра для дітей',
           'Прогулянка на пів дня', 'Диплом за всі печатки', 'Листівка з прогулянки'],
    shots_note='На знімках екрана — чеська версія застосунку.',
    privacy_h='Безпека й конфіденційність',
    privacy='Застосунок не вимагає реєстрації, не містить реклами й не стежить за вами — він збирає лише анонімні щоденні підсумки (скільки разів його запускали й що в ньому відкривали). Місцезнаходження обробляється лише в телефоні; для розрахунку пішого маршруту початкова точка й ціль надсилаються картографічному сервісу. Вміст путівника завантажується з нашого сервера в ЄС. Якщо ви самі надішлете фото, воно зберігається там, а перед публікацією його схвалює адміністратор. Оцінки прогулянки й скарги на фото анонімні — застосунок надсилає лише випадковий номер встановлення, щоб кожен міг проголосувати один раз. Диплом і листівка створюються просто в телефоні й нікуди не надсилаються, доки ви самі ними не поділитеся.',
    policy='Політика конфіденційності (чеською / англійською)',
    req='iOS і Android · історії та фото можна завантажити для використання без зв’язку',
    ai_note='Цю сторінку перекладено за допомогою ШІ.',
    lang_label='Мова сторінки',
)


def e(s):
    return html.escape(s, quote=False)


def page(code):
    t = T[code]
    file = next(l[3] for l in LANGS if l[0] == code)
    alts = ''.join(f'<link rel="alternate" hreflang="{l[0]}" href="https://wenoush.github.io/red-apps/tetinem/{"" if l[3] == "index.html" else l[3]}">\n' for l in LANGS)
    switch = ''.join(
        f'<a href="{l[3]}" hreflang="{l[0]}" lang="{l[0]}" title="{l[2]}"{" aria-current=\"page\"" if l[0] == code else ""}>{l[1]} {l[2]}</a>'
        for l in LANGS)
    pros = ''.join(f"<div class='prednost'><b>{e(a)}</b><p>{e(b)}</p></div>" for a, b in t['pros'])
    feats = ''.join(f'<li>{e(f)}</li>' for f in t['features'])
    shots = ''.join(f'''<figure class="snimek">
      <img src="../obrazky/screenshoty/{f}" alt="TETÍNEM — {e(c)}" loading="lazy">
      <figcaption>{e(c)}</figcaption>
    </figure>''' for f, c in zip(SHOTS, t['shots']))
    note = f'\n      <p class="pozn-snimky">{e(t["shots_note"])}</p>' if t['shots_note'] else ''
    ai = f' · {e(t["ai_note"])}' if t['ai_note'] else ''
    return f'''<!DOCTYPE html><html lang="{code}"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{html.escape(t['desc'])}">
<meta property="og:title" content="{html.escape(t['title'])}">
<meta property="og:description" content="{html.escape(t['desc'])}">
<meta property="og:type" content="website">
{alts}<link rel="icon" href="../obrazky/favicon.png">
<link rel="stylesheet" href="../styl.css">
<style>:root{{--h:#3C6E9A;--h2:#34261A;--akcent:#E2B23A}}
.jazyky{{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:18px;font-size:14px}}
.jazyky a{{color:inherit;opacity:.8;text-decoration:none;white-space:nowrap}}
.jazyky a[aria-current]{{opacity:1;font-weight:700;text-decoration:underline}}
.pozn-snimky{{font-size:13.5px;color:var(--mut);margin-top:6px}}</style>
</head><body class="je-produkt">

<header class="hlava">
  <div class="w">
    <a class="znacka" href="../index.html">
      <span class="znak">w</span>
      <span>RED</span>
    </a>
    <nav>
      <a href="../index.html">{e(t['nav_apps'])}</a>
      <a href="../podpora.html">{e(t['nav_support'])}</a>
    </nav>
  </div>
</header>


<section class="hero produkt">
  <div class="w">
    <img class="ikona" src="../obrazky/tetinem.png" alt="" width="120" height="120">
    <h1>TETÍNEM</h1>
    <p class="podtitul">{e(t['sub'])}</p>
    <p class="lead">{e(t['lead'])}</p>
    <p class="meta">iPhone · Android</p>
    <nav class="jazyky" aria-label="{html.escape(t['lang_label'])}">{switch}</nav>
  </div>
</section>

<main>
  <div class="w">
    <div class="chysta"><b>{e(t['status_b'])}</b> — {t['status']}</div>

    <div class="prednosti">{pros}</div>

    <section class="pas">
      <h2>{e(t['features_h'])}</h2>
      <ul class="funkce">{feats}</ul>
    </section>

    <section class="pas">
      <h2>{e(t['gallery_h'])}</h2>
      <div class="galerie">{shots}</div>{note}
    </section>

    <section class="pas">
      <h2>{e(t['privacy_h'])}</h2>
      <p>{e(t['privacy'])}</p>
      <p class="odkazy"><a href="../soukromi/tetinem-zasady-ochrany-udaju.html">{e(t['policy'])}</a>
        <a href="../podpora.html">{e(t['nav_support'])}</a></p>
    </section>

    <p class="pozadavky">{e(t['req'])}{ai}</p>
  </div>
</main>


<footer class="pata">
  <div class="w">
    <div>
      <strong>RED</strong> — Václav Červený, {e(t['country'])}<br>
      <a href="mailto:redapps.support@gmail.com">redapps.support@gmail.com</a>
    </div>
    <nav>
      <a href="../index.html">{e(t['nav_apps'])}</a>
      <a href="../podpora.html">{e(t['nav_support'])}</a>
      <a href="../soukromi/index.html">{e(t['nav_privacy'])}</a>
    </nav>
  </div>
</footer>
</body></html>
'''


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for code, _, _, file in LANGS:
        t = T[code]
        assert len(t['features']) == len(T['cs']['features']), code
        assert len(t['shots']) == len(SHOTS) and len(t['pros']) == 4, code
        with open(os.path.join(here, file), 'w', encoding='utf-8') as f:
            f.write(page(code))
        print('OK', file)
