#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#? unicode tables - https://www.rapidtables.com/code/text/unicode-characters.html

import os
import sys
import random
import time

from tabulate import tabulate

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
clear = lambda: os.system('clear')
fname = os.path.join(SCRIPT_DIR, 'game-logo.txt')
def show_game_logo_alt():
  with open(fname, 'r') as fin:
      print(fin.read())

##! COLOR CONSTS !##
BRED = "\033[1;31m"
RED = "\033[0;31m"
BGREEN = "\033[1;32m"
GREEN = "\033[0;32m"
BBLUE = "\033[1;34m"
BLUE = "\033[0;34m"
ORANGE = "\033[0;33m"
LGRAY = "\033[0;37m"
DGRAY = "\033[1;30m"
NC = "\033[0m"
BOLD = "\033[1m"
DIMM = "\033[2m"
ITALIC = "\033[3m"
UNDER = "\033[4m"

##! APP CONSTS !##
APP_VER_NO = "0.1 (pre-alpha)"
##! APP VARS !##
logoSleepTime = 0.5
sleepTime = 0.5
settings_print_messages = False
defaults_settings = (0.5, 2, True)

##! GAME FLAGS !##
#* CHAR STATS *#
charName = "Brida Fox"
charAge = 30
charSex = "K"
charProf = "Komendant"
charStrength = 0
charDexterity = 0
charPower = 0
charCondition = 0
charApperance = 0
charEducation = 0
charSize = 0
charInteligence = 0
charHP = 0
charSanity = 0
charLuck = 0
charMP = 0
charDamageBonus = 'Brak'
charBuild = 0
#* SKILLS *#
charAccounting = 5
charAnthropology = 1
charAppraise = 5
charArcheology = 1
charArtCraft = 5
charCharm = 15
charClimb = 20
charCreditRating = 0
charCthulhuMythos = 0
charDisguise = 5
charDodge = int(charDexterity / 2)
charDriveAuto = 20
charElecRepair = 10
charFastTalk = 5
charFightingBrawl = 25
charFirearmsHandgun = 20
charFirearmsRifle = 25
charFirstAid = 30
charHistory = 5
charIntimidate = 15
charJump = 20
charLanguageOwn = charEducation
charLanguageOther = 1
charLaw = 5
charLibraryUse = 20
charListen = 20
charLocksmith = 1
charMechRepair = 10
charMedicine = 1
charNaturalWorld = 10
charNavigate = 10
charOccult = 5
charOpHvMachine = 1
charPersuade = 10
charPilot = 1
charPsychology = 10
charPsychoanalysis = 1
charRide = 5
charScience = 1
charSleightOfHand = 10
charSpotHidden = 25
charStealh = 20
charSurvival = 10
charSwim = 20
charThrow = 20
charTrack = 10

#* HELPER VARS *#
choice = '0'
roll = 0
test_result = 0

#* GAME VARS *#
selectedProblems = []
handgunRounds = 0
rifleRounds = 0
ownedNotes = [] #? Add ID's of notes to set them available to player

