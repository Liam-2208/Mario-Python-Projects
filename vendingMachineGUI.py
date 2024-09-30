import time
import os
from tkinter import *

root = Tk()
root.title("Vending Machine")
root.config(bg="black")
root.geometry("550x605+50+50")

frame_width = 110
frame_height = 100
gap = 50

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

# First row
item1_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item1_frame.place(x=10, y=10)

item2_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item2_frame.place(x=125, y=10)

item3_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item3_frame.place(x=240, y=10)

# Second row
item4_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item4_frame.place(x=10, y=10 + frame_height + gap)

item5_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item5_frame.place(x=125, y=10 + frame_height + gap)

item6_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item6_frame.place(x=240, y=10 + frame_height + gap)

# Third row
item7_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item7_frame.place(x=10, y=10 + 2 * (frame_height + gap))

item8_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item8_frame.place(x=125, y=10 + 2 * (frame_height + gap))

item9_frame = Frame(root, bg="black", width=frame_width, height=frame_height)
item9_frame.place(x=240, y=10 + 2 * (frame_height + gap))



root.mainloop()


    
