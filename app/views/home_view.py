from flet import View, Text
from app.config.settings import Settings

class HomeView(View):
    def __init__(self):
        super().__init__()

        self.controls.append(self._build())

    def _build(self):
        return Text(f"Welcome to {Settings.APP_NAME}!")