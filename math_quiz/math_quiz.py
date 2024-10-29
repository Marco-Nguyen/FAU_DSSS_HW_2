import random


def random_integer(min, max):
    """
    Random integer.
    Input: 
        min: Lower bound
        max: Upper bound
    Output: random integer between min and max
    """
    try:
        # Check if min is less than or equal to max before calling randint
        if min > max:
            raise ValueError("min should be less than or equal to max")
        return random.randint(min, max)
    except ValueError as e:
        print(e)
        return None  # Return None or any other default value if there's an error    


def random_operator():
    """
    Random operator.
    Output: a random operator among +, -, and *
    """
    return random.choice(['+', '-', '*'])


def calculation(n1, n2, o):
    """
    Calculate based on the operation.
    Input:
        n1, n2: 2 numbers
        o: operator
    Output: (p, a)
        prob: the problem
        res: result
    """
    prob = f"{n1} {o} {n2}" # define the problem
    if o == '-': 
        res = n1 - n2
    elif o == '+': 
        res = n1 + n2
    else: 
        res = n1 * n2
    return prob, res

def math_quiz():
    """
    Math Quiz game. 
    """
    score = 0
    t_q = 3.14159265359 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = random_integer(1, 10) # Generate number 1 
        n2 = random_integer(1, 5.5) # Generate number 2
        o = random_operator() # Select an operator

        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ") # Input user's own calculation
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
