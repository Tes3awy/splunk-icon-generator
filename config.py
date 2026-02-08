import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "7f7e46525736ec38e237933fa9a43fe3683b425b36b753b11b7557f0ddcc61ac"
    )
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "svg"}
    ICON_SPECS = [
        # Standard Square Icons - Force specific dimensions
        {"name": "appIcon.png", "size": (36, 36), "resize_mode": "force"},
        {"name": "appIcon_2x.png", "size": (72, 72), "resize_mode": "force"},
        {"name": "appIconAlt.png", "size": (36, 36), "resize_mode": "force"},
        {"name": "appIconAlt_2x.png", "size": (72, 72), "resize_mode": "force"},
        # Navigation Logos - Fit within max dimensions (preserve aspect ratio)
        {"name": "appLogo.png", "size": (160, 40), "resize_mode": "fit"},
        {"name": "appLogo_2x.png", "size": (320, 80), "resize_mode": "fit"},
    ]
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MBs
    STATS_FILE = "stats.json"


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
    TESTING = False


# Dictionary to map environment names to config classes
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
