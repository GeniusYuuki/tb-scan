import requests
import json
from datetime import datetime

# ※ここは許可されたAPIのURLに置き換えてください
# 例として、GitHubの公開イベント情報を取得するAPIを使用します
URL = "https://api.github.com/events"

def main():
    try:
        # データを取得
        response = requests.get(URL)
        response.raise_for_status()
        
        # JSON形式に整形（差分を見やすくするため）
        data = response.json()
        formatted_data = json.dumps(data[:5], indent=2, ensure_ascii=False) # 最新5件だけ取得
        
        # 取得したデータを data.json というファイルに上書き保存
        with open("data.json", "w", encoding="utf-8") as f:
            f.write(formatted_data)
            
        print("データの取得と保存が完了しました。")
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
