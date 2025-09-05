import flet as ft
import sentry_sdk

from .config.settings import Settings
from .config.logger import logger
from .views.home_view import HomeView

class AppWindow:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.width = Settings.DEFAULT_WINDOW_WIDTH
        self.page.window.height = Settings.DEFAULT_WINDOW_HEIGHT
        self.page.window.focused = True
        self.page.window.center()

        self.page.on_route_change = self.on_route_change
        self.page.on_view_pop = self.on_view_pop

        self.page.go("/")

        logger.info("Application initialized")

    def on_route_change(self, router):
        try:
            self.page.views.clear()

            if router.route == "/":
                self.page.views.append(HomeView())

            self.page.update()
        except Exception as e:
            logger.error(f"Error during route change to {router.route}: {e}")
            sentry_sdk.capture_exception(e)

    def on_view_pop(self, _):
        try:
            self.page.views.pop()
            self.page.update()
        except Exception as e:
            logger.error(f"Error during view pop: {e}")
            sentry_sdk.capture_exception(e)