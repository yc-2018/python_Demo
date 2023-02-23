# By：仰晨
# 文件名：表白
# 时 间：2022/11/1 21:41


from tkinter import *
from tkinter import messagebox


def close_window():
    messagebox.showinfo(title="警告", message="不许关闭，好好回答")
    return


def love():
    love2 = Toplevel(window)
    love2.geometry("300x100+520+260")
    love2.title("好巧，我也是")
    label2 = Label(love2, text="好巧，我也是", font=("微软雅黑", 20))
    label2.pack()
    btn2 = Button(love2, text="确定", width=10, height=2, command=close_all_window)
    btn2.pack()
    love2.protocol("WM_DELETE_WINDOW", close_love)


def close_love():
    return


def close_all_window():
    window.destroy()


def no_love():
    no_love2 = Toplevel(window)
    no_love2.geometry("300x100+520+260")
    no_love2.title("再考虑考虑")
    label2 = Label(no_love2, text="再考虑考虑呗", font=("微软雅黑", 25))
    label2.pack()
    btn2 = Button(no_love2, text="好的", width=10, height=2, command=no_love2.destroy)
    btn2.pack()
    no_love2.protocol("WM_DELETE_WINDOW", close_no_love)


def close_no_love():
    no_love()


window = Tk()
window.title("你喜欢我吗？")
window.geometry('380x450')
window.geometry('+500+240')
window.protocol("WM_DELETE_WINDOW", close_window)
label = Label(window, text="hey,女神名字", font=("微软雅黑", 15), fg='red')
label.grid(row=0, column=0, sticky=W)
label1 = Label(window, text="喜欢我吗？", font=("微软雅黑", 30))
label1.grid(row=1, column=1, sticky=E)
photo = PhotoImage(file="女神照片.png")
image_label = Label(window, image=photo)
image_label.grid(row=2, columnspan=2)
btn = Button(window, text="喜欢", width=15, height=2, command=love)
btn.grid(row=3, column=0, sticky=W)
btn1 = Button(window, text="不喜欢", command=no_love)
btn1.grid(row=3, column=1, sticky=E)
window.mainloop()














