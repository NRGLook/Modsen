import tkinter as tk
import matplotlib.pyplot as plt
import json

from tkinter import (
    filedialog, messagebox, Menu,
    Toplevel, Label, Entry, Button
)

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from PIL import Image

from TestTask.src.augmentation.loader import load_images_from_directory
from TestTask.src.augmentation.transformer import (
    overlay_image, overlay_text,
    add_noise, change_brightness,
    flip_image, change_contrast,
    shift_image, random_crop,
    rotate_image, resize_image
)
from TestTask.src.augmentation.saver import save_image


class ImageAugmentationApp:
    """
    Main application class for the Image Augmentation Tool.
    Provides a GUI for loading images, applying transformations,
    and saving results.
    """

    def __init__(self, master):
        """
        Initialize the application with the main Tkinter window.

        Args:
            master: The main Tkinter window.
        """
        self.master = master
        master.title("Image Augmentation Tool")

        # Create button for loading images
        self.load_button = tk.Button(master, text="Load Images",
                                     command=self.load_images)
        self.load_button.pack(pady=10)

        # Create button for applying transformations
        self.transform_button = tk.Button(master, text="Apply Transformations",
                                          command=self.show_transform_menu)
        self.transform_button.pack(pady=10)

        # Create menu for selecting transformations
        self.transform_menu = Menu(master, tearoff=0)
        self.add_transformation_menu_options()

        # Create button for saving images
        self.save_button = tk.Button(master, text="Save Images",
                                     command=self.save_images)
        self.save_button.pack(pady=10)

        # Create button for saving settings
        self.save_settings_button = tk.Button(master, text="Save Settings",
                                              command=self.save_settings)
        self.save_settings_button.pack(pady=10)

        # Create button for loading settings
        self.load_settings_button = tk.Button(master, text="Load Settings",
                                              command=self.load_settings)
        self.load_settings_button.pack(pady=10)

        # Frame for visualization of loaded and augmented images
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.prev_button = tk.Button(master, text="Previous Image",
                                     command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.next_button = tk.Button(master, text="Next Image",
                                     command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=5, pady=10)

        self.directory = ""
        self.images = []
        self.transformed_images = []
        self.current_image_index = 0
        self.params = {}

    def show_transform_menu(self):
        """
        Display the parameter dialog for entering transformation parameters.
        """
        param_dialog = ParamDialog(self.master)
        self.master.wait_window(param_dialog.top)
        params = param_dialog.params

        if params:
            self.params = params
            self.apply_transformations(params)

    def add_transformation_menu_options(self):
        """
        Add options for image transformations to the transformation menu.
        """
        transformations = {
            "Rotate Image": rotate_image,
            "Flip Image": flip_image,
            "Resize Image": resize_image,
            "Change Brightness": change_brightness,
            "Change Contrast": change_contrast,
            "Add Noise": add_noise,
            "Shift Image": shift_image,
            "Random Crop": random_crop,
            "Overlay Text": overlay_text,
            "Overlay Image": overlay_image
        }
        for name, func in transformations.items():
            self.transform_menu.add_command(label=name, command=lambda
                f=func: self.apply_transformation(f))

    def load_images(self):
        """
        Load images from the specified directory.
        """
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.images = load_images_from_directory(self.directory)
            self.current_image_index = 0
            if self.images:
                self.display_images(
                    self.images[self.current_image_index],
                    None
                )
            messagebox.showinfo("Load Images",
                                f"Loaded {len(self.images)} images.")

    def apply_transformations(self, params):
        """
        Apply the selected transformations to the loaded images.

        Args:
            params (dict): Dictionary of transformation parameters.
        """
        if not self.images:
            messagebox.showerror("Error", "No images loaded.")
            return
        try:
            self.transformed_images = self.images.copy()
            if 'degrees' in params:
                self.transformed_images = [
                    rotate_image(img, degrees=params['degrees']) for img in
                    self.transformed_images]
            if 'mode' in params:
                self.transformed_images = [flip_image(img, mode=params['mode'])
                                           for img in self.transformed_images]
            if 'size' in params:
                self.transformed_images = [
                    resize_image(img, size=params['size']) for img in
                    self.transformed_images]
            if 'factor_brightness' in params:
                self.transformed_images = [
                    change_brightness(img, factor=params['factor_brightness'])
                    for img in self.transformed_images]
            if 'factor_contrast' in params:
                self.transformed_images = [
                    change_contrast(img, factor=params['factor_contrast']) for
                    img in self.transformed_images]
            if 'amount' in params:
                self.transformed_images = [
                    add_noise(img, amount=params['amount']) for img in
                    self.transformed_images]
            if 'shift' in params:
                self.transformed_images = [
                    shift_image(img, shift=params['shift']) for img in
                    self.transformed_images]
            if 'crop_size' in params:
                self.transformed_images = [
                    random_crop(img, size=params['crop_size']) for img in
                    self.transformed_images]
            if 'text' in params:
                self.transformed_images = [
                    overlay_text(img, text=params['text']) for img in
                    self.transformed_images]
            if 'overlay_img' in params:
                self.transformed_images = [
                    overlay_image(img, overlay=params['overlay_img'],
                                  transparency=params.get('transparency', 0.5))
                    for img in self.transformed_images]

            if self.transformed_images:
                self.display_images(
                    self.images[self.current_image_index],
                    self.transformed_images[self.current_image_index]
                )

            messagebox.showinfo(
                "Transformation",
                "Applied transformations successfully."
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_images(self):
        """
        Save the transformed images to the specified directory.
        """
        if not self.transformed_images:
            messagebox.showerror(
                "Error",
                "No transformed images to save."
            )
            return
        save_dir = filedialog.askdirectory()
        if save_dir:
            for i, img in enumerate(self.transformed_images):
                if img is not None:
                    save_image(img, save_dir, f"transformed_{i}.jpg")
            messagebox.showinfo(
                "Save Images",
                "All transformed images have been saved."
            )

    def display_images(self, original_image, transformed_image):
        """
        Display the original and transformed images using matplotlib on the
        Tkinter canvas.

        Args:
            original_image (Image): The original image to display.
            transformed_image (Image): The transformed image to display.
        """
        if original_image is None and transformed_image is None:
            return

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        if original_image:
            axs[0].imshow(original_image)
            axs[0].set_title("Original Image")
            axs[0].axis('off')
        else:
            axs[0].axis('off')

        if transformed_image:
            axs[1].imshow(transformed_image)
            axs[1].set_title("Transformed Image")
            axs[1].axis('off')
        else:
            axs[1].axis('off')

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_previous_image(self):
        """
        Display the previous image in the list.
        """
        if self.current_image_index > 0:
            self.current_image_index -= 1
            original = self.images[self.current_image_index]
            transformed = self.transformed_images[self.current_image_index] \
                if self.transformed_images else None
            self.display_images(original, transformed)

    def show_next_image(self):
        """
        Display the next image in the list.
        """
        if self.current_image_index < len(self.images) - 1:
            self.current_image_index += 1
            original = self.images[self.current_image_index]
            transformed = self.transformed_images[self.current_image_index] \
                if self.transformed_images else None
            self.display_images(original, transformed)

    def save_settings(self):
        """
        Save the current transformation settings to a JSON file.
        """
        if not self.params:
            messagebox.showerror("Error", "No transformation settings to save.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json")])
        if save_path:
            try:
                with open(save_path, 'w') as f:
                    json.dump(self.params, f)
                messagebox.showinfo("Save Settings", "Settings have been saved.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save settings: {e}")

    def load_settings(self):
        """
        Load transformation settings from a JSON file.
        """
        load_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if load_path:
            try:
                with open(load_path, 'r') as f:
                    self.params = json.load(f)
                self.apply_transformations(self.params)
                messagebox.showinfo("Load Settings", "Settings have been loaded and applied.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load settings: {e}")


