import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"==================================================================")
print(f" HiLabs Case Management Workbench MVP is running!")
print(f" Local URL: http://localhost:{PORT}")
print(f" Opening default web browser automatically...")
print(f" Press Ctrl+C in this terminal to stop the server.")
print(f"==================================================================")

try:
    webbrowser.open(f"http://localhost:{PORT}")
except Exception:
    pass

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")

