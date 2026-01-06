import random
import os

SCORE_FILE = "score.txt"

def load_scores():
    """スコアファイルを読み込む"""
    if not os.path.exists(SCORE_FILE):
        return []
    with open(SCORE_FILE, "r") as f:
        scores = [int(line.strip()) for line in f.readlines()]
    return scores

def save_score(new_score):
    """スコアを保存する"""
    with open(SCORE_FILE, "a") as f:
        f.write(str(new_score) + "\n")

def show_ranking(scores):
    """ランキング表示"""
    print("\n=== 🏆 ランキング 🏆 ===")
    if not scores:
        print("まだ記録がありません")
        return

    sorted_scores = sorted(scores)
    for i, score in enumerate(sorted_scores[:5], start=1):
        print(f"{i}位 : {score} 回")
    print("=======================\n")


# --- メインゲーム部分 ---

print("=== 数当てゲーム！ランキング対応版 ===")

# 起動時にランキング表示
scores = load_scores()
show_ranking(scores)

answer = random.randint(1, 100)
count = 0

while True:
    guess = input("数字を入力してください： ")

    if not guess.isdigit():
        print("数字を入力してね！")
        continue

    guess = int(guess)
    count += 1

    if guess < answer:
        print("もっと大きい数字だよ！")
    elif guess > answer:
        print("もっと小さい数字だよ！")
    else:
        print(f"正解！！ 🎉 {count} 回で当たったよ！")

        # スコア保存
        save_score(count)
        print("スコアを保存しました！")

        break