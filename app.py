from flask import Flask, render_template, request, redirect, session
import random
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secretkey123"

# 保存ファイル
RANKING_FILE = "ranking.json"


# ランキング読み込み
def load_ranking():
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []


# ランキング保存
def save_ranking(ranking):
    with open(RANKING_FILE, "w") as f:
        json.dump(ranking, f, ensure_ascii=False, indent=4)


# ランキングデータ（最初に読み込み）
RANKING = load_ranking()

# 仮ユーザー
USER_DATA = {
    "aoi": "pass123",
    "test": "test123"
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in USER_DATA and USER_DATA[username] == password:
            session["username"] = username
            session["answer"] = random.randint(1, 100)
            session["attempts"] = 0
            return redirect("/guess")
        else:
            return render_template("login.html", message="ユーザー名またはパスワードが違います")

    return render_template("login.html")


@app.route("/guess", methods=["GET", "POST"])
def guess():
    if "username" not in session:
        return redirect("/")

    message = None

    if request.method == "POST":
        guess_num = int(request.form.get("guess"))
        session["attempts"] += 1

        answer = session["answer"]
        if guess_num < answer:
            message = "もっと大きいよ！"
        elif guess_num > answer:
            message = "もっと小さいよ！"
        else:
            return redirect("/result")

    return render_template("guess.html",
                           message=message,
                           attempts=session.get("attempts", 0))


@app.route("/result")
def result():
    if "username" not in session:
        return redirect("/")

    username = session["username"]
    attempts = session["attempts"]

    global RANKING
    RANKING = load_ranking()

    # 新しい記録を追加（最新10件だけ残す）
    new_record = {
        "user": username,
        "score": attempts,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    RANKING.append(new_record)

    # 最新10件を残す（同じユーザーでもOK）
    RANKING = sorted(RANKING, key=lambda x: x["score"])[:10]

    save_ranking(RANKING)

    return render_template("result.html",
                           answer=session["answer"],
                           attempts=attempts)


@app.route("/restart")
def restart():
    session["answer"] = random.randint(1, 100)
    session["attempts"] = 0
    return redirect("/guess")


@app.route("/ranking")
def ranking():
    global RANKING
    RANKING = load_ranking()
    # スコアが少ない順に並べる
    sorted_rank = sorted(RANKING, key=lambda x: x["score"])
    return render_template("ranking.html", ranking=sorted_rank)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)