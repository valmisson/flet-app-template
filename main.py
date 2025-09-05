"""
Main entry point for the Flet application.
"""

from flet import app
from app.window import AppWindow

if __name__ == "__main__":
    app(target=AppWindow)