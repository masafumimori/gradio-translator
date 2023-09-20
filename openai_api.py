import openai

class OpenAIApi:
    def __init__(self, api_key, model = "gpt-4-0613", system_prompt= ""):
        if not api_key:
            raise Exception("OpenAI API Key must be specified.")

        openai.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt

    def get_response(self, system_prompt = "", user_prompt = ""):

        if not system_prompt and not self.system_prompt:
            raise Exception("System prompt must be specified.")

        try:

            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            response_text = completion.choices[0].message.content
            return response_text

        except Exception as e:
            raise Exception(f"Something went wrong while getting response from OpenAI: {str(e)}")