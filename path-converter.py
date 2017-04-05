
import tkinter as tk
import os, sys
import re
import pathlib

class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.init_widgets()

    def init_widgets(self):
        self.master.title("Path Converter")
        root.geometry("600x300")

        # ------- frame1
        self.frame1 = tk.Frame(root)

        self.radio1_val=tk.IntVar()
        self.radio1_val.set(0)
        tk.Radiobutton(self.frame1, text="win->mac",
                       variable=self.radio1_val, value=0).pack(side='left')
        tk.Radiobutton(self.frame1, text="mac->win",
                       variable=self.radio1_val, value=1).pack(side='left')
        
        self.frame1.pack(anchor="nw")

        # ------- frame2
        self.frame2 = tk.Frame(root)
        
        self.label1 = tk.Label(self.frame2, text="input")
        self.label1.grid(row=0,column=0)
        self.edit1 = tk.Entry(self.frame2,width=50)
        self.edit1.grid(row=0,column=1)
        self.edit1.insert(tk.END, "入力する文字")
        self.button_clear = tk.Button(self.frame2, text="Clear",
                                      command=self.clear)
        self.button_clear.grid(row=0,column=2)
        
        self.button_convert = tk.Button(self.frame2, text="Convert",
                                        command=self.convert)
        self.button_convert.grid(row=1,column=0)
        self.s2=tk.StringVar()
        self.edit2 = tk.Entry(self.frame2, textvariable=self.s2,
                              width=50)
        self.edit2.grid(row=1,column=1)
        self.edit2.insert(tk.END, "")
        self.button_open = tk.Button(self.frame2, text="Open",
                                     command = self.open)
        self.button_open.grid(row=1,column=2)
        
        self.button_quit = tk.Button(self.frame2, text="Quit",
                                     fg="red", command=root.destroy)
        self.button_quit.grid(row=2,column=2)
        self.message=tk.StringVar()
        self.edit_message = tk.Label(self.frame2, textvariable=self.message,
                                     anchor=tk.W, width=40)
        self.edit_message.grid(row=3,column=0,columnspan=3,sticky="w")
        self.frame2.pack()

    def convert(self):
        s1 = self.edit1.get()
        s2 = ""
        if self.is_win2mac(): # win2mac
            s2 = re.sub(r"\\", '/', re.sub(r"\\\\",'smb://',s1))
        else: #mac2win
            s2 = re.sub("/", r"\\", re.sub('smb://',r"\\\\",s1))
        self.s2.set(s2)
        
        self.show_message("hello [%s] [%s]" % (s1, s2))
    def clear(self):
        self.show_message("clear")
        self.edit1.delete(0, tk.END)
        self.edit2.delete(0, tk.END)

    def is_win2mac(self):
        return self.radio1_val.get()==0
    def open(self):
        path = self.edit2.get().strip()
        command = "open \"%s\"" % path if self.is_win2mac() \
                  else "explorer %s" % path
        # self.show_message(command)
        os.system(command)
            
    def show_message(self,s):
        self.message.set(s)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(master=root)
    app.mainloop()
    
        
