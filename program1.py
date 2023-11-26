# Import

import customtkinter
from tkinter import *
from tkinter import messagebox
import openpyxl as xl

# Window Set-up

window=customtkinter.CTk ()
window.title("Fruit Store")
window.geometry("900x500")
window.config(bg="#FFB9B9")
window.resizable (False, False)

# Fonts

font1= ("Christmas Day", 60)
font2= ("Bell MT", 20,'bold')
font3= ("Bell MT", 16,"italic")

# Price List

apple_price = 20
orange_price = 25

# Images

orange_image=PhotoImage(file="oranges.png").subsample(3, 3)
apple_image=PhotoImage(file="apples.png").subsample(3,3)

# Commands

def cancel():
    apple_variable.set(0)
    orange_variable.set(0)
    variable_pay.set(0)

def pay ():
    variable_pay=apple_variable.get()*apple_price+orange_variable.get()*orange_price
    total_label=customtkinter.CTkLabel(bill_frame,text=variable_pay, font=font1, text_color="#9E4244", bg_color="#F3C5C5").place(x=680, y=145)

def confirm():
    pop_up_window = Toplevel (window)
    pop_up_window.title("Order Confirmation")
    pop_up_window.geometry("500x200")
    pop_up_window.configure(bg="#FFB9B9")
    alert =Label(pop_up_window, text="Order confirmed! Thank you for your purchase!",fg='black',border=0, bg='#FFB9B9',font=font3).place(x=70, y=40)
    button1= Button(pop_up_window, text="Okay!",width=15, pady=7,bg='gray', fg='black', border=0, command=window.destroy).place(x=180, y=90)
    alert.pack()
    button1.pack()
    pop_up_window.mainloop ()

# Store and Bill Frame

store_label = customtkinter.CTkLabel(window, text="Fruit Store", font=font1, text_color="#9E4244", bg_color="#FFB9B9").place(x=300, y=15)
store_frame = customtkinter.CTkFrame(window, bg_color="#FFB9B9", fg_color ='#FFDDD2', corner_radius=10, width=500, height=350).place(x=40,y=100)
bill_frame = customtkinter.CTkFrame(window, bg_color='#FFB9B9', fg_color="#FFDDD2", width=310, height=350).place(x=550,y=100)


# Variables

apple_variable=IntVar()
orange_variable=IntVar()
variable_pay=IntVar()

# Store Display
orange_button=customtkinter.CTkLabel(store_frame, text="",font=font2,fg_color="#FFDDD2",bg_color="#FDCEDF",text_color="black", width=5, height=10,image=orange_image, compound= TOP).place(x=50, y=104)
orange_label = customtkinter.CTkLabel(window, text="Php 25/pc", font=font2, text_color="#9E4244", bg_color="#FFDDD2").place(x=117, y=315)

apple_button=customtkinter.CTkLabel(store_frame, text="",font=font2,fg_color="#FFDDD2",bg_color="#FDCEDF",text_color="black", width=3, height=10,image=apple_image, compound= TOP).place(x=280, y=100)
apple_label = customtkinter.CTkLabel(window, text="Php 20/pc", font=font2, text_color="#9E4244", bg_color="#FFDDD2", height=2, width=1).place(x=353, y=315)

quantity_apple=Spinbox(store_frame,from_=0,to=1000, textvariable=apple_variable, font=font2, background="#FDCEDF", justify=CENTER).place(x=450,y=600)
quantity_orange=Spinbox(store_frame,from_=0,to=1000,textvariable=orange_variable, font=font2, background="#FDCEDF", justify=CENTER).place(x=105,y=600)
quantity_label = customtkinter.CTkLabel(store_frame, text="Please choose your preferred quantity for each.", font=font3, text_color="#9E4244", bg_color="#FFDDD2").place(x=139, y=360)
line = Frame(store_frame, height=2, width=620, bg="#9E4244").place(x=113, y=530)

# Bill Display

price_frame=customtkinter.CTkFrame(window, bg_color='#FFB9B9', fg_color="#F3C5C5", width=250, height=70, corner_radius=10).place(x=580,y=145) 
price_label=customtkinter.CTkLabel(bill_frame, text="TOTAL PRICE:", font=font2, text_color="#9E4244", bg_color="#FFDDD2").place(x=565, y=110)
pay_button=customtkinter.CTkButton(bill_frame, command=pay, text="Buy Now", font=font2,fg_color="#FFDDD2", bg_color="#FFDDD2",text_color="#9E4244", border_width=2, border_color="#9E4244", hover_color="white").place(x=628, y=280)
cancel_button=customtkinter.CTkButton(bill_frame,command=cancel, text="Cancel Purchase", font=font2,fg_color="#FFDDD2", bg_color="#FFDDD2",text_color="#9E4244", border_width=2, border_color="#9E4244", hover_color="white").place(x=623, y=330)
new_button=customtkinter.CTkButton(bill_frame, command=confirm, text="Confirm Purchase", font=font2,fg_color="#FFDDD2", bg_color="#FFDDD2",text_color="#9E4244", border_width=2, border_color="#9E4244", hover_color="white").place(x=618, y=380)                            
line = Frame(store_frame, height=2, width=430, bg="#9E4244").place(x=842, y=350)
option_label = customtkinter.CTkLabel(store_frame, text="Please choose one below.", font=font3, text_color="#9E4244", bg_color="#FFDDD2").place(x=570, y=240)

window.mainloop()
