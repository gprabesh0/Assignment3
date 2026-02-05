# Image Editor

## Overview
This repository contains the source code for a desktop image editing application developed as part of Assignment 3. The project demonstrates a strong understanding of Object-Oriented Programming (OOP) principles, GUI development using Tkinter, and image processing using OpenCV. It allows users to load, apply various effects to, and save images in common formats (JPG, PNG, BMP).

The repository is public and was created before starting the assignment.

https://github.com/gprabesh0/Assignment3

## Acknowledgments
### Group Members:
- Fuad Ahmed Anonto   - S399378
- Prabesh Tamang      - S398925
- Pramisha Shrestha   - S399137
- Sushil Dhungana     - S399406

## Functional Requirements Met

### OOP: 
Structured with four classes (ImageEditorGUI, ImageProcessor, HistoryManager, and orchestration in main.py), demonstrating encapsulation (private attributes), constructors, methods, and class interactions.

### OpenCV Image Processing:
All required features implemented:
***Grayscale Conversion (toggleable)***
***Blur Effect (Gaussian blur, adjustable intensity)***
***Edge Detection (Canny algorithm, toggleable)***
***Brightness Adjustment (increase/decrease)***
***Contrast Adjustment***
***Image Rotation (90°, 180°, 270°)***
***Image Flip (horizontal/vertical)***
***Resize/Scale***

### Tkinter GUI: 
Flexible, user-friendly interface with:
***Main window (900x700, titled "Image Editor")***
***Menu bar (File: Open, Save, Save As, Exit; Edit: Undo, Redo)***
***Scrollable canvas for image display***
***Control panel with toggle buttons, sliders (with Apply/Reset), and buttons for effects***
***Status bar (filename, dimensions)***
***File dialogs for open/save***
***Sliders for adjustable effects (e.g., blur intensity)***
***Message boxes for confirmations/errors***

## Requirements
***Python 3.x (tested on 3.14)***
***Dependencies: opencv-python, numpy,tkinter (built-in)***

## Installation
1.Install dependencies:

```bash
pip install opencv-python pillow
```

2. Clone the repository:

```bash
git clone https://github.com/gprabesh0/Assignment3.git
```

3. Navigate to the project directory:

```bash
cd Assignment3
```

## Usage
1. Run the application:

```bash
python main.py
```

2. Load an image via File > Open (supports JPG, PNG, BMP).
3. Apply effects using the sidebar:
***Toggle Grayscale or Edge Detection (click to apply/remove).***
***Adjust sliders for Blur, Brightness, Contrast, or Scale, then click "Apply" (or "Reset" to default).***
***Click buttons for Rotate or Flip.***
4. Use Edit > Undo/Redo for changes.
5. Reset via File > Reset to Original.
6. Save via File > Save or Save As.

## Project Structure
***main.py: Entry point; initializes classes and GUI.***
***gui.py: Tkinter GUI implementation (menus, canvas, controls).***
***image_processor.py: OpenCV image processing logic.***
***history_manager.py: Undo/redo history management.***
***README.md: This documentation.***
