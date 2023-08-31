import tkinter as tk
import os
import datetime

now = 0
later = 160
minutes = 1

window = tk.Tk()
window.title('肥胖龟树脂计算器')
window.geometry('330x165')

var = tk.StringVar()
command = tk.Label(window, textvariable=var, bg='white', font=('Arial,12'), width=40, height=2)
command.place(x=0,y=0)
var.set("肥胖龟树脂计算器")

now_text = tk.Label(window,text='请输入目前树脂数量:',width=20,height=2,bg='white', font=('Arial,12'))
now_text.place(x=0,y=40)

now_Entry = tk.Entry(window,show=None)
now_Entry.place(x=168,y=40,width=37,height=35)

later_text = tk.Label(window,text='请输入目标树脂数量:',width=20,height=2,bg='white', font=('Arial,12'))
later_text.place(x=0,y=80)

later_Entry = tk.Entry(window,show=None)
later_Entry.place(x=168,y=80,width=37,height=35)

def now_def():
    global now
    now = now_Entry.get()
    global later
    later = later_Entry.get()
    if int(now) >= 0:
        if int(later) >= int(now):
            if int(later) <= 160:
                minutes = (int(later) - int(now)) * 8
                var.set("距离达到"+str(later)+"个树脂还需要"+str(minutes)+"分钟")
                if int(minutes) > 60:
                    # 使用整数除法运算符来计算小时数
                    hours = minutes // 60

                    # 使用取余运算符来计算剩余的分钟数
                    minutes_left = minutes % 60

                    # 使用字符串连接符来显示转换结果，注意要加上空格和单位
                    var.set("距离达到"+str(later)+"个树脂还需要"+str(hours) + " 小时 " + str(minutes_left) + " 分钟")
                    # 获取当前的日期和时间，并转换为字符串格式
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # 打印当前的日期和时间
                    print(f"现在的日期和时间是：{now}")
                    # 将当前的日期和时间转换为datetime对象
                    now = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
                    # 创建一个timedelta对象，表示指定的分钟数
                    delta = datetime.timedelta(minutes=minutes)
                    # 计算经过指定分钟后的日期和时间，并转换为字符串格式
                    later2 = (now + delta).strftime("%Y-%m-%d %H:%M:%S")
                    # 打印经过指定分钟后的日期和时间
                    var2.set("到"+str(later2)+"就达到"+str(later)+"个树脂了")
            else:
                var.set("树脂超过160就不会自动恢复了哦")
        else:
            var.set("目的树脂数量不能小于或等于当前树脂数量")
    else:
        var.set("树脂不能为负数")

cal_Button = tk.Button(window,text='计算', width=7, height=4, command=now_def)
cal_Button.place(x=207, y=40)

def about():
    about_window = tk.Toplevel()
    about_window.title('肥胖龟自动去除片尾 - 关于软件')
    about_window.geometry('800x125')

    about_text = tk.Label(about_window, text='肥胖龟树脂计算器：是一款由肥胖龟（隶属于肥胖龟公司、TL工作室）开发的树脂计算器软件。', bg='white', font=('Arial', 12))
    about_text.pack()

    about_text_2 = tk.Label(about_window, text='树脂：是一款由米哈游自主研发的一款全新开放世界冒险游戏《原神》中的虚拟物品', bg='white', font=('Arial', 12))
    about_text_2.pack()

    about_text_3 = tk.Label(about_window, text='联系作者：QQ2947158920，邮箱qianzhemayi1234567@163.com，哔哩哔哩肥胖龟。', bg='white', font=('Arial', 12))
    about_text_3.pack()

    def juanxian():
        os.system('start https://postimg.cc/K121LGX9')

    juanxian_Button = tk.Button(about_window,text='捐献', width=55, height=2, command=juanxian)
    juanxian_Button.place(x=0, y=75)

    def kaiyuan():
        os.system('start https://github.com/FatTurtle2022/FatTurtle_Cut_End/releases')

    kaiyuan_Button = tk.Button(about_window,text='开源', width=55, height=2, command=kaiyuan)
    kaiyuan_Button.place(x=400, y=75)

    about_window.mainloop()

cal_Button = tk.Button(window,text='关于', width=7, height=4, command=about)
cal_Button.place(x=267, y=40)

var2 = tk.StringVar()
later_time = tk.Label(window, textvariable=var2, bg='white', font=('Arial,12'), width=40, height=2)
later_time.place(x=0,y=120)
var2.set("")

window.mainloop()