import random
from tabulate import tabulate
from utils.helpers import *


class Investigator(object):
    
    def __init__(self, name, age, sex, profession):
        self.name = name
        self.age = age
        self.sex = sex
        self.profession = profession

        # * CHAR STATS * #
        self.strength = 0
        self.dexterity = 0
        self.power = 0
        self.condition = 0
        self.appearance = 0
        self.education = 0
        self.size = 0
        self.intelligence = 0
        self.healthPoints = 0
        self.sanity = 0
        self.luck = 0
        self.magicPoints = 0
        self.damageBonus = 'Brak'
        self.build = 0

        # * SKILLS * #
        self.accounting = 5
        self.anthropology = 1
        self.appraise = 5
        self.archeology = 1
        self.artCraft = 5
        self.charm = 15
        self.climb = 20
        self.creditRating = 0
        self.cthulhuMythos = 0
        self.disguise = 5
        self.dodge = int(self.dexterity / 2)
        self.driveAuto = 20
        self.electricRepair = 10
        self.fastTalk = 5
        self.fightingBrawl = 25
        self.firearmsHandgun = 20
        self.firearmsRifle = 25
        self.firstAid = 30
        self.history = 5
        self.intimidate = 15
        self.jump = 20
        self.languageOwn = self.education
        self.languageOther = 1
        self.law = 5
        self.libraryUse = 20
        self.listen = 20
        self.locksmith = 1
        self.mechanicRepair = 10
        self.medicine = 1
        self.naturalWorld = 10
        self.navigate = 10
        self.occult = 5
        self.opHvMachine = 1
        self.persuade = 10
        self.pilot = 1
        self.psychology = 10
        self.psychoanalysis = 1
        self.ride = 5
        self.science = 1
        self.sleightOfHand = 10
        self.spotHidden = 25
        self.stealth = 20
        self.survival = 10
        self.swim = 20
        self.throw = 20
        self.track = 10

    # * CHAR STATS * #
    # self.Name = "Brida Fox"
    # self.Age = 30
    # self.Sex = "K"
    # self.Prof = "Komendant"

        self.selectedProblems = []
        self.handgunRounds = 0
        self.rifleRounds = 0
        self.ownedNotes = []  # ? Add ID's of notes to set them available to player

    def reset_stats_to_default(self):
        pass

    def create_character(self):
        self.selectedProblems = []
        random_new_character = input_text("Czy chesz stworzyć losową postać? T/n > ")
        if random_new_character == 'n':
            print()
            print("╒═════════════════╕")
            print("│    TWORZENIE    │")
            print("│     POSTACI     │")
            print("╘═════════════════╛")
            char_name = input_text("Jak się nazywasz (imię i nazwisko)? > ")
            self.name = char_name
            char_age = 100
            while 18 >= char_age >= 70:
                char_age = input_number("Ile masz lat? > ")
                if 18 >= char_age >= 70:
                    print("Podaj prawidłowy wiek")
            char_sex = ''
            while char_sex != 'k' and char_sex != 'm':
                char_sex = input_text("Twoja płeć? (M/K) > ")
            char_sex = char_sex.upper()
            self.sex = char_sex
            self.set_basic_stats()
            self.set_player_occupation_skills()
            self.set_random_investigator_problems()
        else:
            self.set_random_basic_stats()
            self.set_random_occupation_skills()
            self.set_random_investigator_problems()

    def set_basic_stats(self):
        skills_list = [
            self.strength, self.dexterity, self.power, self.condition, self.appearance, self.education, self.size,
            self.intelligence,
            self.healthPoints, self.sanity, self.luck, self.magicPoints, self.damageBonus, self.build
        ]
        stats_values = [40, 50, 50, 50, 60, 60, 70, 80]

        for i in range(len(stats_values)):
            local_choice = 0
            while local_choice < 1 or local_choice > 8:
                clear()
                self.update_basic_stats(skills_list)
                print("")
                print(f"Dostępne wartości: {stats_values}")
                print(f"Wartość do wstawienia: {BOLD}{stats_values[-1]}{NC}")
                print("")
                print("╒═════════════════╕")
                print("│     WYBIERZ     │")
                print("│   UMIEJĘTNOŚĆ   │")
                print("╘═════════════════╛")
                print("")
                local_choice = input_number("Wybór > ")
            skills_list[local_choice - 1] = stats_values.pop(-1)
        clear()

    def update_basic_stats(self, skills_list):
        self.strength = skills_list[0]
        self.dexterity = skills_list[1]
        self.power = skills_list[2]
        self.condition = skills_list[3]
        self.appearance = skills_list[4]
        self.education = skills_list[5]
        self.size = skills_list[6]
        self.intelligence = skills_list[7]

        self.healthPoints = int((self.size + self.condition) / 10)
        self.sanity = self.power
        self.luck = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 5
        self.magicPoints = int(self.power / 5)
        if self.power + self.size > 124:
            self.damageBonus = '+1K4'
            self.build = 1
        self.dodge = int(self.dexterity / 2)
        self.languageOwn = self.education

        skills_table = [
            ('1)', f'Siła [{BLUE}{self.strength}{NC}]'),
            ('2)', f'Zręczność [{BLUE}{self.dexterity}{NC}]'),
            ('3)', f'Moc [{BLUE}{self.power}{NC}]'),
            ('4)', f'Kondycja [{BLUE}{self.condition}{NC}]'),
            ('5)', f'Wygląd [{BLUE}{self.appearance}{NC}]'),
            ('6)', f'Wykształcenie [{BLUE}{self.education}{NC}]'),
            ('7)', f'Budowa ciała [{BLUE}{self.size}{NC}]'),
            ('8)', f'Inteligencja [{BLUE}{self.intelligence}{NC}]')
        ]
        print(tabulate(skills_table, tablefmt="pretty"))

    def set_player_occupation_skills(self):
        skills_list = [
            self.anthropology, self.archeology, self.firearmsRifle, self.firearmsHandgun, self.disguise, self.electricRepair,
            self.fastTalk, self.history, self.ride, self.languageOther, self.languageOwn, self.libraryUse,
            self.accounting, self.creditRating, self.mechanicRepair, self.medicine, self.listen, self.science, self.navigate,
            self.opHvMachine, self.occult, self.persuade, self.firstAid,
            self.pilot, self.swim, self.law, self.driveAuto, self.psychoanalysis, self.psychology, self.throw, self.jump,
            self.spotHidden, self.artCraft, self.survival, self.locksmith,
            self.track, self.stealth, self.dodge, self.charm, self.fightingBrawl, self.naturalWorld, self.climb,
            self.appraise,
            self.intimidate, self.sleightOfHand
        ]
        stats_values = [40, 40, 40, 50, 50, 50, 60, 60, 70]

        for i in range(len(stats_values)):
            local_choice = 0
            while local_choice < 1 or local_choice > 45:
                clear()
                self.update_occupation_skills(skills_list)
                print("")
                print(f"Dostępne wartości: {stats_values}")
                print(f"Wartość do wstawienia: {BOLD}{stats_values[-1]}{NC}")
                print("")
                print("╒═════════════════╕")
                print("│     WYBIERZ     │")
                print("│   UMIEJĘTNOŚĆ   │")
                print("╘═════════════════╛")
                print("")
                local_choice = input_number("Wybór > ")
            skills_list[local_choice - 1] = stats_values.pop(-1)
        clear()

    def update_occupation_skills(self, skills_list):
        self.anthropology = skills_list[0]
        self.archeology = skills_list[1]
        self.firearmsRifle = skills_list[2]
        self.firearmsHandgun = skills_list[3]
        self.disguise = skills_list[4]
        self.electricRepair = skills_list[5]
        self.fastTalk = skills_list[6]
        self.history = skills_list[7]
        self.ride = skills_list[8]
        self.languageOther = skills_list[9]
        self.languageOwn = skills_list[10]
        self.libraryUse = skills_list[11]

        self.accounting = skills_list[12]
        self.creditRating = skills_list[13]
        self.mechanicRepair = skills_list[14]
        self.medicine = skills_list[15]
        self.listen = skills_list[16]
        self.science = skills_list[17]
        self.navigate = skills_list[18]
        self.opHvMachine = skills_list[19]
        self.occult = skills_list[20]
        self.persuade = skills_list[21]
        self.firstAid = skills_list[22]
        self.pilot = skills_list[23]

        self.swim = skills_list[24]
        self.law = skills_list[25]
        self.driveAuto = skills_list[26]
        self.psychoanalysis = skills_list[27]
        self.psychology = skills_list[28]
        self.throw = skills_list[29]
        self.jump = skills_list[30]
        self.spotHidden = skills_list[31]
        self.artCraft = skills_list[32]
        self.survival = skills_list[33]
        self.locksmith = skills_list[34]
        self.track = skills_list[35]

        self.stealth = skills_list[36]
        self.dodge = skills_list[37]
        self.charm = skills_list[38]
        self.fightingBrawl = skills_list[39]
        self.naturalWorld = skills_list[40]
        self.climb = skills_list[41]
        self.appraise = skills_list[42]
        self.intimidate = skills_list[43]
        self.sleightOfHand = skills_list[44]

        skills_table = [
            (
            '1)', f'Antropologia [{BLUE}{self.anthropology}{NC}]', '13)', f'Księgowość [{BLUE}{self.accounting}{NC}]',
            '25)',
            f'Pływanie [{BLUE}{self.swim}{NC}]', '37)', f'Ukrywanie [{BLUE}{self.stealth}{NC}]'),
            ('2)', f'Archeologia [{BLUE}{self.archeology}{NC}]', '14)', f'Majętność [{BLUE}{self.creditRating}{NC}]',
             '26)',
             f'Prawo [{BLUE}{self.law}{NC}]', '38)', f'Unik [{BLUE}{self.dodge}{NC}]'),
            (
            '3)', f'Broń (Długa) [{BLUE}{self.firearmsRifle}{NC}]', '15)', f'Mechanika [{BLUE}{self.mechanicRepair}{NC}]',
            '27)',
            f'Prow. samoch. [{BLUE}{self.driveAuto}{NC}]', '39)', f'Urok osobisty [{BLUE}{self.charm}{NC}]'),
            (
            '4)', f'Broń (Krótka) [{BLUE}{self.firearmsHandgun}{NC}]', '16)', f'Medycyna [{BLUE}{self.medicine}{NC}]',
            '28)',
            f'Psychoanaliza [{BLUE}{self.psychoanalysis}{NC}]', '40)',
            f'Walka wręcz [{BLUE}{self.fightingBrawl}{NC}]'),
            ('5)', f'Charakteryzacja [{BLUE}{self.disguise}{NC}]', '17)', f'Nasłuchiwanie [{BLUE}{self.listen}{NC}]',
             '29)',
             f'Psychologia [{BLUE}{self.psychology}{NC}]', '41)',
             f'Wiedza o Naturze [{BLUE}{self.naturalWorld}{NC}]'),
            ('6)', f'Elektryka [{BLUE}{self.electricRepair}{NC}]', '18)', f'Nauka [{BLUE}{self.science}{NC}]', '30)',
             f'Rzucanie [{BLUE}{self.throw}{NC}]', '42)', f'Wspinaczka [{BLUE}{self.climb}{NC}]'),
            ('7)', f'Gadanina [{BLUE}{self.fastTalk}{NC}]', '19)', f'Nawigacja [{BLUE}{self.navigate}{NC}]', '31)',
             f'Skakanie [{BLUE}{self.jump}{NC}]', '43)', f'Wycena [{BLUE}{self.appraise}{NC}]'),
            ('8)', f'Historia [{BLUE}{self.history}{NC}]', '20)', f'Obsł. cież. sprz. [{BLUE}{self.opHvMachine}{NC}]',
             '32)',
             f'Spostrzegawczość [{BLUE}{self.spotHidden}{NC}]', '44)', f'Zastraszanie [{BLUE}{self.intimidate}{NC}]'),
            ('9)', f'Jeździectwo [{BLUE}{self.ride}{NC}]', '21)', f'Okultyzm [{BLUE}{self.occult}{NC}]', '33)',
             f'Sztuka/Rzemiosło [{BLUE}{self.artCraft}{NC}]', '45)',
             f'Zręczne palce [{BLUE}{self.sleightOfHand}{NC}]'),
            ('10)', f'Język Obcy [{BLUE}{self.languageOther}{NC}]', '22)', f'Perswazja [{BLUE}{self.persuade}{NC}]',
             '34)',
             f'Sztuka przetrw. [{BLUE}{self.survival}{NC}]', '', ''),
            ('11)', f'Jezyk Ojczysty [{BLUE}{self.languageOwn}{NC}]', '23)',
             f'Pierwsza pomoc [{BLUE}{self.firstAid}{NC}]',
             '35)', f'Ślusarstwo [{BLUE}{self.locksmith}{NC}]', '', ''),
            ('12)', f'Korzystanie z bibl. [{BLUE}{self.libraryUse}{NC}]', '24)',
             f'Pilotowanie [{BLUE}{self.pilot}{NC}]',
             '36)', f'Tropienie [{BLUE}{self.track}{NC}]', '', '')
        ]
        print(tabulate(skills_table, tablefmt="pretty"))

    def set_random_basic_stats(self):
        stats_values = [40, 50, 50, 50, 60, 60, 70, 80]
        used_elems = []
        for i in range(len(stats_values)):
            selected_val = random.randint(0, len(stats_values) - 1)
            used_elems.append(stats_values.pop(selected_val))
        self.strength = used_elems[0]
        self.dexterity = used_elems[1]
        self.power = used_elems[2]
        self.condition = used_elems[3]
        self.appearance = used_elems[4]
        self.education = used_elems[5]
        self.size = used_elems[6]
        self.intelligence = used_elems[7]
        self.healthPoints = int((self.size + self.condition) / 10)
        self.sanity = self.power
        self.luck = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 5
        self.magicPoints = int(self.power / 5)
        if self.power + self.size > 124:
            self.damageBonus = '+1K4'
            self.build = 1
        self.dodge = int(self.dexterity / 2)
        self.languageOwn = self.education

    def set_random_occupation_skills(self):
        stats_values = [40, 40, 40, 50, 50, 50, 60, 60, 70]
        used_elems = []
        for i in range(len(stats_values)):
            selected_val = random.randint(0, len(stats_values) - 1)
            used_elems.append(stats_values.pop(selected_val))
        self.artCraft = used_elems[0]
        self.firearmsHandgun = used_elems[1]
        self.law = used_elems[2]
        self.listen = used_elems[3]
        self.charm = used_elems[4]
        self.psychology = used_elems[5]
        self.spotHidden = used_elems[6]
        self.track = used_elems[7]
        self.creditRating = used_elems[8]

    def set_random_investigator_problems(self):
        problem_1 = random.randint(0, 9)
        problem_2 = problem_1
        while problem_2 == problem_1:
            problem_2 = random.randint(0, 9)
        self.selectedProblems.append(self.problems[problem_1])
        self.selectedProblems.append(self.problems[problem_2])

    def show_character_stats(self):
        char_data = [
            ('Siła', self.strength, 'Antropologia', self.anthropology, 'Księgowość', self.accounting, 'Pilotowanie',
             self.pilot,
             'Tropienie', self.track),
            ('Zręczność', self.dexterity, 'Archeologia', self.archeology, 'Majętność', self.creditRating, 'Pływanie',
             self.swim,
             'Ukrywanie', self.stealth),
            ('Moc', self.power, 'Broń (Długa)', self.firearmsRifle, 'Mechanika', self.mechanicRepair, 'Prawo', self.law,
             'Unik',
             self.dodge),
            ('Kondycja', self.condition, 'Broń (Krótka)', self.firearmsHandgun, 'Medycyna', self.medicine,
             'Prow. samoch.',
             self.driveAuto, 'Urok osobisty', self.charm),
            ('Wygląd', self.appearance, 'Charakteryzacja', self.disguise, 'Mity Cthulhu', self.cthulhuMythos,
             'Psychoanaliza',
             self.psychoanalysis, 'Walka wręcz', self.fightingBrawl),
            (
            'Wykształcenie', self.education, 'Elektryka', self.electricRepair, 'Nasłuchiwanie', self.listen, 'Psychologia',
            self.psychology, 'Wiedza o Naturze', self.naturalWorld),
            ('Budowa ciała', self.size, 'Gadanina', self.fastTalk, 'Nauka', self.science, 'Rzucanie', self.throw,
             'Wspinaczka',
             self.climb),
            ('Inteligencja', self.intelligence, 'Historia', self.history, 'Nawigacja', self.navigate, 'Skakanie',
             self.jump,
             'Wycena', self.appraise),
            ('Punkty życia', self.healthPoints, 'Jeździectwo', self.ride, 'Obsł. cież. sprz.', self.opHvMachine,
             'Spostrzegawczość',
             self.spotHidden, 'Zastraszanie', self.intimidate),
            (
                'Punkty poczytalności', self.sanity, 'Język Obcy', self.languageOther, 'Okultyzm', self.occult,
                'Sztuka/Rzemiosło',
                self.artCraft, 'Zręczne palce', self.sleightOfHand),
            ('Punkty szczęścia', self.luck, 'Jezyk Ojczysty', self.languageOwn, 'Perswazja', self.persuade,
             'Sztuka przetrw.',
             self.survival, '', ''),
            ('Punkty mocy', self.magicPoints, 'Korzystanie z bibl.', self.libraryUse, 'Pierwsza pomoc', self.firstAid,
             'Ślusarstwo',
             self.locksmith, '', '')
        ]

        headers = [self.name + ' (' + self.sex + ')', 'Lat ' + str(self.age), 'Profesja: ' + self.profession, '',
                   'Modyfikator obr.',
                   self.damageBonus, 'Krzepa', str(self.build), 'Ruch', '-']

        print(f'{BOLD}Statystyki Twojej postaci{NC}:')
        print(tabulate(char_data, headers, tablefmt="pretty"))
        print(f'{BOLD}Przymioty postaci{NC}:	', end='')
        for item in self.selectedProblems:
            print(item + '; ', end='')
        print()
        print(f'{BOLD}Wyposażenie{NC}:		', end='')
        for item in self.equipment:
            print(item + ', ', end='')
        if self.handgunRounds > 0:
            print(f"\n{BOLD}Naboje do pistoletu{NC} - " + str(self.handgunRounds))
        if self.rifleRounds > 0:
            print(f"\n{BOLD}Naboje do strzelby{NC} - " + str(self.rifleRounds))
        print('\n')

    problems = ["Uzależniona od papierosów", "Uzależniona od alkoholu", "Uzależniona od hazardu",
                "Ma problemy finansowe",
                "Współmałżonek odszedł lub zmarł kilka lat temu", "Samotnie wychowuje krnąbrne dziecko",
                "Ma problem ze zdrowiem",
                "Opiekuje się niesamodzielnym rodzicem", "Skrywa przeszłość kryminalną i jest szantażowana",
                "Nękana przez kolegów przestępcy, którego wsadziła do więzienia"]
    equipment = ["Kajdanki", "Zapalniczka"]
