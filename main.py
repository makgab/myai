#!/usr/bin/python3
#
# OpenAI chatbot demo
#
#
# before run in CLI: export OPENAI_API_KEY=<your_key>
# ./main.py
#
#

import os
import openai

# variables
API_KEY="OPENAI_API_KEY"

# functions
def askGPT(text):
  openai.api_key = os.getenv( API_KEY )
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = text,
    temperature = 0.6,
    max_tokens = 150,
  )
  return print(response.choices[0].text)

def main():
  if not API_KEY in os.environ:
    print("\nNo API_KEY variable set. Please set it:\nexport OPENAI_API_KEY=\"your-key-here\"")
    exit(0)

  while True:
    print("GPT: Ask me a question (q: Quit)\n")
    myQn = input()
    if myQn == "q":
      exit(0)
    askGPT( myQn )
    print("\n")



# the main function
main()

