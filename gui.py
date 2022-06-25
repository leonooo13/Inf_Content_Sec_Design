import tkinter as tk
def show():
    print("de")
if __name__=="__main__":
    root=tk.Tk()
    root.geometry("300x200")
    tk.Label(root,text="URL: ").grid(row=0)
    tk.Label(root,text="URL: ",).grid(row=1)
    input1=tk.Entry(root)
    input1.grid(row=0,column=1)
    input2=tk.Entry(root)
    input2.grid(row=1,column=1)
    c1=input1.get()
    c2=input2.get()
    tk.Button(root,text="点击计算",command=show).grid(row=1,column=2)
    tk.Text(root).grid(row=2,column=1)
    root.mainloop()