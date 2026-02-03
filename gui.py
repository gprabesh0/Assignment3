import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os

class ImageEditorGUI:
    def __init__(self, root, processor):
        """Constructor: Setup GUI components."""
        self.root = root
        self.processor = processor  # Interaction
        self.current_file = None
        self.image_tk = None

        self.root.title("HIT137 Image Editor")
        self.root.geometry("900x700")

        # Menu Bar
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_image)
        filemenu.add_command(label="Save", command=self.save_image)
        filemenu.add_command(label="Save As", command=self.save_as_image)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_command(label="Redo", command=self.redo)
        menubar.add_cascade(label="Edit", menu=editmenu)
        self.root.config(menu=menubar)

        # Control Panel (Left Sidebar)
        self.control_frame = ttk.Frame(self.root, padding=10)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y)

        buttons = [
            ("Grayscale", self.apply_grayscale),
            ("Edge Detection", self.apply_edge),
            ("Rotate 90°", lambda: self.apply_rotate(90)),
            ("Rotate 180°", lambda: self.apply_rotate(180)),
            ("Rotate 270°", lambda: self.apply_rotate(270)),
            ("Flip Horizontal", lambda: self.apply_flip('horizontal')),
            ("Flip Vertical", lambda: self.apply_flip('vertical'))
        ]
        for text, cmd in buttons:  # Loop for button creation
            ttk.Button(self.control_frame, text=text, command=cmd).pack(fill=tk.X, pady=2)

        # Sliders with Apply Buttons
        self._create_slider("Blur Intensity", 0, 10, self.apply_blur)
        self._create_slider("Brightness", -100, 100, self.apply_brightness)
        self._create_slider("Contrast", 0.5, 3.0, self.apply_contrast, resolution=0.1)
        self._create_slider("Scale", 0.1, 2.0, self.apply_resize, resolution=0.1)

        # Image Display Area (Scrollable Canvas)
        self.canvas_frame = ttk.Frame(self.root)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.h_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.v_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL)
        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(self.canvas_frame, bg="gray", xscrollcommand=self.h_scroll.set, yscrollcommand=self.v_scroll.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.h_scroll.config(command=self.canvas.xview)
        self.v_scroll.config(command=self.canvas.yview)

        # Status Bar
        self.status_var = tk.StringVar(value="Welcome! Load an image to start.")
        ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W).pack(side=tk.BOTTOM, fill=tk.X)

    def _create_slider(self, label, from_, to, apply_cmd, resolution=1):
        """Helper: Create slider with label and apply button."""
        ttk.Label(self.control_frame, text=label).pack()
        slider = tk.Scale(self.control_frame, from_=from_, to=to, orient=tk.HORIZONTAL, resolution=resolution)
        slider.pack(fill=tk.X)
        ttk.Button(self.control_frame, text=f"Apply {label}", command=lambda: apply_cmd(slider.get())).pack(fill=tk.X, pady=2)

    def open_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.bmp")])
        if filepath:
            try:
                img = self.processor.load_image(filepath)
                self.current_file = filepath
                self.display_image(img)
                self.update_status()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def save_image(self):
        if not self.current_file:
            return self.save_as_image()
        if messagebox.askyesno("Confirm Save", "Overwrite existing file?"):
            self.processor.save_image(self.current_file)
            messagebox.showinfo("Success", "Saved!")

    def save_as_image(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")])
        if filepath:
            self.processor.save_image(filepath)
            self.current_file = filepath
            messagebox.showinfo("Success", "Saved!")
            self.update_status()

    def display_image(self, img):
        if img is None:
            return
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_img)
        self.image_tk = ImageTk.PhotoImage(pil_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.canvas.config(scrollregion=(0, 0, pil_img.width, pil_img.height))

    def update_status(self):
        if self.current_file:
            name = os.path.basename(self.current_file)
            h, w = self.processor.get_dimensions()
            self.status_var.set(f"File: {name} | Size: {w}x{h}")
        else:
            self.status_var.set("No image loaded.")

    # Apply Methods (Wrapper for processor calls)
    def apply_grayscale(self): self._apply_and_display(self.processor.grayscale)
    def apply_blur(self, val): self._apply_and_display(self.processor.blur, val)
    def apply_edge(self): self._apply_and_display(self.processor.edge_detection)
    def apply_brightness(self, val): self._apply_and_display(self.processor.adjust_brightness, val)
    def apply_contrast(self, val): self._apply_and_display(self.processor.adjust_contrast, val)
    def apply_rotate(self, angle): self._apply_and_display(self.processor.rotate, angle)
    def apply_flip(self, dir): self._apply_and_display(self.processor.flip, dir)
    def apply_resize(self, scale): self._apply_and_display(self.processor.resize, scale)

    def _apply_and_display(self, method, *args):
        if self.processor.get_current_image() is None:
            messagebox.showwarning("Warning", "Load an image first.")
            return
        try:
            img = method(*args)
            self.display_image(img)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def undo(self):
        img = self.processor._history.undo()  # Access via processor's history
        if img is not None:
            self.processor._current_image = img
            self.display_image(img)
            messagebox.showinfo("Undo", "Done!")
        else:
            messagebox.showwarning("Undo", "Nothing to undo.")

    def redo(self):
        img = self.processor._history.redo()
        if img is not None:
            self.processor._current_image = img
            self.display_image(img)
            messagebox.showinfo("Redo", "Done!")
        else:
            messagebox.showwarning("Redo", "Nothing to redo.")