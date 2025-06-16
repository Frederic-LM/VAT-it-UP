# VAT Invoicing Dashboard

VAT it Up is a  simple but powerful desktop utility for calculating VAT and summing up multiple items for invoicing or quoting. Built with Python and `tkinter`.


---

## Table of Contents
- [About The Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [For End-Users (Running the Application)](#for-end-users)
  - [For Developers (Running from Source)](#for-developers)
- [How to Build the Executable](#how-to-build-the-executable)
- [File Structure](#file-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---


## About The Project

This application was designed to solve a common problem for freelancers and small businesses: quickly calculating the pre-tax (HT) price and VAT amount from a final price (TTC), and keeping a running total of multiple items with different VAT rates.

It provides a clean, three-column dashboard interface:
- **Item Calculators:** Two dedicated sections for items with two different VAT rates 20% and 5.5% (dafault values, but can be changed in the options tab or hardcoded to suit your needs).
- **Grand Totals:** A clear, automatically updated summary of the total TTC, HT, and VAT for all added items.
- **Activity Log:** A timestamped log that records every item added to the total, providing a clear audit trail.

---
## Screenshot

![vat_it_up](https://github.com/user-attachments/assets/d47b71f6-e66b-4671-b792-c5d50a141dbf)


## Features

- ✅ **Dual VAT Calculators:** Simultaneously handle items with 20% and 5.5% VAT.
- ✅ **Real-Time Calculation:** Prices before tax (HT) and VAT amounts are calculated automatically as you type.
- ✅ **Summation Feature:** Easily add items to a running grand total with a single click.
- ✅ **Clear Totals Display:** See the total TTC, HT, and VAT amounts clearly summarized.
- ✅ **Timestamped Activity Log:** Keep track of every addition for easy review.
- ✅ **Reset Functionality:** Clear the totals and the log with one button to start a new invoice.
- ✅ **Standalone Executable:** Packaged into a single `.exe` file that runs on any modern Windows machine without needing Python installed.

---

## Getting Started

You can either run the pre-built application directly or run it from the source code if you are a developer.

### For End-Users

The easiest way to use the application is to download the pre-compiled executable.

1.  Go to the [**Releases**](https://github.com/Frederic-LM/VAT-it-UP/releases) page of this repository.
2.  Download the `VAT-Dashboard.exe` file from the latest release.
3.  Save the file to your computer and double-click it to run. No installation is needed!

### For Developers

If you want to run the application from the source code or modify it, you'll need Python installed on your system.

**Prerequisites:**
- Python 3.6 or newer

**Setup Instructions:**

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Frederic-LM/VAT-it-UP.git
    cd VAT-it-UP
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    - On Windows:
      ```sh
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

4.  **Install dependencies:**
    This project uses `PyInstaller` to build the executable. Create a file named `requirements.txt` with the following content:
    ```
    pyinstaller
    ```
    Then, install it using pip:
    ```sh
    pip install -r requirements.txt
    ```

5.  **Run the application:**
    ```sh
    python vat_it_up.py
    ```

---

## How to Build the Executable

You can compile the Python script into a single standalone `.exe` file using `PyInstaller`.

1.  Make sure you have followed the setup instructions for developers and have `PyInstaller` installed.
2.  Navigate to the project directory in your terminal.
3.  Run the following command:
    ```sh
    pyinstaller --onefile --windowed --name="VAT Dashboard" vat_it_up.py
    ```
    - `--onefile`: Bundles everything into a single executable file.
    - `--windowed`: Prevents a console window from appearing in the background when the GUI runs.
    - `--name`: Sets the name of the final executable.

4.  The finished `VAT Dashboard.exe` will be located in the newly created `dist` folder.

---

## File Structure

```
.
├── vat_it_up.py            # The main application source code
├── requirements.txt        # Project dependencies (for developers)
├── screenshot.png          # A screenshot of the application
└── README.md               # This file
```

---

## License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.

---

## Acknowledgments

- This project was built iteratively based on excellent and precise user feedback.
- Hat tip to the developers of Python, `tkinter`, and `PyInstaller` for creating powerful and accessible tools.