#* ARRAYS *#
problems = ["Uzależniona od papierosów", "Uzależniona od alkoholu", "Uzależniona od hazardu", "Ma problemy finansowe",
"Współmałżonek odszedł lub zmarł kilka lat temu", "Samotnie wychowuje krnąbrne dziecko", "Ma problem ze zdrowiem",
"Opiekuje się niesamodzielnym rodzicem", "Skrywa przeszłość kryminalną i jest szantażowana",
"Nękana przez kolegów przestępcy, którego wsadziła do więzienia"]
equipment = ["Kajdanki", "Zapalniczka"]
notes = [
  {'id':1, 'name':"Odciski palców",
  'text':f'''\n  Data: {DIMM}12 lutego 2005r.{NC}                                                Numer: {DIMM}1233{NC}\n
                         FORMULARZ POBIERANIA ODCISKÓW PALCÓW\n
  IMIĘ I NAZWISKO: {DIMM}Branja Madsen{NC}
  DATA URODZENIA:  {DIMM}14 LUTEGO 2003 r.{NC}   MIEJSCE URODZENIA: {DIMM}Stoksjö{NC}
  PŁEĆ: {DIMM}K{NC}   RASA: {DIMM}B{NC}   WZROST: {DIMM}82{NC}   WAGA: {DIMM}13{NC}   OCZY: {DIMM}piwne{NC}   WŁOSY: {DIMM}brązowe{NC}
  ═════════════════════════════════════════════════════════════════════════════════
  DATA POBRANIA: {DIMM}12 LUTEGO 2005 r.{NC}   MIEJSCE POBRANIA: {DIMM}komisariat policji w Stoksjö{NC}
  POBRAŁ: {DIMM}Hjortur Stenberg{NC}   -   {DIMM}komendant{NC}
  POWÓD POBRANIA ODCISKÓW PALCÓW: {DIMM}ofiara przestępstwa{NC}
  UWAGI POBIERAJĄCEGO: {DIMM}odciski linii papilarnych zostały przeniesione z kubka i
              talerzyka, których używała zaginiona w sprawie o sygn. BM/12/2005{NC}\n
                                                                {ITALIC}12.02.2005 Stenberg{NC}\n'''},
  {'id':2, 'name':"Protokół lekarski",
  'text':f'''\n                                                             Sygn: {ITALIC}{DIMM}3/2020{NC}\n
                BIURO REJONOWEGO LEKARZA SĄDOWEGO W {ITALIC}{DIMM}Stoksjö{NC}\n
  PERSONALIA: {ITALIC}{DIMM}brak danych{NC}               RASA: {ITALIC}{DIMM}B{NC}   PŁEĆ: {ITALIC}{DIMM}K{NC}   WIEK: {ITALIC}{DIMM}—{NC}
  ADRES: {ITALIC}{DIMM}brak danych{NC}                    ZAWÓD: {ITALIC}{DIMM}b.d.{NC}
  ════════════════════════════════════════════════════════════════════════
  OPIS OSOBY:     {ITALIC}{DIMM}częściowo ubrana{NC}
                Oczy: {ITALIC}{DIMM}piwne{NC}    Włosy: {ITALIC}{DIMM}brązowe{NC}    Wąsy: {ITALIC}{DIMM}—{NC}    Broda: {ITALIC}{DIMM}—{NC}
                Waga: {ITALIC}{DIMM}46{NC}  Wysokość: {ITALIC}{DIMM}172{NC}  Temp. ciała: {ITALIC}{DIMM}32°C{NC}  Data: {ITALIC}{DIMM}—{NC}\n
  OMÓWIENIE:
    {ITALIC}{DIMM}Pacjentka nie reaguje na kontakt, ale poddaje się badaniu.
    Wiek pomiędzy 15-20 lat, lekka niedowaga. Liczne drobne skaleczenia na
    całym ciele. Lekkie odwracalne odmrożenia stóp.
    {UNDER}Rentgen:{NC}{ITALIC}{DIMM}
    - ślad po złamaniu kości szczęki (5-10 lat temu)
    - ślad po złamaniu nosa (5-10 lat temu)
    - prawdopodobne zwyrodnienie lędźwiowych kręgów kręgosłupa
      (dzwiganie ciężkich przedmiotów?)
    {UNDER}Badanie krwi:{NC}{ITALIC}{DIMM}
    - nadmiernie wysoki poziom limfocytów - możliwa choroba
      układu odpornościowego
    {UNDER}Inne badania:{NC}{ITALIC}{DIMM}
    - pacjentka leworęczna
    - wychłodzenie organizmu
    - wycieńczenie i odwodnienie
    {UNDER}Wywiad psychologiczny:{NC}{ITALIC}{DIMM}
    - pacjentka nie reaguje na kontakt
    - b.wysoki poziom lęku
    - pacjentka wpada w stan odrętwienia
    - incydentalnie reaguje bierną agresją
    - światłowstręt
    - incydentalnie krzyczy (mowa nie zrozumiała) i płacze
    - możliwe zaburzenia psychiczne{NC}
  ════════════════════════════════════════════════════════════════════════
  ZDOLNA DO PRZEPROWADZENIA DALSZYCH CZYNNOŚCI ŚLEDCZYCH:
    {ITALIC}{DIMM}niezdolna - utrudniony lub niemożliwy kontakt,
    wymaga leczenia psychiatrycznego bądź terapii{NC}\n
                                                          {ITALIC}{DIMM}Nielsen Andre{NC}\n'''},
  {'id':3, 'name':"Pamiętnik Branji",
  'text':f'''\n    {ITALIC}Dobra robota Branjo!
  Doskonała robota! Matka doprowadzona do białej gorączki po tym
  jak wyciągnęłam jej kasę z torebki. Jakub rozkochany po uszy,
  wkrótce będzie {UNDER}jadł mi z ręki.{NC}{ITALIC} Stary będzie zadowolony, bo lubi
  tłamsić tych silnych bardziej, niż kogokolwiek innego. Ale to ja
  go do tego doprowadzę. Złamię jego wolę, zniszczę jego bunt, a
  potem zabiorę go w podróż, po której będzie żałował, że się urodził!
  Taki z niego buntownik, haha! Wkrótce światło jego oczu {UNDER}zgaśnie{NC}{ITALIC}
  i wypełni je pustka.
    Przede/mną ostatnie dni szampańskiej zabawy. Chyba nigdy nie
  nalatałam się tyle po klubach, nie wytańczyłam tak za wszystkie czasy
  i nie zdarłam gardła na koncertach. Odliczam do 14 lutego.
  Jakie to romantyczne, nie Jakub?
  Czy to nie piękne, że {UNDER}w Walentynki{NC}{ITALIC} wyruszymy w podróż naszego życia?
  A właściwie mojego, bo twoje będzie udręką. Ja zato otrzymam skrzydła
  i poszybuję wysoko. Nikt już nigdy nie uzna mnie za słabą. Zasiądę
  po prawicy Starego i będę {BOLD}rządzić{NC}{ITALIC} u jego boku potężna, niebezpieczna
  i piękna niczym KRÓLOWA, a wszyscy ci żałośni niewolni (tak, ty też Jakub)
  będą mi usługiwać. Nam usługiwać. Ojciec będzie ze mnie {UNDER}dumny.{NC}
    {ITALIC}Wczorajszej nocy odwiedził mnie we śnie, aby przypomnieć o
  obietnicy. No jasne, że pamiętam, a co ja niby robię ?! Tylko dlaczego
  był taki wściekły? :(
    Coś się stało. Coś się na pewno stało. Ale to już nie ma znaczenia,
  bo wkrótce znowu będziemy {BOLD}razem{NC}{ITALIC}. Stary i ja. Już na zawsze razem ...{NC}\n'''},
  {'id':4, 'name':"Notatka służbowa",
  'text':'''\n  Kom. Hjortur Stenberg                       Stoksjö, 17 lutego 2005 r.
  Komenda Policji w Stoksjö
  prow. Helbjerg\n
                            NOTATKA SŁUŻBOWA\n
    W związku z podjętą przez prokuraturę okręgową decyzją o umorzeniu
  śledztwa o sygn. BM/12/2005, oraz koniecznością przekazania akt sprawy do
  archiwum, ninejszym przedkładam podsumowanie śledztwa, które powierzono
  mi do prowadzenia.
    W dniu 12 lutego br. o godzinie 06:12 Komenda Policji w Stoksjö
  otrzymała telefoniczne zgłoszenie zaginięcia 2-letniego dziecka Branji
  Madsen. Zawiadamiającym był 35-letni ojciec Yngvar Madsen. Ze względu na
  panującą w miasteczku epidemię grypy, która dotknęła także moich
  podwładnych, osobiście udałem się do domu państwa Madsenów, przy ul.
  Bekkefaret 3, gdzie zastałem zawiadamiającego oraz jego 33-letnią małżonkę,
  Ingrid Madsen, matkę dziewczynki. Rodzice poinformowali mnie, że 2-letnia
  Branja zniknęła ze swojego pokoju w nocy o nieokreślonej godzinie.
  W ziązku z powyższym wraz z podwładnymi dokonałem przeszukania domu
  i okolicy, w wyniku czego odkryłem ślady mogące wskazywać na uprowadzenie.
    Z uwagi na uzasadnione podejrzenie uprowadzenia dziecka,
  zawiadomiłem o tym fakcie przełożonych z Helbjerg, podjąłem działania
  wynikające z procedur na wypadek porwania oraz poleciłem podwładnym
  koordynację mobilizacji miejscowej ludności, celem przeczesywania
  okolicznych lasów.
    W dniu 14 lutego br. około godziny 13:30 otrzymałem telefon od Ingrid
  Madsen, że dziecko się odnalazło. Zgodnie z uzyskaną informacją, jedna z osób
  zaangażowanych w poszukiwania, 64-letnia Hilda Krogg, znalazła wyziębioną
  dziewczynkę błąkającą się w okolicy starej cegielni na zachód od miasta.
  Dziecko zostało zbadane pod kątem medycznym, żadnych poważnych obrażeń
  ani śladów przemocy nie ujawniono, o czym również niezwłocznie
  zawiadomiłem przełożonych.
    W związku z poleceniem służbowym zmieniłem kwalifikację zdarzenia
  z uprowadzenia na zaginięcie, zamknąłem sprawę i niezwłocznie skieruję ją
  do archiwizacji.\n
                                                            Hjortur Stenberg'''},
  {'id':5, 'name':"Wycinek #1",
  'text':f'''\nHELBJERG | 13 LUTEGO 2005\n
  {BOLD}Stoksjö: ZAGINĘŁA DWULETNIA BRANJA MADSEN{NC}\n
  Policja poszukuje dziewczynki, która    Gwarantujemy dyskrecję oraz anonimowość!
  zaginęła ze swojego domu w Stoksjö.     Prosimy także o zgłoszenia wolontariuszy
  Podejrzewane uprowadzenie!              do grupy poszukiwawczej, która będzie
                                          przeszukiwać okoliczne lasy.
    Branja Madsen zniknęła wczorajszej    
  nocy z pokoju dziecinnego               Jak dowiedzieli się nasi dziennikarze,
  powiedział naszym dziennikarzom         zaginiona jest córką Ingrid Madsen,
  prowadzący śledztwo komendant           lokalnej aktywistki społecznej. Czy
  Hjortut Stenberg. - Prowadzimy sprawę   uprowadzenie może mieć jakikolwiek
  w kierunku uprowadzenia. Jeżeli         związek z organizowanymi przez nią
  ktokolwiek posiada informacje, które    akcjami informacyjnymi, dotyczącymi
  mogą rzucić światło na to zaginięcie,   lokalnych polityków? Tego jeszcze nie
  prosimy o pilny kontakt z naszą         wiemy, ale będziemy informawać, jeśli
  komendą policji.                        grypa nie położy nas wszystkich. (Z)\n'''},
  {'id':6, 'name':"Wycinek #2",
  'text':f'''\nWtorek, 11 maja 1999 r., No 455\n
  FELIETON INGEGARD
  {BOLD}STOKSJO PEŁNE TAJEMNIC{NC}\n
  Niewiele jest w kraju miejsc o równie tajemniczej historii jak
  prowincja Helbjerg, a jednak w tym regionie kraju, pod
  względem wydarzeń tyleż dziwnych co niejasnych, królują
  okolice Stoksjö. Choć mieścina ta liczy zaledwie 2 tysiące dusz,
  zdaje się prosperować lepiej niż niejedna porównywalnej
  wielkości osada z bogatszych i bardziej dochodowych
  regionów. Choć prócz nieprzebytych lasów, zasobów,
  złóż czy innych dóbr tu niewiele lud żyje harmonijnie
  i dostatnio, a pech dotykający okolicy zdaje się w ogóle nie
  dotykać miasteczka, jakby los celowo mu sprzyjał.\n
  Nie można tego jednak powiedzieć o obserwowanej na
  przestrzeni ostatnich 40 lat, pladze zaginięć i ucieczek
  z domu. Pierwsze zdarzyło się wczesną wiosną w 1960 r., kiedy
  to cała prowincja Halbjerg cierpiała klęskę nieurodzaju,
  związaną ze zbyt długo utrzymującą się zimą. Artykuły
  z tamtego czasu wnoszą, że w Stoksjö zaginęło wtedy dwóch
  nastolatków, którzy wybrali się na połów ryb. Na szczęście
  w tym przypadku historia kończy się szczęśliwie;
  poszukiwania trwały niemal tydzień, gdy obaj chłopcy zdrowi
  i cali odnaleźli się w lesie.\n
  Kolejne zaginięcie odnotowano w połowie lat 70-tych. Tym
  razem zniknęła 22-letnia nauczycielka, Annika Ollson.
  Akta sprawy głoszą, że kobieta była przyjezdna i że najpewniej
  potajemnie uciekła z miasteczka, obawiając się reakcji miesz-
  kańców na nieplanowaną ciążę. Zaiste, z notatek policyjnych
  wyczytać można, że ponoć świadkowie widzieli ją potem w
  stolicy prowincji, jednak nie ma co do tego bezwzględnej
  pewności.\n
  Najbardziej tajemnicze zaginięcie miało miejsce w 1973 r.,
  w czasie w którym region drżał przed historycznie
  ostatnim w dziejach naszego kraju wybuchem ospy. Stoksjö,
  które choroba najwyraźniej ominęła, zmagało się w tym
  czasie z kryzysem spowodowanym zaginięciem 7-letniego
  Mikaela Bjorge. Archiwalia nie są jasne co do
  tego przypadku. W jednych źródłach wyczytać można, że
  chłopak się odnalazł. W drugich, że jego rzekome odnalezienie
  okazało się pomyłką - za chłopaka wzięto inną osobę,
  włóczęgę i złodzieja, który w tym czasie zawędrował w okolice.\n
  Jaka jest prawda o tych przypadkach? Tego się dziś już
  pewnie nie dowiemy. (ING)'''},
  {'id':7, 'name':"Książka z biblioteki",
  'text':'''\nHISTORIA, MITY I LEGENDY SKANDYNAWII                                    VOL.2\n
  STOKSJÖ, HELBJERG\n
    Położona w tej części prowincji Helbjerg osada o nazwie Stoksjö powstała
  pod koniec XIX wieku za sprawą odkrywkowej kopalni kredy, której złoża
  znaleziono tutaj w 1889 roku. Spodziewano się, że złoże jest bogate, lecz
  rzeczywistość szybko rozwiała oczekiwania, co zwykle doprowadziłoby do
  rychłego opuszczenia trudno dostępnych, gęsto zalesionych wzgórz. Tak się
  jednak nie stało, gdyż garstka rodzin górniczych, dla których szybko
  zabrakło pracy i pieniędzy, mimo niegościnnego otoczenia zdecydowała się
  osiąść w tej okolicy na stałe, a potomkowie tych rodzin żyją w Stoksjö do
  dzisiaj.\n
    Zważywszy na to, że ludności tutaj napływowa, kultywowane tu zwyczaje
  pochodzą z wielu regionów kraju, w zakresie świąt i baśni duplikując te
  opowiadane chićby na zachodzie czy północy. Rdzennie okoliczne wydają się
  tylko te opowieści, które dotyczą nigdzie inndziej niezanotowanych w kraju
  wierzeń o Sennym lub Piaskowym Dziadku, które bardziej zdają się mieć
  związek z folklorem niemieckim i literackimi bajkami Ernsta Theodora
  Amadeusa Hoffmana niż w którąkolwiek ze skandynawskich legend.\n
  Gwoli przypomnienia niemiecki "Der Sandmann" przewija się w kulturach
  wielu krajów (m.in. brytyjski Billy Winker czy szkocki Wee Willie Winky)
  i nawiązuje do niego choćby Duńczyk Hans Chrisitan Andersen. Jest to
  upiorna postać, która nocą nawiedza dzieci odmawiające pójścia spać i sypie
  im w oczy piasek. W najbardziej makabrycznych opowieściach Piaskowy
  Dziadek wyrywa niegrzecznym dzieciom oczy i karmi nimi swoje upiorne
  potomstwo.\n
  W okolicach Stoksjö legenda ta przybiera jednak zgoła inną postać,
  zachowując jednakowoż pewne podobieństwa do oryginału. Podług nich
  Piaskowy Dziadek zazwyczaj przynosi obfite plony i dostatek, a gdy w okolicy
  dzieje się krzywda, potrafi wyratować mieszkańców w potrzebie. Kierowane
  do niego prośby mają jednak swoją cenę, Dziadek bowiem zażądać może
  wymiany - coś za coś. Czasem to będzie uczynek, czasem trzoda, a czasem
  i coś gorszego, o czym lokalni nie chcą nawet wspominać.\n
  Najstarsze legendy okolic opisują Dziadka jako bardzo starego, ale nieustannie
  płodnego starca o nieludzkich rysach twarzy. Niegdyś przedstawiano go
  siedzącego na tronie splecionym z gałęzi i konarów drzew. W innym
  przypadku zachował się podanie, jokoby nosił on poroże jelenia. Jako istota
  ściśle związana tutaj z leśnymi ostępami, ponoć jedyne, czego znieść nie
  może, to otwarty ogień, który napawa go pewnym obrzydzeniem. Jak wskazuje
  jedna z przypisanych mu nazw, Senny Dziadek potrafi zsyłać na ludzi sny,
  zależne od tego, co kto sobie zasłużył: od snów lubieżnych jak on sam, po sny
  najbardziej koszmarne. Na jego dworze kłębi się od dziesiątek, czy nawet
  setek pomniejszych potomków, co kojarzy się z kultywowanymi w innych regionach
  świata wierzeniami o Leśnej Kozie i jej tysiącu młodych, a potomkowie
  ci są ponoć zdeprawowani i zepsuci do cna.\n'''}
]

