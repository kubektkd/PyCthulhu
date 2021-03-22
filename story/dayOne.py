from utils.helpers import *
from gameEngine.interface import *
from gameEngine.gameMechanics import *

# * WHAT CHARACTER KNOW * #
GirlHitByCar = 0
CarChecked = 0
CalledForMechanic = 0
GirlHysteria = 0


def initiate_history():
    global GirlHitByCar
    print_text('''Stoksjö to liczące zaledwie 2 tys. mieszkańców miasteczko położone w centrum prowincji o nazwie
Helbjerg, w którym pełnisz rolę komendanta małego posterunku policji.''')
    time.sleep(config.sleepTime)
    print_text('''Jest 12 lutego 2020 r. Wracasz późną nocą autem z oddalonego o przeszło 80 km miasta, w którym
składałeś przed sądem zeznania dotyczące jednej z Twoich ostatnich spraw. Na wąskiej, nierozjeżdżonej drodze do
domu, biegncej dnem kotliny między dwoma porośniętymi ciemnym lasem wzgórzami, leży świeży śnieg.''')
    time.sleep(config.sleepTime)
    print_text('''Niespodziewanie, wyjeżdżając zza zakrętu, dostrzegasz w światłach samochodu sylwetkę dziewczyny,
słaniającej się na bosych nogach poboczem w kierunku miasta, która prawdopodobnie za chwilę wejdzie pod koła
Twojego radiowozu.''')
    time.sleep(config.sleepTime)

    while config.choice != 0:
        generate_title_box('TWORZENIE POSTACI')
        generate_title_box('CO ROBISZ?')
        generate_title_box('Menu główne')
        generate_title_box('wybierz umiejętności')
        print("")
        print("╒═════════════════╕")
        print("│   CO ROBISZ ?   │")
        print("╘═════════════════╛")
        print("1) Staram się ją ominąć")
        print("2) Jadę dalej - tylko mi się wydawało")
        standard_menu_options()
        config.choice = input_number("Wybór > ")
        clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 8 and player.ownedNotes:
            player.show_owned_notes()

        if config.choice == 2:
            GirlHitByCar = 1
            girl_hit_by_car()

        if config.choice == 1:
            test_result = test_skill('prowadzenia samochodu', player.driveAuto)
            if test_result >= 1:
                girl_on_road()
            else:
                GirlHitByCar = 1
                girl_hit_by_car()


def girl_on_road():
    print_text('''Wpadasz w poślizg, ale kilka szybkich ruchów kierownicą i po chwili udaje Ci się wyrównanać tor
jazdy i bezpiecznie zatrzymać pojazd.''')
    while config.choice != 0:
        print("")
        print("╒═════════════════╕")
        print("│   CO ROBISZ ?   │")
        print("╘═════════════════╛")
        print("1) Wysiadam z samochodu")
        print("2) Rozglądam się po samochodzie")
        standard_menu_options()
        config.choice = input_number("Wybór > ")
        clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 8 and player.ownedNotes:
            player.show_owned_notes()

        if config.choice == 2:
            check_car_interior()

        if config.choice == 1:
            get_out_of_the_car()


def girl_hit_by_car():
    print_text('''Słyszysz huk uderzenia o maskę Twojego samochodu. Auto wpada w poślizg i mimo Twoich prób
opanowowania pojazdu nie udaje Ci się utrzymać na jezdni. Samochód wpada do rowu. Nagłe, mocne uderzenie Twojej
głowy o kierownicę powoduje chwilową dezorientację.''')
    time.sleep(config.sleepTime)
    print_text('''Najwyraźniej postać dziewczyny nie była Twoimi halucynacjami wywołanymi zmęczeniem i hektolitrami
kawy. Dochodząc powoli do siebie wyczuwasz metaliczny posmak w ustach oraz pieczenie nad lewą brwią.''')
    time.sleep(config.sleepTime)

    while config.choice != 0:
        print("")
        print("╒═════════════════╕")
        print("│   CO ROBISZ ?   │")
        print("╘═════════════════╛")
        print("1) Wysiadam z samochodu")
        print("2) Dzwonię po pomoc")
        print("3) Rozglądam się po samochodzie")
        standard_menu_options()
        config.choice = input_number("Wybór > ")
        clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 8 and player.ownedNotes:
            player.show_owned_notes()

        if config.choice == 3:
            check_car_interior()

        if config.choice == 2:
            call_for_help()

        if config.choice == 1:
            get_out_of_the_car()


