def chatbot_response(user_input):
    # Convert user input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()

    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    # Asking for help
    elif "help" in user_input or "assist" in user_input:
        return "Sure! What do you need help with?"

    # Asking about the weather
    elif "weather" in user_input:
        return "I can't check the weather right now, but I hope it's nice wherever you are!"

    # Asking about the time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."

    # Asking about the date
    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."

    # Asking about the chatbot's name
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot. You can call me Chatbot!"

    # Default response for unrecognized inputs
    else:
        return "I'm sorry, I don't understand that. Can you try asking something else?"

# Main program loop
def main():
    print("Chatbot: Hello! I am a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the conversation if the user types 'exit'
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Get chatbot response
        response = chatbot_response(user_input)

        # Print chatbot response
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()
