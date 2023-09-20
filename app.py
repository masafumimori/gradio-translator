import gradio as gr
from translator import Translator
from evaluator import Evaluator

def create_meeting_summary(openai_key, model_name,system_prompt, prompt_text):
    translator = Translator(openai_key, model=model_name,
                    system_prompt=system_prompt if not system_prompt else "You are a helpful assistant.")
    evaluator = Evaluator(openai_key, model=model_name,
                    system_prompt=system_prompt if not system_prompt else "You are a helpful assistant.")
    try:
        response = translator.to_english(input=prompt_text)
        evaluation = evaluator.evaluate(japanese=prompt_text, english=response)

        return response, evaluation

    except Exception as e:
        return f"An error occurred: {str(e)}"

inputs = [
    gr.Textbox(lines=1, label="openai_key"),
    gr.Radio(choices=[
        "gpt-4", 
        "gpt-4-0613", 
        "gpt-4-32k", 
        "gpt-4-32k-0613", 
        "gpt-3.5-turbo", 
        "gpt-3.5-turbo-0613", 
        "gpt-3.5-turbo-16k", 
        "gpt-3.5-turbo-16k-0613"
    ], default="gpt-4-0613", label="model_name"),
    gr.Textbox(lines=3, label="system_prompt"),
    gr.Textbox(lines=3, label="prompt_text"),
]

outputs = [
    gr.Textbox(label="Translated text"),
    gr.Textbox(label="Evaluation"),
]
app = gr.Interface(
    fn=create_meeting_summary,
    inputs=inputs,
    outputs=outputs,
    title="Translator from Japanese to English",
    description="入力された日本語テキストの英語翻訳を行います。"
)

app.launch(debug=True)
