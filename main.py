import tkinter as tk
from gui import ImageEditorGUI
from image_processor import ImageProcessor
from history_manager import HistoryManager

if __name__ == "__main__":
    root = tk.Tk()
    history = HistoryManager()  # Separate history management
    processor = ImageProcessor(history)
    app = ImageEditorGUI(root, processor)
    root.mainloop()