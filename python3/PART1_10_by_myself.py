import random

def hangman(word):
    wrong_count = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    # hoji by list
    remmained_words = list(word)
    # status of correce answer
    seikai_and_mada = ["_"] * len(remmained_words)

    while  wrong_count < len(stages):
        char = input("Enter an alphabet:")
        while len(char) != 1:
            print("input one char")
            char = input("Enter ONLY ONE alphabet:")
        
        if char in remmained_words:
            print("Match!")
            index_char = remmained_words.index(char)
            remmained_words[index_char] = '$'
            seikai_and_mada[index_char] = char
            show_status(seikai_and_mada, stages, wrong_count)

            if "_" not in seikai_and_mada:
                print("You WIN!")
                break
        else:
            print("Not Match!")
            wrong_count += 1
#            print("Now status is...\n")
#            print(seikai_and_mada)
#            print(stages[0:wrong_count])
            show_status(seikai_and_mada, stages, wrong_count)

            if wrong_count == len(remmained_words):
                print("You TOO MATCH miss...")
                break

def show_status(seikai_and_mada, stages, wrong_count):
            print("Now status is...")
            print("Your wrong_count is ", wrong_count)
            print(seikai_and_mada)
            print("\n".join(stages[0:(wrong_count+1)]))
 
ans_candidate_list = ["cat",
                      "dog",
                      "bird",
                      "penguin",
                     ]

num_answers = len(ans_candidate_list)
target_answer = random.randint(0, num_answers)

print("hangman start!")
hangman(ans_candidate_list[target_answer])