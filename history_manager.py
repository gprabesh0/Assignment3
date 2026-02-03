class HistoryManager:
    def __init__(self, max_history=20):
        """Constructor: Set max history to prevent memory issues."""
        self._max_history = max_history
        self._history = []  # Past images
        self._redo_stack = []  # Undone images

    def add(self, image):
        """Add image to history, clear redo, trim if exceeds max."""
        self._history.append(image)
        self._redo_stack.clear()
        if len(self._history) > self._max_history:
            self._history.pop(0)  # Loop implicitly via list ops

    def undo(self):
        """Undo: Pop history, push to redo."""
        if len(self._history) > 1:
            undone = self._history.pop()
            self._redo_stack.append(undone)
            return self._history[-1]  # Current after undo
        return None

    def redo(self):
        """Redo: Pop redo, push to history."""
        if self._redo_stack:
            redone = self._redo_stack.pop()
            self._history.append(redone)
            return redone
        return None

    def clear(self):
        """Clear all stacks."""
        self._history = []
        self._redo_stack = []