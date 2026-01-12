# 数当てゲーム（Number Guess Game）

Python（Flask）で作成した、ログイン機能付きの数当てゲームです。  
1〜100のランダムな数字を当て、試行回数を競います。  
ランキング機能とデータの永続化も実装しています。

未経験からWebアプリ開発の流れを学ぶ目的で作成しました。

---

## 🔹 アプリ概要

- ログイン機能あり
- 数当てゲーム（1〜100）
- 試行回数の表示
- ランキング機能（上位10件）
- ランキングはファイル保存で永続化
- Render にデプロイ済み

---

## 🔐 ログイン情報（デモ用）
ID: test
Password: test123
---

## 🛠 使用技術

- Python 3
- Flask
- Gunicorn
- HTML / CSS
- Git / GitHub
- Render（デプロイ）

---

## 🚀 機能一覧

- ユーザーログイン / ログアウト
- 数当てゲームロジック
- 試行回数のカウント
- ランキング表示
- ゲーム再スタート機能
- データのファイル保存（JSON）

---

## 📦 ローカルでの起動方法

```bash
git clone https://github.com/ogata940513-ship-it/number-guess-game.git
cd number-guess-game
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
