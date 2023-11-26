# Import

import customtkinter as ctk
from tkinter import PhotoImage, Label, Text, Canvas, ttk
import tkinter as tk

# Main Window

app = ctk.CTk()
app.title('Fruit Shop')
app.geometry("900x500")
app.config(bg="#FFB9B9")
app.resizable(False, False)

# Fonts

font1= ("Christmas Day", 40)
font2= ("Bell MT", 18,'bold')
font3= ("Bell MT", 16,"italic")
font4= ("Christmas Day", 60)
font5= ("Bell MT", 25,'bold')

# Image

apple_image=PhotoImage(file="apples.png").subsample(3,3)

# Heading

store_label = ctk.CTkLabel(app, text="Fruit Store", font=font4, text_color="#9E4244", bg_color="#FFB9B9").place(x=315, y=15)

# Frames

store_frame = ctk.CTkFrame(app, bg_color="#FFB9B9", fg_color ='#FFDDD2', corner_radius=10, width=500, height=350).place(x=365,y=100)
calculator_frame = ctk.CTkFrame(app, bg_color='#FFB9B9', fg_color="#FFDDD2", width=320, height=350).place(x=35,y=100)
result_frame = ctk.CTkFrame(app, width=450, height=100, fg_color="#F1C5C5", bg_color="#FFDDD2", corner_radius=30)
result_frame.place(x=390, y=250)
result_frame.pack_propagate(False)  

# Store Frame

apple_button=ctk.CTkLabel(store_frame, text="",font=font2,fg_color="#FFDDD2",bg_color="#FDCEDF",text_color="black", width=3, height=7,image=apple_image, compound= "top").place(x=75, y=100)
price_label= ctk.CTkLabel(store_frame, text="How much for an apple?", font=font2, text_color="#9E4244", bg_color="#FFDDD2").place(x=100, y=320)
price_entry = ctk.CTkEntry(app, font=font1, corner_radius=10,  text_color="#9E4244",justify="center", fg_color="#F1C5C5", bg_color="#FFDDD2", border_width=0, width=200)
price_entry.place(x=95, y=355)

# Bill Frame

money_label=ctk.CTkLabel(calculator_frame, text="How much money do you have?", font=font2, text_color="#9E4244", bg_color="#FFDDD2").place(x=390, y=110)
money_entry = ctk.CTkEntry(app, font=font1, corner_radius=10,  text_color="#9E4244",justify="center", fg_color="#F1C5C5", bg_color="#FFDDD2", border_width=0, width=200)
money_entry.place(x=435, y=150)

# Result Frame

result_title_label = ctk.CTkLabel(app, text="RESULT:", font=font5, text_color="#9E4244", bg_color="#FFDDD2").place(x=390, y=215)
result_label = Label(result_frame, text="", font=font2, bg='#F1C5C5', fg='#9E4244')
result_label.pack(pady=1)

# Commands
def reset ():
    price_entry.delete(0, 'end')
    money_entry.delete(0, 'end')
    result_label.config(text="")

def pay():
    try:
        user_price = int(price_entry.get())
        user_money = int(money_entry.get())

        if user_money < user_price:
            result_label.config(text="\nAww!\n I'm sorry but that will not be enough. \n Come back when you already have more!")
        elif user_price == 0:
            result_label.config(text="\nAww!\nYou're out of money already Time to save up for more apples!")
        elif user_money == user_price:
            result_label.config(text="\nGreat!\n You'll have exactly 1 apple. \n Come around again!")
        elif user_money % user_price == 0:
            quantity_apples = user_money // user_price
            result_label.config(text=f"\nHmm...\nLooks like {quantity_apples} apples can be bought with your money. \nEnjoy!")
        else:
            max_apple_quantity = user_money // user_price
            money_change = user_money % user_price
            result_label.config(text=f"\nHmm... \n Looks like {max_apple_quantity} apples can be bought with your money. \n Given that, you'll have ₱{money_change} left.")

    except ValueError:
        result_label.config(text="\n""\n Please enter valid numeric values.")

# Buttons

calculate_button=ctk.CTkButton(store_frame, command=pay, text="CALCULATE", font=font2,fg_color="#FFDDD2", bg_color="#FFDDD2",text_color="#9E4244", border_width=2, border_color="#9E4244", hover_color="#D8AC9C").place(x=655, y=160)
okay_button=ctk.CTkButton(store_frame, command=app.destroy, text="OKAY", font=font2,fg_color="#FFDDD2", bg_color="#FFDDD2",text_color="#9E4244", border_width=2, border_color="#9E4244", hover_color="#D8AC9C").place(x=450, y=385)
new_button=ctk.CTkButton(store_frame, command=reset, text="NEW", font=font2,fg_color="#FFDDD2", bg_color="#FFDDD2",text_color="#9E4244", border_width=2, border_color="#9E4244", hover_color="#D8AC9C").place(x=640, y=385)

app.mainloop()