import tkinter as tk
import logic

def create_gui():
    root = tk.Tk()
    root.title("Calculator")
    root.configure(bg="#1E1E1E")  # Set background color

    # Entry widget for displaying the calculation result
    entry = tk.Entry(root, width=30, borderwidth=2, font=("Arial", 18), justify="right", bg="#2E2E2E", fg="#FFFFFF")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

    # Button labels and corresponding grid positions
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
    ]

    # Function to handle button clicks
    def button_click(value):
        if value == '=':
            try:
                result = logic.evaluate_expression(entry.get())
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            except Exception as e:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
        elif value == 'C':
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, value)

    # Create buttons and attach click event handlers
    for button in buttons:
        text, row, column = button
        button_bg = "#2E2E2E"  # Set button background color
        button_fg = "#FFFFFF"  # Set button text color
        button_width = 10  # Set button width
        button_height = 3  # Set button height
        button_font = ("Arial", 14)  # Set button font
        button_borderwidth = 2  # Set button border width
        button_relief = "flat"  # Set button relief style to flat

        button = tk.Button(root, text=text, padx=10, pady=10, font=button_font, bg=button_bg, fg=button_fg,
                           width=button_width, height=button_height, borderwidth=button_borderwidth,
                           relief=button_relief, command=lambda value=text: button_click(value))
        button.grid(row=row, column=column, sticky="nsew")

    # Make all rows and columns expandable
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
