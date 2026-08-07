import random
import sympy as sp
import re



x = sp.Symbol("x")

def format_fixer(expr):
    text = str(expr)
    powers = {
        "0": "⁰",
        "1": "¹",
        "2": "²",
        "3": "³",
        "4": "⁴",
        "5": "⁵",
        "6": "⁶",
        "7": "⁷",
        "8": "⁸",
        "9": "⁹"
    }
    for number, power in powers.items():
        text = text.replace(f"**{number}", power)

    text = text.replace("*", "")
    text = text.replace("/"," ⁄ " )
    text = text.replace("I","i" )
    text = text.replace("pi","π")
    text = text.replace("sqrt","√")

    text = re.sub( #finds sec, things inside sec, and the power, the rearranges it in the correct format
        r"(sec)\((.*?)\)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        r"\1\3(\2)",
        text
    )
    return text

def complex_pair_generator(): #creates a pair of real and complex number, eg 3+5i
    imaginary = random.randint(-10,10)
    if imaginary == 0:
        imaginary += random.randint(2,7)
    real_number = random.randint(-10,10)
    if real_number == 0:
        real_number += random.randint(2,7)

    return real_number + imaginary*sp.I

def differentiation_basic_achieved():
    question = 0
    for power in range(random.randint(2,4)+1):#range starts from 0,needs +1 for full range
        coefficient = random.randint(-10,10) 

        if coefficient != 0:
            question += coefficient * x ** power

    answer = sp.diff(question, x)
    return question,answer

def differentiation_product_achieved():
    f = 0
    for power in range(random.randint(1,2)+1):#range starts from 0,needs +1 for full range
        coefficient = random.randint(-10,10) 

        if coefficient != 0:
            f += coefficient * x ** power
    g = 0
    for power2 in range(random.randint(1,2)+1):#range starts from 0,needs +1 for full range
        coefficient2 = random.randint(-10,10) 

        if coefficient2 != 0:
            g += coefficient2 * x ** power2
    
    question = f * g
    answer = sp.diff(question, x)
    return question,answer

def differentiation_quotient_achieved():
    f = 0
    for power in range(2,3):
        coefficient = random.randint(-10,10)
        if coefficient != 0:
            f += coefficient * x**power

    g = 0
    for power2 in range(2):
        coefficient2 = random.randint(3,10)
        if coefficient2 != 0:
            g += coefficient2 * x**power2

    question = sp.Mul(f, sp.Pow(g, -1), evaluate=False) #prevents it from being simplifed
    #sp.pow adds a power of -1, turning it into a denominator

    answer = sp.together(sp.diff(question,x))#simplifies the whole thing to be less of a mess

    numerator, denominator = sp.fraction(answer) #splits it into a fraction

    answer = f"({numerator})/({denominator})"
    return question,answer

def differentiation_chain_achieved():
    question = sp.Integer(0)

    for power in range(random.randint(1,2)):
        coefficient = random.randint(-10,10)

        if coefficient != 0:
            question += coefficient * x**power

    if not question.has(x):
        question += random.randint(1, 10) * x

    picker = random.randint(1,4)

    if picker == 1:
        question = sp.sin(question, evaluate=False)
    elif picker == 2:
        question = sp.cos(question, evaluate=False)
    elif picker == 3:
        question = sp.tan(question, evaluate=False) #evaluate prevents pi from showing up
    elif picker == 4:
        question = sp.Pow(question, random.randint(2,4), evaluate=False)
    
    answer = sp.diff(question,x)

    if picker == 3:
        inner = question.args[0] #.args gets the numbers inside the tan
        inner_derivative = sp.diff(inner, x)
        answer = inner_derivative * sp.sec(inner)**2 #diffs the inner, then adds it back onto the tan, which is converted into sec^2
    else:
        answer = sp.diff(question, x)

    return question, answer

def complex_multiplication_achieved():
    terms = []

    for i in range(random.randint(2, 3)):
        terms.append(complex_pair_generator()) #adds pairs of compex numbers to the

    question = (sp.Mul(*terms, evaluate=False))
    answer = sp.expand(sp.Mul(*terms))

    return question, answer

def complex_division_achieved():
    numerator = complex_pair_generator()
    denominator = complex_pair_generator()

    while denominator == 0:
        denominator = complex_pair_generator()

    question = sp.Mul(
        numerator,
        sp.Pow(denominator, -1),
        evaluate=False
    )

    conjugate = sp.conjugate(denominator)

    answer = sp.expand(numerator * conjugate) / sp.expand(denominator * conjugate)

    return question, answer

def complex_argument_achieved():
    z = complex_pair_generator()

    question = z

    a = sp.re(z)
    b = sp.im(z)

    answer = sp.atan2(b, a)

    return question, answer

def complex_modulus_achieved():
    z = complex_pair_generator()

    a = sp.re(z)
    b = sp.im(z)

    question = random.randint(1,3) * (a + b*sp.I)

    answer = sp.sqrt(sp.expand_complex(question * sp.conjugate(question)))

    return question, answer

def complex_quadratic_achieved():
    p = random.randint(-5, 5)
    q = random.randint(1, 5)

    question = x**2 - 2*p*x + (p**2 + q**2)

    answer = sp.solve(question,x)

    return question, answer

def complex_cartesian_merit():

    r = random.randint(1,6)

    angles = [
        sp.pi/6,
        sp.pi/4,
        sp.pi/3,
        sp.pi/2,
        2*sp.pi/3,
        3*sp.pi/4,
        5*sp.pi/6,
        sp.pi
    ]

    theta = random.choice(angles)

    question = r * (sp.cos(theta, evaluate = False) + sp.I*sp.sin(theta, evaluate = False))

    answer = sp.expand_complex(question)

    return question, answer

def differentiation_stationary_merit():

    question = sp.Integer(0)
    numbers = [-5,-4,-3,-2,2,3,4,5]
    for power in range(3):
        coefficient = random.choice(numbers)

        if coefficient != 0:
            question += coefficient * x**power


    x_values = sp.stationary_points(question, x)

    answer = [(value, question.subs(x, value)) for value in x_values]

    return question,answer

def differentiation_tangent_merit():

    function = 0

    for power in range(random.randint(2, 3) + 1):
        coefficient = random.randint(-6, 6)
        if coefficient != 0:
            function += coefficient * x**power

    derivative = sp.diff(function, x)

    x_value = random.randint(-3, 3)

    y_value = function.subs(x, x_value)

    gradient = derivative.subs(x, x_value)

    tangent = sp.expand(gradient*(x - x_value) + y_value)

    question = (
        f"y = {function}, "
        f"tangent equation x = {x_value}."
    )

    answer = f"y = {tangent}"

    return question, answer
def complex_polarform_merit():

    question = complex_pair_generator()
    
    Imaginary = sp.im(question)
    Real = sp.re(question)

    hyp = sp.sqrt(sp.Add(sp.Pow(Real,2),sp.Pow(Imaginary,2)))

    theta = sp.sin(sp.Mul(Imaginary,sp.Pow(hyp,-1)))

    answer = f"{hyp} (cos({theta}) + isin({theta}))"

    return question,answer
