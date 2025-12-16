import random


def match_variable(var, replacement, bindings):
    binding = bindings.get(var)
    if not binding:
        bindings.update({var: replacement})
        return bindings
    if replacement == bindings[var]:
        return bindings
    return False


def is_variable(pattern):
    return (type(pattern) is str and pattern.startswith("?") and len(pattern) > 1)


def match_pattern(pattern, input, bindings=None):
    if bindings is False:
        return False
    if not pattern and not input:
        return bindings
    bindings = bindings or {}
    if pattern and is_variable(pattern[0]):
        var = pattern[0][1:]
        for i in range(len(input) + 1):
            new_bindings = match_variable(var, input[:i], dict(bindings))
            match = match_pattern(pattern[1:], input[i:], new_bindings)
            if match is not False:
                return match
        return False
    elif pattern and input and pattern[0] == input[0]:
        return match_pattern(pattern[1:], input[1:], bindings)
    else:
        return False


rules = [

    ("?*X HI ?*Y", [
        "Hi there! How’s your training going?",
        "Hello! Ready to talk fitness?",
        "Hey athlete! What’s your workout plan today?"
    ]),
    ("?*X HELLO ?*Y", [
        "Hello athlete! Welcome to Sports & Gym ChatBot.",
        "Hey there! Ready to talk about your fitness journey?",
        "Hi champion! Let’s explore your training and sports goals."
    ]),
    ("?*X HEY ?*Y", [
        "Hey! How’s your fitness routine?",
        "Hey champ! Do you prefer gym or sports today?",
        "Hey there! Let’s talk workouts."
    ]),
    ("?*X MY TRAINING IS GOING GOOD ?*Y", ["That’s excellent! Consistency is the key to progress.",
                                           "Glad your training is going well! What’s your current focus?",
                                           "Awesome! Do you want to share your workout routine?"]),
    ("?*X SALAM ?*Y", [
        "Salam! Hope your sports journey is going well.",
        "Wa Alaikum Salam! How’s your fitness routine?",
        "Salam athlete! Do you want to discuss gym or sports?"
    ]),
    ("?*X HOW ARE YOU ?*Y", [
        "I’m feeling strong and motivated! How about you?",
        "I’m doing great, thanks for asking. How’s your training?",
        "I’m ready to talk fitness. How are you feeling today?"
    ]),
    ("?*X WHAT'S UP ?*Y", [
        "Just keeping fit and focused! What’s up with you?",
        "Thinking about workouts and sports. What’s new with you?",
        "All good here! How’s your routine going?"
    ]),
    ("?*X GOOD MORNING ?*Y", [
        "Good morning! Did you plan a workout today?",
        "Morning champ! Are you training today?",
        "Good morning athlete! How’s your energy level?"
    ]),
    ("?*X GOOD EVENING ?*Y", [
        "Good evening! Did you finish your workout?",
        "Evening athlete! How was your training today?",
        "Good evening champ! Ready to relax after sports?"
    ]),
    ("I FEEL ?*X", [
        "Why do you feel ?X during workouts?",
        "Do you often feel ?X after sports?",
        "What makes you feel ?X in training?"
    ]),
    ("I AM ?*X", [
        "Why do you say you are ?X?",
        "How does being ?X affect your training?"
    ]),
    ("?*X I DON'T WANT TO TRAIN ?*Y", [
        "Why don’t you want to train?",
        "What usually motivates you when you feel this way?"
    ]),
    ("?*X I AM LAZY ?*Y", [
        "Why do you think you are lazy?",
        "What could help you overcome laziness in training?"
    ]),
    ("?*X I WANT TO BUILD ?*Y", [
        "What makes you want to build ?Y?",
        "How long have you wanted to build ?Y?",
        "What steps are you taking to build ?Y?"
    ]),
    ("?*X I WANT TO LOSE ?*Y", [
        "Why do you want to lose ?Y?",
        "What methods are you trying to lose ?Y?"
    ]),
    ("?*X GYM ?*Y", [
        "Do you enjoy going to the gym?",
        "What’s your favorite gym routine?",
        "How often do you train at the gym?"
    ]),
    ("?*X WORKOUT ?*Y", [
        "Which workout do you enjoy most?",
        "Do you prefer cardio or strength training?",
        "How do you structure your workouts?"
    ]),
    ("?*X TIRED ?*Y", [
        "Why do you think you are tired?",
        "Do you get enough rest after workouts?",
        "Does training make you feel tired often?"
    ]),
    ("?*X INJURY ?*Y", [
        "Sorry to hear about your injury. How did it happen?",
        "How are you recovering from your injury?",
        "Does the injury stop you from training?"
    ]),
    ("?*X MUSCLE PAIN ?*Y", [
        "Muscle pain is common after workouts. How do you deal with it?",
        "Do you stretch or recover properly after training?"
    ]),
    ("?*X INTRODUCTION ?*Y", ["I’m Sports & Gym ChatBot, a chatbot that reflects on your fitness thoughts.",
                              "Think of me as your workout buddy who listens and asks questions.",
                              "I’m here to talk about gym, sports, recovery, and motivation."
                              ]),
    ("?*X START ?*Y", [
        "Let’s begin! Tell me about your sports routine.",
        "We’re starting fresh. What’s your favorite workout?",
        "Kick-off time! Do you prefer gym or outdoor sports?"
    ]),

    ("I FEEL ?*X", [
        "Why do you feel ?X during workouts?",
        "Do you often feel ?X after sports?",
        "What makes you feel ?X in training?"
    ]),
    ("I AM ?*X", [
        "Why do you say you are ?X?",
        "How does being ?X affect your training?"
    ]),
    ("?*X I DON'T WANT TO TRAIN ?*Y", [
        "Why don’t you want to train?",
        "What usually motivates you when you feel this way?"
    ]),
    ("?*X I AM LAZY ?*Y", [
        "Why do you think you are lazy?",
        "What could help you overcome laziness in training?"
    ]),

    ("?*X I WANT TO BUILD ?*Y", [
        "What makes you want to build ?Y?",
        "How long have you wanted to build ?Y?",
        "What steps are you taking to build ?Y?"
    ]),
    ("?*X I WANT TO LOSE ?*Y", [
        "Why do you want to lose ?Y?",
        "What methods are you trying to lose ?Y?"
    ]),

    ("?*X GYM ?*Y", [
        "Do you enjoy going to the gym?",
        "What’s your favorite gym routine?",
        "How often do you train at the gym?"
    ]),
    ("?*X WORKOUT ?*Y", [
        "Which workout do you enjoy most?",
        "Do you prefer cardio or strength training?",
        "How do you structure your workouts?"
    ]),

    ("?*X TIRED ?*Y", [
        "Why do you think you are tired?",
        "Do you get enough rest after workouts?",
        "Does training make you feel tired often?"
    ]),
    ("?*X INJURY ?*Y", [
        "Sorry to hear about your injury. How did it happen?",
        "How are you recovering from your injury?",
        "Does the injury stop you from training?"
    ]),
    ("?*X MUSCLE PAIN ?*Y", [
        "Muscle pain is common after workouts. How do you deal with it?",
        "Do you stretch or recover properly after training?"
    ]),

    ("?*X CRICKET ?*Y", [
        "How often do you play cricket?",
        "What do you enjoy most about cricket?",
        "Do you play cricket casually or competitively?"
    ]),
    ("?*X FOOTBALL ?*Y", [
        "Do you play football regularly?",
        "What position do you like in football?",
        "How does football training compare to gym workouts?"
    ]),
    ("?*X SPORTS ?*Y", [
        "Which sport excites you the most?",
        "Do you prefer team sports or solo training?",
        "How do sports fit into your fitness routine?"
    ]),

    ("?*X FOOD ?*Y", [
        "What kind of food do you eat after training?",
        "Do you follow a special diet for fitness?",
        "How important is nutrition in your routine?"
    ]),
    ("?*X PROTEIN ?*Y", [
        "Do you take protein supplements?",
        "What’s your favorite protein source?",
        "How do you balance protein with other nutrients?"
    ]),

    ("?*X ROUTINE ?*Y", [
        "Do you follow a strict fitness routine?",
        "How consistent are you with your routine?",
        "What’s the hardest part of sticking to a routine?"
    ]),
]