#* WHAT CHARACTER KNOW *#
GirlHitByCar = 0
CarChecked = 0
CalledForMechanic = 0
GirlHisteria = 0


##! HELPER FUNCTIONS !##
def inputNumber(inputMessage):
  while True:
    try:
      userInput = int(input(inputMessage))
    except ValueError:
      print("Wprowadź liczbę.")
      continue
    else:
      return userInput

def inputFloat(inputMessage):
  while True:
    try:
      userInput = float(input(inputMessage))
    except ValueError:
      print("Wprowadź liczbę.")
      continue
    else:
      return userInput

def inputText(inputMessage):
  userInput = input(inputMessage).lower().strip()
  return userInput

def printText(message):
  if settings_print_messages:
    for character in message:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.04)
    print()
  else:
    print(message)

##! FUNCTIONS !##
def show_game_logo():
  os_cmd = f'lolcat {SCRIPT_DIR}/game-logo.txt'
  if os.system(os_cmd) != 0:
    show_game_logo_alt()
  time.sleep(logoSleepTime)
  print(f"\n  Wykonał - {ORANGE}Jakub Michniewicz{NC}                Wersja - {BRED}{APP_VER_NO}{NC}\n")
  time.sleep(logoSleepTime)

def reset_stats_to_default():
  pass

