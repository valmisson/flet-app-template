from app.config.settings import Settings


def test_settings_values():
    # Settings Enum stores values directly; compare stringification for stable check
    assert str(Settings.APP_NAME) == "Flet App Template"
    assert str(Settings.APP_VERSION) == "0.1.0"
    assert isinstance(int(Settings.DEFAULT_WINDOW_WIDTH), int)
    assert isinstance(int(Settings.DEFAULT_WINDOW_HEIGHT), int)
    # IS_DEV is boolean-like when stringified
    assert str(Settings.IS_DEV) in ("True", "False")
    assert "logs/app.log" in str(Settings.LOG_FILE_PATH)
