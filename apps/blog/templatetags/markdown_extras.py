import logging
import markdown
from django import template
from django.conf import settings

# Set up logging
logger = logging.getLogger(__name__)

# Initialize template library
register = template.Library()

# Default markdown extensions with more advanced features
DEFAULT_EXTENSIONS = [
    "extra",  # Adds extra features (e.g., abbreviation support, footnotes, etc.)
    "nl2br",  # Converts newlines to <br> tags
    "tables",  # Enables table support in markdown
    "codehilite",  # Adds syntax highlighting for code blocks
    "admonition",  # Provides support for block quotes like notes, warnings, etc.
    "footnotes",  # Allows usage of footnotes
    # "strikethrough",  # Adds support for strikethrough syntax
    # "pymdownx.emoji",  # Support for emoji shortcuts like :smile:
    # "pymdownx.highlight",  # Custom syntax highlighting for fenced code blocks
    # "pymdownx.superfences",  # Enhanced support for fenced code blocks and tables
    "toc",  # Automatically generates a table of contents
    # For math rendering (requires MathJax)
    # "markdown_math",  # Optional: For rendering LaTeX-style math
]

@register.filter(name="markdown")
def markdown_filter(value, extensions=None):
    """
    Convert Markdown text to HTML with optional extensions.

    Args:
        value (str): The markdown text to be converted.
        extensions (list, optional): A list of markdown extensions to enable. If None, the default extensions are used.

    Returns:
        str: The rendered HTML.
    """
    if not value:
        return ""

    # Use custom extensions if provided, otherwise fall back to default extensions
    extensions_to_use = extensions or DEFAULT_EXTENSIONS

    try:
        # Render the markdown text to HTML
        return markdown.markdown(
            value,
            extensions=extensions_to_use,
        )
    except Exception as e:
        # Log any errors that occur during markdown processing
        logger.error(f"Error processing markdown: {e}")
        return f"<p>Error processing markdown content.</p>"