default_responses = [
    "Consistency beats intensity. Keep going!",
    "Interesting, tell me more about your sports routine.",
    "I’m not sure I understand you fully, can you explain?",
    "Please continue about your fitness goals."
]


def replace(word, replacements):
    for old, new in replacements:
        if word == old:
            return new
    return word


###########################################################################
def switch_viewpoint(words):
    replacements = [('I', 'YOU'), ('YOU', 'I'), ('ME', 'YOU'),
                    ('MY', 'YOUR'), ('AM', 'ARE'), ('ARE', 'AM')]
    return [replace(word, replacements) for word in words]


###########################################################################
def respond(rules, input, default_responses):
    input = input.split()
    matching_rules = []
    for pattern, responses in rules:
        pattern = pattern.split()
        bindings = match_pattern(pattern, input)
        if bindings:
            matching_rules.append((responses, bindings))
    if matching_rules:
        responses, bindings = random.choice(matching_rules)
        response = random.choice(responses)
    else:
        bindings = {}
        response = default_responses[0]
    for variable, value in bindings.items():
        value = ' '.join(switch_viewpoint(value))
        if value:
            response = response.replace('?' + variable, value)
    return response


###########################################################################
def chatbot(prompt, rules, default_responses):
    while True:
        try:
            userinput = input(prompt).upper()
            if not userinput:
                continue
        except:
            break
        print(respond(rules, userinput, default_responses))


chatbot('ChatBot> ', rules, default_responses)
