#!/usr/bin/env bash

clear
trap 'echo " - Aby wyjść ze skryptu naciśnij Q."' SIGINT SIGTERM SIGTSTP

GAME_LOGO=$(cat << "EOF"
#                                                                       
#                                ,,    ,,                  ,...         
#            .g8"""bgd         `7MM  `7MM                .d' ""         
#          .dP'     `M           MM    MM                dM`            
#          dM'       ` ,6"Yb.    MM    MM       ,pW"Wq. mMMmm           
#          MM         8)   MM    MM    MM      6W'   `Wb MM             
#          MM.         ,pm9MM    MM    MM      8M     M8 MM             
#          `Mb.     ,'8M   MM    MM    MM      YA.   ,A9 MM             
#            `"bmmmd' `Moo9^Yo..JMML..JMML.     `Ybmd9'.JMML.           
#                      ,,                    ,,    ,,                   
#    .g8"""bgd  mm   `7MM                  `7MM  `7MM     `7MMF'   `7MF'
#  .dP'     `M  MM     MM                    MM    MM       MM       M  
#  dM'       `mmMMmm   MMpMMMb.`7MM  `7MM    MM    MMpMMMb. MM       M  
#  MM           MM     MM    MM  MM    MM    MM    MM    MM MM       M  
#  MM.          MM     MM    MM  MM    MM    MM    MM    MM MM       M  
#  `Mb.     ,'  MM     MM    MM  MM    MM    MM    MM    MM YM.     ,M  
#    `"bmmmd'   `Mbmo.JMML  JMML.`Mbod"YML..JMML..JMML  JMML.`bmmmmd"'  
#             ___          _             _ _ _   _                      
#            | _ ) __ _ __| |_    ___ __| (_) |_(_)___ _ _              
#            | _ \/ _` (_-< ' \  / -_) _` | |  _| / _ \ ' \             
#            |___/\__,_/__/_||_| \___\__,_|_|\__|_\___/_||_|            
#                                                                       
EOF
)

## COLOR VARS ##
LRED='\033[1;31m'
RED='\033[0;31m'
LGREEN=='\033[1;32m'
GREEN='\033[0;32m'
LBLUE=='\033[1;34m'
BLUE='\033[0;34m'
ORANGE='\033[0;33m'
LGRAY='\033[0;37m'
DGRAY='\033[1;30m'
NC='\033[0m'

## APP VARS ##
APP_VER_NO=0.1
SLEEP_TIME=2

## GAME FLAGS ##
# CHAR STATS #
CHAR_NAME="Brida Fox"
CHAR_AGE=30
CHAR_SEX="K"
CHAR_PROF="Komendant"
CHAR_STRENGTH=0
CHAR_DEXTERITY=0
CHAR_POWER=0
CHAR_CONDITION=0
CHAR_APPERANCE=0
CHAR_EDUCATION=0
CHAR_SIZE=0
CHAR_INTELIGENCE=0
CHAR_HP=0
CHAR_INSANE=0
CHAR_LUCK=0
CHAR_MP=0
# SKILLS #
CHAR_ACCOUNTING=5
CHAR_ANTHROPOLOGY=1
CHAR_APPRAISE=5
CHAR_ARCHEOLOGY=1
CHAR_ART_CRAFT=5
CHAR_CHARM=15
CHAR_CLIMB=20
CHAR_CREDIT_RATING=0
CHAR_CTHULHU_MYTHOS=0
CHAR_DISGUISE=5
CHAR_DODGE=$(($CHAR_DEXTERITY/2))
CHAR_DRIVE_AUTO=20
CHAR_ELEC_REPAIR=10
CHAR_FAST_TALK=5
CHAR_FIGHTING_BRAWL=25
CHAR_FIREARMS_HANDGUN=20
CHAR_FIREARMS_RIFLE=25
CHAR_FIRST_AID=30
CHAR_HISTORY=5
CHAR_INTIMIDATE=15
CHAR_JUMP=20
CHAR_LANGUAGE_OWN=$CHAR_EDUCATION
CHAR_LANGUAGE_OTHER=1
CHAR_LAW=5
CHAR_LIBRARY_USE=20
CHAR_LISTEN=20
CHAR_LOCKSMITH=1
CHAR_MECH_REPAIR=10
CHAR_MEDICINE=1
CHAR_NATURAL_WORLD=10
CHAR_NAVIGATE=10
CHAR_OCCULT=5
CHAR_OP_HV_MACHINE=1
CHAR_PERSUADE=10
CHAR_PILOT=1
CHAR_PSYCHOLOGY=10
CHAR_PSYCHOANALYSIS=1
CHAR_RIDE=5
CHAR_SCIENCE=1
CHAR_SLEIGHT_OF_HAND=10
CHAR_SPOT_HIDDEN=25
CHAR_STEALH=20
CHAR_SURVIVAL=10
CHAR_SWIM=20
CHAR_THROW=20
CHAR_TRACK=10

