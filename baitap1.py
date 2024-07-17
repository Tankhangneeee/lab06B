import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("FPS Recorder")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # Title Label
        self.title_label = tk.Label(root, text="FPS Recorder", font=("Helvetica", 24), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # FPS Input Frame
        self.fps_frame = tk.Frame(root, bg="#f0f0f0")
        self.fps_frame.pack(pady=10)
        self.fps_label = tk.Label(self.fps_frame, text="FPS:", font=("Helvetica", 14), bg="#f0f0f0")
        self.fps_label.pack(side=tk.LEFT, padx=10)
        self.fps_entry = tk.Entry(self.fps_frame, font=("Helvetica", 14))
        self.fps_entry.pack(side=tk.LEFT)

        # Button Frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)
        self.pause_button = tk.Button(self.button_frame, text="Tạm dừng", font=("Helvetica", 14), command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.start_button = tk.Button(self.button_frame, text="Bắt đầu", font=("Helvetica", 14), command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.end_button = tk.Button(self.button_frame, text="Kết thúc", font=("Helvetica", 14), command=self.end)
        self.end_button.pack(side=tk.LEFT, padx=10)

        # Status Label
        self.status_label = tk.Label(root, text="Trạng thái: Chưa ghi", font=("Helvetica", 14), bg="#f0f0f0")
        self.status_label.pack(pady=20)

        # FPS Listbox
        self.fps_list_label = tk.Label(root, text="Danh sách FPS ghi được:", font=("Helvetica", 14), bg="#f0f0f0")
        self.fps_list_label.pack()
        self.fps_listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=8)
        self.fps_listbox.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(root, text="Xóa danh sách", font=("Helvetica", 14), command=self.reset)
        self.reset_button.pack(pady=10)

    def pause(self):
        self.status_label.config(text="Trạng thái: Đã tạm dừng")

    def start(self):
        fps_value = self.fps_entry.get()
        if fps_value.isdigit():
            self.fps_listbox.insert(tk.END, fps_value)
            self.status_label.config(text="Trạng thái: Đang ghi")
        else:
            tk.messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên vào ô FPS.")

    def end(self):
        self.status_label.config(text="Trạng thái: Đã kết thúc")

    def reset(self):
        self.fps_listbox.delete(0, tk.END)
        self.status_label.config(text="Trạng thái: Chưa ghi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
