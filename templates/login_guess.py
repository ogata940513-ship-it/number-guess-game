import random
import os

USER_FILE = "users.txt"

def load_users():
    """ユーザー情報を読み込む"""
    if not os.path.exists(USER_FILE):
        return {}

    users = {}
    with open(USER_FILE, "r") as f:
        for line in f:
            username, password = line.strip().split(",")
            users[username] = password
    return users


def save_user(username, password):
    """ユーザー登録を保存"""
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password}\n")


def sign_up(users):
    """新規登録"""
    print("\n=== 新規登録 ===")
    while True:
        username = input("ユーザー名: ")
        if username in users:
            print("このユーザー名は既に使われています。")
            continue
        password = input("パスワード: ")
        save_user(username, password)
        print("登録完了！")
        return username


def sign_in(users):
    """ログイン"""
    print("\n=== ログイン ===")
    while True:
        username = input("ユーザー名: ")
        password = input("パスワード: ")

        if username in users and users[username] == password:
            print("ログイン成功！")
            return username
        else:
            print("ユーザー名またはパスワードが違います。")


def number_game(username):
    """数当てゲーム本体"""
    answer = random.randint(1, 100)
    count = 0

    print(f"\n=== 数当てゲーム（{username} さん） ===")

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
            break


# ==== メイン処理 ====
users = load_users()

print("=== ログイン機能つき数当てゲーム ===")
choice = input("1:ログイン / 2:新規登録 → ")

if choice == "1":
    username = sign_in(users)
else:
    username = sign_up(users)

number_game(username)