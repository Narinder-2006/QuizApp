import os
import time
import random
import matplotlib.pyplot as plt

def load_questions(filename):
    questions = {}
    with open(filename, 'r') as file:
        for line in file:
            if line := line.strip():
                q_num, q_text = line.split(': ', 1)
                q_text = q_text.replace('\\n', '\n')
                questions[int(q_num)] = q_text.strip()
    return questions

def load_answers(filename):
    answers = {}
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line := line.strip():
                q_num, ans = line.split(': ', 1)
                answers[int(q_num)] = ans.strip()
    return answers

def load_topic_questions(topic):
    return {
        "Easy": load_questions(f'./questions/{topic}/Easy.txt'),
        "Medium": load_questions(f'./questions/{topic}/Medium.txt'),
        "Hard": load_questions(f'./questions/{topic}/Hard.txt')
    }

def load_topic_answers(topic):
    return {
        "Easy": load_answers(f'./answers/{topic}/Easy.txt'),
        "Medium": load_answers(f'./answers/{topic}/Medium.txt'),
        "Hard": load_answers(f'./answers/{topic}/Hard.txt')
    }

# Question Banks
list_questions = load_topic_questions('Lists')
string_questions = load_topic_questions('Strings')
dict_questions = load_topic_questions('Dictionaries')
operator_questions = load_topic_questions('Operators')
function_questions = load_topic_questions('Functions')

topics = {
    "Lists": list_questions,
    "Strings": string_questions,
    "Dictionaries": dict_questions,
    "Operators": operator_questions,
    "Functions": function_questions,
}

# Answer Banks
list_answers = load_topic_answers('Lists')
string_answers = load_topic_answers('Strings')
dict_answers = load_topic_answers('Dictionaries')
operator_answers = load_topic_answers('Operators')
function_answers = load_topic_answers('Functions')

ans = {
    "Lists": list_answers,
    "Strings": string_answers,
    "Dictionaries": dict_answers,
    "Operators": operator_answers,
    "Functions": function_answers,
}

userAns = {}

# Utilities
def clear_screen():
    """
    Clears the console screen.
    Works for both Windows and Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def result(score, total):
    """
    Displays the result of the quiz.

    Args:
        score (int): Total number of correct answers.
        total (int): Total number of questions attempted.
    """
    print(f"You got {score}/{total} correct answers!")

c = {}  # Stores selected questions
times = {}  # Stores time taken for each question
l = {}  # Stores selected question IDs for each topic
d = []  # Temporary storage for question IDs
accuracy = {}
def quiz():
    """
    Main function to conduct the quiz.
    Handles question selection, timing, accuracy calculation, and result visualization.
    """
    global c, userAns, score, total, time, start_time, end_time, l, d, times
    global userAns  # Ensure userAns is updated globally
    
    diff_mode = input("Enter Difficulty mode of Quiz (Easy, Medium and Hard): ")
    try:
        a = int(input("Enter the number of topics: \nLists\nDictionaries\nStrings\nOperators\nFunctions\n"))
    except:
        print("Invalid input, Topics are less than your input.")
    
    for i in range(a):
        b = input(f"Enter topic {i + 1}: ")
        try:
            no_of_ques = int(input("Enter number of questions: "))
        except:
            print("Invalid input, Number of questions are less than your input.")
        
        prefernce_ques = int(0.6 * no_of_ques) + 1
        # Reset d and select questions
        d = [i for i in range(1, 6)]
        selected_questions = random.sample(d, prefernce_ques)
        
        c[b] = {"Easy": {}, "Medium": {}, "Hard": {}}
        for j in selected_questions:
            c[b][diff_mode][j] = [topics[b][diff_mode][j]]
        
        if diff_mode == "Easy":
            left_ques = no_of_ques - prefernce_ques
            d1 = [i for i in range(1, 6)]
            selected_questions1 = random.sample(d1, left_ques // 2)
            for j in selected_questions1:
                c[b]["Medium"][j] = [topics[b]["Medium"][j]]
            selected_questions2 = random.sample(d1, left_ques - (left_ques // 2))
            for j in selected_questions2:
                c[b]["Hard"][j] = [topics[b]["Hard"][j]]

        elif diff_mode == "Medium":
            left_ques = no_of_ques - prefernce_ques
            d1 = [i for i in range(1, 6)]
            selected_questions1 = random.sample(d1, left_ques // 2)
            for j in selected_questions1:
                c[b]["Easy"][j] = [topics[b]["Easy"][j]]
            selected_questions2 = random.sample(d1, left_ques - (left_ques // 2))
            for j in selected_questions2:
                c[b]["Hard"][j] = [topics[b]["Hard"][j]]

        elif diff_mode == "Hard":
            left_ques = no_of_ques - prefernce_ques
            d1 = [i for i in range(1, 6)]
            selected_questions1 = random.sample(d1, left_ques // 2)
            for j in selected_questions1:
                c[b]["Easy"][j] = [topics[b]["Easy"][j]]
            selected_questions2 = random.sample(d1, left_ques - (left_ques // 2))
            for j in selected_questions2:
                c[b]["Medium"][j] = [topics[b]["Medium"][j]]

    print(c)
    g = 1  # Question index across topics
    for topic in c:
        userAns[topic] = {}
        
        count = 0  # Correct answers for this topic
        for j in ["Easy", "Medium", "Hard"]:
            userAns[topic][j] = {}

            for question_id in c[topic][j]:
                clear_screen()
                start_time = time.time()
                userAns[topic][j][question_id] = {}
                print(c[topic][j][question_id][0])
                userAns[topic][j][question_id] = input("Your answer: ").strip()

                end_time = time.time()
                times[g] = end_time - start_time
                g += 1

                # Check answer
                correct_answer = ans[topic][j][question_id].strip().strip('"')  # Strip the correct answer
                user_answer = userAns[topic][j][question_id].strip()  # Already stripped
                if user_answer == correct_answer:
                    print("Correct answer!")
                    count += 1
                else:
                    print(f"Incorrect answer {user_answer}! Correct answer was: {correct_answer}")
                time.sleep(1.3)

        # Calculate accuracy for the topic
        accuracy[topic] = (count / (len(c[topic]["Easy"]) + len(c[topic]["Medium"]) + len(c[topic]["Hard"]))) * 100
        
    # Visualization
    visualize_results(accuracy, times)

def visualize_results(accuracy, times):
    """
    Visualizes the quiz results using side-by-side bar charts.

    Args:
        accuracy (dict): Accuracy per topic as a percentage.
        times (dict): Time taken for each question.
    """
    # Create a figure with two subplots side by side
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))  # 1 row, 2 columns

    # Plot accuracy bar chart
    x = list(accuracy.keys())
    y = list(accuracy.values())
    axs[0].bar(x, y, color='blue')
    axs[0].set_title("Accuracy by Topic")
    axs[0].set_xlabel("Topic")
    axs[0].set_ylabel("Accuracy (%)")
    axs[0].tick_params(axis='x', rotation=45)

    # Plot time bar chart
    x1 = list(times.keys())
    x2 = list(times.values())
    axs[1].bar(x1, x2, color='green')
    axs[1].set_title("Time Taken per Question")
    axs[1].set_xlabel("Question Index")
    axs[1].set_ylabel("Time (seconds)")

    # Adjust layout for better spacing
    plt.tight_layout()
    plt.show()

# Run the quiz
quiz()
print("Thanks")