class ParamDialog:
    """
    Dialog class for entering transformation parameters.
    """

    def __init__(self, parent):
        """
        Initialize the dialog with input fields for transformation parameters.

        Args:
            parent: The parent Tkinter window.
        """
        top = self.top = Toplevel(parent)
        self.params = {}

        top.geometry("400x600")
        top.title("Transformation Parameters")

        self.degree_label = Label(top, text="Rotate degrees (e.g., 45):")
        self.degree_label.pack()
        self.degree_entry = Entry(top)
        self.degree_entry.pack()
        self.degree_entry.insert(0, "0")

        self.mode_label = Label(top, text="Flip mode (horizontal/vertical):")
        self.mode_label.pack()
        self.mode_entry = Entry(top)
        self.mode_entry.pack()
        self.mode_entry.insert(0, "horizontal")

        self.width_label = Label(top, text="Resize width (e.g., 256):")
        self.width_label.pack()
        self.width_entry = Entry(top)
        self.width_entry.pack()
        self.width_entry.insert(0, "256")

        self.height_label = Label(top, text="Resize height (e.g., 256):")
        self.height_label.pack()
        self.height_entry = Entry(top)
        self.height_entry.pack()
        self.height_entry.insert(0, "256")

        self.brightness_label = Label(top,
                                      text="Brightness factor (e.g., 1.0):")
        self.brightness_label.pack()
        self.brightness_entry = Entry(top)
        self.brightness_entry.pack()
        self.brightness_entry.insert(0, "1.0")

        self.contrast_label = Label(top, text="Contrast factor (e.g., 1.0):")
        self.contrast_label.pack()
        self.contrast_entry = Entry(top)
        self.contrast_entry.pack()
        self.contrast_entry.insert(0, "1.0")

        self.noise_label = Label(top, text="Noise amount (e.g., 0.02):")
        self.noise_label.pack()
        self.noise_entry = Entry(top)
        self.noise_entry.pack()
        self.noise_entry.insert(0, "0.02")

        self.shift_x_label = Label(top, text="Shift x (pixels):")
        self.shift_x_label.pack()
        self.shift_x_entry = Entry(top)
        self.shift_x_entry.pack()
        self.shift_x_entry.insert(0, "0")

        self.shift_y_label = Label(top, text="Shift y (pixels):")
        self.shift_y_label.pack()
        self.shift_y_entry = Entry(top)
        self.shift_y_entry.pack()
        self.shift_y_entry.insert(0, "0")

        self.crop_width_label = Label(top, text="Crop width (e.g., 100):")
        self.crop_width_label.pack()
        self.crop_width_entry = Entry(top)
        self.crop_width_entry.pack()
        self.crop_width_entry.insert(0, "100")

        self.crop_height_label = Label(
            top,
            text="Crop height (e.g., 100):"
        )
        self.crop_height_label.pack()
        self.crop_height_entry = Entry(top)
        self.crop_height_entry.pack()
        self.crop_height_entry.insert(0, "100")

        self.text_label = Label(
            top,
            text="Overlay text:"
        )
        self.text_label.pack()
        self.text_entry = Entry(top)
        self.text_entry.pack()

        self.overlay_path_button = Button(
            top,
            text="Select overlay image",
            command=self.load_overlay_image
        )
        self.overlay_path_button.pack()

        self.transparency_label = Label(
            top,
            text="Overlay transparency (0.0 to 1.0):"
        )
        self.transparency_label.pack()
        self.transparency_entry = Entry(top)
        self.transparency_entry.pack()
        self.transparency_entry.insert(0, "0.5")

        self.ok_button = Button(top, text="OK", command=self.ok)
        self.ok_button.pack(pady=10)

    def load_overlay_image(self):
        """
        Load an overlay image from the file system.
        """
        self.overlay_path = filedialog.askopenfilename()
        if self.overlay_path:
            self.overlay_img = Image.open(self.overlay_path)

    def ok(self):
        """
        Collect parameters from the input fields and store them in the params
        dictionary.
        """
        if self.degree_entry.get() != "0":
            self.params['degrees'] = float(self.degree_entry.get())
        if self.mode_entry.get() != "horizontal":
            self.params['mode'] = self.mode_entry.get()
        if self.width_entry.get() != "256" or self.height_entry.get() != "256":
            self.params['size'] = (
                int(self.width_entry.get()), int(self.height_entry.get()))
        if self.brightness_entry.get() != "1.0":
            self.params['factor_brightness'] = float(
                self.brightness_entry.get())
        if self.contrast_entry.get() != "1.0":
            self.params['factor_contrast'] = float(self.contrast_entry.get())
        if self.noise_entry.get() != "0.02":
            self.params['amount'] = float(self.noise_entry.get())
        if self.shift_x_entry.get() != "0" or self.shift_y_entry.get() != "0":
            self.params['shift'] = (
                int(self.shift_x_entry.get()), int(self.shift_y_entry.get()))
        if (self.crop_width_entry.get() != "100" or
                self.crop_height_entry.get() != "100"):
            self.params['crop_size'] = (int(self.crop_width_entry.get()),
                                        int(self.crop_height_entry.get()))
        if self.text_entry.get():
            self.params['text'] = self.text_entry.get()
        if hasattr(self, 'overlay_img'):
            self.params['overlay_img'] = self.overlay_img
        if self.transparency_entry.get() != "0.5":
            self.params['transparency'] = float(self.transparency_entry.get())
        self.top.destroy()
