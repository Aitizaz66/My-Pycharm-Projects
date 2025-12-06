def chatbot_reply(msg):
    msg = msg.lower()
    patterns = {
        "weather": ["weather", "rain", "sun", "hot", "cold", "temperature", "climate"],
        "study": ["study", "course", "exam", "assignment", "homework", "test"],
        "health": ["health", "sick", "medicine", "doctor", "pain", "headache"],
        "greeting": ["hi", "hello", "hey", "salam"],
        "food": ["food", "eat", "hungry", "meal", "breakfast", "dinner"],
        "technology": ["computer", "laptop", "mobile", "ai", "python", "programming"],
        "yes": ["ok", "yes", "good"],
    }
    responses = {
        "yes": "Okay tell me more about",
        "weather": "Sounds like you're talking about weather. Is it pleasant today or too hot/cold?",
        "study": "Study topics can be tough. Which subject are you focusing on?",
        "health": "Looks like you're talking about health. Hope you're okay. Do you want to describe how you feel?",
        "greeting": "Hello! Nice to chat with you. How can I help?",
        "food": "Food is always an interesting topic. What do you feel like eating?",
        "technology": "Technology is fun to explore. Are you working on something specific?",
        "unknown": "I couldn't figure that out, but I'm here if you want to share more."
    }
    for topic in patterns:
        for k in patterns[topic]:
            if k in msg:
                return responses[topic]
    return responses["unknown"]


print("Chatbot ready. Type 'bye' to exit.\n")
while True:
    text = input("You: ")
    if "bye" in text.lower():
        print("Bot: Goodbye! Take care.")
        break
    reply = chatbot_reply(text)
    print("Bot:", reply)
