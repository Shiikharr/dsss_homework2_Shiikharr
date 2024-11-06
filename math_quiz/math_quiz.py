import random


def generate_random_number(min, max): #changing function name to make it more meaningful
    """
    Return random number within a specified range.

    Parameters : 
        param1 (int) : First number of range
        param2 (int) : Last number of range

    Returns :
        (int) : random number between the input range
    
    Raises : 
        ValueError : If the input type is not Integer.
    """
    return random.randint(min, max)


def generate_random_operator():  #changing function name to make it more meaningful
    """
    Return random operator among three operators.

    Parameters : 
        None

    Returns :
        (String) : random operator
    
    """
    return random.choice(['+', '-', '*'])


def generate_question_answer(n1, n2, o): #changing function name to make it more meaningful
    """
    Return an object having a math question and it's answer

    Parameters : 
        param1 (int) : First random number
        param2 (int) : Second random number
        param3 (String) : operator - add / subtract / multiply

    Returns :
        (String),(int) : Math question by concatenating input params, addition / subtraction / multiplication of the question generated
    
    Raises : 
        ValueError : If the input type is not Integer.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2   #changing - to + as it is an addition operator
    elif o == '-': a = n1 - n2  #changing + to - as it is an addition operator
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    no_of_questions =  2    #changed the float value 3.14159265359 to 3 as it is giving type error and variable name

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(no_of_questions):
        n1 = generate_random_number(1, 10); 
        n2 = generate_random_number(1, 5); #changing 5.5 to 5 as randint function expects integer value
        o = generate_random_operator()

        PROBLEM, ANSWER = generate_question_answer(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)  #adding try block if incase the user input anything other than Integer like String or float
        except ValueError:
            print("Please enter an Integer Value.")
            continue   #to go to the next iteration and skip this one
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1  #It is an unnecessary way to increment s which can be easily done by s=s+1 or s+=1 so changing the s += -(-1) to s+=1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{no_of_questions}")

if __name__ == "__main__":
    math_quiz()
