import cv2
import cv3
import os


def process_image(image):
    """
    Find face on image
    :param image: cap.read()
    :return: (image, len(faces))
    """
    face_cascade = cv2.CascadeClassifier(
        os.getcwd() + r'\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
    )
    gray = cv3.rgb2gray(image)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10)
    )
    # Рисуем квадраты вокруг лиц
    for (x, y, w, h) in faces:
        cv3.rectangle(image, x, y, x + w, y + h, color=(0, 255, 255), t=2)
    return image, len(faces)


def mainloop():
    cap = on_cam()

    while True:

        frame = cap.read()
        frame, num_face = process_image(frame)
        windows = cv3.Window('Robowife', flag=1)
        windows.imshow(frame)

        if cv3.waitKey(1) == ord('q'):
            break

    off_cam(cap)


def find_faces(cap: cv3.VideoCapture) -> int:
    """
    :param cap: камера
    :return: число лиц
    """
    frame = cap.read()
    frame, num_face = process_image(frame)
    cv3.imshow('Robowife', frame)
    cv3.waitKey(1)
    return num_face


def on_cam():
    """
    вклучает камеру
    :return: камера
    """
    return cv3.VideoCapture(0)


def off_cam(cap: cv3.VideoCapture) -> None:
    """
    выключает камеру
    :param cap: камера
    :return: None
    """
    cap.release()
    cv3.destroy_windows()


if __name__ == '__main__':
    mainloop()
