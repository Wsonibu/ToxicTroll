import tkinter as tk
import threading
import time
import sys

class ErrorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Error App")
        self.root.geometry("200x100")
        
        self.start_button = tk.Button(root, text="Start", command=self.start_error)
        self.start_button.pack(pady=10)
        
        self.close_button = tk.Button(root, text="Close", command=self.start_error)
        self.close_button.pack(pady=10)
        
        # Bind the "R" key to the stop_error method
        self.root.bind('<r>', self.stop_error)
        
        self.error_running = False

    def start_error(self):
        self.error_running = True
        threading.Thread(target=self.create_error_windows).start()

    def create_error_windows(self):
        while self.error_running:
            error_window = tk.Toplevel(self.root)
            error_window.title("Error")
            error_window.geometry("300x200")
            label = tk.Label(error_window, text="Error", font=("Helvetica", 24))
            label.pack(expand=True)
            label_info = tk.Label(error_window, text="Press 'R' to stop", font=("Helvetica", 10))
            label_info.pack(expand=True)
            error_window.update()
            time.sleep(0.1)  # Small delay to prevent freezing

    def stop_error(self, event):
        self.error_running = False
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ErrorApp(root)
    root.mainloop()
