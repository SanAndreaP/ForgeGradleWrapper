import ttk


__author__ = 'SanAndreas'


class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.pack()
        #self.grid()
        self.quitButton = ttk.Button(self, text='Quit', command=self.quit, width=100)
        self.quitButton.pack()

app = Application()
app.master.title('Sample application')
app.mainloop()

