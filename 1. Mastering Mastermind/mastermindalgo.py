import feedback as fb
import ast, random


# Basicly just do a random guess, pretty easy
def random_guess(colors):
    guess_list = []
    for i in range(0, 4):
        guess_list.append(colors[random.randint(0, 5)])
    return guess_list


# uses the simple strategy from YET ANOTHER MASTERMIND STRATEGY by Barteld Kooi
def simple_algorithm(possible_combis, feedback, guess):
    print(len(possible_combis), " left before")
    new_list = []
    for i in possible_combis:
        if fb.auto_feedback(guess, i) == feedback:
            new_list.append(i)
    print(len(new_list), " left after")
    return new_list


# Uses the worst case strategy from YET ANOTHER MASTERMIND STRATEGY by Barteld Kooi
# First run takes some time
def best_worstcase_algorithm(possible_combis):
    worst_dict = {}
    for i in possible_combis:
        worst_dict[f"{i}"] = []
        for j in possible_combis:
            feedback = fb.auto_feedback(i, j)
            worst_dict[f"{i}"].append(feedback)
    all_highest = []
    for key in worst_dict:
        # print(key)
        unilist = []
        countlist = []
        q = worst_dict[key]
        for i in q:
            if i not in unilist:
                unilist.append(i)
        for i in unilist:
            countlist.append(q.count(i))
        highest = max(countlist)
        all_highest.append([key, unilist[countlist.index(highest)], highest])

    allcounts = []
    for i in all_highest:
        allcounts.append(i[2])
    lowest = min(allcounts)
    options = []
    for i in all_highest:
        if i[2] <= lowest:
            options.append(i)
    return ast.literal_eval(options[0][0])


# My selfmade algorithm, checks
def selfmade_algorithm(possible_combis, feedback, guess):
    new_list = []
    if guess[0] and guess[1] and guess[2] == guess[3]:
        last_guess_num = guess[0]
        if feedback == (0, 0):
            for i in possible_combis:
                if guess[0] not in i:
                    new_list.append(i)
        else:
            new_list = possible_combis
        if int(guess[0]) < 6:
            if guess in new_list:
                print("REMOVED", guess)
                new_list.remove(guess)
            new_guess_num = f"{int(last_guess_num) + 1}"
            new_list.insert(0, [new_guess_num, new_guess_num, new_guess_num,
                                new_guess_num])
    else:
        new_list = possible_combis
        new_list.remove(guess)
        random.shuffle(new_list)
    return new_list
