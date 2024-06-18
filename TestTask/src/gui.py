import tkinter as tk
from tkinter import (
    filedialog,
    messagebox
)
from augmentations import (
    load_images_from_directory,
    save_images_to_directory,
    apply_augmentations
)


class ImageAugmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Augmentation Tool")

        self.input_dir = ""
        self.output_dir = ""

        self.create_widgets()

    def create_widgets(self):
        # Input Directory
        tk.Label(self.root, text="Input Directory:").grid(row=0, column=0,
                                                          padx=10, pady=10)
        self.input_dir_entry = tk.Entry(self.root, width=50)
        self.input_dir_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse",
                  command=self.browse_input_dir).grid(row=0, column=2, padx=10,
                                                      pady=10)

        # Output Directory
        tk.Label(self.root, text="Output Directory:").grid(row=1, column=0,
                                                           padx=10, pady=10)
        self.output_dir_entry = tk.Entry(self.root, width=50)
        self.output_dir_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse",
                  command=self.browse_output_dir).grid(row=1, column=2,
                                                       padx=10, pady=10)

        # Augmentation Parameters
        tk.Label(self.root, text="Resize (Width, Height):").grid(row=2,
                                                                 column=0,
                                                                 padx=10,
                                                                 pady=10)
        self.resize_entry = tk.Entry(self.root, width=20)
        self.resize_entry.grid(row=2, column=1, padx=10, pady=10)
        self.resize_entry.insert(0, "256,256")

        tk.Label(self.root, text="Crop (Width, Height):").grid(
            row=3, column=0,
            padx=10, pady=10
        )
        self.crop_entry = tk.Entry(self.root, width=20)
        self.crop_entry.grid(row=3, column=1, padx=10, pady=10)
        self.crop_entry.insert(0, "200,200")

        tk.Label(self.root, text="Rotate Limit:").grid(row=4, column=0,
                                                       padx=10, pady=10)
        self.rotate_entry = tk.Entry(self.root, width=20)
        self.rotate_entry.grid(row=4, column=1, padx=10, pady=10)
        self.rotate_entry.insert(0, "45")

        tk.Label(self.root, text="Flip Probability:").grid(
            row=5, column=0,
            padx=10, pady=10
        )
        self.flip_entry = tk.Entry(self.root, width=20)
        self.flip_entry.grid(
            row=5, column=1,
            padx=10, pady=10
        )
        self.flip_entry.insert(0, "0.5")

        tk.Label(self.root, text="Brightness/Contrast Probability:").grid(
            row=6, column=0, padx=10, pady=10)
        self.brightness_contrast_entry = tk.Entry(self.root, width=20)
        self.brightness_contrast_entry.grid(
            row=6,
            column=1,
            padx=10,
            pady=10
        )
        self.brightness_contrast_entry.insert(0, "0.2")

        tk.Label(self.root, text="Blur Probability:").grid(
            row=7, column=0,
            padx=10, pady=10
        )
        self.blur_entry = tk.Entry(self.root, width=20)
        self.blur_entry.grid(
            row=7,
            column=1,
            padx=10,
            pady=10
        )
        self.blur_entry.insert(0, "0.1")

        # Start Button
        tk.Button(
            self.root,
            text="Start Augmentation",
            command=self.start_augmentation
        ).grid(
            row=8,
            column=0,
            columnspan=3,
            pady=20
        )

    def browse_input_dir(self):
        self.input_dir = filedialog.askdirectory()
        self.input_dir_entry.delete(0, tk.END)
        self.input_dir_entry.insert(0, self.input_dir)

    def browse_output_dir(self):
        self.output_dir = filedialog.askdirectory()
        self.output_dir_entry.delete(0, tk.END)
        self.output_dir_entry.insert(0, self.output_dir)

    def start_augmentation(self):
        if not self.input_dir or not self.output_dir:
            messagebox.showerror(
                "Error",
                "Please specify both input and output directories."
            )
            return

        try:
            resize_size = tuple(map(int, self.resize_entry.get().split(',')))
            crop_size = tuple(map(int, self.crop_entry.get().split(',')))
            rotate_limit = int(self.rotate_entry.get())
            flip_prob = float(self.flip_entry.get())
            brightness_contrast_prob = float(
                self.brightness_contrast_entry.get())
            blur_prob = float(self.blur_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid augmentation parameters."
            )
            return

        images, filenames = load_images_from_directory(self.input_dir)
        if not images:
            messagebox.showerror(
                "Error",
                "No images found in the input directory."
            )
            return

        augmented_images = apply_augmentations(images, resize_size, crop_size,
                                               rotate_limit, flip_prob,
                                               brightness_contrast_prob,
                                               blur_prob)
        save_images_to_directory(augmented_images, filenames, self.output_dir)
        messagebox.showinfo(
            "Success",
            "Augmentation completed successfully!"
        )
