import json
import os

from flask import current_app


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[
        1
    ].lower() in current_app.config.get("ALLOWED_EXTENSIONS")


def get_download_count():
    """Reads the current download count from the stats file."""
    if not os.path.exists(current_app.config.get("STATS_FILE")):
        return 0
    try:
        with open(current_app.config.get("STATS_FILE"), "rt") as f:
            data = json.load(f)
            return data.get("downloads", 0)
    except (json.JSONDecodeError, IOError, Exception):
        # If any error occurs reading (permissions, corruption), return 0
        return 0


def increment_download_count():
    """Increments the download count safely, ignoring errors on read-only systems."""
    # 1. Check if we are on Vercel or a read-only environment
    # Vercel sets the 'VERCEL' environment variable
    if os.environ.get("VERCEL"):
        return

    try:
        count = get_download_count() + 1
        with open(current_app.config.get("STATS_FILE"), "wt") as f:
            json.dump({"downloads": count}, f, indent=4)
    except IOError:
        pass  # Fail silently if we can't write (e.g. read-only filesystem)
