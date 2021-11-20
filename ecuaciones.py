import tkinter as tk
from math import sqrt
from tkinter.font import Font
from tkinter import * 
ventana = tk.Tk()
ventana.title("Resolución de expresiones")
ventana.geometry('700x500+100+100')
ventana.configure(background='#66806A')
                
Titulo_font = Font(family="Roboto Cn", size=18) 

t1 = tk.Label(ventana, text='Selecciona el tipo de ecuación a resolver', bg = "#B4C6A6", fg="Black",font=Titulo_font)
t1.pack(padx=5, pady= 5,ipadx=5,ipady=5,fill=tk.X)
radioValue = tk.IntVar() 
rdioOne = tk.Radiobutton(ventana, text='Ecuación Lineal', variable=radioValue, value=0, bg="#FFC286") 
rdioOne.place(x=85, y=90, width=200, height=30)
rdioTwo = tk.Radiobutton(ventana, text='Ecuación Cuadratica', variable=radioValue, value=1,bg="#FFC286") 
rdioTwo.place(x=415, y=90, width=200, height=30)
frame1=Frame()
frame1.config(bg="#FFF1AF")
frame1.place(x=50, y=150, width=270, height=150)
frame2=Frame()
frame2.config(bg="#FFF1AF")
frame2.place(x=380, y=150, width=270, height=150)
t2 = tk.Label(ventana, text='Forma: ax + b = 0', bg = "#FFF1AF", fg="Black")
t2.place(x=50, y=160, width=270, height=20)
t3 = tk.Label(ventana, text='Ingrese conficiente a:', bg = "#FFF1AF", fg="Black")
validate_entry = lambda text: text.isdecimal()
t3.place(x=70, y=203, width=150, height=20)
entry1 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
entry1.place(x=220, y=203, width=40, height=20)
t4 = tk.Label(ventana, text='Ingrese conficiente b:', bg = "#FFF1AF", fg="Black")
t4.place(x=70, y=235, width=150, height=20)
entry2 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
entry2.place(x=220, y=235, width=40, height=20)
t6 = tk.Label(ventana, text='Forma: ax² + bx + c = 0', bg = "#FFF1AF", fg="Black")
t6.place(x=380, y=160, width=270, height=20)
t7 = tk.Label(ventana, text='Ingrese conficiente a:', bg = "#FFF1AF", fg="Black")
t7.place(x=390, y=200, width=150, height=20)
entry3 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
entry3.place(x=541, y=200, width=40, height=20)
t8 = tk.Label(ventana, text='Ingrese conficiente b:', bg = "#FFF1AF", fg="Black")
t8.place(x=390, y=230, width=150, height=20)
entry4 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
entry4.place(x=541, y=230, width=40, height=20)
t9 = tk.Label(ventana, text='Ingrese conficiente c:', bg = "#FFF1AF", fg="Black")
t9.place(x=390, y=260, width=150, height=20)
entry5 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
entry5.place(x=541, y=260, width=40, height=20)
texto = tk.Text()
texto.place(x=50, y=370, width=600, height=100)

def resolver():
    if (radioValue.get() == 1):
        a = int(entry3.get())
        b = int(entry4.get())
        c = int(entry5.get())
        # calculamos el discriminante
        discriminante =  b * b - 4 * a * c

        if discriminante < 0: 
            texto.insert(tk.INSERT, f'La ecuación no tiene soluciones reales.')
        else:
            raiz = sqrt(discriminante)      
            x_1 = (-b + raiz) / (2 * a)     
            if discriminante != 0:         
                x_2 = (-b - raiz) / (2 * a) 
                texto.insert(tk.INSERT, f'Las soluciones son: {x_1} y {x_2}.') 
            else:
                texto.insert(tk.INSERT, f'La solución es: x = {x_1}') 
    if (radioValue.get() ==0):
        a = float(entry1.get())
        b = float(entry2.get())

        if a != 0:
            x = (-b/a)
   
            texto.insert(tk.INSERT, 'Solución de la ecuación: x=%4.3f  ' % (x))
        else:
            if  a == 0 and  b != 0:
                texto.insert(tk.INSERT, "La ecuación no tiene solucion:")
            else:
                texto.insert(tk.INSERT, "La ecuación tiene soluciones infinitas. ")

def Limpiar():
    entry5.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.delete(0, tk.END)
    texto.delete("1.0","end")              

boton = tk.Button(ventana, text="Resolver",bg = "#9AE66E", fg="Black", command=resolver)
boton.place(x=70, y=315, width=250, height=35)
boton = tk.Button(ventana, text="Borrar",bg = "#FF6D6D", fg="Black", command=Limpiar)
boton.place(x=380, y=315, width=250, height=35)

t10 = tk.Label(ventana, text='Luis Gonzalez Kevin Ivan', bg = "#66806A", fg="#142F43")
t10.place(x=520, y=480, width=150, height=20)
ventana.mainloop()