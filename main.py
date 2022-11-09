from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from PIL import ImageGrab, Image
from random import randint
from tkinter.colorchooser import *

# Глобальные переменные
Work = False
Color = 'black'
X = Y = 0


def Star(x, y):  # Отрисовка кисти-звёздочки
    size = -1 * int(SBT.get())
    x1 = x
    y1 = y + size
    x2 = x - size / 15 * 3
    y2 = y + size / 15 * 4
    x3 = x - size / 5 * 4
    y3 = y + size / 5 * 3
    x4 = x - size / 15 * 4
    y4 = y - size / 15 * 3
    x5 = x - size / 5 * 3
    y5 = y - size / 5 * 4
    x6 = x
    y6 = y - size / 3
    x7 = x + size / 5 * 3
    y7 = y - size / 5 * 4
    x8 = x + size / 15 * 4
    y8 = y - size / 15 * 3
    x9 = x + size / 5 * 4
    y9 = y + size / 5 * 3
    x10 = x + size / 15 * 3
    y10 = y + size / 15 * 4
    Field.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, fill=Color,
                         outline=Color)


def Angle5(x, y):  # Отрисовка кисти-пятиугольника
    size = -1 * int(SBT.get())
    x1 = x
    y1 = y + size
    x3 = x - size / 5 * 4
    y3 = y + size / 5 * 3
    x5 = x - size / 5 * 3
    y5 = y - size / 5 * 4
    x7 = x + size / 5 * 3
    y7 = y - size / 5 * 4
    x9 = x + size / 5 * 4
    y9 = y + size / 5 * 3
    Field.create_polygon(x1, y1, x3, y3, x5, y5, x7, y7, x9, y9, fill=Color, outline=Color)


def Romb(x, y):  # Отрисовка кисти-ромба
    size = -1 * int(SBT.get()) / 2
    x1 = x
    y1 = y + size
    x2 = x - size
    y2 = y
    x3 = x
    y3 = y - size
    x4 = x + size
    y4 = y
    Field.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=Color, outline=Color)


def Pshik(x, y):  # Отрисовка кисти-балончика
    size = int(SBT.get())
    for i in range(size):
        dx = randint(-1 * size, size)
        dy = randint(-1 * size, size)
        Field.create_oval(x + dx, y + dy, x + dx, y + dy, fill=Color, outline=Color)


def ChangeColor():  # Смена цвета
    global Color
    Color = askcolor()[1]
    CurColor.configure(bg=Color)


def click(event):  # Обработка нажатия мыши
    global Work, X, Y, Cir, Sqr
    X = event.x
    Y = event.y
    Work = True
    size = int(SBT.get())
    if ToolVar.get() == 1:  # Карандаш
        Field.create_oval(X - size / 2, Y - size / 2, X + size / 2, Y + size / 2, outline=Color, fill=Color)
    elif ToolVar.get() == 2:  # Кисть
        if BrushVar.get() == 1:
            Star(event.x, event.y)
        elif BrushVar.get() == 2:
            Angle5(event.x, event.y)
        elif BrushVar.get() == 3:
            Romb(event.x, event.y)
        elif BrushVar.get() == 4:
            Pshik(event.x, event.y)
    elif ToolVar.get() == 3:  # Прямоугольник
        if FillVar.get():
            Sqr = Field.create_rectangle(X, Y, X, Y, width=size, outline=Color, fill=Color)
        else:
            Sqr = Field.create_rectangle(X, Y, X, Y, width=size, outline=Color)
    elif ToolVar.get() == 4:  # Круг
        if FillVar.get():
            Cir = Field.create_oval(X, Y, X, Y, width=size, outline=Color, fill=Color)
        else:
            Cir = Field.create_oval(X, Y, X, Y, width=size, outline=Color)
    else:  # Ластик
        Field.create_oval(X - size / 2, Y - size / 2, X + size / 2, Y + size / 2, fill='white', outline='white')


def unclick(event):  # Обработка отпуска мышки
    global Work
    Work = False


