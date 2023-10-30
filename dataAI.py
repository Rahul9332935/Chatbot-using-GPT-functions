import openai
import requests
import json
import os

weather_api_key = os.environ['W_API']

def get_current_weather(location, unit):
    try:
        resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric&sys=unix")
        resp.raise_for_status()  # Raise an exception if the response status is not OK  
        data= json.loads(resp.content)
        forecast = data['weather'][0]['description']
        weather_info = {
            "location": location,
            "temperature":data['main']['temp'],
            "unit": "celsius",
            "forecast": forecast,
        }
        return json.dumps(weather_info)
    except requests.exceptions.HTTPError as err:
        error_message = str(err)
        return json.dumps({"error": error_message})
    except Exception as err:
        error_message = str(err)
        return json.dumps({"error": error_message})

# def run_conversation(query):
#     # Step 1: send the conversation and available functions to GPT
#     messages = [{"role": "user", "content": query}]
#     functions = [
#         {
#             "name": "get_current_weather",
#             "description": "Get the current weather in a given location",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "location": {
#                         "type": "string",
#                         "description": "The city and state, e.g. San Francisco, CA",
#                     },
#                     "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
#                 },
#                 "required": ["location"],
#             },
#         }
#     ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=messages,
#         functions=functions,
#         function_call="auto",  # auto is default, but we'll be explicit
#     )
#     response_message = response["choices"][0]["message"]

#     # Step 2: check if GPT wanted to call a function
#     if response_message.get("function_call"):
#         # Step 3: call the function
#         # Note: the JSON response may not always be valid; be sure to handle errors
#         available_functions = {
#             "get_current_weather": get_current_weather,
#         }  # only one function in this example, but you can have multiple
#         function_name = response_message["function_call"]["name"]
#         function_to_call = available_functions[function_name]
#         function_args = json.loads(response_message["function_call"]["arguments"])
#         function_response = function_to_call(
#             location=function_args.get("location"),
#             unit=function_args.get("unit"),
#         )

#         # Step 4: send the info on the function call and function response to GPT
#         messages.append(response_message)  # extend conversation with assistant's reply
#         messages.append(
#             {
#                 "role": "function",
#                 "name": function_name,
#                 "content": function_response,
#             }
#         )  # extend conversation with function response
#         second_response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo-0613",
#             messages=messages,
#         )  # get a new response from GPT where it can see the function response
#         return second_response["choices"][0]["message"]["content"]
#     else:
#       # If the query is not related to greetings or weather, use ChatGPT to respond
#       messages = [{"role": "user", "content": query}]
#       response = openai.ChatCompletion.create(
#           model="gpt-3.5-turbo",
#           messages=messages,
#       )
#       response_message = response["choices"][0]["message"]
#       return response_message["content"]
conversation_history = [] 
def run_conversation(query):
  # Extend the conversation history with the new user message
  conversation_history.append({"role": "user", "content": query})

  # Create a copy of the conversation history to avoid modifying the original
  messages = list(conversation_history)

  functions = [
      {
          "name": "get_current_weather",
          "description": "Get the current weather in a given location",
          "parameters": {
              "type": "object",
              "properties": {
                  "location": {
                      "type": "string",
                      "description": "The city and state, e.g. San Francisco, CA",
                  },
                  "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
              },
              "required": ["location"],
          },
      }
  ]

  response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=functions,
            function_call="auto",
        )

  response_message = response["choices"][0]["message"]

        # Check if GPT wanted to call a function
  if response_message.get("function_call"):
      available_functions = {
          "get_current_weather": get_current_weather,
      }

      function_name = response_message["function_call"]["name"]
      function_to_call = available_functions[function_name]
      function_args = json.loads(response_message["function_call"]["arguments"])
      function_response = function_to_call(
          location=function_args.get("location"),
          unit=function_args.get("unit"),
      )

      # Extend the conversation history with the function call and response
      conversation_history.append(response_message)
      conversation_history.append(
          {
              "role": "function",
              "name": function_name,
              "content": function_response,
          }
      )

      # Get a new response from GPT with updated conversation history
      messages = list(conversation_history)
      second_response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo-0613",
          messages=messages,
      )

      second_response_message = second_response["choices"][0]["message"]
      return second_response_message["content"]
  else:
      # If the query is not related to greetings or weather, use ChatGPT to respond
      return response_message["content"]





# print(run_conversation("what is weather of patna"))