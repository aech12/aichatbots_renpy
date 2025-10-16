import requests
import json

# Replace these with your actual values
OPENROUTER_API_KEY = ""

# API request
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    },
    data=json.dumps({
        "model": "google/gemini-2.0-flash-exp:free",
        "messages": [
            {
                "role": "user",
                "content": "Guess how old I am"
            }
        ]
    })
)

# Handle the response
if response.status_code == 200:
    response_data = response.json()
    print("Response:", json.dumps(response_data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")

# Response: {
#   "id": "gen-1760552060-y5gm3d4CLU2CVK9WMUup",
#   "provider": "OpenAI",
#   "model": "openai/gpt-4o",
#   "object": "chat.completion",
#   "created": 1760552060,
#   "choices": [
#     {
#       "logprobs": null,
#       "finish_reason": "stop",
#       "native_finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": "The meaning of life is a profound question that has been explored by philosophers, theologians, scientists, and thinkers throughout history. It can be interpreted in various ways depending on one's beliefs, culture, or personal experiences. Some common perspectives include:\n\n1. **Philosophical:** Many philosophical traditions explore the idea that the meaning of life might be connected to the pursuit of knowledge, virtue, or personal happiness. Existentialists, for example, often argue that life has no inherent meaning, so it's up to individuals to create their own purpose.\n\n2. **Religious:** In many religions, the meaning of life is connected to fulfilling the will of a higher power, achieving a spiritual or moral goal, or reaching an afterlife or state of enlightenment.\n\n3. **Scientific:** From a scientific perspective, some might argue that life\u2019s meaning is rooted in survival, reproduction, and the continuation of our species.\n\n4. **Personal and Subjective:** For many people, the meaning of life is a personal and subjective matter, involving family, love, creativity, and other individual experiences and values.\n\nUltimately, the meaning of life might be something each person defines for themselves based on their own beliefs, values, and experiences.",
#         "refusal": null,
#         "reasoning": null
#       }
#     }
#   ],
#   "system_fingerprint": "fp_f64f290af2",
#   "usage": {
#     "prompt_tokens": 14,
#     "completion_tokens": 244,
#     "total_tokens": 258,
#     "prompt_tokens_details": {
#       "cached_tokens": 0,
#       "audio_tokens": 0
#     },
#     "completion_tokens_details": {
#       "reasoning_tokens": 0
#     }
#   }
# }
