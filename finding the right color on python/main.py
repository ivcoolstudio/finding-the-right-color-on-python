import time
import numpy
from mss import mss
import pyautogui

# область экрана с отступом
monitor = {
    "left": 30,
    "top": 50,
    "width": 900,
    "height": 1000,
}


# Поиск цвета на экране
def find_color(our_color, monitor={}):
    # Возмём кусок экрана
    m = mss()

    # Получаем пиксель с экрана монитора
    img = m.grab(monitor)

    # Преобразуем этот пиксель в матрицу
    img_arr = numpy.array(img)

    # Поиск цвета (b, g, r, alpha)
    our_map = (our_color[2], our_color[1], our_color[0], 255)
    indexes = numpy.where(numpy.all(img_arr == our_map, axis=-1))
    our_crd = numpy.transpose(indexes)
    return our_crd


# Искомый цвет
our_color = [75,90,110]


while True:
    result = find_color(our_color, monitor)
    if result.__len__():
        x = result[0][1] + monitor.get('left')
        y = result[0][0] + monitor.get('top')
        print([x, y])
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)

    # Ожидание
    time.sleep(3)