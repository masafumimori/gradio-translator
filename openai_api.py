from typing import Optional

import openai

class OpenAIApi:
    """
    A wrapper class for interacting with the OpenAI API.
    """
    def __init__(self, api_key: str, model: str = "gpt-4-0613", system_prompt: Optional[str] = None, temperature = 0) -> None:
        """
        Initialize the OpenAIApi object.

        Parameters:
        - api_key: The API key for OpenAI
        - model: The model name
        - system_prompt: An optional system prompt
        """
        openai.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt or ""
        self.temperature = temperature

    def get_response(self, system_prompt: Optional[str] = None, user_prompt: Optional[str] = None) -> 'ChatResponse':
        """
        Get a chat response from the OpenAI API.

        Parameters:
        - system_prompt: An optional system prompt
        - user_prompt: The user's prompt
        """
        if not self.system_prompt and not system_prompt:
            raise Exception("System prompt must be specified.")

        try:
            completion = openai.ChatCompletion.create(
                model=self.model,
                temperature=self.temperature,
                messages=[
                    {"role": "system", "content": system_prompt or self.system_prompt},
                    {"role": "user", "content": user_prompt or ""}
                ]
            )
            message = completion.choices[0].message.content
            total_tokens = completion.usage.total_tokens
            return ChatResponse(message, total_tokens)

        except Exception as e:
            raise Exception(f"Something went wrong while getting response from OpenAI: {str(e)}")


class ChatResponse:
    """
    A class representing the chat response from OpenAI.
    """
    def __init__(self, message: str, total_tokens: int) -> None:
        """
        Initialize the ChatResponse object.

        Parameters:
        - message: The message content
        - total_tokens: The total token count
        """
        self._message = message
        self._total_tokens = total_tokens

    @property
    def message(self) -> str:
        """
        Get the message content.
        """
        return self._message

    @property
    def total_tokens(self) -> int:
        """
        Get the total token count.
        """
        return self._total_tokens
