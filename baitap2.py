import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Security App")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        # Main Frame
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Sidebar Frame
        self.sidebar_frame = tk.Frame(self.main_frame, width=200, bg="#3498db")
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Sidebar Contents
        self.status_label = tk.Label(self.sidebar_frame, text="Trạng thái", font=("Helvetica", 14), bg="#3498db", fg="white")
        self.status_label.pack(pady=10, padx=10, anchor="w")
        self.update_label = tk.Label(self.sidebar_frame, text="Cập nhật", font=("Helvetica", 14), bg="#3498db", fg="white")
        self.update_label.pack(pady=10, padx=10, anchor="w")
        self.scan_button = tk.Button(self.sidebar_frame, text="Quét ngay", font=("Helvetica", 14), command=self.scan_now, bg="#2980b9", fg="white")
        self.scan_button.pack(pady=10, padx=10)

        # Main Content Frame
        self.content_frame = tk.Frame(self.main_frame, bg="#e74c3c")
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Main Content
        self.title_label = tk.Label(self.content_frame, text="Security App", font=("Helvetica", 24), bg="#e74c3c", fg="white")
        self.title_label.pack(pady=20)
        self.subtitle_label = tk.Label(self.content_frame, text="Your safety is our priority", font=("Helvetica", 18), bg="#e74c3c", fg="white")
        self.subtitle_label.pack(pady=10)
        
        self.quick_scan_button = tk.Button(self.content_frame, text="Quét nhanh", font=("Helvetica", 14), command=self.quick_scan, bg="#c0392b", fg="white")
        self.quick_scan_button.pack(pady=10, ipadx=20)
        self.web_protection_button = tk.Button(self.content_frame, text="Bảo vệ web", font=("Helvetica", 14), command=self.web_protection, bg="#e67e22", fg="white")
        self.web_protection_button.pack(pady=10, ipadx=20)
        self.full_scan_button = tk.Button(self.content_frame, text="Quét toàn bộ", font=("Helvetica", 14), command=self.full_scan, bg="#e67e22", fg="white")
        self.full_scan_button.pack(pady=10, ipadx=20)

        # Status Label
        self.current_status_label = tk.Label(root, text="Trạng thái hiện tại: Đang chờ", font=("Helvetica", 14), bg="#f0f0f0")
        self.current_status_label.pack(pady=20)

    def scan_now(self):
        self.current_status_label.config(text="Trạng thái hiện tại: Đang quét ngay")
        messagebox.showinfo("Quét ngay", "Đã bắt đầu quét ngay.")

    def quick_scan(self):
        self.current_status_label.config(text="Trạng thái hiện tại: Đang quét nhanh")
        messagebox.showinfo("Quét nhanh", "Đã bắt đầu quét nhanh.")

    def web_protection(self):
        self.current_status_label.config(text="Trạng thái hiện tại: Bảo vệ web")
        messagebox.showinfo("Bảo vệ web", "Đang bật chế độ bảo vệ web.")

    def full_scan(self):
        self.current_status_label.config(text="Trạng thái hiện tại: Đang quét toàn bộ")
        messagebox.showinfo("Quét toàn bộ", "Đã bắt đầu quét toàn bộ.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
