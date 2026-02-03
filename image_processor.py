import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, history):
        self._original_image = None
        self._current_image = None
        self._history = history

    def load_image(self, filepath):
        """Load and set image, initialize history."""
        self._original_image = cv2.imread(filepath)
        if self._original_image is None:
            raise ValueError("Invalid image file.")
        self._current_image = self._original_image.copy()
        self._history.clear()
        self._history.add(self._current_image.copy())
        return self._current_image

    def save_image(self, filepath):
        """Save current image."""
        cv2.imwrite(filepath, self._current_image)

    def get_current_image(self):
        """Getter for current image."""
        return self._current_image.copy() if self._current_image is not None else None

    def get_dimensions(self):
        """Get image height and width."""
        return self._current_image.shape[:2] if self._current_image is not None else (0, 0)

    def _apply(self, func, *args, **kwargs):
        """Apply function and update history using a loop for consistency."""
        new_image = func(*args, **kwargs)
        self._current_image = new_image
        self._history.add(new_image.copy())

    # Image Processing Methods
    def grayscale(self):
        def apply_func():
            gray = cv2.cvtColor(self._current_image, cv2.COLOR_BGR2GRAY)
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        self._apply(apply_func)
        return self._current_image

    def blur(self, intensity=5):
        kernel = max(1, intensity * 2 + 1)  # Odd kernel
        def apply_func():
            return cv2.GaussianBlur(self._current_image, (kernel, kernel), 0)
        self._apply(apply_func)
        return self._current_image

    def edge_detection(self):
        def apply_func():
            gray = cv2.cvtColor(self._current_image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        self._apply(apply_func)
        return self._current_image

    def adjust_brightness(self, value=0):
        def apply_func():
            return cv2.convertScaleAbs(self._current_image, beta=value)
        self._apply(apply_func)
        return self._current_image

    def adjust_contrast(self, value=1.0):
        def apply_func():
            return cv2.convertScaleAbs(self._current_image, alpha=value)
        self._apply(apply_func)
        return self._current_image

    def rotate(self, angle=90):
        rotations = {90: cv2.ROTATE_90_CLOCKWISE, 180: cv2.ROTATE_180, 270: cv2.ROTATE_90_COUNTERCLOCKWISE}
        if angle not in rotations:
            raise ValueError("Invalid angle.")
        def apply_func():
            return cv2.rotate(self._current_image, rotations[angle])
        self._apply(apply_func)
        return self._current_image

    def flip(self, direction='horizontal'):
        flips = {'horizontal': 1, 'vertical': 0}
        if direction not in flips:
            raise ValueError("Invalid direction.")
        def apply_func():
            return cv2.flip(self._current_image, flips[direction])
        self._apply(apply_func)
        return self._current_image

    def resize(self, scale=1.0):
        if scale <= 0:
            raise ValueError("Scale must be positive.")
        height, width = self._current_image.shape[:2]
        new_size = (int(width * scale), int(height * scale))
        def apply_func():
            return cv2.resize(self._current_image, new_size, interpolation=cv2.INTER_AREA)
        self._apply(apply_func)
        return self._current_image
