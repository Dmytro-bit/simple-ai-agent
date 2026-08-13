from openai import OpenAI
from openai.types.chat import ChatCompletion

from call_function import available_functions


class OpenAIClass:
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """

    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key, )

        self.messages = [
            {
                "role": "system",
                "context": self.system_prompt
            }
        ]

    @staticmethod
    def _print_stats(response, message):
        print(f"User prompt: {message}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    def send_message(self, message: str, verbose: bool):
        self.messages.append(
            {
                "role": "user",
                "context": message
            })

        response: ChatCompletion = self.client.chat.completions.create(
            model="openrouter/free",
            messages=self.messages,
            tools=available_functions
        )


        if response.usage and verbose:
            self._print_stats(response, message)

        self.messages.append(self.parse_response(response)[0])
        return response

    @staticmethod
    def parse_response(response: ChatCompletion):
        return response.choices[0].message.content, response.choices[0].message.tool_calls
