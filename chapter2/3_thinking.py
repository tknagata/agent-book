# 必要なライブラリをインポート
import boto3
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Bedrock呼び出し用のAPIクライアントを作成
client = boto3.client("bedrock-runtime")

# Converse APIを実行
response = client.converse(
    # modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    modelId="arn:aws:bedrock:us-west-2:201189646499:inference-profile/global.anthropic.claude-sonnet-4-20250514-v1:0", # モデルID
    messages=[{
        "role": "user",
        "content": [{
            "text": "こんにちは"
        }]
    }],
    additionalModelRequestFields={
        "thinking": {
            "type": "enabled",      # 拡張思考をオン
            "budget_tokens": 1024   # 思考トークンの予算
        },
    },
)

# 思考プロセスと最終回答を表示
for content in response["output"]["message"]["content"]:
    if "reasoningContent" in content:
        print("<thinking>")
        print(content["reasoningContent"]["reasoningText"]["text"])
        print("</thinking>")
    elif "text" in content:
        print(content["text"])