import tkinter
from tkinter import filedialog
from pathlib import Path


class GUI:
    def __init__(self):

        # Store image path
        self.file_path = None

        # Window and basic config
        self.window = tkinter.Tk()
        self.window.title("Watermark your Photos!")
        self.window.minsize(width=500, height=500)

        # Create Title label on Desktop
        self.label = tkinter.Label(text="PyImage Watermarking App!")
        self.label.config(font=("Arial", 16), padx=100, pady=25)
        self.label.grid(row=0, column=0)

        # Upload file label
        self.file_btn = tkinter.Button(text="Upload Image", command=self.upload_file)
        self.file_btn.grid(row=1, column=0)

        # Label to display file name
        self.file_label = tkinter.Label(text="No image uploaded yet...")
        self.file_label.grid(row=2, column=0)

        self.window.mainloop()

    def upload_file(self):
        self.file_path = Path(
            filedialog.askopenfilename(
                title="Select a File",
                filetypes=[("JPEG Files", "*.jpg"), ("PNG Files", "*.png")]
            )
        )
        if self.file_path:
            self.file_label.config(text=f"Uploaded Image: {self.file_path}")

