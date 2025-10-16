# In your main script file (script.rpy)
define t1 = Character("test")

label chat_start:
    t1 "testtt"

    # Initialize the AI chat instance
    $ ai_chat = AIChat()
    
    # # Define your character
    $ char_name = "Luna"
    $ char_persona = "A friendly and curious cat girl who loves adventure."
    $ current_scenario = "You meet Luna in a cozy coffee shop on a rainy afternoon."
    
    # jump chat_loop

label chat_loop:
    # Get user input
    $ user_input = renpy.input("You: ", length=200)
    
    if user_input.strip() == "":
        jump chat_loop
    
    if user_input.lower() in ["quit", "exit", "bye"]:
        "Goodbye!"
        return
    
    # Show thinking indicator
    "Luna is typing..."
    
    # Get AI response
    $ ai_response = ai_chat.send_request(user_input, char_name, char_persona, current_scenario)
    
    # Display the response
    "[char_name]: [ai_response]"
    
    jump chat_loop