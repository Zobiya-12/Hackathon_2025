import tkinter as tk
from tkinter import messagebox, simpledialog

# ------------------- Static Data ------------------- #
users = [
    {"id": 1, "username": "john", "password": "john123", "role": "customer"},
    {"id": 2, "username": "emma", "password": "emma123", "role": "customer"},
    {"id": 3, "username": "alice", "password": "alice123", "role": "official"},
]

applications = [
    {"id": 1, "user_id": 1, "name": "John Doe", "age": 30, "phone": "1234567890", "health_status": "Diabetes", "treatment": "Ayurveda Therapy", "status": "submitted"},
    {"id": 2, "user_id": 2, "name": "Emma Smith", "age": 28, "phone": "9876543210", "health_status": "Arthritis", "treatment": "Unani Medicine", "status": "pending"},
]

documents = [
    {"id": 1, "user_id": 1, "filename": "ayurveda_prescription.pdf", "status": "approved"},
    {"id": 2, "user_id": 2, "filename": "unani_test_results.pdf", "status": "under review"},
]

resources = [
    {"title": "AYUSH Guidelines", "link": "https://ayush.gov.in/guidelines"},
    {"title": "Traditional Medicine Information", "link": "https://ayush.gov.in/resources"},
]

# ------------------- GUI Functions ------------------- #
def notify_user(message):
    messagebox.showinfo("Notification", message)

def create_window(title, width=600, height=400):
    window = tk.Toplevel()
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(bg="#E3F2FD")  # Light blue background
    return window

def show_customer_dashboard(user):
    dashboard = create_window("Customer Dashboard", 700, 500)

    def view_application():
        app_window = create_window("My Application", 600, 400)
        for app in applications:
            if app["user_id"] == user["id"]:
                for key, value in app.items():
                    if key != 'user_id' and key != 'id':
                        tk.Label(app_window, text=f"{key.replace('_', ' ').title()}: {value}", bg="#E3F2FD").pack()

    def upload_document():
        filename = simpledialog.askstring("Upload Document", "Enter document filename:")
        if filename:
            documents.append({"id": len(documents)+1, "user_id": user["id"], "filename": filename, "status": "uploaded"})
            notify_user("Document uploaded successfully.")

    def view_documents():
        doc_window = create_window("My Documents")
        for doc in documents:
            if doc["user_id"] == user["id"]:
                tk.Label(doc_window, text=f"File: {doc['filename']} | Status: {doc['status']}", bg="#E3F2FD").pack()

    def access_resources():
        res_window = create_window("Resources")
        for res in resources:
            tk.Label(res_window, text=f"{res['title']}: {res['link']}", bg="#E3F2FD").pack()

    tk.Button(dashboard, text="View My Application", command=view_application, bg="#64B5F6", fg="white").pack(pady=5)
    tk.Button(dashboard, text="Upload Document", command=upload_document, bg="#64B5F6", fg="white").pack(pady=5)
    tk.Button(dashboard, text="View My Documents", command=view_documents, bg="#64B5F6", fg="white").pack(pady=5)
    tk.Button(dashboard, text="Access Resources", command=access_resources, bg="#64B5F6", fg="white").pack(pady=5)

def show_official_dashboard(user):
    dashboard = create_window("Official Dashboard", 700, 500)

def login(role):
    login_window = create_window(f"{role.title()} Login", 400, 300)

    tk.Label(login_window, text="Username:", bg="#E3F2FD").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password:", bg="#E3F2FD").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        user = next((u for u in users if u["username"] == username and u["password"] == password and u["role"] == role), None)
        if user:
            if role == "customer":
                show_customer_dashboard(user)
            else:
                show_official_dashboard(user)
            login_window.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials or role.")

    tk.Button(login_window, text="Login", command=handle_login, bg="#42A5F5", fg="white").pack(pady=5)

def main():
    root = tk.Tk()
    root.title("AYUSH Customer Document Portal")
    root.geometry("600x400")
    root.configure(bg="#E3F2FD")

    tk.Label(root, text="Welcome to AYUSH Portal", font=("Arial", 16), bg="#E3F2FD").pack(pady=10)
    tk.Button(root, text="Login as Customer", width=20, command=lambda: login("customer"), bg="#1976D2", fg="white").pack(pady=5)
    tk.Button(root, text="Login as Official", width=20, command=lambda: login("official"), bg="#1976D2", fg="white").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()