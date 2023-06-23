import pyautogui as pag
import tkinter as tk

def counter():
    global tmr # 関数内の変数tmrをグローバル変数のtmrとして扱う宣言
    m_posi_x, m_posi_y = pag.position()
    if (tmr % 2 == 0):
        pag.moveTo(m_posi_x + 20, m_posi_y)
    else:
        pag.moveTo(m_posi_x - 20, m_posi_y)
    pag.press('ctrl')
    tmr += 1
    label["text"] = SideStep[tmr%2]
    root.after(1000, counter) # 1秒毎にcounter()を実行

SideStep = ['←','→']
tmr = 0 # 経過時間を記録する変数

root = tk.Tk()
root.title("右左")
root.geometry("400x50")
label = tk.Label(font=("Ubunt Mono", 20))
label.pack()
counter() # 最初のcounter()を実行しリアルタイム処理を始める
root.mainloop()
