import os
import sys
import traceback

# Add parent dir to path so we can import app.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Top-level `app` binding (Vercel's static scan needs to see this name unambiguously)
app = None

try:
    from app import app as _flask_app
    app = _flask_app
except Exception as e:
    # Fallback: surface error in browser instead of crashing the function
    from flask import Flask
    _err_msg = f"Import error: {type(e).__name__}: {e}\n\n{traceback.format_exc()}"
    app = Flask(__name__)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def _err(path):
        return (
            f"<pre style='font-family:monospace;padding:20px;color:#ef4444'>{_err_msg}</pre>",
            500,
        )

# Vercel also accepts `handler` as an alias
handler = app
