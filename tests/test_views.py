import types

import flet as ft

from app.views.home_view import HomeView
from app.window import AppWindow


class DummyWindow:
    def __init__(self):
        self.width = None
        self.height = None
        self.focused = False
    def center(self):
        # no-op center used by AppWindow
        pass


class DummyPage:
    def __init__(self):
        self.window = DummyWindow()
        self.views = []
        self._route = None
        self.on_route_change = None
        self.on_view_pop = None

    def go(self, route):
        # Simulate router object passed to on_route_change
        self._route = route
        if self.on_route_change:
            router = types.SimpleNamespace(route=route)
            self.on_route_change(router)

    def update(self):
        # no-op for tests
        pass


def test_home_view_builds_text():
    home_view = HomeView()
    # HomeView should append exactly one control that is a Text instance
    assert len(home_view.controls) == 1
    control = home_view.controls[0]
    assert isinstance(control, ft.Text)
    assert "Welcome to" in control.value


def test_appwindow_route_and_window_settings():
    page = DummyPage()
    # Create AppWindow which will set page.window dimensions
    app_window = AppWindow(page)

    # window size should be set from Settings
    assert page.window.width == app_window.page.window.width
    assert page.window.height == app_window.page.window.height

    # Trigger navigation to root and ensure a HomeView was added
    page.go("/")
    assert any(isinstance(v, HomeView) for v in page.views)
