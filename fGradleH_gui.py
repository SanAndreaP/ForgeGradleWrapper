import ttk
import Tkinter

__author__ = 'SanAndreas'


class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.quitButton = Tkinter.Button(self, text='Quit', command=self.quit, width=100)
        self.btnImg = Tkinter.PhotoImage(file="test_button.png")
        self.quitButton.config(image=self.btnImg, width="389", height="34")
        self.quitButton.pack()

root = Tkinter.Tk()
app = Application(root)
app.master.title('Sample application')
root.geometry('640x480')
app.mainloop()