def create_caracter():
  global charName, charAge, charSex
  global selectedProblems

  selectedProblems = []
  randomNewCharacter = inputText("Czy chesz stworzyć losową postać? T/n ")
  if randomNewCharacter == 'n':
    print()
    print("╒═════════════════╕")
    print("│    TWORZENIE    │")
    print("│     POSTACI     │")
    print("╘═════════════════╛")
    charName = inputText("Jak się nazywasz (imię i nazwisko)? > ")
    charAge = 100
    while charAge >= 100 and charAge <= 18:
      charAge = inputNumber("Ile masz lat? > ")
      if charAge >= 100:
        print("Podaj prawidłowy wiek")
    charSex = ''
    while charSex != 'k' and charSex != 'm':
      charSex = inputText("Twoja płeć? (M/K) > ")
    charSex = charSex.upper()
    set_basic_stats()
    set_player_occupation_skills()
    set_random_investigator_problems()
  else:
    set_random_basic_stats()
    set_random_occupation_skills()
    set_random_investigator_problems()

def set_basic_stats():
  skills_list = [
    charStrength, charDexterity, charPower, charCondition, charApperance, charEducation, charSize, charInteligence,
    charHP, charSanity, charLuck, charMP, charDamageBonus, charBuild
  ]
  statsValues = [40, 50, 50, 50, 60, 60, 70, 80]

  for i in range(len(statsValues)):
    local_choice = 0
    while local_choice < 1 or local_choice > 8:
      clear()
      update_basic_stats(skills_list)
      print("")
      print(f"Dostępne wartości: {statsValues}")
      print(f"Wartość do wstawienia: {BOLD}{statsValues[-1]}{NC}")
      print("")
      print("╒═════════════════╕")
      print("│     WYBIERZ     │")
      print("│   UMIEJĘTNOŚĆ   │")
      print("╘═════════════════╛")
      print("")
      local_choice = inputNumber("Wybór > ")
    skills_list[local_choice-1] = statsValues.pop(-1)
  clear()

def update_basic_stats(skillsList):
  global charStrength, charDexterity, charPower, charCondition, charApperance, charEducation, charSize, charInteligence
  global charHP, charSanity, charLuck, charMP, charDamageBonus, charBuild
  global charDodge, charLanguageOwn

  charStrength = skillsList[0]
  charDexterity = skillsList[1]
  charPower = skillsList[2]
  charCondition = skillsList[3]
  charApperance = skillsList[4]
  charEducation = skillsList[5]
  charSize = skillsList[6]
  charInteligence = skillsList[7]

  charHP = int((charSize + charCondition) / 10)
  charSanity = charPower
  charLuck = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 5
  charMP = int(charPower / 5)
  if charPower + charSize > 124:
    charDamageBonus = '+1K4'
    charBuild = 1
  charDodge = int(charDexterity / 2)
  charLanguageOwn = charEducation

  skills_table = [
    ('1)',f'Siła [{BLUE}{charStrength}{NC}]'),
    ('2)',f'Zręczność [{BLUE}{charDexterity}{NC}]'),
    ('3)',f'Moc [{BLUE}{charPower}{NC}]'),
    ('4)',f'Kondycja [{BLUE}{charCondition}{NC}]'),
    ('5)',f'Wygląd [{BLUE}{charApperance}{NC}]'),
    ('6)',f'Wykształcenie [{BLUE}{charEducation}{NC}]'),
    ('7)',f'Budowa ciała [{BLUE}{charSize}{NC}]'),
    ('8)',f'Inteligencja [{BLUE}{charInteligence}{NC}]')
  ]
  print(tabulate(skills_table, tablefmt="pretty"))

def set_player_occupation_skills():
  skills_list = [
    charAnthropology, charArcheology, charFirearmsRifle, charFirearmsHandgun, charDisguise, charElecRepair, charFastTalk, charHistory, charRide, charLanguageOther, charLanguageOwn, charLibraryUse,
    charAccounting, charCreditRating, charMechRepair, charMedicine, charListen, charScience, charNavigate, charOpHvMachine, charOccult, charPersuade, charFirstAid,
    charPilot, charSwim, charLaw, charDriveAuto, charPsychoanalysis, charPsychology, charThrow, charJump, charSpotHidden, charArtCraft, charSurvival, charLocksmith,
    charTrack, charStealh, charDodge, charCharm, charFightingBrawl, charNaturalWorld, charClimb, charAppraise, charIntimidate, charSleightOfHand
  ]
  statsValues = [40, 40, 40, 50, 50, 50, 60, 60, 70]

  for i in range(len(statsValues)):
    local_choice = 0
    while local_choice < 1 or local_choice > 45:
      clear()
      update_occupation_skills(skills_list)
      print("")
      print(f"Dostępne wartości: {statsValues}")
      print(f"Wartość do wstawienia: {BOLD}{statsValues[-1]}{NC}")
      print("")
      print("╒═════════════════╕")
      print("│     WYBIERZ     │")
      print("│   UMIEJĘTNOŚĆ   │")
      print("╘═════════════════╛")
      print("")
      local_choice = inputNumber("Wybór > ")
    skills_list[local_choice-1] = statsValues.pop(-1)
  clear()