def check_car_interior():
    global CarChecked
    test_result = test_skill("spostrzegawczości", player.spotHidden)
    if test_result >= 1:
        bullets = random.randint(2, 8)
        print_text(f'''Na podłodze pod kokpitem od strony pasażera leży latarka, która wcześniej spoczywała na
fotelu. W schowku znajdujesz pistolet SIG-Sauer P225 z magazynkiem, w którym znajduje się kilka naboi ({bullets}).
Na tylym siedzeniu leży zimowa policyjna kurtka.''')
        time.sleep(config.sleepTime)
        CarChecked = 1
    elif test_result < 1:
        if test_result == 0:
            print_text('''Na podłodze pod kokpitem od strony pasażera leży latarka, która wcześniej spoczywała na
fotelu. Na tylym siedzeniu leży zimowa policyjna kurtka.''')
            time.sleep(config.sleepTime)
            CarChecked = 0
        else:
            print_text('''Może to kwestia tego, że samochód wpadł w poślizg i wszyskie luźne rzeczy porozrzucane są
po całym samochodzie, ale nie znajdujesz niczego przydatnego w tej chwili.''')
            time.sleep(config.sleepTime)
            CarChecked = -1

    while config.choice != 0:
        print("")
        print("╒═════════════════╕")
        print("│   CO ROBISZ ?   │")
        print("╘═════════════════╛")
        print("1) Wysiadam z samochodu")
        print("2) Dzwonię po pomoc")
        if CarChecked != -1:
            print("3) Zabieram rzeczy")
        standard_menu_options()
        config.choice = input_number("Wybór > ")
        clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 8 and player.ownedNotes:
            player.show_owned_notes()

        if config.choice == 3 and CarChecked != -1:
            if CarChecked == 0:
                player.equipment = player.equipment + ["Latarka", "Policyjna kurtka zimowa"]
                CarChecked = -1
            else:
                player.handgunRounds = player.handgunRounds + bullets
                player.equipment = player.equipment + ["Pistolet", "Latarka", "Policyjna kurtka zimowa"]
                CarChecked = -1
            print_text('''Zabierasz potrzebne rzeczy. Ta mroźna, zimowa noc będzie teraz trochę bardziej do
zniesienia...''')

        if config.choice == 2:
            call_for_help()

        if config.choice == 1:
            get_out_of_the_car()


def get_out_of_the_car():
    global GirlHitByCar
    if GirlHitByCar == 1:
        print_text('''Otwierasz drzwi. Mroźne powietrze zimowej nocy pomaga Ci złapać z powrotem kontakt z
rzeczywistością. Wychodząc z samochodu zauważasz, że Twoja podróż zakończyła się w przydrożnym rowie,
którego opuszczenie bez pomocy drogowej raczej nie będzie możliwe.''')
        time.sleep(config.sleepTime)
    else:
        print_text('''Jest ciemno, włączasz więc sygnały światlne na dachu radiowozu, aby rozświetlić co nieco
okolicę i jednocześnie być bardziej widocznym dla ewentualnych przejedżających tędy pojazdów. Wysiadasz z
samochodu i kierujesz się w stronę dziewczyny.''')
        time.sleep(config.sleepTime)
    if "Latarka" in player.equipment:
        print_text('''Oprócz reflektorów Twojego pojazdu, nie ma w najbliższej okolicy żadnego źródła światła,
dlatego podchodząc w kierunku dziewczyny włączasz swoją latarkę, aby lepiej rozejrzeć się w sytuacji.''')
        time.sleep(config.sleepTime)
    print_text('''Z bliska biedaczka wygląda na przemarzniętą i wycieńczoną. Nie ma butów, a jedyne jej ubranie to
sfatygowana halka. Na jej prawym nadgarstku zauważasz zawiązaną wyblakłą różową wstążkę, zwykle służącą do
związywania włosów.''')
    time.sleep(config.sleepTime)
    if GirlHitByCar == 1:
        print_text('''Dziewczyna jest nieprzytomna, ale oddycha. Zderzenie z Twoim samochodem spowodowało na
szczęście jedynie niewielkie obrażenia i kilka drobnych otarć. W każdym razie powinna zostać zbadana przez
lekarza, aby upewnić się, czy poza tym nic poważnego nie zagraża jej zdrowiu.''')
    time.sleep(config.sleepTime)

    while config.choice != 0:
        print("")
        print("╒═════════════════╕")
        print("│   CO ROBISZ ?   │")
        print("╘═════════════════╛")
        print("1) Sprawdzam jej stan zdrowia")
        print("2) Dzwonię po pomoc")
        standard_menu_options()
        config.choice = input_number("Wybór > ")
        clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 8 and player.ownedNotes:
            player.show_owned_notes()

        if config.choice == 2:
            call_for_help()

        if config.choice == 1:
            check_girl_health()


