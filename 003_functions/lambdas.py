import tkinter as tk

"""
Lambdas start with the lambda keyword, continues with the function's 
arguments and after the :, there is the lambda's body.
"""

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def main():
    button = tk.Button(
        frame,
        text = "Click me",
        fg = "red",
        command = lambda: print("Hello world")
    )

    button.pack(side = tk.LEFT)
    root.mainloop()


if __name__ == "__main__":
    main()