def update_occupation_skills(skillsList):
  global charAnthropology, charArcheology, charFirearmsRifle, charFirearmsHandgun, charDisguise, charElecRepair, charFastTalk, charHistory, charRide, charLanguageOther, charLanguageOwn, charLibraryUse
  global charAccounting, charCreditRating, charMechRepair, charMedicine, charListen, charScience, charNavigate, charOpHvMachine, charOccult, charPersuade, charFirstAid, charPilot
  global charSwim, charLaw, charDriveAuto, charPsychoanalysis, charPsychology, charThrow, charJump, charSpotHidden, charArtCraft, charSurvival, charLocksmith, charTrack
  global charStealh, charDodge, charCharm, charFightingBrawl, charNaturalWorld, charClimb, charAppraise, charIntimidate, charSleightOfHand

  charAnthropology = skillsList[0]
  charArcheology = skillsList[1]
  charFirearmsRifle = skillsList[2]
  charFirearmsHandgun = skillsList[3]
  charDisguise = skillsList[4]
  charElecRepair = skillsList[5]
  charFastTalk = skillsList[6]
  charHistory = skillsList[7]
  charRide = skillsList[8]
  charLanguageOther = skillsList[9]
  charLanguageOwn = skillsList[10]
  charLibraryUse = skillsList[11]

  charAccounting = skillsList[12]
  charCreditRating = skillsList[13]
  charMechRepair = skillsList[14]
  charMedicine = skillsList[15]
  charListen = skillsList[16]
  charScience = skillsList[17]
  charNavigate = skillsList[18]
  charOpHvMachine = skillsList[19]
  charOccult = skillsList[20]
  charPersuade = skillsList[21]
  charFirstAid = skillsList[22]
  charPilot = skillsList[23]

  charSwim = skillsList[24]
  charLaw = skillsList[25]
  charDriveAuto = skillsList[26]
  charPsychoanalysis = skillsList[27]
  charPsychology = skillsList[28]
  charThrow = skillsList[29]
  charJump = skillsList[30]
  charSpotHidden = skillsList[31]
  charArtCraft = skillsList[32]
  charSurvival = skillsList[33]
  charLocksmith = skillsList[34]
  charTrack = skillsList[35]

  charStealh = skillsList[36]
  charDodge = skillsList[37]
  charCharm = skillsList[38]
  charFightingBrawl = skillsList[39]
  charNaturalWorld = skillsList[40]
  charClimb = skillsList[41]
  charAppraise = skillsList[42]
  charIntimidate = skillsList[43]
  charSleightOfHand = skillsList[44]

  skills_table = [
    ('1)',f'Antropologia [{BLUE}{charAnthropology}{NC}]',       '13)',f'Księgowość [{BLUE}{charAccounting}{NC}]',         '25)',f'Pływanie [{BLUE}{charSwim}{NC}]',                '37)',f'Ukrywanie [{BLUE}{charStealh}{NC}]'),
    ('2)',f'Archeologia [{BLUE}{charArcheology}{NC}]',          '14)',f'Majętność [{BLUE}{charCreditRating}{NC}]',        '26)',f'Prawo [{BLUE}{charLaw}{NC}]',                    '38)',f'Unik [{BLUE}{charDodge}{NC}]'),
    ('3)',f'Broń (Długa) [{BLUE}{charFirearmsRifle}{NC}]',      '15)',f'Mechanika [{BLUE}{charMechRepair}{NC}]',          '27)',f'Prow. samoch. [{BLUE}{charDriveAuto}{NC}]',      '39)',f'Urok osobisty [{BLUE}{charCharm}{NC}]'),
    ('4)',f'Broń (Krótka) [{BLUE}{charFirearmsHandgun}{NC}]',   '16)',f'Medycyna [{BLUE}{charMedicine}{NC}]',             '28)',f'Psychoanaliza [{BLUE}{charPsychoanalysis}{NC}]', '40)',f'Walka wręcz [{BLUE}{charFightingBrawl}{NC}]'),
    ('5)',f'Charakteryzacja [{BLUE}{charDisguise}{NC}]',        '17)',f'Nasłuchiwanie [{BLUE}{charListen}{NC}]',          '29)',f'Psychologia [{BLUE}{charPsychology}{NC}]',       '41)',f'Wiedza o Naturze [{BLUE}{charNaturalWorld}{NC}]'),
    ('6)',f'Elektryka [{BLUE}{charElecRepair}{NC}]',            '18)',f'Nauka [{BLUE}{charScience}{NC}]',                 '30)',f'Rzucanie [{BLUE}{charThrow}{NC}]',               '42)',f'Wspinaczka [{BLUE}{charClimb}{NC}]'),
    ('7)',f'Gadanina [{BLUE}{charFastTalk}{NC}]',               '19)',f'Nawigacja [{BLUE}{charNavigate}{NC}]',            '31)',f'Skakanie [{BLUE}{charJump}{NC}]',                '43)',f'Wycena [{BLUE}{charAppraise}{NC}]'),
    ('8)',f'Historia [{BLUE}{charHistory}{NC}]',                '20)',f'Obsł. cież. sprz. [{BLUE}{charOpHvMachine}{NC}]', '32)',f'Spostrzegawczość [{BLUE}{charSpotHidden}{NC}]',  '44)',f'Zastraszanie [{BLUE}{charIntimidate}{NC}]'),
    ('9)',f'Jeździectwo [{BLUE}{charRide}{NC}]',                '21)',f'Okultyzm [{BLUE}{charOccult}{NC}]',               '33)',f'Sztuka/Rzemiosło [{BLUE}{charArtCraft}{NC}]',    '45)',f'Zręczne palce [{BLUE}{charSleightOfHand}{NC}]'),
    ('10)',f'Język Obcy [{BLUE}{charLanguageOther}{NC}]',       '22)',f'Perswazja [{BLUE}{charPersuade}{NC}]',            '34)',f'Sztuka przetrw. [{BLUE}{charSurvival}{NC}]',     '',''),
    ('11)',f'Jezyk Ojczysty [{BLUE}{charLanguageOwn}{NC}]',     '23)',f'Pierwsza pomoc [{BLUE}{charFirstAid}{NC}]',       '35)',f'Ślusarstwo [{BLUE}{charLocksmith}{NC}]',         '',''),
    ('12)',f'Korzystanie z bibl. [{BLUE}{charLibraryUse}{NC}]', '24)',f'Pilotowanie [{BLUE}{charPilot}{NC}]',             '36)',f'Tropienie [{BLUE}{charTrack}{NC}]',              '','')
  ]
  print(tabulate(skills_table, tablefmt="pretty"))

def set_random_basic_stats():
  global charStrength, charDexterity, charPower, charCondition, charApperance, charEducation
  global charSize, charInteligence, charHP, charSanity, charLuck, charMP, charDamageBonus, charBuild
  global charDodge, charLanguageOwn

  statsValues = [40, 50, 50, 50, 60, 60, 70, 80]
  usedElems = []
  for i in range(len(statsValues)):
    selectedVal = random.randint(0, len(statsValues)-1)
    usedElems.append(statsValues.pop(selectedVal))
  charStrength = usedElems[0]
  charDexterity = usedElems[1]
  charPower = usedElems[2]
  charCondition = usedElems[3]
  charApperance = usedElems[4]
  charEducation = usedElems[5]
  charSize = usedElems[6]
  charInteligence = usedElems[7]
  charHP = int((charSize + charCondition) / 10)
  charSanity = charPower
  charLuck = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 5
  charMP = int(charPower / 5)
  if charPower + charSize > 124:
    charDamageBonus = '+1K4'
    charBuild = 1
  charDodge = int(charDexterity / 2)
  charLanguageOwn = charEducation

def set_random_occupation_skills():
  global charArtCraft, charFirearmsHandgun, charLaw, charListen, charCharm
  global charPsychology, charSpotHidden, charTrack, charCreditRating
  statsValues = [40, 40, 40, 50, 50, 50, 60, 60, 70]
  usedElems = []
  for i in range(len(statsValues)):
    selectedVal = random.randint(0, len(statsValues)-1)
    usedElems.append(statsValues.pop(selectedVal))
  charArtCraft = usedElems[0]
  charFirearmsHandgun = usedElems[1]
  charLaw = usedElems[2]
  charListen = usedElems[3]
  charCharm = usedElems[4]
  charPsychology = usedElems[5]
  charSpotHidden = usedElems[6]
  charTrack = usedElems[7]
  charCreditRating = usedElems[8]

def set_random_investigator_problems():
  problem_1 = random.randint(0, 9)
  problem_2 = problem_1
  while problem_2 == problem_1:
    problem_2 = random.randint(0, 9)
  selectedProblems.append(problems[problem_1])
  selectedProblems.append(problems[problem_2])

