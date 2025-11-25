#!/usr/bin/env python3
"""
Simple HTTP Server for Development
Serves static files from the current directory
Perfect for testing the portfolio landing page locally
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Configuration
PORT = 8000
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler with better logging and MIME types"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom logging format
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")

def run_server():
    """Start the development server"""
    
    # Change to the script directory
    os.chdir(DIRECTORY)
    
    # Create server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("🚀 Portfolio Development Server")
        print("=" * 60)
        print(f"📁 Serving files from: {DIRECTORY}")
        print(f"🌐 Server running at: http://localhost:{PORT}")
        print(f"🔗 Open in browser: http://localhost:{PORT}/index.html")
        print("=" * 60)
        print("Press Ctrl+C to stop the server")
        print("=" * 60)
        print()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n" + "=" * 60)
            print("🛑 Server stopped")
            print("=" * 60)
            sys.exit(0)

if __name__ == "__main__":
    run_server()
