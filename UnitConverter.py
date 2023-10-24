from tkinter import *
from math import *


root = Tk()
root.title("UNIT CONVERTOR")
root.geometry("400x800")


def length_convert():
    x = float(length_entry.get())
    from_ = from_length_var.get()
    to_ = to_unit_var.get()
    factors = {
            "Meters": 1.0,
            "Feet": 3.28084,
            "Inches": 39.3701,
            "Centimeters": 100.0,
            "Angstrom":pow(10,-10),
            "Millimeters":1000.0,
            "Mile":0.000621371
    }
    result = x * factors[from_]/factors[to_]
    result_length.config(text=f"{x} {from_} = {result:} {to_}")

def temp_convert():
    x = float(temp_entry.get())
    from_ = from_temp_var.get()
    to_ = to_temp_var.get()

    # Conversion formulas for temperature units (Celsius to Fahrenheit and vice versa)
    result = 0
    if from_=="Celsius" and to_=="Fahrenheit":
        result = (x*9/5)+32
    elif from_=="Fahrenheit" and to_=="Celsius":
        result = (x-32)*5/9
    elif from_=="Kelvin" and to_=="Celsius":
        result = x - 270
    elif from_=="Celsius" and to_=="Kelvin":
        result = x + 270
    elif from_=="Fahrenheit" and to_=="Kelvin":
        result = ((x-32)*5/9) + 270
    elif from_=="Kelvin" and to_=="Fahrenheit":
        result = ((x-32)*5/9) -270
    
    result_temp.config(text=f"{x} {from_} = {result:.2f} {to_}") 


def weight_convert():
    x = float(weight_entry.get())
    from_ = from_weight_var.get()
    to_ = to_weight_var.get()
    factors = {
            "Killogram":pow(10,3),
            "Ounces":0.0353,
            "Pound":0.0022,
            "Tonne":1.102 * pow(10,-6),
            "Gram":1.0,
            "Milligram":1000.0,
            "Gigatonne":1.102 * pow(10,-15),
    }
    result = x * factors[from_]/factors[to_]
    result_weight.config(text=f"{x} {from_} = {result:} {to_}")


def time_convert():
    x = float(time_entry.get())
    from_ = from_time_var.get()
    to_ = to_time_var.get()
    factors = {
            "Second":1.00,
            "Minute":60.00,
            "Hour":3600.00,
            "Nanosecond":pow(10,9),
            "Microsecond":pow(10,6),
            "Millisecond":1000.00,
            "Day":1.157 * pow(10,-5),
            "Week":1.653 * pow(10,-6),
            "Month":3.805 * pow(10,-7),
            "Year":3.171 * pow(10,-8)
    }
    result = x * factors[from_]/factors[to_]
    result_time.config(text=f"{x} {from_} = {result:} {to_}")
    
    
#LENGTH CHANGE

length = Label(root,text="CHANGE LENGTH").pack()

length_entry = Entry(root)
length_entry.pack()

from_length_var = StringVar()
from_length_var.set("Meters")
from_length_menu = OptionMenu(root, from_length_var, "Meters", "Feet", "Inches", "Centimeters","Angstrom","Millimeters","Mile").pack()

to_unit_var = StringVar()
to_unit_var.set("Feet")
to_unit_menu = OptionMenu(root, to_unit_var, "Meters", "Feet", "Inches", "Centimeters","Angstrom","Millimeters","Mile").pack()

length_btn = Button(root,text="CONVERT",command=length_convert).pack(pady=20)
result_length = Label(text="")
result_length.pack()

#TEMPERATURE CHANGE

Temperature = Label(root, text="CHANGE TEMPERATURE").pack()

temp_entry = Entry(root)
temp_entry.pack()

from_temp_var = StringVar()
from_temp_var.set("Celsius")
from_temp_menu = OptionMenu(root, from_temp_var,"Celsius","Farhaneit","Kelvin").pack()

to_temp_var = StringVar()
to_temp_var.set("Farhaneit")
to_temp_menu = OptionMenu(root, to_temp_var,"Celsius","Frahaneit","Kelvin").pack()

temp_btn = Button(root,text="CONVERT",command=temp_convert).pack(pady=20)
result_temp = Label(text="")
result_temp.pack()

#WEIGHT CHANGE

Weight = Label(root, text="CHANGE WEIGHT").pack()

weight_entry = Entry(root)
weight_entry.pack()

from_weight_var = StringVar()
from_weight_var.set("Gram")
from_weight_menu = OptionMenu(root, from_weight_var,"Killogram","Ounces","Pound","Gram","Milligram","Gigatonne","Tonne").pack()

to_weight_var = StringVar()
to_weight_var.set("Killogram")
to_weight_menu = OptionMenu(root, to_weight_var,"Killogram","Ounces","Pound","Gram","Milligram","Gigatonne","Tonne").pack()

weight_btn = Button(root,text="CONVERT",command=weight_convert).pack(pady=20)
result_weight = Label(text="")
result_weight.pack()

#TIME CHANGE

time = Label(root, text="CHANGE TIME").pack()

time_entry = Entry(root)
time_entry.pack()

from_time_var = StringVar()
from_time_var.set("Second")
from_time_menu = OptionMenu(root, from_time_var,"Hour","Minute","Second","Nanosecond","Microsecond","Millisecond","Day","Week","Month","Year").pack()

to_time_var = StringVar()
to_time_var.set("Hour")
to_time_menu = OptionMenu(root, to_time_var,"Hour","Minute","Second","Nanosecond","Microsecond","Millisecond","Day","Week","Month","Year").pack()

time_btn = Button(root,text="CONVERT",command=time_convert).pack(pady=20)
result_time = Label(text="")
result_time.pack()




mainloop()