import os
import sys
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
import webbrowser
import threading
import time
import tkinter as tk

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libr.settings')  # Replace 'libr' with your project name

def run_server():
    execute_from_command_line(['', 'runserver', '--noreload'])

def open_browser():
    webbrowser.open('http://127.0.0.1:8000')

def open_browser_window():
    time.sleep(2)  # Wait for the server to start
    open_browser()

def close_app():
    print("Arrêt du serveur...")
    sys.exit(0)

if __name__ == '__main__':
    django.setup()

    # Start the Django server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Open the browser
    browser_thread = threading.Thread(target=open_browser_window)
    browser_thread.daemon = True
    browser_thread.start()

    # Create the GUI
    root = tk.Tk()
    root.title("Gestion de la Bibliothèque")
    root.geometry("600x400")  # Set window size to 400x200 pixels

    # Create a label with a font that supports French
    label = tk.Label(root, text="L'application de gestion de bibliothèque fonctionne", font=("Arial", 14))
    label.pack(pady=20)

    # Create a button to reopen the browser
    reopen_button = tk.Button(root, text="Rouvrir le navigateur", command=open_browser, font=("Arial", 12))
    reopen_button.pack(pady=10)

    # Create a button to close the app
    close_button = tk.Button(root, text="Fermer", command=close_app, font=("Arial", 12))
    close_button.pack(pady=10)

    root.mainloop()
