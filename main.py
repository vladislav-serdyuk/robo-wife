# робожена 2.4 стабильная
import assistail  # потключаем ассистента
import see  # и зрение
import tkinter
import time


def delete_window() -> None:
    """
    Новый протокол закрытия.
    Прощается.
    :return: None
    """
    assistail.speak('До свидания')
    root.destroy()


if __name__ == '__main__':
    root = tkinter.Tk()  # создание окна
    root.title('Robowife')
    root.overrideredirect(True)  # delete - o x
    root.state('zoomed')  # full screen
    root.protocol('WM_DELETE_WINDOW', delete_window)

    canvas_width = 1600
    canvas_height = 900

    c = tkinter.Canvas(root, width=canvas_width, height=canvas_height)  # холста
    image = tkinter.PhotoImage(file="robowife.gif")
    c.create_image(0, 0, image=image, anchor=tkinter.NW)  # изображения
    c.pack()

    cam = see.on_cam()

    while see.find_faces(cam) == 0:  # ждём пока не найдом лица
        time.sleep(0.1)

    see.off_cam(cam)

    root.after(50, assistail.start)  # ассистент здоровается и слушает в фоне

    root.mainloop()
