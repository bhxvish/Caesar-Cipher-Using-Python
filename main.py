import tkinter as tk
from gui_components import CaesarCipherGUI
from gui_constants import GUI_TITLE

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.title(GUI_TITLE)
    root.mainloop()
