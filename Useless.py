import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Pointless Button")
root.geometry("400x300")

# Function to move the button to a random position and change its label
def move_button():
    # Generate random x, y coordinates
    x = random.randint(0, root.winfo_width() - 100)
    y = random.randint(0, root.winfo_height() - 50)
    
    # Move the button to a new location
    button.place(x=x, y=y)
    
    # Change the button text to something random
    button.config(text=random.choice(["Not Yet!", "Almost!", "Try Again", "Click Me!"]))

# Create the button
button = tk.Button(root, text="Click Me!", command=move_button)
button.place(x=150, y=120)

# Run the main loop
root.mainloop()
