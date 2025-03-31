import sys
import argparse
from openai import OpenAI

parser = argparse.ArgumentParser(
    description="Run the OpenAI client script with your API key."
)

parser.add_argument(
        "--api-key",
    type=str,
    required=True,
    help="Your OpenAI API key",
)
args = parser.parse_args()

client = OpenAI(
    api_key=args.api_key,
)


history = [
    {
        "role": "user",
        "content": " please generate a 5 in script that rides at the numbers for 1 to 10."
    }
]

response = client.responses.create(
    model="gpt-3.5-turbo",
    instructions="You are a coding assistant that talks like a pirate.",
    input=history,
    store=False
)

print(history)
print(response.output_text)

while True:
    
    history += [{"role": el.role, "content": el.content} for el in response.output]
    medelsen = input()
    history.append({ "role": "user", "content": medelsen })

    response = client.responses.create(
        input=history,
        instructions="You are a coding assistant that talks like a pirate.",
        model="gpt-3.5-turbo",
        store=False
    )

    print(response.output_text)
