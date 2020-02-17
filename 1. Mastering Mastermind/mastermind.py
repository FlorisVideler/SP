import random, ast
import mastermindalgo
import feedback as fb

colors = [
    {
        "Kleur": "Groen",
        # "Afkorting": "G"
        "Afkorting": "1"
    },
    {
        "Kleur": "Rood",
        # "Afkorting": "R"
        "Afkorting": "2"
    },
    {
        "Kleur": "Blauw",
        "Afkorting": "3"
        # "Afkorting": "B"
    },
    {
        "Kleur": "Oranje",
        # "Afkorting": "O"
        "Afkorting": "4"
    },
    {
        "Kleur": "Wit",
        # "Afkorting": "W"
        "Afkorting": "5"
    },
    {
        "Kleur": "Paars",
        "Afkorting": "6"
        # "Afkorting": "P"
    }
]

code_global = []


def menu():
    print("Welkom to mastermind!")
    gives_feedback = "n"
    pcstrat = "n"
    while True:
        who_is_playing = input("Raadt de speler? (y/n) ")
        if who_is_playing.lower() == "y":
            break
        elif who_is_playing.lower() == "n":
            while True:
                gives_feedback = input("Geeft de pc feedback? (y/n) ")
                if gives_feedback.lower() == "y" or gives_feedback.lower() == "n":
                    if gives_feedback.lower() == "n":
                        gives_feedback = "y"
                    else:
                        gives_feedback = "n"
                break
            pcstrat = input("algoritme moet de pc gebruiken? ")
            break
    return who_is_playing, gives_feedback, pcstrat


def player_game():
    board = ""
    steps = 0
    # Set code
    code = []
    for i in range(0, 4):
        code.append(colors[random.randint(0, 5)]["Afkorting"])
    # code = random.sample(colors, k=4)
    # tmpcode = []
    # for i in code:
    #     tmpcode.append(i["Afkorting"])
    # code = tmpcode
    print(code)
    while True:
        try:
            print(
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n=========================================================")
            print(board)
            guess_input = input("Doe een gok: ")
            guess_list = guess_input.upper().replace(" ", "").split(",")
            # print(guess_list)
            guess_response = fb.auto_feedback(guess_list, code)
            steps += 1
            right_color_str = ""
            if guess_response[0] > 0:
                right_color_str = "?" * guess_response[0]
            right_place_str = ""
            if guess_response[1] > 0:
                right_place_str = "!" * guess_response[1]
            board += "{:^10} {:^10} {:^10} {:^10} || {:^10} {:^10}\n".format(guess_list[0], guess_list[1],
                                                                             guess_list[2], guess_list[3],
                                                                             right_place_str, right_color_str)
            if guess_response[1] == 4:
                print(f"WINNER WINNER CHICKEN DINNER.\nJE HEBT DE CODE GERADEN IN {steps} STAPPEN!")
                break
        except Exception as ex:
            print("GEEN GELDIGE INPUT!")
        # try:
        #     guess_list = guess_input.upper().replace(" ", "").split(",")
        #     # print(guess_list)
        #     guess_response = auto_feedback(guess_list, code)
        #     steps += 1
        #     right_color_str = ""
        #     if guess_response[0] > 0:
        #         right_color_str = "?" * guess_response[0]
        #     right_place_str = ""
        #     if guess_response[1] > 0:
        #         right_place_str = "!" * guess_response[1]
        #     board += "{:^10} {:^10} {:^10} {:^10} || {:^10} {:^10}\n".format(guess_list[0], guess_list[1],
        #                                                                      guess_list[2], guess_list[3],
        #                                                                      right_place_str, right_color_str)
        #     if guess_response[1] == 4:
        #         print(f"WINNER WINNER CHICKEN DINNER.\nJE HEBT DE CODE GERADEN IN {steps} STAPPEN!")
        #         break
        #     # print(guess_response)
        # except Exception as ex:
        #     print("GEEN GELDIGE INPUT!")
        #     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        #     message = template.format(type(ex).__name__, ex.args)
        #     print(message)


def pc_game(feedback, strat):
    manual_feedback = False
    if feedback == "y":
        manual_feedback = True
    board = ""
    steps = 0
    code = input("Verzin een code: ").upper().replace(" ", "").split(",")
    plausible_codes = []
    for a in colors:
        for b in colors:
            for c in colors:
                for d in colors:
                    plausible_codes.append([a["Afkorting"], b["Afkorting"], c["Afkorting"], d["Afkorting"]])
    n = 0
    feedback = 0, 0
    while True:
        print(board)
        if strat == "simple":
            if n > 0:
                plausible_codes = mastermindalgo.simple_algortime(plausible_codes, feedback, guess_list)
            else:
                n += 1
            guess_list = random.choice(plausible_codes)
        elif strat == "worstcase":
            if n > 0:
                plausible_codes = mastermindalgo.simple_algortime(plausible_codes, feedback, guess_list)
            else:
                n += 1
                #Best guess based on expected size
            guess_list = mastermindalgo.best_worstcase_algortime(plausible_codes)

        elif strat == "zelfbedacht":
            if n > 0:
                plausible_codes = mastermindalgo.selfmade_algortime(plausible_codes, feedback, guess_list)
            else:
                n += 1
                #Best guess based on expected size
            guess_list = plausible_codes[0]

        elif strat == "random":
            guess_list = mastermindalgo.random_guess(colors)

        if manual_feedback:
            guess_response = fb.manual_feedback(guess_list, code)
            feedback = guess_response
        else:
            guess_response = fb.auto_feedback(guess_list, code)
            feedback = guess_response

        steps += 1
        right_color_str = ""
        if guess_response[0] > 0:
            right_color_str = "?" * guess_response[0]
        right_place_str = ""
        if guess_response[1] > 0:
            right_place_str = "!" * guess_response[1]
        print(guess_list)
        board += "{:^10} {:^10} {:^10} {:^10} || {:^10} {:^10}\n".format(guess_list[0], guess_list[1],
                                                                         guess_list[2], guess_list[3],
                                                                         right_place_str, right_color_str)
        if guess_response[1] == 4:
            print(board)
            print(f"WINNER WINNER CHICKEN DINNER.\nJE HEBT DE CODE GERADEN IN {steps} STAPPEN!")
            break






# def set_code(code):
#     code.clear()
#     code_global = code
#     # for i in code:
#     #     code_global.append(i["Afkorting"])
#     print("Code is set!")
#     print(code_global)

def explain():
    for c in colors:
        print(f'{c["Kleur"]} = {c["Afkorting"]}')


def game():
    explain()
    settings = menu()
    if settings[0] == "y":
        player_game()
    if settings[0] == "n":
        pc_game(settings[1], settings[2])


game()
