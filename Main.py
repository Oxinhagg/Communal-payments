import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        
    def init_main(self):
        #Отрисуем тулбар
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)
        
        #Отрисуем грид
        grid_columns = {'payment_date':'Дата', 'summ_of_pay':'Сумма', 'cold_water':'Холодная вода', 'hot_water':'Горячая вода', 
                        'electricity_day':'Электричество день', 'electricity_night':'Электричество ночь', 'ethernet':'Интернет'}
        self.tree = ttk.Treeview(self, columns=list(grid_columns), height=15, show='headings')
        for grid_column,grid_heading in grid_columns.items():
            self.tree.column(grid_column, width=150, anchor=tk.CENTER)
            self.tree.heading(grid_column, text=grid_heading)
        self.tree.pack()

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
    
    def init_child(self):
        self.title('Добавить платеж')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        #Отрисуем лейблы
        label_list = ['Дата:', 'Холодная вода:', 'Горячая вода:', 'Электричество день:', 'Электричество ночь:']
        pos_y = 20
        for i,el in enumerate(label_list):
           if i != 0:
              pos_y += 30
           self.label = None
           self.label = tk.Label(self, text=el)
           self.label.place(x=50, y = pos_y)
       
        #Отрисуем формы входных значений
        self.cal = DateEntry(self, width=18, background='grey', foreground='white', borderwidth=2)
        self.cal.place(x=200, y=20)
        self.entry_cold_water = ttk.Entry(self)
        self.entry_cold_water.place(x=200, y=50)
        self.entry_hot_water = ttk.Entry(self)
        self.entry_hot_water.place(x=200, y=80)
        self.entry_electricity_day = ttk.Entry(self)
        self.entry_electricity_day.place(x=200, y=110)
        self.entry_electricity_night = ttk.Entry(self)
        self.entry_electricity_night.place(x=200, y=140)

        #Отрисуем кнопки
        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=300, y=170)
        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    s = ttk.Style(root)
    s.theme_use('clam')
    app = Main(root)
    app.pack()
    root.title("Коммунальные платежи")
    root.geometry("1050x450+300+200")
    root.resizable(True, True)
    root.mainloop()