def check_girl_health():
    test_result = test_skills("medycyny lub pierwszej pomocy", [player.medicine, player.firstAid])
    if test_result >= 1:
        if GirlHitByCar != 1:
            print_text('''Kobieta wygląda na oszołomioną i przerażoną. Oceniając na szybko, dziewczyna może mieć co
najwyżej 20 lat i sądząc po jej stopach na mrozie znajduje się od jakichś kilkudziesięciu minut. Nie
odpowiada na pytania, szlocha i próbuje się bronić.''')
            time.sleep(config.sleepTime)
        else:
            print_text('''Młoda kobieta wygląda na co najwyżej 20 lat i sądząc po jej stopach, na mrozie znajduje się
od jakichś kilkudziesięciu minut.''')
            time.sleep(config.sleepTime)
    else:
        if GirlHitByCar != 1:
            print_text('''Poza tym, że ma kilka raczej niegroźnych otarć, najpewniej od gałęzi, w tych warunkach nie
znajdujesz niczego bardziej istotnego. Kobieta nie odpowiada na pytania, szlocha i próbuje się bronić.''')
            time.sleep(config.sleepTime)
        else:
            print_text('''Niezbyt sprzyjające warunki nie pozwalają na dokładniejsze przyjrzenie się nieprzytomnej
dziewczynie. Kilka siniaków i otarć, pozostałych po spotkaniu z Twoim radiowozem, to jedyne co jesteś w
stanie teraz zauważyć.''')
            time.sleep(config.sleepTime)

    while config.choice != 0:
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
        config.choice = input_number("Wybór > ")
        clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 8 and player.ownedNotes:
            player.show_owned_notes()

        if config.choice == 2:
            if GirlHitByCar != 1:
                calm_down_girl()
            else:
                take_girl_to_hospital()

        if config.choice == 1:
            call_for_help()


def calm_down_girl():
    global GirlHysteria
    test_result = test_skill("psychoanalizy", player.psychoanalysis)
    if test_result >= 1:
        print_text('''Może to ciepły dzwięk Twojego głosu, a może Twój przyjacielski dotyk sprawił, że dziewczyna
uspokoiła się na tyle, żeby bez większych trudności udało Ci się wsiąść z nią do samochodu. Jednak przez cały
ten czas dziewczyna nie wydawała się rozumieć co do niej mówisz.''')
        time.sleep(config.sleepTime)
    else:
        print_text('''Niestety Twoje próby uspokojenia dziewczyny nie pomogły, a wręcz spowodowały, że zaczęła
krzyczeć w przerażeniu i odpychać Cię rękami i nogami. W pewnym momencie wyrywa Ci się z rąk, upada plecami
na przydrożny śnieg i zaczyna się cofać...''')
        time.sleep(config.sleepTime)
        GirlHysteria = 1

    while config.choice != 0:
        print("")
        print("╒═════════════════╕")
        print("│   CO ROBISZ ?   │")
        print("╘═════════════════╛")
        print("1) Dzwonię po pomoc")
        if GirlHysteria != 1:
            print("2) Zabieram ją do szpitala")
            print("3) Zabieram ją na komisariat")
        else:
            print("2) Staram się ją zatrzymać")
        standard_menu_options()
        config.choice = input_number("Wybór > ")
        clear()

        if config.choice == 9:
            player.show_character_stats()

        if config.choice == 8 and player.ownedNotes:
            player.show_owned_notes()

        if config.choice == 3:
            take_girl_to_police()

        if config.choice == 2:
            if GirlHitByCar != 1:
                stop_the_girl()
            else:
                take_girl_to_hospital()

        if config.choice == 1:
            call_for_help()


def call_for_help():
    print_text('''Dzwonisz do swojego partnera Joela Krogga, który w momencie Twojego telefonu parzył sobie kolejną
kawę, aby nie zasnąć podczas jego nocnej zmiany na posterunku. Przekazujesz mu niezbędne informacje i prosisz o
załatwienie transportu. ''')

    print_text('''Gdy pomoc dociera na miejsce, dziewczyna zostaje przewieziona do szpitala, a Ciebie zabrano na
posterunek w celu ustalenia szczegółów zdarzenia.''')
    # TODO: Add further paragraphs
    the_end()


def take_girl_to_police():
    the_end()
    pass


def take_girl_to_hospital():
    if GirlHitByCar == 1:
        print_text('''Zabierasz przemarzniętą i nieprzytomną dziewczynę do samochodu i jedziesz do szpitala w
Stoksjö.''')
        time.sleep(config.sleepTime)
    print_text('''Podjeżdżasz pod szpital, parkujesz na miejscu dla pojazdów uprzywilejowanych. Wysiadasz i zabierasz
stojący obok wózek inwalidzki, aby posadzić na niego dziewczynę. Wchodzicie do szpitala i kierujecie się w stronę
recepcji.''')
    time.sleep(config.sleepTime)
    the_end()
