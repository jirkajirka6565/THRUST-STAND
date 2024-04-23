import customtkinter

root = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  


button = customtkinter.CTkButton(master=root, width=50, height=20, corner_radius=3, text="Test button")
button.pack()


root.mainloop()

