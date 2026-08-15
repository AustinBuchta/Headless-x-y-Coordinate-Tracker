import tkinter as tk
import ctypes

SW_HIDE = 0

def hide_my_console():
    try:
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        hWnd = kernel32.GetConsoleWindow()
        if hWnd != 0:
            user32.ShowWindow(hWnd, SW_HIDE)
    except Exception:
        pass

class MovableGreyTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Overlay Container")
        
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        
        self.root.config(bg="#00ff00")
        self.root.attributes("-transparentcolor", "#00ff00")
        
        # Store window dimensions as variables for boundary checking
        self.win_width = 150
        self.win_height = 27
        self.root.geometry(f"{self.win_width}x{self.win_height}+25+25")
        
        self.label = tk.Label(
            root, 
            text="X: 0, Y: 0", 
            font=("Courier", 14, "bold"), 
            fg="white", 
            bg="#1a1a1a",
            bd=0,
            padx=5,
            pady=2
        )
        self.label.place(relx=0.5, rely=0.5, anchor="center")
        
        self.start_x = 0
        self.start_y = 0
        
        # --- INPUT BINDINGS ---
        self.label.bind("<Button-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.drag_window)
        self.label.bind("<Button-3>", self.exit_program)
        self.root.bind("<Escape>", self.exit_program)
        
        self.update_coordinates()

    def start_drag(self, event):
        self.root.focus_set()
        self.start_x = event.x
        self.start_y = event.y

    def drag_window(self, event):
        deltax = event.x - self.start_x
        deltay = event.y - self.start_y
        
        # Target coordinates where the user wants to push the window
        new_x = self.root.winfo_x() + deltax
        new_y = self.root.winfo_y() + deltay
        
        # Get live monitor resolution bounds
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # --- SCREEN EDGE SNAPPING LOGIC ---
        # Left edge snap
        if new_x < 0:
            new_x = 0
        # Right edge snap (Screen Width minus the width of the GUI box)
        elif new_x + self.win_width > screen_width:
            new_x = screen_width - self.win_width
            
        # Top edge snap
        if new_y < 0:
            new_y = 0
        # Bottom edge snap (Screen Height minus the height of the GUI box)
        elif new_y + self.win_height > screen_height:
            new_y = screen_height - self.win_height
        
        # Apply clamped coordinates
        self.root.geometry(f"+{new_x}+{new_y}")

    def update_coordinates(self):
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()
        
        self.label.config(text=f"X:{str(x).rjust(4)} Y:{str(y).rjust(4)}")
        self.root.after(30, self.update_coordinates)

    def exit_program(self, event=None):
        self.root.destroy()

if __name__ == "__main__":
    hide_my_console()
    root = tk.Tk()
    app = MovableGreyTracker(root)
    root.mainloop()