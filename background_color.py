import tkinter as tk

def change_bg_color():
    color = color_entry.get()
    root.config(bg=color)

root = tk.Tk()
root.title("Background Color Changer")

# Entry for user to input color
color_entry = tk.Entry(root)
color_entry.pack(pady=10)

# Button to change background color
change_button = tk.Button(root, text="Change Background Color", command=change_bg_color)
change_button.pack(pady=5)

root.mainloop()