# VALUES #
ROLL=0

# WHAT CHAR KNOW #
GIRL_KILLED=0

## HELPER FUNCTIONS ##
function printTable()
{
    local -r delimiter="${1}"
    local -r data="$(removeEmptyLines "${2}")"

    if [[ "${delimiter}" != '' && "$(isEmptyString "${data}")" = 'false' ]]
    then
        local -r numberOfLines="$(wc -l <<< "${data}")"

        if [[ "${numberOfLines}" -gt '0' ]]
        then
            local table=''
            local i=1

            for ((i = 1; i <= "${numberOfLines}"; i = i + 1))
            do
                local line=''
                line="$(sed "${i}q;d" <<< "${data}")"

                local numberOfColumns='0'
                numberOfColumns="$(awk -F "${delimiter}" '{print NF}' <<< "${line}")"

                # Add Line Delimiter

                if [[ "${i}" -eq '1' ]]
                then
                    table="${table}$(printf '%s#+' "$(repeatString '#+' "${numberOfColumns}")")"
                fi

                # Add Header Or Body

                table="${table}\n"

                local j=1

                for ((j = 1; j <= "${numberOfColumns}"; j = j + 1))
                do
                    table="${table}$(printf '#| %s' "$(cut -d "${delimiter}" -f "${j}" <<< "${line}")")"
                done

                table="${table}#|\n"

                # Add Line Delimiter

                if [[ "${i}" -eq '1' ]] || [[ "${numberOfLines}" -gt '1' && "${i}" -eq "${numberOfLines}" ]]
                then
                    table="${table}$(printf '%s#+' "$(repeatString '#+' "${numberOfColumns}")")"
                fi
            done

            if [[ "$(isEmptyString "${table}")" = 'false' ]]
            then
                echo -e "${table}" | column -s '#' -t | awk '/^\+/{gsub(" ", "-", $0)}1'
            fi
        fi
    fi
}

function removeEmptyLines()
{
    local -r content="${1}"

    echo -e "${content}" | sed '/^\s*$/d'
}

function repeatString()
{
    local -r string="${1}"
    local -r numberToRepeat="${2}"

    if [[ "${string}" != '' && "${numberToRepeat}" =~ ^[1-9][0-9]*$ ]]
    then
        local -r result="$(printf "%${numberToRepeat}s")"
        echo -e "${result// /${string}}"
    fi
}

function isEmptyString()
{
    local -r string="${1}"

    if [[ "$(trimString "${string}")" = '' ]]
    then
        echo 'true' && return 0
    fi

    echo 'false' && return 1
}

function trimString()
{
    local -r string="${1}"

    sed 's,^[[:blank:]]*,,' <<< "${string}" | sed 's,[[:blank:]]*$,,'
}

function get_random_number() { # from ($1) - to ($2)
	jot -r 1 $1 $2
	# shuf -i $1-$2 -n 1
}

## FUNCTIONS ##
function create_caracter() {
	read -p "Czy chesz stworzyć losową postać? Y/n " RANDOM_STATS
	case $RANDOM_STATS in
		[nN] | [nN][oO])
			echo ""
			echo "-------------------"
			echo " TWORZENIE POSTACI "
			echo "-------------------"
			read -p "Jak się nazywasz? > " CHAR_NAME
			read -p "Ile masz lat? > " CHAR_AGE
			read -p "Twoja płeć? (M/K) > " CHAR_SEX
			set_random_stats
		;;
		*)
			set_random_stats
		;;
	esac
}

function set_random_stats() {
	CHAR_STRENGTH=$(get_random_number 0 99)
	CHAR_DEXTERITY=$(get_random_number 0 99)
	CHAR_POWER=$(get_random_number 0 99)
	CHAR_CONDITION=$(get_random_number 0 99)
	CHAR_APPERANCE=$(get_random_number 0 99)
	CHAR_EDUCATION=$(get_random_number 0 99)
	CHAR_SIZE=$(get_random_number 0 99)
	CHAR_INTELIGENCE=$(get_random_number 0 99)
	CHAR_HP=$(get_random_number 0 99)
	CHAR_INSANE=$(get_random_number 0 99)
	CHAR_LUCK=$(get_random_number 0 99)
	CHAR_MP=$(get_random_number 0 99)
}

