import random

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0:wrong]))
        print("You lose! It was {}."
              .format(word))

num_answers = 4
target_answer = random.randint(0, num_answers)
ans_candidate_0 = "cat"
ans_candidate_1 = "dog"
ans_candidate_2 = "bird"
ans_candidate_3 = "penguin"

ans_candidate_list = [ans_candidate_0,
                      ans_candidate_1,
                      ans_candidate_2,
                      ans_candidate_3
                     ]

#print("ans_candidate_list is ...", ans_candidate_list)
#print("list module test, ", ans_candidate_list[3] )
#print("list module test, ", ans_candidate_list.index("bird") )
#print("random answer is ...", ans_candidate_list.index(target_answer))
hangman(ans_candidate_list[target_answer])