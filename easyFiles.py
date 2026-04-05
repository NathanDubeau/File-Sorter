import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

  
def main():
    root = tk.Tk() 
    root.title("Easy Files")
    ttk.Label(root, text="Welcome to Easy Files!", font=(18)).pack(pady=10)
    
    bottom_frame = ttk.Frame(root)
    bottom_frame.pack(pady=20)

    entry = ttk.Entry(bottom_frame)
    entry.pack(side='left', padx=(0, 10))

    button = ttk.Button(bottom_frame, text="Browse", command=lambda: browse_file(entry))
    button.pack(side='left')


    root.mainloop()

    
if __name__ == "__main__":
    main()
    

