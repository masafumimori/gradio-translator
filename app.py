import gradio as gr
from translator import Translator, TranslationError
from evaluator import Evaluator, EvaluationError

def translate_and_evaluate(openai_key, model_name,system_prompt, prompt_text):
    translator = Translator(openai_key, model=model_name,
                    system_prompt=system_prompt if not system_prompt else "You are a helpful assistant.")
    evaluator = Evaluator(openai_key, model=model_name,
                    system_prompt=system_prompt if not system_prompt else "You are a helpful assistant.")
    try:
        response = translator.to_english(input=prompt_text)
        evaluation = evaluator.evaluate(japanese=prompt_text, english=response.message)
        total_tokens = response.total_tokens + evaluation.total_tokens
        return response.message, evaluation.message, total_tokens

    except TranslationError as e:
        return str(e), "", 0
    except EvaluationError as e:
        return response.message, str(e), response.total_tokens
    except Exception as e:
        return f"An error occurred: {str(e)}", "", 0

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
    gr.Textbox(label="Total tokens"),
]
app = gr.Interface(
    fn=translate_and_evaluate,
    inputs=inputs,
    outputs=outputs,
    title="Translator from Japanese to English",
    description="入力された日本語テキストの英語翻訳を行います。"
)

app.launch(debug=True)
