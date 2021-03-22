import random
from utils.constants import *


def test_skill(skill_name, skill_value):
    roll = random.randint(1, 100)
    print(f"Test {skill_name} ({skill_value}) - Wyrzuciłeś {roll}")
    if roll == 1:
        print(f"{BGREEN}{ITALIC}Krytyczny Sukces{NC}")
        return 4
    elif roll <= (skill_value / 5):
        print(f"{GREEN}{ITALIC}Ekstremalny Sukces{NC}")
        return 3
    elif roll <= (skill_value / 2):
        print(f"{GREEN}{ITALIC}Trudny Sukces{NC}")
        return 2
    elif roll <= skill_value:
        print(f"{GREEN}{ITALIC}Sukces{NC}")
        return 1
    elif roll > skill_value:
        if roll != 100:
            print(f"{RED}{ITALIC}Porażka{NC}")
            return 0
        else:
            print(f"{BRED}{ITALIC}Krytyczna Porażka{NC}")
            return -1


def test_skills(skill_name, skills_list):
    roll = random.randint(1, 100)
    skills_list.sort()
    skill_value = skills_list[-1]
    print(f"Test {skill_name} ({skill_value}) - Wyrzuciłeś {roll}")
    if roll == 1:
        print(f"{BGREEN}{ITALIC}Krytyczny Sukces{NC}")
        return 4
    elif roll <= (skill_value / 5):
        print(f"{GREEN}{ITALIC}Ekstremalny Sukces{NC}")
        return 3
    elif roll <= (skill_value / 2):
        print(f"{GREEN}{ITALIC}Trudny Sukces{NC}")
        return 2
    elif roll <= skill_value:
        print(f"{GREEN}{ITALIC}Sukces{NC}")
        return 1
    elif roll > skill_value:
        if roll != 100:
            print(f"{RED}{ITALIC}Porażka{NC}")
            return 0
        else:
            print(f"{BRED}{ITALIC}Krytyczna Porażka{NC}")
            return -1
