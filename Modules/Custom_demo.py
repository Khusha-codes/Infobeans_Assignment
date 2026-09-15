import customtkinter as ctk

app = ctk.CTk()

app.title("My First App")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Hello World")
label.pack(pady=20)

app.mainloop()