def move(event):  # Обработка движения мышки
    global Work, X, Y, Cir, Sqr
    size = int(SBT.get())
    if Work:  # Если мышка зажата
        if ToolVar.get() == 1:  # Карандаш
            Field.create_line(X, Y, event.x, event.y, capstyle=ROUND, width=size, fill=Color)
            X = event.x
            Y = event.y
        elif ToolVar.get() == 2:  # Кисть
            if BrushVar.get() == 1:
                Star(event.x, event.y)
            elif BrushVar.get() == 2:
                Angle5(event.x, event.y)
            elif BrushVar.get() == 3:
                Romb(event.x, event.y)
            elif BrushVar.get() == 4:
                Pshik(event.x, event.y)
        elif ToolVar.get() == 3:  # Прямоугольник, перересовка
            Field.coords(Sqr, X, Y, event.x, event.y)
        elif ToolVar.get() == 4:  # Окружность, перересовка
            Field.coords(Cir, X, Y, event.x, event.y)
        else:  # Ластик
            Field.create_oval(event.x - size / 2, event.y - size / 2, event.x + size / 2,
                              event.y + size / 2, fill='white', outline='white', tag='Eras')


class Help:  # Загрузка изображения из файла
    def __init__(self, Field):
        self.Field = Field

    def Load(self):
        # Field.create_image(0, 0, image=PhotoImage(file=askopenfilename()))
        self.filename = askopenfilename(initialdir="/", title="Select file",
                                        filetypes=(("all", "*.jpg *.png *.gif *.bmp"),
                                                   ("jpeg files", "*.jpg"), ("png files", "*.png"),
                                                   ("gif files", "*.gif"), ("bmp files", "*.bmp")))
        self.imgtemp = Image.open(self.filename)
        if self.imgtemp.size[0] > 1000 or self.imgtemp.size[1] > 800:
            self.imgtemp = self.imgtemp.resize((1000, 800), Image.ANTIALIAS)
        self.imgtemp.save("Temp.gif", "gif")
        self.file_to_open = PhotoImage(file="Temp.gif")
        self.Field.delete("all")
        self.Field.create_image(500, 400, image=self.file_to_open, anchor=CENTER)


def Save():  # Сохранение изображения
    filename = asksaveasfilename(defaultextension='.bmp')
    if filename is None:
        return
    ImageGrab.grab((653, 38, 1907, 1042)).save(filename)


def Active():
    RBStar.configure(state="active")
    RBRomb.configure(state="active")
    RB5angle.configure(state="active")
    RBPshik.configure(state="active")


def Disabled():
    RBStar.configure(state="disabled")
    RBRomb.configure(state="disabled")
    RB5angle.configure(state="disabled")
    RBPshik.configure(state="disabled")


# Создание окна
window = Tk()
window.title("Рисовашка")
window.attributes('-fullscreen', True)

ToolVar = IntVar()
ToolVar.set(1)
BrushVar = IntVar()
BrushVar.set(1)
FillVar = BooleanVar()
FillVar.set(False)

# Поле рисования
Field = Canvas(window, width=1000, height=800, bg='white', highlightbackground='black')
CurColor = Canvas(window, width=100, height=100, bg=Color)
hlp = Help(Field)  # Для загрузки изображений

# Загрузка/сохранение
BLoad = Button(window, font=("Times New Roman", 22), bg='white', text="Загрузить", fg='black', command=hlp.Load)
BSave = Button(window, font=("Times New Roman", 22), bg='white', text="Сохранить", fg='black', command=Save)

# Выбор инструмента
RBPen = Radiobutton(window, variable=ToolVar, value=1, font=("Times New Roman", 22), bg='white', text='Карандаш',
                    command=Disabled)
RBBrush = Radiobutton(window, variable=ToolVar, value=2, font=("Times New Roman", 22), bg='white', text='Кисть',
                      command=Active)
RBRect = Radiobutton(window, variable=ToolVar, value=3, font=("Times New Roman", 22), bg='white', text='Прямоугольник',
                     command=Disabled)
RBElip = Radiobutton(window, variable=ToolVar, value=4, font=("Times New Roman", 22), bg='white', text='Окружность',
                     command=Disabled)
RBEras = Radiobutton(window, variable=ToolVar, value=5, font=("Times New Roman", 22), bg='white', text='Ластик',
                     command=Disabled)

