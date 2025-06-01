import tkinter as tk
from tkinter import messagebox

def generate_story():
    name = name_entry.get()
    place = place_entry.get()
    animal = animal_entry.get()
    emotion = emotion_entry.get()
    action = action_entry.get()

    if not all([name, place, animal, emotion, action]):
        messagebox.showwarning("Input Error", "Please fill in all fields!")
        return

    story = (
        f"Once upon a time, {name} was galavanting around {place} and ran into a giant {animal} 🐾!\n"
        f"It was {action} around and looked very {emotion}.\n"
        f"So in responce {name} started {action} with it, 'I’ll never go to {place} again!'"
    )
    
    output_box.config(state='normal')
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, story)
    output_box.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Mad Libs Generator")
root.geometry("400x400")

# Labels and input fields
fields = [
    ("Name", "name_entry"),
    ("Place", "place_entry"),
    ("Animal", "animal_entry"),
    ("Emotion", "emotion_entry"),
    ("Action (verb -ing)", "action_entry"),
]

for i, (label_text, var_name) in enumerate(fields):
    tk.Label(root, text=label_text).grid(row=i, column=0, sticky='e', padx=10, pady=5)
    entry = tk.Entry(root, width=25)
    entry.grid(row=i, column=1, padx=10)
    globals()[var_name] = entry  # creates variables like name_entry, etc.

# Generate button
tk.Button(root, text="Generate Story", command=generate_story).grid(row=len(fields), column=0, columnspan=2, pady=10)

# Output text area
output_box = tk.Text(root, height=6, width=45, wrap='word', state='disabled', bg="#f0f0f0")
output_box.grid(row=len(fields)+1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()