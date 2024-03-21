import turtle as t
import random
import time
class Mine(t.Turtle):
    def __init__(self,x,y):
        t.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.hideturtle()
        self.ban=0#是否被翻开
        self.lei=0#是否是雷
        self.lj=0#旁边的雷
        self.bj=0#是否被标记
    def draw(self):
        if self.bj % 2 == 1:
            return
        self.color("grey61")
        self.clear()
        self.penup()
        self.speed(0)
        if self.ban==1:
            self.goto(self.x * 40 - 250+20+100-20, self.y * 40 - 250-30+50)
            self.write(self.lj,align="center",font=("宋体",20,"bold"))
        else:
            self.begin_fill()
            self.goto(self.x * 40-250+100-20, self.y * 40-250+50)
            for _ in range(4):
                self.fd(35)
                self.right(90)
            self.end_fill()
    def bindu(self):
        if self.ban == 1 or self.lei == 1:
            return
        self.ban = 1  # 将ban等于一表示它已经被翻开了
        if self.lj == 0:  # 如果他的旁边的雷数等于零时开始传播
            if 0 <= self.x + 1 <= 9 and 0 <= self.y<= 9:
                A[self.x+1][self.y].bindu()
            if 0 <= self.x - 1 <= 9 and 0 <= self.y <= 9:
                A[self.x-1][self.y].bindu()
            if 0 <= self.x <= 9 and 0 <= self.y - 1 <= 9:
                A[self.x][self.y-1].bindu()
            if 0 <= self.x <= 9 and 0 <= self.y + 1 <= 9:
                A[self.x][self.y+1].bindu()
    def clear1(self):
        self.clear()
    def Yj(self):
        global bj#被标记的数量
        if nb==1:#如果游戏结束就不能按了
            return
        if bj ==10 and self.bj%2==1:#这里的一坨屎是为了防止雷标记的数量大于十个
            self.bj += 1
            bj -= 1
            t3.clear()
            t3.penup()
            t3.goto(9 * 40 - 250 + 20 + 100 + 20 - 110, 9 * 40 - 250 + 70)
            t3.write(f"{10 - bj}", align="center", font=("宋体", 20, "bold"))
            return
        if bj>=10 or self.ban==1:
            return
        self.bj+=1
        if self.bj%2==1:
            bj+=1
            self.penup()
            self.goto(self.x * 40 - 250+20+100-20, self.y * 40 - 250-30+50)
            self.color("red")
            self.write("雷",align="center",font=("宋体",20,"bold"))
        if self.bj%2==0:
            bj-=1
            t3.clear()
            self.clear()
            self.draw()
        t3.clear()
        t3.penup()
        t3.goto(9 * 40 - 250 + 20 + 100 + 20 - 110, 9 * 40 - 250 + 70)
        t3.write(f"{10 - bj}", align="center", font=("宋体", 20, "bold"))

t.tracer(0, 0)  # 关闭动画更新
A=[[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        A[i][j] = Mine(i, j)
ch=1
t.tracer(0, 0)
t.update()
t1=t.Turtle()
t1.color("red")
t1.goto(0,230)
t1.hideturtle()
t4=t.Turtle()
t4.penup()
t4.goto(9*40 -250+20+100-20-190,9*40 -250+70)
t4.write("重启", align="center", font=("宋体", 20, "bold"))
t4.hideturtle()
bj=0
t3=t.Turtle()
t3.hideturtle()
seconds=0
import time
timer_turtle = t.Turtle()
timer_turtle .goto(9*40 -250+20-20-190,9*40 -250+70)
nb=0
def update_timer():#这个是不用循环的时间表
    global seconds#这是时间
    if nb != 1:
        timer_turtle.clear()
        timer_turtle.write("时间: {} 秒".format(seconds), align="center", font=("Arial", 16, "normal"))
        seconds += 1
    # 1000毫秒后再次调用update_timer
    t.ontimer(update_timer, 1000)
update_timer()
timer_turtle.hideturtle()
def fun(x, y):
    global ch, fd,nb,bj
    t5 = t.Turtle()
    t5.color("red")
    t5.hideturtle()
    for i in range(10):
        for j in range(10):
            if i * 40 - 250 + 100 - 20 <= x <= i * 40 - 250 + 40 + 100 - 20 and j * 40 - 250 - 40 + 50 <= y <= j * 40 - 250 + 50:
                if A[i][j].bj%2==1 and  nb !=1:
                    bj -= 1
                    A[i][j].bj+=1
                    t3.clear()
                    A[i][j].clear()
                    A[i][j].draw()
                    return
                A[i][j].bindu()
                if A[i][j].lei == 1:
                    nb = 1
                    t1.write("你输了", align="center", font=("宋体", 50, "bold"))
                if fd == 90:
                    nb = 1
                    t1.write("nb", align="center", font=("宋体", 200, "bold"))
    if 9 * 40 - 250 + 70 <= y <= 9 * 40 - 250 + 70 + 20 and 9 * 40 - 250 + 100 - 20 - 190 < x < 9 * 40 - 250 + 20 + 100 - 190:
        ch = 8#按到重置就循环
def fun1(x,y):
    for i in range(10):
        for j in range(10):
            if i * 40 - 250 + 100 - 20 <= x <= i * 40 - 250 + 40 + 100 - 20 and j * 40 - 250 - 40 + 50 <= y <= j * 40 - 250 + 50:
                A[i][j].Yj ()
t.onscreenclick(fun1,btn=3)
t.onscreenclick(fun)
while(ch!=0):
    t3.clear()
    t3.penup()
    t3.goto(9 * 40 - 250 + 20 + 100 + 20 - 110, 9 * 40 - 250 + 70)
    t3.write("10", align="center", font=("宋体", 20, "bold"))
    bj=0
    seconds = 0
    ch=1
    t1.clear()
    for i in range(10):
        for j in range(10):
            A[i][j].clear1()
            A[i][j] = Mine(i, j)
    n=0
    while n<10:
        C=random.randint(0,9)
        B=random.randint(0,9)
        if A[C][B].lei==0:
            A[C][B].lei=1
            for i in range(3):
                for j in range(3):
                    if 0<=C+i-1<=9 and 0<=B+j-1<=9 :
                        A[C+i-1][B+j-1].lj+=1#把雷旁边的九个格子的雷数加一 包括雷
            n+=1
    fd=0#已经翻了的数量
    t.tracer(0, 0)
    t.update()
    nb=0
    while (1):
        if nb==0:
            for i in range(10):
                for j in range(10):
                    A[i][j].draw()
        if nb==1:
            for i in range(10):
                for j in range(10):
                    if A[i][j].lei == 1:
                        A[i][j].clear1()
                        A[i][j].penup()
                        A[i][j].goto(i * 40 - 250 + 20 + 100 - 20, j * 40 - 250 - 30 + 50)
                        A[i][j].color("red")
                        A[i][j].write("*", align="center", font=("宋体", 20, "bold"))
        t.update()
        if ch==8:#如果按到重置就循环
            break

