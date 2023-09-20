from openai_api import OpenAIApi, ChatResponse

translate_template = """
##prerequisites
タイトル 日本語を英語へ翻訳し、出力する
依頼者条: 日本語を英語へ翻訳したい人物
制作者条件: 日英翻訳のエキスパートで、文脈などを読み取り適切に日本語から英語への翻訳ができる人物
目的と目標: 日本語のテキストを英語へ翻訳する
リソース: 日本語-英語の翻訳API
評価基準: 生成された英語のテキストが正確に日本語を翻訳しているかどうか
明確化の要件:
- 翻訳の際は、文章の直訳ではなく意味を汲み取ったものにすること
- 出力結果が英語であること
- 翻訳結果が正確であることを確認すること
- 翻訳はフォーマルな文面にすること
出力対象: 英語翻訳のみ
## end prerequisites

日本語テキスト:
{input}

翻訳出力:"""

class Translator:

    def __init__(self, api_key, model, system_prompt) -> None:
        self.api = OpenAIApi(api_key, model, system_prompt)

    def to_english(self, input) -> "ChatResponse":
        # here i wanna create complete prompt for openai api
        prompt = translate_template.format(input=input)
        print(prompt)
        response:ChatResponse = self.api.get_response(prompt)

        return response