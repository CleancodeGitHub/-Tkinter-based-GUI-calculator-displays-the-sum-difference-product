import tkinter as tk

def calculate():
    try:
        a = int(entry1.get())
        b = int(entry2.get())

        sum_result.set(a + b)
        difference_result.set(a - b)
        product_result.set(a * b)
        quotient_result.set(a / b)
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("calculates their sum")
root.geometry('400x600')

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label1 = tk.Label(frame, text="First number:")
label1.grid(row=0, column=0, sticky="w")

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

label2 = tk.Label(frame, text="Second number:")
label2.grid(row=1, column=0, sticky="w")

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=2, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, columnspan=2)

sum_label = tk.Label(frame, text="Sum:")
sum_label.grid(row=4, column=0, sticky="w")

sum_result = tk.StringVar()
sum_result_label = tk.Label(frame, textvariable=sum_result)
sum_result_label.grid(row=4, column=1, sticky="w")

difference_label = tk.Label(frame, text="Difference:")
difference_label.grid(row=5, column=0, sticky="w")

difference_result = tk.StringVar()
difference_result_label = tk.Label(frame, textvariable=difference_result)
difference_result_label.grid(row=5, column=1, sticky="w")

product_label = tk.Label(frame, text="Product:")
product_label.grid(row=6, column=0, sticky="w")

product_result = tk.StringVar()
product_result_label = tk.Label(frame, textvariable=product_result)
product_result_label.grid(row=6, column=1, sticky="w")

quotient_label = tk.Label(frame, text="Quotient:")
quotient_label.grid(row=7, column=0, sticky="w")

quotient_result = tk.StringVar()
quotient_result_label = tk.Label(frame, textvariable=quotient_result)
quotient_result_label.grid(row=7, column=1, sticky="w" , )


quotient_label_description = tk.Label(frame, text=( "\n" "This tkinter application prompts the user to enter\n"
"two numbers, calculates their sum, difference,\n"
"product, and quotient, and displays the results\n"
"results in the GUI. If the user enters invalid input\n"
"(e.g., non-numeric characters), it displays a\n"
"message prompting the user to enter valid numbers."))
quotient_label_description.grid(row=8, columnspan=2, sticky="w")

root.mainloop()
