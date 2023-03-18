import random

# Define a list of possible responses
responses = ["Yes", "No", "I don't know", "Maybe", "Sorry, I didn't understand",
             "Can you repeat that?", "Of course!", "Absolutely not.", "It's possible.", 
             "I'm not sure.", "That's a great idea!", "I'm not convinced.", "Definitely!",
             "I disagree.", "That sounds reasonable.", "Let me think about it.", 
             "I'm not sure I understand.", "You're absolutely right!", "I'm not convinced.",
             "That's a tough question.", "I think so.", "I don't think so.", 
             "Let me check.", "That's not possible.", "That's a good point.",
             "I'm not in a position to say.", "I need more information.", "I see what you mean.", 
             "I'm not sure how to answer that.", "That's not my area of expertise.", 
             "I don't have enough information to make a decision.", "I'm not sure I follow you.", 
             "Let's move on to another topic.", "I don't have an opinion on that.", 
             "That's a tricky one.", "I'm not sure that's a good idea.", 
             "That's not something I can help with.", "I'm not sure I can help with that.", 
             "That's an interesting perspective.", "That's not relevant to the conversation.",
             "That's a common misconception.", "I'm not sure what you're asking.", 
             "I'm sorry, I didn't understand the question.", "That's not quite right.", 
             "That's not my experience.", "I'm not sure I agree with you.", "I'm not sure that's accurate.",
             "That's an important point to consider."]

# Generate a random response
def generate_response():
    response = random.choice(responses)
    return response

# Integrate response generation into a chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye!")
        break
    else:
        bot_response = generate_response()
        print("Bot: " + bot_response)
