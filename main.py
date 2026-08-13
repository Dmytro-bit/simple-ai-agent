import argparse
import os
import sys

from dotenv import load_dotenv

from call_function import call_function
from vendors.open_ai.client import OpenAIClass

load_dotenv()
API_KEY = os.environ.get("OPENROUTER_API_KEY")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

if __name__ == "__main__":
    client = OpenAIClass(api_key=API_KEY)

    for loop in range(20):
        print("Loop: ", loop)

        response = client.send_message(args.user_prompt, args.verbose)

        text, tool_calls = client.parse_response(response)

        if tool_calls:
            for tool_call in tool_calls:
                result = call_function(tool_call, verbose=args.verbose)

                client.messages.append(result)

                if args.verbose:
                    print(f"-> {result['content']}")
        else:
            print("Final response:")
            print(text)
            sys.exit()
