import random
import tkinter as tk

root= tk.Tk()
#root.geometry("450x300")
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    start_val = 501
    end_val = 630
    rObj = random.randrange(int(start_val),int(end_val),1)

    label1 = tk.Label(root, text= rObj, fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click me ',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()

#start_val = input("Enter the start value to generate the random number:")
#end_val = input("Enter the end value to generate the random number:")

#print("Start val" + start_val)
#print("End Val" + end_val)

#rObj = random.randrange(int(start_val),int(end_val),1)
#print("Random generated number : " + str(rObj))

#st_label = tk.Label(root,text= "Start Range ").place(x=40,y=60)
#end_label = tk.Label(root,text= "End Range").place(x=40,y=100)#
#start_value = tk.Entry(root,width=30).place(x=110,y=60)
#end_value = tk.Entry(root,width=30).place(x=110,y=100)
#button1 = tk.Button(text='Click me ').place(x=40,y=130)
#3rObj = random.randrange(int(start_value),int(end_value),1)
#3print("Random generated number : " + str(rObj))