def show_character_stats():
  char_data = [
    ('Siła', charStrength,               'Antropologia', charAnthropology,      'Księgowość', charAccounting,         'Pilotowanie', charPilot,            'Tropienie', charTrack),
    ('Zręczność', charDexterity,         'Archeologia', charArcheology,         'Majętność', charCreditRating,        'Pływanie', charSwim,                'Ukrywanie', charStealh),
    ('Moc', charPower,                   'Broń (Długa)', charFirearmsRifle,     'Mechanika', charMechRepair,          'Prawo', charLaw,                    'Unik', charDodge),
    ('Kondycja', charCondition,          'Broń (Krótka)', charFirearmsHandgun,  'Medycyna', charMedicine,             'Prow. samoch.', charDriveAuto,      'Urok osobisty', charCharm),
    ('Wygląd', charApperance,            'Charakteryzacja', charDisguise,       'Mity Cthulhu', charCthulhuMythos,    'Psychoanaliza', charPsychoanalysis, 'Walka wręcz', charFightingBrawl),
    ('Wykształcenie', charEducation,     'Elektryka', charElecRepair,           'Nasłuchiwanie', charListen,          'Psychologia', charPsychology,       'Wiedza o Naturze', charNaturalWorld),
    ('Budowa ciała', charSize,           'Gadanina', charFastTalk,              'Nauka', charScience,                 'Rzucanie', charThrow,               'Wspinaczka', charClimb),
    ('Inteligencja', charInteligence,    'Historia', charHistory,               'Nawigacja', charNavigate,            'Skakanie', charJump,                'Wycena', charAppraise),
    ('Punkty życia', charHP,             'Jeździectwo', charRide,               'Obsł. cież. sprz.', charOpHvMachine, 'Spostrzegawczość', charSpotHidden,  'Zastraszanie', charIntimidate),
    ('Punkty poczytalności', charSanity, 'Język Obcy', charLanguageOther,       'Okultyzm', charOccult,               'Sztuka/Rzemiosło', charArtCraft,    'Zręczne palce', charSleightOfHand),
    ('Punkty szczęścia', charLuck,       'Jezyk Ojczysty', charLanguageOwn,     'Perswazja', charPersuade,            'Sztuka przetrw.', charSurvival,     '', ''),
    ('Punkty mocy', charMP,              'Korzystanie z bibl.', charLibraryUse, 'Pierwsza pomoc', charFirstAid,       'Ślusarstwo', charLocksmith,         '', '')
  ]

  headers = [charName+' ('+charSex+')', 'Lat '+str(charAge), 'Profesja: '+charProf, '', 'Modyfikator obr.', charDamageBonus, 'Krzepa', str(charBuild), 'Ruch', '-']

  print(f'{BOLD}Statystyki Twojej postaci{NC}:')
  print(tabulate(char_data, headers, tablefmt="pretty"))
  print(f'{BOLD}Przymioty postaci{NC}:	', end='')
  for item in selectedProblems:
    print(item + '; ', end = '')
  print()
  print(f'{BOLD}Wyposażenie{NC}:		', end = '')
  for item in equipment:
    print(item + ', ', end = '')
  if handgunRounds > 0:
    print(f"\n{BOLD}Naboje do pistoletu{NC} - " + str(handgunRounds))
  if rifleRounds > 0:
    print(f"\n{BOLD}Naboje do strzelby{NC} - " + str(rifleRounds))
  print('\n')

def show_owned_notes():
  global choice, notes, ownedNotes
  while choice != 0:
    print("╒═════════════════╕")
    print("│ WYBIERZ NOTATKĘ │")
    print("╘═════════════════╛")
    for note in ownedNotes:
      print(f"{note}) {notes[note-1].get('name')}")
    print("0) Powrót")
    choice = inputNumber("Wybór > ")
    clear()
    show_note(choice)
  choice = 99

def show_note(note_id):
  global notes, ownedNotes
  if note_id in ownedNotes:
    print(notes[note_id-1].get('text'))

def test_skill(skillName, skillValue):
  global roll, test_result
  roll = random.randint(1, 100)
  print(f"Test {skillName} ({skillValue}) - Wyrzuciłeś {roll}")
  if roll == 1:
    test_result = 4
    print(f"{BGREEN}{ITALIC}Krytyczny Sukces{NC}")
  elif roll <= (skillValue / 5):
    test_result = 3
    print(f"{GREEN}{ITALIC}Ekstremalny Sukces{NC}")
  elif roll <= (skillValue / 2):
    test_result = 2
    print(f"{GREEN}{ITALIC}Trudny Sukces{NC}")
  elif roll <= skillValue:
    test_result = 1
    print(f"{GREEN}{ITALIC}Sukces{NC}")
  elif roll > skillValue:
    if roll != 100:
      test_result = 0
      print(f"{RED}{ITALIC}Porażka{NC}")
    else:
      test_result = -1
      print(f"{BRED}{ITALIC}Krytyczna Porażka{NC}")

def test_skills(skillName, skillsList):
  global roll, test_result
  roll = random.randint(1, 100)
  skillsList.sort()
  skillValue = skillsList[-1]
  print(f"Test {skillName} ({skillValue}) - Wyrzuciłeś {roll}")
  if roll == 1:
    test_result = 4
    print(f"{BGREEN}{ITALIC}Krytyczny Sukces{NC}")
  elif roll <= (skillValue / 5):
    test_result = 3
    print(f"{GREEN}{ITALIC}Ekstremalny Sukces{NC}")
  elif roll <= (skillValue / 2):
    test_result = 2
    print(f"{GREEN}{ITALIC}Trudny Sukces{NC}")
  elif roll <= skillValue:
    test_result = 1
    print(f"{GREEN}{ITALIC}Sukces{NC}")
  elif roll > skillValue:
    if roll != 100:
      test_result = 0
      print(f"{RED}{ITALIC}Porażka{NC}")
    else:
      test_result = -1
      print(f"{BRED}{ITALIC}Krytyczna Porażka{NC}")

##! START GAME !##
def main():
  global fname, choice
  choice = 0
  clear()
  while choice != 'q' and choice != 'Q':
    show_game_logo()
    print("╒═════════════════╕")
    print("│   MENU GŁÓWNE   │")
    print("╘═════════════════╛")
    print(f"1) {DGRAY}Kontynuuj grę{NC}")
    print("2) Rozpocznij grę")
    print(f"3) {DGRAY}Wczytaj grę{NC}")
    print("4) O grze")
    print("5) Ustawienia")
    print("Q) Wyjście")
    choice = inputText("Wybór > ")
    clear()

    if choice == '1':
      continue_game()

    if choice == '2':
      new_game()

    if choice == '3':
      load_game()

    if choice == '4':
      about_game()

    if choice == '5':
      game_settings()

def about_game():
  global choice
  while choice != 0:
    print("╒════════════════╕")
    print("│     O GRZE     │")
    print("╘════════════════╛")
    print(f"{ORANGE}Wykonawca gry:{NC}	Jakub Michniewicz")
    print(f"{ORANGE}Scenariusz:{NC}	Asia Wiewiórska")
    print(f'''\n{ORANGE}'DRUGA'{NC}
  Scenariusz ten inspirowany jest ponurymi skandynawskimi powieściami i serialami,
  w których główne role odgrywają tajemnica, społeczność i śledztwo. Konwencja ta
  znana jest pod nazwą nordic-noir, lecz scenariusz nawiązuje również do znanych baśni
  ludowych i Lovecraftowskiej Krainy Snów. Akcja gry rozpoczyna się w lutym 2020 r.
  gdzieś w Skandynawii. Oniryczny nastrój buduje tu odosobnione miasteczko otoczone przez
  wzgórza i ciemne lasy oraz surowa, choć urokliwa zimowa aura. To bardzo subtelna historia,
  która nie jest opowieścią akcji.''')

    print(f"\n0) Powrót")
    choice = inputNumber("Wybór > ")
    clear()

# TODO: add save game functionality
def save_game():
  """
  to save: 
  - character stats
  - game flags
  - equipment and found items
  save this data to save file in ~/pythulhu folder
  """
  pass

# TODO: add load game functionality
def load_game():
  print("Niedosępne w wersji DEMO")
  time.sleep(sleepTime)
  clear()

# TODO: add game settings functionality
def game_settings():
  global choice, sleepTime
  while choice != 0:
    print("")
    print("╒════════════════╕")
    print("│   USTAWIENIA   │")
    print("╘════════════════╛")
    print("1) Czas pomiędzy akapitami")
    print("2) Przywróc ustawienia domyślne")
    print("0) Powrót")
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 1:
      print(f"Aktualna wartość: {'%g'%(sleepTime)}s")
      print("(Wprowadź '0' aby nie zmieniać)")
      newTime = inputFloat("Podaj nowy czas w sekundach: ")
      if newTime != 0:
        sleepTime = newTime

    if choice == 2:
      sleepTime = 2
      print("Przywrócono ustawienia domyślne")

