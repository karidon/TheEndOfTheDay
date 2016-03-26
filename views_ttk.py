import tkinter as tk
from timer import Timer

'''
 Valid resource names: background, bd, bg, borderwidth, class,
        colormap, container, cursor, height, highlightbackground,
        highlightcolor, highlightthickness, relief, takefocus, visual, width."""
'''


class ApplicationTop(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(side='top')
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self)
        self.label['font'] = 'arial 16'
        self.label['fg'] = 'black'
        self.label['text'] = 'До окончания рабочего дня:'
        self.label.pack(side='bottom')


class ApplicationExpand(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True)
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self)
        self.label['font'] = 'arial 72'
        self.label['fg'] = '#8ffe09'
        self.label.pack()
        self.tmp = None
        self.label.after_idle(self.tick)

    def tick(self):
        '''
        Returns time functions
        :return: str
        '''
        self.tmp = self.label.after(200, self.tick)
        self.label['text'] = timer.considers_time_difference()

        if self.label['text'] == '':
            self.label['text'] = None
            self.label.after_cancel(self.tmp)
            self.smile_view()

    def smile_view(self):
        # im = tk.PhotoImage(file='smile.gif')
        # self.label.after_idle(self.smile_view)
        # self.label['text'] = 'Ok'
        # self.label['image'] = im


        # self.label.pack(side='bottom')
        pass


class ApplicationBottom(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(side='bottom')
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self)
        self.label['font'] = 'arial 14'
        self.label['fg'] = 'black'
        self.label.pack()
        self.label.after_idle(self.display_day)

    def display_day(self):
        '''
        Shows the name of the day.
        :return: str
        '''
        self.label['text'] = timer.name_day()


class ApplicationBottomDown(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(side='bottom')
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self)
        self.label['font'] = 'arial 14'
        self.label['fg'] = 'black'
        self.label.pack()
        self.label.after_idle(self.display_data)

    def display_data(self):
        '''
        Shows the data.
        :return: str
        '''
        self.label['text'] = timer.get_data()


def window_deleted():
    '''
    Close window.
    :return:
    '''
    print('Окно закрыто')
    root.quit()


if __name__ == '__main__':
    timer = Timer()
    root = tk.Tk()
    root.title('Таймер')  # название окна
    root.geometry('500x400+300+200')  # размерм окна
    root.protocol('WM_DELETE_WINDOW',
                  window_deleted)  # обработчик закрытия окна

    app_top = ApplicationTop(master=root)
    app_expand = ApplicationExpand(master=root)
    app_bottom = ApplicationBottom(master=root)
    app_bottom_down = ApplicationBottomDown(master=root)

    root.mainloop()
