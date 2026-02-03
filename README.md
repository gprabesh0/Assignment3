# Assignment3

# Image Editor Application (Python)

## Overview
This project is a simple **Python-based Image Editor** built using **Tkinter** for the graphical user interface and **Pillow (PIL)** for image processing.  
It allows users to load an image, apply basic edits, and manage changes using **undo and redo functionality**.

The application is designed using **object-oriented principles**, with clear separation between the GUI, image processing logic, and state management.

---

## Features
- Load images from the local file system
- Display images in a GUI editor
- Apply image processing operations (e.g. grayscale)
- Undo and redo image changes
- History size limit to prevent memory issues
- Clean modular design across multiple files

---

## Project Structure
├── main.py # Application entry point
├── gui.py # GUI logic and user interaction
├── image_processor.py # Image processing functions
├── history_manager.py # Undo/redo history management
└── README.md # Project documentation

---

## Technologies Used
- **Python 3**
- **Tkinter** – GUI framework
- **Pillow (PIL)** – Image processing library

---

## How the Application Works

### 1. Image Loading
The user loads an image using a file dialog. The image is stored as a `PIL.Image` object and displayed on the GUI canvas.

### 2. Image Editing
Image operations are handled in `image_processor.py`.  
Each edit produces a new image, ensuring the original remains unchanged.

### 3. Undo / Redo Functionality
The `HistoryManager` class manages:
- A history stack for previous images
- A redo stack for undone images
- A maximum history size to avoid excessive memory usage

Each new edit is added to the history, enabling undo and redo actions.

### 4. GUI Management
The GUI is responsible for:
- User interaction (buttons, menus)
- Displaying images
- Connecting user actions to image processing and history management

---

## How to Run the Application

### Prerequisites
Make sure Python 3 is installed.  

Install the Pillow library if not already available:
```bash
pip install pillow

---

Running the App
From the project directory, run:

```bash
python main.py


---

###Design Principles

##Separation of Concerns: GUI, logic, and history management are separated

##Object-Oriented Design: Each component has a clear responsibility

##Maintainability: Modular structure allows easy extension

##User-Friendly: Simple interface with undo/redo support

##Possible Extensions
#Additional image filters (blur, rotate, brightness)

#Save edited images

#Keyboard shortcuts

#Zoom and pan functionality

###Author
Prabesh Tamang


---

### If you want
I can:
- tailor this README exactly to your **assignment rubric**
- shorten it if there’s a word limit
- add **screenshots section**
- rewrite it in a more **academic/report style**

Just tell me 👍