# TODO: add this functionality by reading last modified 'save' file in ~/pythulhu/ folder
def continue_game():
  print("Niedosępne w wersji DEMO")
  time.sleep(sleepTime)
  clear()

def reset_flags():
  global selectedProblems, handgunRounds, rifleRounds, ownedNotes
  global GirlHitByCar, CarChecked
  #* reset Game Vars
  selectedProblems = []
  handgunRounds = 0
  rifleRounds = 0
  ownedNotes = []
  #* reset Game Flags
  GirlHitByCar = 0
  CarChecked = 0
  CalledForMechanic = 0
  GirlHisteria = 0

def new_game():
  global choice
  reset_flags()
  create_caracter()
  clear()
  show_character_stats()

  while choice != 0:
    print("╒════════════════╕")
    print("│    NOWA GRA    │")
    print("╘════════════════╛")
    print("1) Graj tą postacią")
    print("2) Utwórz nową postać")
    print("9) Pokaż statystyki mojej postaci")
    print("0) Powrót")
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 2:
      create_caracter()
      show_character_stats()

    if choice == 1:
      initiate_history()

def standard_menu_options():
  global ownedNotes
  print("")
  if ownedNotes:
    print("8) Sprawdź posiadane notatki")
  print("9) Pokaż statystyki mojej postaci")
  print("0) Powrót do menu")

def initiate_history():
  global choice, test_result, GirlHitByCar
  printText('''\n  Stoksjö to liczące zaledwie 2 tys. mieszkańców miasteczko położone w centrum prowincji
  o nazwie Helbjerg, w którym pełnisz rolę komendanta małego posterunku policji.''')
  time.sleep(sleepTime)
  printText('''\n  Jest 12 lutego 2020 r. Wracasz późną nocą autem z oddalonego o przeszło 80 km miasta,
  w którym składałeś przed sądem zeznania dotyczące jednej z Twoich ostatnich spraw.
  Na wąskiej, nierozjeżdżonej drodze do domu, biegnącej dnem kotliny między dwoma
  porośniętymi ciemnym lasem wzgórzami, leży świeży śnieg.''')
  time.sleep(sleepTime)
  printText('''\n  Niespodziewanie, wyjeżdżając zza zakrętu, dostrzegasz w światłach samochodu sylwetkę 
  dziewczyny, słaniającej się na bosych nogach poboczem w kierunku miasta, która
  prawdopodobnie za chwilę wejdzie pod koła Twojego radiowozu.\n''')
  time.sleep(sleepTime)

  while choice != 0:
    print("╒═════════════════╕")
    print("│   CO ROBISZ ?   │")
    print("╘═════════════════╛")
    print("1) Staram się ją ominąć")
    print("2) Jadę dalej - tylko mi się wydawało")
    standard_menu_options()
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 8 and ownedNotes:
      show_owned_notes()

    if choice == 2:
      GirlHitByCar = 1
      girl_hit_by_car()

    if choice == 1:
      test_skill('prowadzenia samochodu', charDriveAuto)
      if test_result >= 1:
        girl_on_road()
      else:
        GirlHitByCar = 1
        girl_hit_by_car()

def girl_on_road():
  global choice
  printText('''\n  Wpadasz w poślizg, ale kilka szybkich ruchów kierownicą i po chwili udaje Ci się
  wyrównanać tor jazdy i bezpiecznie zatrzymać pojazd.''')
  while choice != 0:
    print("")
    print("╒═════════════════╕")
    print("│   CO ROBISZ ?   │")
    print("╘═════════════════╛")
    print("1) Wysiadam z samochodu")
    print("2) Rozglądam się po samochodzie")
    standard_menu_options()
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 8 and ownedNotes:
      show_owned_notes()

    if choice == 2:
      check_car_interior()

    if choice == 1:
      get_out_of_the_car()

def girl_hit_by_car():
  global choice
  printText('''\n  Słyszysz huk uderzenia o maskę Twojego samochodu. Auto wpada w poślizg i mimo Twoich
  prób opanowowania pojazdu nie udaje Ci się utrzymać na jezdni. Samochód wpada do rowu.
  Nagłe, mocne uderzenie Twojej głowy o kierownicę powoduje chwilową dezorientację.''')
  time.sleep(sleepTime)
  printText('''\n  Najwyraźniej postać dziewczyny nie była Twoimi halucynacjami wywołanymi zmęczeniem
  i hektolitrami kawy. Dochodząc powoli do siebie wyczuwasz metaliczny posmak w ustach
  oraz pieczenie nad lewą brwią.''')
  time.sleep(sleepTime)

  while choice != 0:
    print("")
    print("╒═════════════════╕")
    print("│   CO ROBISZ ?   │")
    print("╘═════════════════╛")
    print("1) Wysiadam z samochodu")
    print("2) Dzwonię po pomoc")
    print("3) Rozglądam się po samochodzie")
    standard_menu_options()
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 8 and ownedNotes:
      show_owned_notes()

    if choice == 3:
      check_car_interior()

    if choice == 2:
      call_for_help()

    if choice == 1:
      get_out_of_the_car()

def check_car_interior():
  global choice, test_result, equipment, handgunRounds, CarChecked
  test_skill("spostrzegawczości", charSpotHidden)
  if test_result >= 1:
    bullets = random.randint(2, 8)
    printText(f'''\n  Na podłodze pod kokpitem od strony pasażera leży latarka, która wcześniej
  spoczywała na fotelu. W schowku znajdujesz pistolet SIG-Sauer P225 z magazynkiem,
  w którym znajduje się kilka naboi ({bullets}). Na tylym siedzeniu leży zimowa
  policyjna kurtka.''')
    time.sleep(sleepTime)
    CarChecked = 1
  elif test_result < 1:
    if test_result == 0:
      printText('''\n  Na podłodze pod kokpitem od strony pasażera leży latarka, która wcześniej
    spoczywała na fotelu. Na tylym siedzeniu leży zimowa policyjna kurtka.''')
      time.sleep(sleepTime)
      CarChecked = 0
    else:
      printText('''\n  Może to kwestia tego, że samochód wpadł w poślizg i wszyskie luźne rzeczy
    porozrzucane są po całym samochodzie, ale nie znajdujesz niczego przydatnego w tej
    chwili.''')
      time.sleep(sleepTime)
      CarChecked = -1

  while choice != 0:
    print("")
    print("╒═════════════════╕")
    print("│   CO ROBISZ ?   │")
    print("╘═════════════════╛")
    print("1) Wysiadam z samochodu")
    print("2) Dzwonię po pomoc")
    if CarChecked != -1:
      print("3) Zabieram rzeczy")
    standard_menu_options()
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 8 and ownedNotes:
      show_owned_notes()

    if choice == 3 and CarChecked != -1:
      if CarChecked == 0:
        equipment = equipment + ["Latarka", "Policyjna kurtka zimowa"]
        CarChecked = -1
      else:
        handgunRounds = handgunRounds + bullets
        equipment = equipment + ["Pistolet", "Latarka", "Policyjna kurtka zimowa"]
        CarChecked = -1
      printText('''\n  Zabierasz potrzebne rzeczy. Ta mroźna, zimowa noc będzie teraz trochę bardziej
  do zniesienia...''')

    if choice == 2:
      call_for_help()

    if choice == 1:
      get_out_of_the_car()

