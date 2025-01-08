import tkinter
from tkinter import filedialog, messagebox
from pathlib import Path
from watermark import WaterMark

# Define fonts and colors
TITLE_FONT = ("Arial", 24, "bold")
LABEL_FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 12, "bold")
PATH_FONT = ("Arial", 12, "italic")
BUTTON_COLOR = "#4CAF50"  # Green
BUTTON_TEXT_COLOR = "white"


class GUI:
    def __init__(self):

        # Store image and watermark paths
        self.image_path = None
        self.watermark_path = None

        # Window and basic config
        self.window = tkinter.Tk()
        self.window.title("Watermark Your Photos!")
        self.window.geometry("800x650")
        self.window.config(background="#f8f9fa")  # Light gray for neutral background

        # Create Title label
        self.label = tkinter.Label(
            text="PyImage Watermarking App",
            font=TITLE_FONT,
            bg="#343a40",
            fg="white",
            padx=10,
            pady=10,
            relief="groove",
            anchor="center",
            width=40
        )
        self.label.grid(row=0, column=0, pady=20)

        # Divider 1
        self.divider = tkinter.Label(bg="#ced4da", height=1, width=60)
        self.divider.grid(row=1, column=0, pady=10)

        # Section 1: Upload Image
        self.image_label = tkinter.Label(
            text="Step 1: Upload an Image",
            font=LABEL_FONT,
            bg="#f8f9fa",
            fg="#212529"
        )
        self.image_label.grid(row=2, column=0, columnspan=2, pady=5)

        self.file_btn = tkinter.Button(
            text="Upload Image",
            command=self.upload_image,
            font=BUTTON_FONT,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            relief="raised",
            bd=3
        )
        self.file_btn.grid(row=3, column=0, pady=5, padx=20)

        self.file_label = tkinter.Label(
            text="No image uploaded yet...",
            font=PATH_FONT,
            bg="#f8f9fa",
            fg="gray"
        )
        self.file_label.grid(row=4, column=0, pady=5, padx=20)

        # Divider 2
        self.divider = tkinter.Label(bg="#ced4da", height=1, width=60)
        self.divider.grid(row=5, column=0, columnspan=2, pady=10)

        # Section 2: Upload Watermark
        self.watermark_label = tkinter.Label(
            text="Step 2: Upload a Watermark",
            font=LABEL_FONT,
            bg="#f8f9fa",
            fg="#212529"
        )
        self.watermark_label.grid(row=6, column=0, columnspan=2, pady=5)

        self.watermark_btn = tkinter.Button(
            text="Upload Watermark",
            command=self.upload_watermark,
            font=BUTTON_FONT,
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            relief="raised",
            bd=3
        )
        self.watermark_btn.grid(row=7, column=0, pady=5, padx=20)

        self.watermark_label_status = tkinter.Label(
            text="No watermark uploaded yet...",
            font=PATH_FONT,
            bg="#f8f9fa",
            fg="gray",
        )
        self.watermark_label_status.grid(row=8, column=0, pady=5, padx=20)

        # Divider 3
        self.divider = tkinter.Label(bg="#ced4da", height=1, width=60)
        self.divider.grid(row=9, column=0, columnspan=2, pady=10)

        # Submit Section
        self.submit_btn = tkinter.Button(
            text="Add Watermark",
            command=self.place_watermark,
            font=("Arial", 14, "bold"),
            bg="#28a745",  # Green for action
            fg=BUTTON_TEXT_COLOR,
            relief="raised",
            bd=3
        )
        self.submit_btn.grid(row=10, column=0, columnspan=2, pady=20)

        self.output_label = tkinter.Label(
            text="",
            font=PATH_FONT,
            bg="#f8f9fa",
            fg="gray"
        )
        self.output_label.grid(row=11, column=0, pady=5, padx=20)

        # Footer
        self.footer = tkinter.Label(
            text="© 2025 PyImage | All Rights Reserved",
            font=("Arial", 10, "italic"),
            bg="#f8f9fa",
            fg="gray"
        )
        self.footer.grid(row=12, column=0, columnspan=2, pady=10)

        # Add consistent padding
        for widget in self.window.winfo_children():
            widget.grid_configure(padx=10)

    def upload_image(self):
        self.image_path = Path(
            filedialog.askopenfilename(
                title="Select an Image to apply a watermark on",
                filetypes=[("JPEG Files", "*.jpg"), ("PNG Files", "*.png")]
            )
        )
        if self.image_path:
            self.file_label.config(text=f"Image: {self.image_path.name}")

    def upload_watermark(self):
        self.watermark_path = Path(
            filedialog.askopenfilename(
                title="Choose a watermark to apply on your image",
                filetypes=[("PNG Files", "*.png")]
            )
        )
        if self.watermark_path:
            self.watermark_label_status.config(text=f"Watermark: {self.watermark_path.name}")

    def place_watermark(self):

        # Return with error message if image is not added
        if self.image_path is None:
            messagebox.showerror(title="Image not uploaded",
                                 message="Please upload an image before trying to add a watermark.")
            self.output_label.config(text="Please add an image first!")
            return

        # Return with error message if watermark is not added
        if self.watermark_path is None:
            messagebox.showerror(title="Watermark not uploaded",
                                 message="Please upload a watermark to apply on the image.")
            self.output_label.config(text="Please add a watermark first!")
            return

        # Create class and place watermark on image
        watermark_obj = WaterMark()
        watermark_obj.add_watermark_on_image(self.image_path, self.watermark_path)

        self.output_label.config(text=f"Watermark was added successfully!\n"
                                      f"Please find the new image in the outputs folder by the name\n"
                                      f"output-{self.image_path.name}")

