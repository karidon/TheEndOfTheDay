# -*- coding: utf-8 -*-


# TODO 1: отдельно тесты написать
# TODO 2: подправить окно
# TODO 3: подумать как можно запускать при вкл компа
# TODO 4: упоковать в установщик

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-21'

import tkinter

from tkinter import ttk

from timer import Timer


def tick():
    '''
    Returns time functions
    :return: str
    '''
    label2.after(200, tick)
    label2['text'] = timer.considers_time_difference()


def display_day():
    '''
    Shows the name of the day.
    :return: str
    '''
    label3['text'] = timer.name_day()


def display_data():
    '''
    Shows the data.
    :return: str
    '''
    label4['text'] = timer.get_data()


def window_deleted():
    '''
    Close window.
    :return:
    '''
    print('Окно закрыто')
    root.quit()


if __name__ == '__main__':
    timer = Timer()

    root = tkinter.Tk()

    style = ttk.Style()
    style.configure("BW.TLabel", foreground="black", font='arial 16')
    style.configure("BW2.TLabel", foreground="#8ffe09", font='arial 72 ')
    style.configure("BW3.TLabel", foreground="black", font='arial 14')

    root.title('Таймер')  # название окна
    root.geometry('500x400+300+200')  # размерм окна
    root.state('zoomed')  # разварачиваем окно
    #root.state('normal')  # разварачиваем окно

    root.protocol('WM_DELETE_WINDOW',
                  window_deleted)  # обработчик закрытия окна

    label = ttk.Label(root, text='До окончания рабочего дня:', style="BW.TLabel")
    label.pack(side='top')

    label2 = ttk.Label(root, style="BW2.TLabel")  # размер шрифта таймера
    label2.pack(expand=True)
    label2.after_idle(tick)

    label3 = ttk.Label(root, style="BW3.TLabel")
    label3.pack(side='bottom')
    label3.after_idle(display_day)

    label4 = ttk.Label(root, style="BW3.TLabel")
    label4.pack(side='bottom')
    label4.after_idle(display_data)

    root.mainloop()

