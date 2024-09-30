import time
import os
from tkinter import *

root = Tk()
root.title("Vending Machine")
root.config(bg="black")
root.geometry("550x605+50+50")

item_frame_width = 110
item_frame_height = 100
item_frame_gap = 50

data_frame_width = 110
data_frame_height = 40
data_frame_gap = 5

main_frame = Frame(root, width = 350, height = 450)
main_frame.place(x=5,y=5)

left_frame = Frame(root, width = 185, height = 450)
left_frame.place(x=360, y=5)

bottom_frame = Frame(root, width = 540, height = 140)
bottom_frame.place(x=5, y=460)

keypad_frame = Frame(root, bg="black", width = 175, height = 245)
keypad_frame.place(x=365, y=10)

display_frame = Frame(root, bg="black", width=175, height = 35)
display_frame.place(x=365, y=260)

coins_frame = Frame(root, bg="black", width = 175, height=150)
coins_frame.place(x=365, y=300)

#first item
item1_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item1_frame.place(x=10, y=10)

item1_data = Frame(root, bg="black", width=item_frame_width, height=data_frame_height)
item1_data.place(x=10, y=item_frame_height+15 )

#second item
item2_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item2_frame.place(x=125, y=10)

item2_data = Frame(root, bg="black", width=item_frame_width, height=data_frame_height)
item2_data.place(x=125, y=item_frame_height+15 )

#third item
item3_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item3_frame.place(x=240, y=10)

item3_data = Frame(root, bg="black", width=item_frame_width, height=data_frame_height)
item3_data.place(x=240, y=item_frame_height+15 )

#fourth item
item4_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item4_frame.place(x=10, y=10 + item_frame_height + item_frame_gap)

item4_data = Frame(root, bg="black", width=item_frame_width, height=data_frame_height)
item4_data.place(x=10, y=)

item5_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item5_frame.place(x=125, y=10 + item_frame_height + item_frame_gap)

item6_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item6_frame.place(x=240, y=10 + item_frame_height + item_frame_gap)

# Third row
item7_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item7_frame.place(x=10, y=10 + 2 * (item_frame_height + item_frame_gap))

item8_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item8_frame.place(x=125, y=10 + 2 * (item_frame_height + item_frame_gap))

item9_frame = Frame(root, bg="black", width=item_frame_width, height=item_frame_height)
item9_frame.place(x=240, y=10 + 2 * (item_frame_height + item_frame_gap))



root.mainloop()


    