function show_character_stats() {
	echo -e "\nStatystyki Twojej postaci"
	printTable ',' \
"$CHAR_NAME ($CHAR_SEX),Lat $CHAR_AGE,Profesja: $CHAR_PROF,,Modyfikator obr.,0,Krzepa,0,,
Siła,$CHAR_STRENGTH,Antropologia,$CHAR_ANTHROPOLOGY,Księgowość,$CHAR_ACCOUNTING,Pilotowanie,$CHAR_PILOT,Tropienie,$CHAR_TRACK
Zręczność,$CHAR_DEXTERITY,Archeologia,$CHAR_ARCHEOLOGY,Majętność,$CHAR_CREDIT_RATING,Pływanie,$CHAR_SWIM,Ukrywanie,$CHAR_STEALH
Moc,$CHAR_POWER,Broń (Długa),$CHAR_FIREARMS_RIFLE,Mechanika,$CHAR_MECH_REPAIR,Prawo,$CHAR_LAW,Unik,$CHAR_DODGE
Kondycja,$CHAR_CONDITION,Broń (Krótka),$CHAR_FIREARMS_HANDGUN,Medycyna,$CHAR_MEDICINE,Prow. samoch.,$CHAR_DRIVE_AUTO,Urok osobisty,$CHAR_CHARM
Wygląd,$CHAR_APPERANCE,Charakteryzacja,$CHAR_DISGUISE,Mity Cthulhu,$CHAR_CTHULHU_MYTHOS,Psychoanaliza,$CHAR_PSYCHOANALYSIS,Walka wręcz,$CHAR_FIGHTING_BRAWL
Wykształcenie,$CHAR_EDUCATION,Elektryka,$CHAR_ELEC_REPAIR,Nasłuchiwanie,$CHAR_LISTEN,Psychologia,$CHAR_PSYCHOLOGY,Wiedza o Naturze,$CHAR_NATURAL_WORLD
Budowa ciała,$CHAR_SIZE,Gadanina,$CHAR_FAST_TALK,Nauka,$CHAR_SCIENCE,Rzucanie,$CHAR_THROW,Wspinaczka,$CHAR_CLIMB
Inteligencja,$CHAR_INTELIGENCE,Historia,$CHAR_HISTORY,Nawigacja,$CHAR_NAVIGATE,Skakanie,$CHAR_JUMP,Wycena,$CHAR_APPRAISE
Punkty życia,$CHAR_HP,Jeździectwo,$CHAR_RIDE,Obsł. cież. sprz.,$CHAR_OP_HV_MACHINE,Spostrzegawczość,$CHAR_SPOT_HIDDEN,Zastraszanie,$CHAR_INTIMIDATE
Punkty szaleństwa,$CHAR_INSANE,Język Obcy,$CHAR_LANGUAGE_OTHER,Okultyzm,$CHAR_OCCULT,Sztuka/Rzemiosło,$CHAR_ART_CRAFT,Zręczne palce,$CHAR_SLEIGHT_OF_HAND
Punkty szczęścia,$CHAR_LUCK,Jezyk Ojczysty,$CHAR_LANGUAGE_OWN,Perswazja,$CHAR_PERSUADE,Sztuka przetrw.,$CHAR_SURVIVAL,,
Punkty mocy,$CHAR_MP,Korzystanie z bibl.,$CHAR_LIBRARY_USE,Pierwsza pomoc,$CHAR_FIRST_AID,Ślusarstwo,$CHAR_LOCKSMITH,,"
}

function test_skill() { # SKILL_NAME ($1), DIFFICULTY_LVL ($2)
	SKILL_NAME=$1
	DIFFICULTY_LVL=$2
	ROLL=$(get_random_number 0 100)
	echo "Test $1 - Wyrzuciłeś $ROLL"
	[ $ROLL -le $2 ] && echo -e "${GREEN}Sukces${NC}"
	[ $ROLL -gt $2 ] && echo -e "${RED}Porażka${NC}"
}

## SCENES ##
function intro() {
	echo -e "$GAME_LOGO" | lolcat
	[ ! -z $1 ] && sleep 0.5s
	echo -e "\n${LGRAY}Developer - ${ORANGE}Jakub Michniewicz"
	[ ! -z $1 ] && sleep 0.5s
	echo -e "${LGRAY}Wersja - ${LRED}${APP_VER_NO}${NC}"
	[ ! -z $1 ] && sleep 0.5s
}

