import tkinter as tk

class DangerousApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous App")
        
        # Tạo nút "Dangerous"
        self.dangerous_button = tk.Button(root, text="Dangerous", command=self.spawn_windows)
        self.dangerous_button.pack(pady=20)
        
    def spawn_windows(self):
        # Mở vô hạn các cửa sổ con nhỏ
        while True:
            new_window = tk.Toplevel(self.root)
            new_window.title("Dangerous Window")
            label = tk.Label(new_window, text="You cannot close this window!")
            label.pack(padx=30, pady=20)
            new_window.geometry("200x100")
            new_window.protocol("WM_DELETE_WINDOW", lambda: None)  # Ngăn không cho đóng cửa sổ
            
# Tạo cửa sổ chính của ứng dụng
root = tk.Tk()
app = DangerousApp(root)
root.mainloop()
