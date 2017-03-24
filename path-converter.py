import re
import tkinter as tk

class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.init_widgets()

    def init_widgets(self):
        self.master.title("Hello Tkinter")
        root.geometry("400x300")


        self.frame1 = tk.Frame(root)

        self.radio1_val=tk.IntVar()
        self.radio1_val.set(0)
        tk.Radiobutton(self.frame1, text="win->mac",
                       variable=self.radio1_val, value=0).pack()
        tk.Radiobutton(self.frame1, text="mac->win",
                       variable=self.radio1_val, value=1).pack()
        
        self.label1 = tk.Label(self.frame1, text="入力文字")
        self.label1.pack()

        self.edit1 = tk.Entry(self.frame1, bg='red', width=50)
        self.edit1.insert(tk.END, "入力する文字")
        self.edit1.pack()

        self.button_convert = tk.Button(self.frame1, text="Convert",
                                        command=self.convert)
        self.button_convert.pack()

        self.label2 = tk.Label(self.frame1, text="出力文字")
        self.label2.pack()

        self.s2=tk.StringVar()
        self.edit2 = tk.Entry(self.frame1, textvariable=self.s2,
                              bg='red', width=50)
        self.edit2.insert(tk.END, "出力する文字")
        self.edit2.pack()


        
        self.button_quit = tk.Button(self.frame1, text="Quit",
                                     fg="red", command=root.destroy)
        self.button_quit.pack(side="bottom")

        self.frame1.pack()

    def convert(self):
        s1 = self.edit1.get()
        s2 = ""
        if self.radio1_val.get()==0: # win2mac
            s2 = re.sub(r"\\", '/', re.sub(r"\\\\",'smb://',s1))
        else: #mac2win
            s2 = re.sub("/", r"\\", re.sub('smb://',r"\\\\",s1))
        self.s2.set(s2)
        
        print("hello [%s] [%s]" % (s1, s2))
        
if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(master=root)
    app.mainloop()
    
        
