#!/usr/bin/python3

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

WIDTH = 800
HEIGHT = 600



class Stacker(tk.Tk):
    WIDTH = 500
    HEIGHT = 400

    def __init__(self, items=None):
        super().__init__()
        if not items:
            self.items = []
        else:
            self.items = items

        self.title("Stack Visualizer")
        self.geometry("500x400")

        for item in self.items:
            item.pack(side=tk.BOTTOM, fill=tk.X)

        self.item_create= tk.Text(self, height=3, bg="white", fg="black")

        self.item_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.item_create.focus_set()

        self.bind('<Return>', self.new_stack)
        self.color_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}] 


    
    def new_stack(self, event=None):
        item_text = self.item_create.get(1.0, tk.END.strip())

        if len(item_text) > 0:
            new_item = tk.Label(self, text=item_text, pady=10)

            _, item_style_choice = divmod(len(self.items), 2)
            current_style_choice = self.color_schemes[item_style_choice]

            new_item.configure(bg=current_style_choice["bg"])
            new_item.configure(fg=current_style_choice["fg"])

            new_item.pack(side=tk.TOP, fill=tk.X)

            self.items.append(new_item)
        self.item_create.delete(1.0, tk.END)


        pass


if __name__ == "__main__":
    root = Stacker()
    root.mainloop()
