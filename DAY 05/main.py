from random_word_generator import pick_random_word


def change_the_state(current_state, input_char, selected_word):
    modified_word = ""

    for i in range(len(selected_word)):
        if current_state[i] == "_" and selected_word[i]==input_char:
            modified_word += selected_word[i]
        else:
            modified_word += current_state[i]
    return modified_word


def check_in_word(input_char,selected_word,current_state,attempts_remaining):
    if input_char in selected_word:
        current_state = change_the_state(current_state, input_char, selected_word)
    else:
        attempts_remaining-=1

    return current_state, attempts_remaining


def print_current_state(current_state, attempts_remaining):
    print("current word state :", end=" ")
    for i in current_state:
        print(i, end=" ")

    print("\t Attempts Remaining :",attempts_remaining)

def check_the_game(attempts_remaining, current_state, selected_word):
    if(attempts_remaining<=0):
        print("Sorry You Lost! :( Try Again!)")
        print("The word was :", selected_word)
        return False
    
    if(selected_word == current_state):
        print("Congratulation!! Winner winner chicken dinner")
        return False
    
    return True


def play_game():
    selected_word = pick_random_word()
    current_state = ""
    for i in selected_word:
        if i=='a' or i=='e' or i=='i' or i == 'o' or i == 'u':
            current_state+=i
        else:
            current_state+='_'
    attempts_remaining = 5
    print_current_state(current_state, attempts_remaining)
    while(True):
        input_char = input("Guess the character : ")
        current_state, attempts_remaining = check_in_word(input_char,selected_word,current_state,attempts_remaining)
        print_current_state(current_state, attempts_remaining)

        check_game = check_the_game(attempts_remaining, current_state, selected_word)
        if check_game == False:
            break



if __name__ == "__main__":
    play_game()

