import os, sys, traceback

# Add parent dir to path so we can import app.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from app import app
except Exception as e:
    # Fallback: surface error in browser instead of crashing the function
    from flask import Flask
    app = Flask(__name__)
    err_msg = f"Import error: {type(e).__name__}: {e}\n\n{traceback.format_exc()}"

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def _err(path):
        return f"<pre style='font-family:monospace;padding:20px;color:#ef4444'>{err_msg}</pre>", 500
