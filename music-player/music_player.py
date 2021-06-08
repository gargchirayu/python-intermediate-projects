import os
from tkinter import *
from tkinter import filedialog as fd
from pygame import mixer


class MusicPlayer:
    __root = Tk()
    __thisWidth = 300
    __thisHeight = 300
    __musicFile = False
    __playingState = False

    def __init__(self, **kwargs):
        try:
            self.__thisHeight = kwargs['height']
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        self.__root.geometry('%dx%d' % (self.__thisWidth, self.__thisHeight))
        self.__root.resizable(0, 0)
        self.__root.title('Music')

        # var = StringVar()
        load = Button(self.__root, width=5, height=3, font='Helvetica 12 bold', text='LOAD',
                      highlightbackground='#000000', command=self.load)
        play = Button(self.__root, width=5, height=3, font='Helvetica 12 bold', text='START',
                      highlightbackground='black', command=self.start)
        pause = Button(self.__root, width=5, height=3, font='Helvetica 12 bold', text='PLAY/PAUSE',
                       highlightbackground='black', command=self.pause)
        stop = Button(self.__root, width=5, height=3, font='Helvetica 12 bold', text='STOP',
                      highlightbackground='black', command=self.stop)
        self.play_list = Listbox(self.__root, font='Helvetica 12 bold',
                                 selectmode=SINGLE)

        load.pack(fill='x')
        play.pack(fill='x')
        pause.pack(fill='x')
        # unpause.pack(fill='x')
        stop.pack(fill='x')
        self.play_list.pack(fill='both', expand='yes')

        mixer.init()

    def load(self):
        directory = fd.askdirectory()
        os.chdir(directory)
        song_list = os.listdir()
        pos = 0
        for item in song_list:
            self.play_list.insert(pos, item)
            pos += 1

    def start(self):
        mixer.music.load(self.play_list.get(ACTIVE))
        self.__musicFile = self.play_list.get(ACTIVE)
        mixer.music.play()

    def pause(self):
        if not self.__playingState:
            mixer.music.pause()
            self.__playingState = True
        else:
            mixer.music.unpause()
            self.__playingState = False

    def stop(self):
        mixer.music.stop()

    def run(self):
        self.__root.mainloop()


music = MusicPlayer(width=960, height=720)
music.run()
