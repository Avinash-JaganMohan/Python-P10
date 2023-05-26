import tkinter as tk
import math
import re

class My_Gui:
    def __init__(self):

        self.pow_bool = False
        self.power = ""
        self.pow_number = ""
        self.actual_expression = ""
        self.evaluation_expression = ""
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Scientific Calculator")
        self.root.resizable(False, False)

        self.display = tk.Text(self.root, height=2, width=40, font=("Arial", 16))
        self.display.grid(columnspan=6, padx=10, pady=10)

        self.bt_1 = tk.Button(self.root, text="1", command = lambda: self.add_Expression("1"), width=10, height=4)
        self.bt_1.grid(row=2, column=1)

        self.bt_2 = tk.Button(self.root, text="2", command = lambda: self.add_Expression("2"), width=10, height=4)
        self.bt_2.grid(row=2, column=2)

        self.bt_3 = tk.Button(self.root, text="3", command = lambda: self.add_Expression("3"), width=10, height=4)
        self.bt_3.grid(row=2, column=3)

        self.bt_4 = tk.Button(self.root, text="4", command = lambda: self.add_Expression("4"), width=10, height=4)
        self.bt_4.grid(row=3, column=1)

        self.bt_5 = tk.Button(self.root, text="5", command = lambda: self.add_Expression("5"), width=10, height=4)
        self.bt_5.grid(row=3, column=2)

        self.bt_6 = tk.Button(self.root, text="6", command = lambda: self.add_Expression("6"), width=10, height=4)
        self.bt_6.grid(row=3, column=3)

        self.bt_7 = tk.Button(self.root, text="7", command = lambda: self.add_Expression("7"), width=10, height=4)
        self.bt_7.grid(row=4, column=1)

        self.bt_8 = tk.Button(self.root, text="8", command = lambda: self.add_Expression("8"), width=10, height=4)
        self.bt_8.grid(row=4, column=2)

        self.bt_9 = tk.Button(self.root, text="9", command = lambda: self.add_Expression("9"), width=10, height=4)
        self.bt_9.grid(row=4, column=3)

        self.bt_minus = tk.Button(self.root, text="-", command = lambda: self.add_Expression("-"), width=10, height=4)
        self.bt_minus.grid(row=2, column=4)

        self.bt_plus = tk.Button(self.root, text="+", command = lambda: self.add_Expression("+"), width=10, height=4)
        self.bt_plus.grid(row=3, column=4)

        self.bt_multiply = tk.Button(self.root, text="*", command = lambda: self.add_Expression("*"), width=10, height=4)
        self.bt_multiply.grid(row=4, column=4)

        self.bt_0 = tk.Button(self.root, text="0", command = lambda: self.add_Expression("0"), width=10, height=4)
        self.bt_0.grid(row=5, column=1)

        self.bt_clear = tk.Button(self.root, text="Clear", command = self.clear_Expression, width=10, height=4)
        self.bt_clear.grid(row=5, column=2)

        self.bt_dot = tk.Button(self.root, text=".", command = lambda: self.add_Expression("."), width=10, height=4)
        self.bt_dot.grid(row=5, column=3)

        self.bt_divide = tk.Button(self.root, text="/", command = lambda: self.add_Expression("/"), width=10, height=4)
        self.bt_divide.grid(row=5, column=4)

        self.bt_equal = tk.Button(self.root, bg="#0096FF", fg="#FFFFFF", text="=", command = self.evaluate_Expression, width=10, height=4)
        self.bt_equal.grid(row=6, column=1)

        self.bt_sin = tk.Button(self.root, text="Sin", command = lambda: self.add_Math_Expression("sin"), width=10, height=4)
        self.bt_sin.grid(row=6, column=2)

        self.bt_cos = tk.Button(self.root, text="Cos", command = lambda: self.add_Math_Expression("cos"), width=10, height=4)
        self.bt_cos.grid(row=6, column=3)

        self.bt_open = tk.Button(self.root, text="(", command = lambda: self.add_Expression("("), width=10, height=4)
        self.bt_open.grid(row=6, column=4)
        
        self.bt_close = tk.Button(self.root, text=")", command = lambda: self.add_Expression(")"), width=10, height=4)
        self.bt_close.grid(row=2, column=5)

        self.bt_log = tk.Button(self.root, text="log", command = lambda: self.add_Math_Expression("log"), width=10, height=4)
        self.bt_log.grid(row=3, column=5)

        self.bt_exp = tk.Button(self.root, text="exp", command = lambda: self.add_Expression("exp"), width=10, height=4)
        self.bt_exp.grid(row=4, column=5)

        self.bt_pow = tk.Button(self.root, text="^", command = lambda: self.add_Pow("^"), width=10, height=4)
        self.bt_pow.grid(row=5, column=5)

        self.bt_tan = tk.Button(self.root, text="tan", command = lambda: self.add_Math_Expression("tan"), width=10, height=4)
        self.bt_tan.grid(row=6, column=5)

        self.root.mainloop()

    def add_Expression(self, element):
        if(self.pow_bool and element.isdigit()):
            self.actual_expression += element
            self.power += element 
            self.display.delete("1.0", tk.END)
            self.display.insert(tk.END, self.actual_expression)
        
        elif(self.pow_bool and not element.isdigit()):
            self.actual_expression = re.sub(r'\d+$', '', self.actual_expression)
            self.actual_expression += self.power + element
            self.evaluation_expression += f"math.pow({self.pow_number}, {self.power}){element}"
            self.pow_bool = False
            self.power = ""
            print(self.evaluation_expression)
            self.display.delete("1.0", tk.END)
            self.display.insert(tk.END, self.actual_expression)
            
        else:   
            self.actual_expression += element
            self.evaluation_expression += element
            print(self.evaluation_expression)
            self.display.delete("1.0", tk.END)
            self.display.insert(tk.END, self.actual_expression)
    
    def clear_Expression(self):
        self.display.delete("1.0", tk.END)
        self.actual_expression = ""
        self.evaluation_expression = ""

    def evaluate_Expression(self):
        if(self.pow_bool):
            self.evaluation_expression += f"math.pow({self.pow_number}, {self.power})"
        result = eval(self.evaluation_expression)
        print(result)
        self.display.delete("1.0", tk.END)
        self.display.insert(tk.END, str(result))

    def add_Math_Expression(self, element):
        self.actual_expression += element
        math_key_word = "math."
        self.evaluation_expression += (math_key_word + element)
        print(self.evaluation_expression)
        self.display.delete("1.0", tk.END)
        self.display.insert(tk.END, self.actual_expression)

    def add_Pow(self, element):
        number_list = []
        number = ""
        self.actual_expression += element
        for char in self.actual_expression:
            if char.isdigit():
                number += char
            else:
                number_list.append(number)
                number = ""

        self.pow_number = number_list[len(number_list) - 2]
        self.evaluation_expression = re.sub(r'\d+$', '', self.evaluation_expression)
        self.pow_bool = True
        print(self.evaluation_expression)
        self.display.delete("1.0", tk.END)
        self.display.insert(tk.END, self.actual_expression)
My_Gui()