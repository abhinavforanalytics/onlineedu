"""Framework for model quote."""


class QuoteModel:
    """Framework for model quote."""

    def __init__(self, body="", author=""):
        """Initialize text and author variables."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return the model of the quote."""
        return f"{self.body} - {self.author}"
