import sys
import tkinter as tk
from tkinter import ttk
import random
import webbrowser

questions = [
    ("どんなプレイスタイルが好き？", ["アクション", "ゆっくり探索", "頭を使う"]),
    ("プレイ時間は？", ["短め", "長くじっくり", "毎日ちょっとずつ"]),
    ("ストーリー重視？", ["はい", "いいえ"]),
    ("好きなグラフィックは？", ["リアル", "ドット絵", "アニメ調"]),
    ("オンライン要素は？", ["必須", "なくてもOK", "ソロがいい"]),
]

q_count = 0

# 選択肢が押されたとき
def answer_selected():
    global q_count
    q_count += 1

    if q_count < len(questions):
        show_question()
    else:
        show_thinking()

# 質問を表示する
def show_question():
    for widget in root.winfo_children():
        widget.destroy()

    q, op = questions[q_count]
    label = tk.Label(root, text=q, font=("Helvetica", 16))
    label.pack(pady=20)

    for o in op:
        btn = tk.Button(root, text=o, width=30, command=answer_selected)
        btn.pack(pady=5)

def open_link(event):
    webbrowser.open_new(event)

#　結果を表示する
def show_result():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text='あなたにぴったりのゲームは......', font=("Helvetica", 14))
    label.pack(pady=30)

    rdm = random.randint(0, 2)
    games = ["Killing Floor", "Killing Floor 2", "Killing Floor 3"]
    games_link = [
        "https://store.steampowered.com/app/1250/Killing_Floor/", 
        "https://store.steampowered.com/app/232090/Killing_Floor_2/", 
        "https://store.steampowered.com/app/1430190/Killing_Floor_3/"
        ]
    game_label = tk.Label(root, text=f"▶▶ {games[rdm]} ◀◀", font=("Helvetica", 24), fg="red")
    game_label.pack(pady=10)

    link = tk.Label(root, text=f"{games[rdm]} を Steam で見る\n(クリックでブラウザが開きます)", fg="blue", cursor="hand2", font=("Helvetica", 14, "underline"))
    link.pack(pady=50)
    # link.bind("<Button-1>", open_link(games_link[rdm]))
    # 上記だと関数を呼び出してしまい、その返り値が渡されてしまうため、結果画面が表示されたときにリンクが開かれる
    link.bind("<Button-1>", lambda event: open_link(games_link[rdm]))

    reset_button = tk.Button(root, text="もう一度やる", command=retry)
    reset_button.pack(pady=10)

# リトライボタンが押されたとき
def retry():
    global q_count
    q_count = 0
    show_start()


# スタート画面表示
def show_start():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text='5つの質問に答えるだけで\n最新AIがあなたにピッタリなゲームをおすすめします!', font=("Helvetica", 14))
    label.pack(pady=30)

    start_button = tk.Button(root, text="スタート", width=25, height=3, command=show_question)
    start_button.pack()

# プログレスバー表示
def show_thinking():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="AIがあなたに最適なゲームを考え中...", font=("Helvetica", 16))
    label.pack(pady=20)

    progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", maximum=100)
    progress.pack(pady=20)

    for i in range(101):
        progress.configure(value=i+1)
        progress.update()

        if 55 <= i <= 58 or 84 <= i <= 88:
            delay = 200
        else:
            delay = 10
        root.after(delay)

        if i == 100:
            show_result()



# main window
root = tk.Tk()
root.title("Game Recommender")
root.geometry("600x400")

show_start()

root.mainloop()