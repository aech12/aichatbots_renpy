# aichat.rpy
init python:
    import json

    class AIChat:
        def __init__(self):
            # Initialize chat history as a list of message dictionaries
            self.chat_history = []
            self.api_key = ""
            self.model = "google/gemini-2.0-flash-exp:free"

        def send_request(self, user_message, character_name, character_persona, scenario):
            """
            Send a request to OpenRouter API and return the AI's response.
            
            Args:
                user_message (str): The user's input message.
                character_name (str): The name of the character.
                character_persona (str): The character's persona description.
                scenario (str): The current scenario context.
            
            Returns:
                str: The AI's response or an error message.
            """
            # Construct the system prompt
            system_prompt = f"""You are roleplaying as {character_name}.

Character Persona:
{character_persona}

Current Scenario:
{scenario}

Stay in character and respond naturally to the player's messages. Keep responses concise and engaging."""

            # Build the messages list
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend(self.chat_history)
            messages.append({"role": "user", "content": user_message})

            # Prepare the API request payload
            payload = {
                "model": self.model,
                "messages": messages
            }

            # API headers
            headers = {
                "Authorization": f"Bearer {self.api_key}",  # Replace with your API key
                "Content-Type": "application/json"
            }

            # Make the async API request using renpy.fetch
            renpy.log(f"Logging")

            try:
                response = renpy.fetch(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    method="POST",
                    headers=headers,
                    data=json.dumps(payload),
                )
                print(f"Raw API Response: {response}")

                # Debug: Log the raw response
                renpy.log(f"Raw API Response: {response}")

                # Parse the response
                response_data = json.loads(response)

                # Debug: Log the parsed response structure
                renpy.log(f"Parsed Response Data: {json.dumps(response_data, indent=2)}")
                print(f"Parsed Response Data: {json.dumps(response_data, indent=2)}")

                # Debug: Check what keys are present
                renpy.log(f"Response keys: {response_data.keys()}")
                
                if "choices" in response_data and len(response_data["choices"]) > 0:
                    ai_response = response_data["choices"][0]["message"]["content"]
                    # Append to chat history
                    self.chat_history.append({"role": "user", "content": user_message})
                    self.chat_history.append({"role": "assistant", "content": ai_response})
                    return ai_response
                else:
                    return "Error: No valid response from the API."
            except json.JSONDecodeError as e:
                # Specific error for JSON parsing issues
                renpy.log(f"JSON Parse Error: {str(e)}")
                renpy.log(f"Raw response was: {response}")
                return f"Error parsing JSON: {str(e)}"
                
            except Exception as e:
                # Log full error details
                renpy.log(f"Exception Type: {type(e).__name__}")
                renpy.log(f"Exception Message: {str(e)}")
                import traceback
                renpy.log(f"Traceback: {traceback.format_exc()}")
                return f"Error making API request: {str(e)}"