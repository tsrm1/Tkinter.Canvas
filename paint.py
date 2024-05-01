# https://www.youtube.com/watch?v=pHTIFxGQAws
# https://www.youtube.com/watch?v=R4bu1R2LE8k
from tkinter import Canvas, Tk, Button, N,W,S,E, filedialog, messagebox



canvas_width = 1280
canvas_height = 720
brush_size = 3
color = "white"

def paint(event):
    global brush_size, color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    window.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def brush_size_change(new_size):
    global brush_size
    brush_size = new_size

def color_change(new_color):
    global color
    color = new_color

def save_file():
    # from PIL import Image
    # window.postscript(file='my_drawing.ps', colormode='color')
    # img = Image.open("my_drawing.ps")
    # img.save("my_drawing.png", "png")

    import PIL.ImageGrab as ImageGrab



    try: 
        filename = filedialog.asksaveasfilename(defaultextension='.png')
        x = root.winfo_rootx() + window.winfo_x()
        y = (root.winfo_rooty() + window.winfo_y())

        x1 = x + window.winfo_width()
        y1 = y + window.winfo_height()

        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
        messagebox.showinfo('Сохранить рисунок',
            'Изображение сохранено в: ' + str(filename) )
    except:
        messagebox.showerror('Сохранить рисунок', 
            'Изображение не сохранено\nОшибка')



root =Tk()
root.title("Paint on Python")


window = Canvas(root,  width=canvas_width, height=canvas_height, bg='black')
window.bind("<B1-Motion>", paint)   # B1 - левая кнопка мыши
window.bind("<B3-Motion>", paint)   # B3 - правая кнопка мыши

btn_red = Button(text='Red', width=10, command=lambda: color_change('red'))
btn_orange = Button(text='Orange', width=10, command=lambda: color_change('orange'))
btn_yellow = Button(text='Yellow', width=10, command=lambda: color_change('yellow'))

btn_green = Button(text='Green', width=10, command=lambda: color_change('green'))
btn_cyan = Button(text='Cyan', width=10, command=lambda: color_change('cyan'))
btn_blue = Button(text='Blue', width=10, command=lambda: color_change('blue'))
btn_white = Button(text='White', width=10, command=lambda: color_change('white'))
btn_black = Button(text='Gummy', width=10, command=lambda: color_change('black'))
btn_erase = Button(text='Erase', width=10, command=lambda: window.delete('all'))
btn_save = Button(text='Save', width=10, command=save_file)

btn_3 = Button(text="3", width=10, command=lambda: brush_size_change(3))
btn_5 = Button(text="5", width=10, command=lambda: brush_size_change(5))
btn_8 = Button(text="8", width=10, command=lambda: brush_size_change(8))
btn_10 = Button(text="10", width=10, command=lambda: brush_size_change(10))
btn_12 = Button(text="12", width=10, command=lambda: brush_size_change(12))
btn_14 = Button(text="14", width=10, command=lambda: brush_size_change(14))
btn_16 = Button(text="16", width=10, command=lambda: brush_size_change(16))
btn_18 = Button(text="18", width=10, command=lambda: brush_size_change(18))
btn_20 = Button(text="20", width=10, command=lambda: brush_size_change(20))

window.grid(row=2, column=0, columnspan=11, padx=5, pady=5, sticky=N+W+S+E)
window.columnconfigure(6, weight=1)
window.rowconfigure(2, weight=1)

btn_red.grid(row=0, column=0)
btn_orange.grid(row=0, column=1)
btn_yellow.grid(row=0, column=2)
btn_green.grid(row=0, column=3)
btn_cyan.grid(row=0, column=4)
btn_blue.grid(row=0, column=5)
btn_white.grid(row=0, column=6)
btn_black.grid(row=0, column=7)
btn_erase.grid(row=0, column=8)
btn_save.grid(row=0, column=10)

btn_3.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_8.grid(row=1, column=2)
btn_10.grid(row=1, column=3)
btn_12.grid(row=1, column=4)
btn_14.grid(row=1, column=5)
btn_16.grid(row=1, column=6)
btn_18.grid(row=1, column=7)
btn_20.grid(row=1, column=8)

root.mainloop()