# Толщина линий
LT = Label(window, font=("Times New Roman", 14), text="Толщина карандаша/ластика")
SBT = Spinbox(window, from_=1, to=100, font=("Times New Roman", 14), repeatdelay=100, repeatinterval=10,
              state='readonly')

# Выбор режима кисти
RBStar = Radiobutton(window, variable=BrushVar, value=1, font=("Times New Roman", 14), bg='white', state="disabled",
                     text=' Звезда')
RB5angle = Radiobutton(window, variable=BrushVar, value=2, font=("Times New Roman", 14), bg='white', state="disabled",
                       text='Пятиугольник')
RBRomb = Radiobutton(window, variable=BrushVar, value=3, font=("Times New Roman", 14), bg='white', state="disabled",
                     text='Ромб')
RBPshik = Radiobutton(window, variable=BrushVar, value=4, font=("Times New Roman", 14), bg='white', state="disabled",
                      text='Распылитель')

# Выбор цвета
BColor = Button(window, text='Выбор цвета', command=ChangeColor)

# Заливка
CBColor = Checkbutton(window, text="Заливка", variable=FillVar)

# Интерфейс вне рисования: позиционирование
BLoad.place(x=125, y=725, anchor=CENTER)
BSave.place(x=375, y=725, anchor=CENTER)
RBPen.place(x=125, y=100, anchor=CENTER)
RBEras.place(x=125, y=150, anchor=CENTER)
RBRect.place(x=125, y=225, anchor=CENTER)
RBElip.place(x=125, y=275, anchor=CENTER)
RBBrush.place(x=125, y=375, anchor=CENTER)
LT.place(x=375, y=100, anchor=CENTER)
SBT.place(x=375, y=150, anchor=CENTER)
RBStar.place(x=125, y=425, anchor=CENTER)
RB5angle.place(x=375, y=425, anchor=CENTER)
RBRomb.place(x=125, y=475, anchor=CENTER)
RBPshik.place(x=375, y=475, anchor=CENTER)
BColor.place(x=375, y=200, anchor=CENTER)
CurColor.place(x=375, y=275, anchor=CENTER)
CBColor.place(x=275, y=275, anchor=CENTER)
Field.place(x=window.winfo_screenwidth() / 3 * 2, y=window.winfo_screenheight() / 2, anchor=CENTER)
window.

# Важные бинды
Field.bind('<ButtonPress-1>', click)
Field.bind('<Motion>', move)
Field.bind('<ButtonRelease-1>', unclick)

# Красивые бинды
RBPen.bind('<Enter>', lambda event: RBPen.configure(bg='gold'))
RBBrush.bind('<Enter>', lambda event: RBBrush.configure(bg='gold'))
RBRect.bind('<Enter>', lambda event: RBRect.configure(bg='gold'))
RBElip.bind('<Enter>', lambda event: RBElip.configure(bg='gold'))
RBEras.bind('<Enter>', lambda event: RBEras.configure(bg='gold'))
RBStar.bind('<Enter>', lambda event: RBStar.configure(bg='silver'))
RB5angle.bind('<Enter>', lambda event: RB5angle.configure(bg='silver'))
RBRomb.bind('<Enter>', lambda event: RBRomb.configure(bg='silver'))
RBPshik.bind('<Enter>', lambda event: RBPshik.configure(bg='silver'))
RBPen.bind('<Leave>', lambda event: RBPen.configure(bg='white'))
RBBrush.bind('<Leave>', lambda event: RBBrush.configure(bg='white'))
RBRect.bind('<Leave>', lambda event: RBRect.configure(bg='white'))
RBElip.bind('<Leave>', lambda event: RBElip.configure(bg='white'))
RBEras.bind('<Leave>', lambda event: RBEras.configure(bg='white'))
RBStar.bind('<Leave>', lambda event: RBStar.configure(bg='white'))
RB5angle.bind('<Leave>', lambda event: RB5angle.configure(bg='white'))
RBRomb.bind('<Leave>', lambda event: RBRomb.configure(bg='white'))
RBPshik.bind('<Leave>', lambda event: RBPshik.configure(bg='white'))
window.mainloop()