function initiate_history() {
	echo ""
	echo -e "Stoksjö to liczące zaledwie 2 tys. mieszkańców miasteczko położone w centrum prowincji
o nazwie Helbjerg, w którym pełnisz rolę komendanta małego posterunku policji."
	sleep $SLEEP_TIME
	echo -e "\nJest 12 lutego 2020 r. Wracasz późną nocą autem z oddalonego o przeszło 80 km miasta,
w którym składałeś zeznania przed sądem. Na wąskiej, nierozjeżdżonej drodze biegnącej
dnem kotliny między dwoma porośniętymi ciemnym lasem wzgórzami leży śnieg."
	sleep $SLEEP_TIME
	echo -e "\nNiespodziewanie, wyjeżdżając zza zakrętu, dostrzegasz w światłach samochodu
sylwetkę dziewczyny, słaniającej się na bosych nogach poboczem w kierunku miasta,
która za chwilę wejdzie pod koła Twojego pojazdu."
	sleep $SLEEP_TIME
	while (( CHOICE != 0 && CHOICE != 2 )); do
		echo ""
		echo "-------------------"
		echo "    CO ROBISZ ?    "
		echo "-------------------"
		echo "1) Staram się ją ominąć"
		echo "2) Jadę dalej - tylko mi się to wydaje"
		echo "9) Pokaż statystyki mojej postaci"
		echo "0) Powrót do menu"
		read -p "Wybór > " CHOICE
		clear

		if [ "$CHOICE" == 9 ]; then
			show_character_stats
		fi

		if [ "$CHOICE" == 2 ]; then
			echo "Dziewczyna umiera potrącona przez Ciebie..."
			sleep $SLEEP_TIME
			echo -e "\n### KONIEC ###\n"
			read -p "Wciśnij Enter aby kontynuować... "
			CHOICE=0
			clear
		fi

		if [ "$CHOICE" == 1 ]; then
			test_skill "Prowadzenia samochodu" $CHAR_DRIVE_AUTO
		fi
	done
}

# SHOW MAIN MENU #
intro true

while [ "$CHOICE" != "Q" ] && [ "$CHOICE" != "q" ]; do
	[ ! -z $CHOICE ] && intro
	echo ""
	echo "-------------------"
	echo "    MENU GŁÓWNE    "
	echo "-------------------"
	echo "1) Rozpocznij grę"
	echo -e "2) ${DGRAY}Wczytaj grę${NC}"
	echo "3) O grze"
	echo "4) Ustawienia"
	echo "Q) Wyjście"
	read -p "Wybór > " CHOICE
	clear

	if [ "$CHOICE" == 3 ]; then
		while [ "$CHOICE" != 0 ]; do
			echo "------------------"
			echo "      O GRZE      "
			echo "------------------"
			echo -e "${ORANGE}Autor projektu:${NC}	Jakub Michniewicz"
			echo -e "${ORANGE}Scenariusz:${NC}	Asia Wiewiórska"
			echo -e "\n${ORANGE}'DRUGA'${NC}
Scenariusz ten inspirowany jest ponurymi skandynawskimi powieściami i serialami,
w których główne role odgrywają tajemnica, społeczność i śledztwo. Konwencja ta
znana jest pod nazwą nordic-noir, lecz scenariusz nawiązuje również do znanych baśni
ludowych i Lovecraftowskiej Krainy Snów. Akcja gry rozpoczyna się w lutym 2020 r.
gdzieś w Skandynawii. Oniryczny nastrój buduje tu odosobnione miasteczko otoczone przez
wzgórza i ciemne lasy oraz surowa, choć urokliwa zimowa aura. To bardzo subtelna historia,
która nie jest opowieścią akcji."
			
			echo -e "\n0) Powrót"
			read -p "Wybór > " CHOICE
			clear
		done
	fi

	if [ "$CHOICE" == 4 ]; then
		while [ "$CHOICE" != 0 ]; do
			echo ""
			echo "------------------"
			echo "    USTAWIENIA    "
			echo "------------------"
			echo -e "1) Czas pomiędzy akapitami"
			echo -e "2) Przywróc ustawienia domyślne"
			echo "0) Powrót"
			read -p "Wybór > " CHOICE
			clear

			if [ "$CHOICE" == 1 ]; then
				echo "Aktualna wartość: ${SLEEP_TIME}s"
				echo "(pozostaw puste aby nie zmieniać)"
				read -p "Podaj nowy czas w sekundach: " NEW_TIME
				if [ "$NEW_TIME" != "" ]; then
					SLEEP_TIME=$NEW_TIME
				fi
			fi

			if [ "$CHOICE" == 2 ]; then
				SLEEP_TIME=2
				echo "Przywrócono ustawienia domyślne"
			fi
		done
	fi

	if [ "$CHOICE" == 1 ]; then
		create_caracter
		clear
		show_character_stats

		while [ "$CHOICE" != 0 ]; do
			echo ""
			echo "------------------"
			echo "     NOWA GRA     "
			echo "------------------"
			echo "1) Graj tą postacią"
			echo "2) Utwórz nową postać"
			echo "9) Pokaż statystyki mojej postaci"
			echo "0) Powrót"
			read -p "Wybór > " CHOICE
			clear

			if [ "$CHOICE" == 9 ]; then
				show_character_stats
			fi

			if [ "$CHOICE" == 2 ]; then
				create_caracter
				show_character_stats
			fi

			if [ "$CHOICE" == 1 ]; then
				initiate_history
			fi
		done
	fi

done