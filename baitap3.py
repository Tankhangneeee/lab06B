import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("User Information Form")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # User Info Frame
        self.user_info_frame = ttk.LabelFrame(root, text="Thông tin người dùng", padding=10)
        self.user_info_frame.pack(fill=tk.X, padx=10, pady=10)

        self.create_user_info_widgets()

        # Registration Frame
        self.registration_frame = ttk.LabelFrame(root, text="Thông tin đăng ký", padding=10)
        self.registration_frame.pack(fill=tk.X, padx=10, pady=10)

        self.create_registration_widgets()

        # Terms Frame
        self.terms_frame = ttk.LabelFrame(root, text="Điều khoản và điều kiện", padding=10)
        self.terms_frame.pack(fill=tk.X, padx=10, pady=10)

        self.create_terms_widgets()

        # Submit Button
        self.submit_button = tk.Button(root, text="Gửi", font=("Helvetica", 12), command=self.submit)
        self.submit_button.pack(pady=20)

    def create_user_info_widgets(self):
        tk.Label(self.user_info_frame, text="Tên:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.first_name_entry = tk.Entry(self.user_info_frame, font=("Helvetica", 12))
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.user_info_frame, text="Họ:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.last_name_entry = tk.Entry(self.user_info_frame, font=("Helvetica", 12))
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.user_info_frame, text="Chức danh:", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.title_entry = tk.Entry(self.user_info_frame, font=("Helvetica", 12))
        self.title_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.user_info_frame, text="Tuổi:", font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.age_entry = tk.Entry(self.user_info_frame, font=("Helvetica", 12))
        self.age_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.user_info_frame, text="Quốc tịch:", font=("Helvetica", 12)).grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.nationality_entry = tk.Entry(self.user_info_frame, font=("Helvetica", 12))
        self.nationality_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    def create_registration_widgets(self):
        self.registration_var = tk.BooleanVar()
        self.registration_checkbox = tk.Checkbutton(self.registration_frame, text="Đăng ký", variable=self.registration_var, font=("Helvetica", 12))
        self.registration_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        tk.Label(self.registration_frame, text="Số khóa học đã hoàn thành:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.courses_spinbox = tk.Spinbox(self.registration_frame, from_=0, to=100, font=("Helvetica", 12), width=5)
        self.courses_spinbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.registration_frame, text="Học kỳ:", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.semester_spinbox = tk.Spinbox(self.registration_frame, from_=1, to=12, font=("Helvetica", 12), width=5)
        self.semester_spinbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    def create_terms_widgets(self):
        self.terms_var = tk.BooleanVar()
        self.terms_checkbox = tk.Checkbutton(self.terms_frame, text="Tôi chấp nhận các điều khoản và điều kiện", variable=self.terms_var, font=("Helvetica", 12))
        self.terms_checkbox.pack(anchor="w")

    def submit(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        title = self.title_entry.get()
        age = self.age_entry.get()
        nationality = self.nationality_entry.get()
        registration_status = "Đã đăng ký" if self.registration_var.get() else "Chưa đăng ký"
        courses_completed = self.courses_spinbox.get()
        semester = self.semester_spinbox.get()
        terms_accepted = "Đã chấp nhận" if self.terms_var.get() else "Chưa chấp nhận"

        print("Thông tin người dùng:")
        print(f"Tên: {first_name}")
        print(f"Họ: {last_name}")
        print(f"Chức danh: {title}")
        print(f"Tuổi: {age}")
        print(f"Quốc tịch: {nationality}")
        print("Thông tin đăng ký:")
        print(f"Trạng thái đăng ký: {registration_status}")
        print(f"Số khóa học đã hoàn thành: {courses_completed}")
        print(f"Học kỳ: {semester}")
        print("Điều khoản và điều kiện:")
        print(f"Chấp nhận điều khoản và điều kiện: {terms_accepted}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
