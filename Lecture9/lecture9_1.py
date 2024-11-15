import tkinter as tk

def convert_text():
    input_text = entry.get()
    result = ''.join(
        char.upper() if char.islower() else char.lower() if char.isupper() else '' 
        for char in input_text
    )
    output_label.config(text=result)

# Create the main application window
root = tk.Tk()
root.title("Text Converter")

# Set the window size
root.geometry("300x150")

# Create a frame with a blue background
frame = tk.Frame(root, bg="blue", height=20)
frame.pack(fill=tk.X)

# Add the input entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Add the convert button
convert_button = tk.Button(root, text="Convert", command=convert_text, font=("Arial", 12))
convert_button.pack()

# Add the output label
output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack(pady=10)

# Run the application
root.mainloop()
