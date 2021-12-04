from tkinter import *
root = Tk()
root.title("Sales management")
root.geometry("900x900")

root.config(bg="#ffffff")
root.attributes('-alpha',0.750)

Months = ("January","February","March","April","May","June","July","August","September","October","November","December")
Profit = (99000,45000,23000,34000,12000,27000,70000,84000,57690,31000,90000,66000)

Lbl_max =Label(root, fg = "black")
Lbl_min =Label(root, fg = "black")
Lbl_month = Label(root, text=Months)
Lbl_Profit = Label(root, text=Profit)


max_profit = max(Profit)
max_profit_index = Profit.index(max_profit)
print(max_profit_index)
max_profit_month = Months[max_profit_index]
print("The maximum profit of " + str(max_profit) + " was recorded in " + str(max_profit_month))

min_profit = min(Profit)
min_profit_index = Profit.index(min_profit)
print(min_profit_index)
min_profit_month = Months[min_profit_index]
print("The minimum profit of " + str(min_profit) + " was recorded in " + str(min_profit_month))

def Calculate():
    global max_profit
    global max_profit_index
    global max_profit_month
    max_profit = max(Profit)
    max_profit_index = Profit.index(max_profit)
    print(max_profit_index)
    max_profit_month = Months[max_profit_index]
    Lbl_max["text"] = "The maximum profit of " + str(max_profit) + " was recorded in " + str(max_profit_month)
    
def calculate():
    global min_profit
    global min_profit_index
    global min_profit_month
    min_profit = min(Profit)
    min_profit_index = Profit.index(min_profit)
    print(max_profit_index)
    min_profit_month = Months[min_profit_index]
    Lbl_min["text"] = "The minimum profit of " + str(min_profit) + " was recorded in " + str(min_profit_month)

btn_Max = Button(root,text = "show min profit",  bg = "salmon", command=Calculate)
btn_Max.place(relx = 0.5, rely = 0.3, anchor=CENTER)

btn_Min = Button(root,text = "show max profit",  bg = "salmon", command=calculate)
btn_Min.place(relx = 0.5, rely = 0.4, anchor=CENTER)

Lbl_max.place(relx = 0.5, rely = 0.6, anchor=CENTER)
Lbl_min.place(relx = 0.5, rely = 0.7, anchor=CENTER)
Lbl_month.place(relx = 0.5, rely = 0.1, anchor=CENTER)
Lbl_Profit.place(relx = 0.5, rely = 0.2, anchor=CENTER)



root.mainloop()