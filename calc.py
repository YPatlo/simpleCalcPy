# importingModules
import sys
import string
import math


# makingSureOthersCantHackTheQuadEq
def safeeval(equation):
    if not set(equation).intersection(string.ascii_letters + '{}[]_;\n'):
        return eval(equation)
    else:
        print("Get lost from my computer, Bloody Idiot")
        sys.exit()


# definingMainCodeForQuadraticEq
def quadeq():
    # takingInput
    eq = input("""Enter Quadratic Equation, finds least whole number answers(if any).
    (for x square, enter x**2. If no coefficient, enter 1)""")

    # definingVariables
    x = 0
    time = 0
    # fundamentalCode,UsingTrialAndErrorMethod
    equation = eq.replace("x**2", "*x**2").replace("x", "*x")
    while safeeval(equation) != 0 and time <= 10 ** 4:
        x += 1
        time += 1
        equation = eq.replace("x**2", f"*{x}**2").replace("x", f"*{x}")

    # returningResult
    return x


# creatingARestartMethod
def restart(abc):
    if abc == "<>":
        while abc == "<>":
            calculate()
    else:
        print("GoodBye!")


# definingMethod.isFloat
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# mainMethod
def calculate():
    # printStatementsForUserUnderstanding
    num1 = 0
    num2 = 0
    print("-----------------------------------------")
    print("   Lets Calculate   ")
    print("-----------------------------------------")
    print("""Press + for Addition,\n
    Press - for Subtraction,\n
    Press * for Multiplication,\n
    Press / for Division, \n
    Press ^ for Exponentiation,\n
    Press !^ for Roots\n
    Press ! for Factorial\n
    or Press x** for Quadratic Equations""")

    # gettingInput
    operator = input(" ")

    # takingAppropriateNumericalInput
    if operator == "+":
        num1 = input("Type the first number")
        num2 = input("Type the second number")
    elif operator == "-":
        num1 = input("Type the first number")
        num2 = input("Type the second number")
    elif operator == "*":
        num1 = input("Type the first number")
        num2 = input("Type the second number")
    elif operator == "/":
        num1 = input("Type the dividend")
        num2 = input("Type the divisor")
    elif operator == "^":
        num1 = input("Type the base")
        num2 = input("Type the power")
    elif operator == "!^":
        num1 = input("Type the number")
        num2 = input("Which root of the number do you want?")
    elif operator == "x**":
        quadeq()
        void = input("Press <> to Restart or >< to end.")
        restart(void)
    elif operator == "!":
        num1 = input("Type the number")

    else:
        print("Input isn't valid.")
        num1 = 0
        num2 = 0
        void = input("Press <> to Restart or >< to end.")
        restart(void)

    # checkingIfUserInputIsValid
    if isfloat(num1) is True:
        if isfloat(num2) is True:
            print(f"Please confirm:\nNum1 = {num1}\nNum2 = {num2}")
            num1 = float(num1)
            num2 = float(num2)
            void = input("Press any key to Continue or Press <> to Restart")
            if void == "<>":
                restart(void)
            else:

                # Computing
                if operator == "+":
                    ans = num1 + num2
                    print("Answer is:", ans)
                elif operator == "-":
                    ans = num1 - num2
                    print("Answer is:", ans)
                elif operator == "*":
                    ans = num1 * num2
                    print("Answer is:", ans)
                elif operator == "/":
                    ans = num1 / num2
                    print("Answer is:", ans)
                elif operator == "^":
                    ans = num1 ** num2
                    print("Answer is:", ans)
                elif operator == "!^":
                    ans = num1 ** (1 / num2)
                    print("Answer is:", ans)
                elif operator == "!":
                    ans = math.factorial(int(num1))
                    print("Answer is:", ans)
                else:
                    print("An error occurred.")
                print("Type <> to restart or >< to end.")
                void = input(" ")
                if void == "<>":
                    restart(void)
                else:
                    pass
        else:
            print("Input isn't valid.")
            void = input("Press <> to Restart or >< to end.")
            restart(void)
    else:
        print("Input isn't valid.")
        void = input("Press <> to Restart or >< to end.")
        restart(void)


# runningTheCode
calculate()
