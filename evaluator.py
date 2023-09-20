class EvaluationError(Exception):
    """Custom exception for evaluation errors"""
    def __init__(self, message):
        super().__init__(message)

from openai_api import OpenAIApi,ChatResponse

evaluate_template = """
##prerequisites
タイトル: 英語翻訳がオリジナル日本語テキストに忠実か採点
依頼者条: 英語翻訳を作成しオリジナルの日本語テキストに正確かを確認したい人物
制作者条件: 日英翻訳のエキスパートで、文脈などを読み取り適切に日英翻訳ができる高度なスキルを持っている人物
目的と目標: 英語翻訳を採点する
リソース: 日本語-英語の翻訳API
評価基準: 英語のテキストが正確に日本語を翻訳しているかどうか
明確化の要件:
- 日本語文章の直訳ではなく意味を汲み取ったものにすること
- 細かく確認し改善点があれば指摘すること
- 出力は日本語で改善点のみ（ある場合）であること
## end prerequisites

日本語テキスト:
{japanese}

英語翻訳:
{english}

評価出力："""

class Evaluator:

    def __init__(self, api_key, model, system_prompt) -> None:
        self.api = OpenAIApi(api_key, model, system_prompt)

    def evaluate(self, japanese, english) -> "ChatResponse":
        prompt = evaluate_template.format(japanese=japanese, english=english)

        try:
            response = self.api.get_response(prompt)
        except Exception as e:
            raise EvaluationError(f"Something went wrong while evaluating: {str(e)}")
        return response