def get_out_of_the_car():
  global choice, GirlHitByCar
  if GirlHitByCar == 1:
    printText('''\n  Otwierasz drzwi. Mroźne powietrze zimowej nocy pomaga Ci złapać z powrotem kontakt
  z rzeczywistością. Wychodząc z samochodu zauważasz, że Twoja podróż zakończyła się w
  przydrożnym rowie, którego opuszczenie bez pomocy drogowej raczej nie będzie możliwe.''')
    time.sleep(sleepTime)
  else:
    printText('''\n  Jest ciemno, włączasz więc sygnały światlne na dachu radiowozu, aby rozświetlić
  co nieco okolicę i jednocześnie być bardziej widocznym dla ewentualnych przejedżających
  tędy pojazdów. Wysiadasz z samochodu i kierujesz się w stronę dziewczyny.''')
    time.sleep(sleepTime)
  if "Latarka" in equipment:
    printText('''\n  Oprócz reflektorów Twojego pojazdu, nie ma w najbliższej okolicy żadnego źródła
  światła, dlatego podchodząc w kierunku dziewczyny włączasz swoją latarkę, aby lepiej
  rozejrzeć się w sytuacji.''')
    time.sleep(sleepTime)
  printText('''\n  Z bliska biedaczka wygląda na przemarzniętą i wycieńczoną. Nie ma butów, a jedyne jej
  ubranie to sfatygowana halka. Na jej prawym nadgarstku zauważasz zawiązaną wyblakłą
  różową wstążkę, zwykle służącą do związywania włosów.''')
  time.sleep(sleepTime)
  if GirlHitByCar == 1:
    printText('''\n  Dziewczyna jest nieprzytomna, ale oddycha. Zderzenie z Twoim samochodem spowodowało
  na szczęście jedynie niewielkie obrażenia i kilka drobnych otarć. W każdym razie
  powinna zostać zbadana przez lekarza, aby upewnić się, czy poza tym nic poważnego
  nie zagraża jej zdrowiu.''')
  time.sleep(sleepTime)

  while choice != 0:
    print("")
    print("╒═════════════════╕")
    print("│   CO ROBISZ ?   │")
    print("╘═════════════════╛")
    print("1) Sprawdzam jej stan zdrowia")
    print("2) Dzwonię po pomoc")
    standard_menu_options()
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 8 and ownedNotes:
      show_owned_notes()

    if choice == 2:
      call_for_help()

    if choice == 1:
      check_girl_health()

def check_girl_health():
  global choice, test_result
  test_skills("medycyny lub pierwszej pomocy", [charMedicine, charFirstAid])
  if test_result >= 1:
    if GirlHitByCar != 1:
      printText('''\n  Kobieta wygląda na oszołomioną i przerażoną. Oceniając na szybko, dziewczyna może
  mieć co najwyżej 20 lat i sądząc po jej stopach na mrozie znajduje się od jakichś 
  kilkudziesięciu minut. Nie odpowiada na pytania, szlocha i próbuje się bronić.''')
      time.sleep(sleepTime)
    else:
      printText('''\n  Młoda kobieta wygląda na co najwyżej 20 lat i sądząc po jej stopach, na mrozie
  znajduje się od jakichś kilkudziesięciu minut.''')
      time.sleep(sleepTime)
  else:
    if GirlHitByCar != 1:
      printText('''\n  Poza tym, że ma kilka raczej niegroźnych otarć, najpewniej od gałęzi, w tych warunkach
  nie znajdujesz niczego bardziej istotnego. Kobieta nie odpowiada na pytania, szlocha
  i próbuje się bronić.''')
      time.sleep(sleepTime)
    else:
      printText('''\n  Niezbyt sprzyjające warunki nie pozwalają na dokładniejsze przyjrzenie się
  nieprzytomnej dziewczynie. Kilka siniaków i otarć, pozostałych po spotkaniu z Twoim
  radiowozem, to jedyne co jesteś w stanie teraz zauważyć.''')
      time.sleep(sleepTime)

  while choice != 0:
    print("")
    print("╒═════════════════╕")
    print("│   CO ROBISZ ?   │")
    print("╘═════════════════╛")
    print("1) Dzwonię po pomoc")
    if GirlHitByCar != 1:
      print("2) Próbuję ją uspokoić")
    else:
      print("2) Zabieram ją do szpitala")
    standard_menu_options()
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 8 and ownedNotes:
      show_owned_notes()

    if choice == 2:
      if  GirlHitByCar != 1:
        calm_down_girl()
      else:
        take_girl_to_hospital()

    if choice == 1:
      call_for_help()

def calm_down_girl():
  global choice, test_result
  test_skill("psychoanalizy", charPsychoanalysis)
  if test_result >= 1:
    printText('''\n  Może to ciepły dzwięk Twojego głosu, a może Twój przyjacielski dotyk sprawił, że
  dziewczyna uspokoiła się na tyle, żeby bez większych trudności udało Ci się wsiąść
  z nią do samochodu. Jednak przez cały ten czas dziewczyna nie wydawała się rozumieć 
  co do niej mówisz.''')
    time.sleep(sleepTime)
  else:
    printText('''\n  Niestety Twoje próby uspokojenia dziewczyny nie pomogły, a wręcz spowodowały, że
  zaczęła krzyczeć w przerażeniu i odpychać Cię rękami i nogami. W pewnym momencie
  wyrywa Ci się z rąk, upada plecami na przydrożny śnieg i zaczyna się cofać...''')
    time.sleep(sleepTime)
    GirlHisteria = 1

  while choice != 0:
    print("")
    print("╒═════════════════╕")
    print("│   CO ROBISZ ?   │")
    print("╘═════════════════╛")
    print("1) Dzwonię po pomoc")
    if GirlHisteria != 1:
      print("2) Zabieram ją do szpitala")
      print("3) Zabieram ją na komisariat")
    else:
      print("2) Staram się ją zatrzymać")
    standard_menu_options()
    choice = inputNumber("Wybór > ")
    clear()

    if choice == 9:
      show_character_stats()

    if choice == 8 and ownedNotes:
      show_owned_notes()

    if choice == 3:
      take_girl_to_police()

    if choice == 2:
      if  GirlHitByCar != 1:
        stop_the_girl()
      else:
        take_girl_to_hospital()

    if choice == 1:
      call_for_help()

def call_for_help():
  printText('''\n  Dzwonisz do swojego partnera Joela Krogga, który w momencie Twojego telefonu parzył
  sobie kolejną kawę, aby nie zasnąć podczas jego nocnej zmiany na posterunku. Przekazujesz 
  mu niezbędne informacje i prosisz o załatwienie transportu. ''')

  printText('''\n  Gdy pomoc dociera na miejsce, dziewczyna zostaje przewieziona do szpitala, a Ciebie
  zabrano na posterunek w celu ustalenia szczegółów zdarzenia.''')
  # TODO: Add futher paragraphs
  the_end()

def take_girl_to_police():
  the_end()
  pass

def take_girl_to_hospital():
  global choice, test_result
  if GirlHitByCar == 1:
    printText('''\n  Zabierasz przemarzniętą i nieprzytomną dziewczynę do samochodu i jedziesz do szpitala
  w Stoksjö.''')
    time.sleep(sleepTime)
  printText('''\n  Podjeżdżasz pod szpital, parkujesz na miejscu dla pojazdów uprzywilejowanych. Wysiadasz
  i zabierasz stojący obok wózek inwalidzki, aby posadzić na niego dziewczynę. Wchodzicie
  do szpitala i kierujecie się w stronę recepcji.''')
  time.sleep(sleepTime)
  the_end()
  pass

def the_end():
  global choice
  time.sleep(sleepTime)
  print(f"\n  ### KONIEC WERSJI DEMO ###\n")
  choice = input("Wciśnij Enter aby wrócić do menu głównego... ")
  choice = 0
  clear()

#? Let this file to be imported as module
if __name__ == "__main__":
  main()

# TODO: Add and import futher days as a mudules
