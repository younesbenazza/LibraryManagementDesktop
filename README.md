# Django React App served as Desktop App

This project is a Django and React-based application packaged as a desktop app using PyInstaller. The application allows for full desktop functionality, serving both the frontend and backend components in a single executable.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12.5**: Required to run Django and package the app.
- **pip**: Python package installer to manage dependencies.
- **PyInstaller**: To package the application as an executable.

**HOW TO USE**
Install the required Python dependencies by running:
```bash
pip install -r requirements.txt
```
To package the app as an executable, run:
```bash
pyinstaller --clean apprun.spec
```
This command cleans up previous builds and uses the apprun.spec configuration to package the application.

Once the build is complete, you can find the executable in the dist folder.

**DATABASE**

once you open the App you'll find the db in "APPDATA\MYAPP"
