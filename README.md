# 🧮 VAT It Up
### *Simple & Powerful VAT Invoicing Dashboard*

> A desktop utility built with Python and tkinter for quick VAT calculations and multi-item invoicing

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6+-green.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://github.com/Frederic-LM/VAT-it-UP/releases)

---

## 🎯 About The Project

**VAT It Up** solves a common challenge for freelancers and small businesses: **quickly calculating pre-tax (HT) prices and VAT amounts** from final prices (TTC), while maintaining a running total across multiple items with different VAT rates.

### The Problem It Solves
- ⚡ Instant VAT calculations without manual math
- 📊 Managing multiple items with different tax rates
- 🧾 Keeping accurate totals for invoicing and quoting
- 📝 Maintaining an audit trail of all calculations

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **🔢 Dual VAT Calculators** | Handle 20% and 5.5% VAT rates simultaneously (customizable) |
| **⚡ Real-Time Calculation** | Automatic HT and VAT calculation as you type |
| **➕ Smart Summation** | One-click addition to running grand totals |
| **📈 Clear Totals Display** | Clean summary of total TTC, HT, and VAT amounts |
| **📋 Activity Log** | Timestamped record of every item added |
| **🔄 Reset Functionality** | Quick clear for starting new invoices |
| **📦 Standalone Executable** | No Python installation required |

---

## 📸 Screenshot

![VAT It Up Dashboard](https://github.com/user-attachments/assets/d47b71f6-e66b-4671-b792-c5d50a141dbf)

*Clean three-column interface: Item Calculators | Grand Totals | Activity Log*

---

## 🚀 Quick Start

### 📥 For End Users

**The simplest way to get started:**

1. 🎯 Visit our [**Releases Page**](https://github.com/Frederic-LM/VAT-it-UP/releases)
2. 📦 Download `VAT-Dashboard.exe` from the latest release
3. ▶️ Double-click to run - **no installation needed!**

> 🚀 **Quick Download:** [VAT Dashboard V1 (Ready to use!)](https://github.com/Frederic-LM/VAT-it-UP/releases/download/V1/VAT.Dashboard.exe)

### 👨‍💻 For Developers

**Want to customize or contribute?**

#### Prerequisites
- Python 3.6 or newer
- Git (optional but recommended)

#### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/Frederic-LM/VAT-it-UP.git
cd VAT-it-UP

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install pyinstaller

# 5. Run the application
python vat_it_up.py
```

---

## 🏗️ Building Your Own Executable

Want to create your own standalone executable? Here's how:

```bash
# Navigate to project directory
cd VAT-it-UP

# Build single executable file
pyinstaller --onefile --windowed --name="VAT Dashboard" vat_it_up.py
```

**Build Options Explained:**
- `--onefile` → Single executable file
- `--windowed` → No console window
- `--name` → Custom executable name

📁 Find your executable in the newly created `dist/` folder

---

## 📁 Project Structure

```
VAT-it-UP/
├── 📄 vat_it_up.py          # Main application source
├── 📄 requirements.txt      # Python dependencies
├── 🖼️ screenshot.png        # Application preview
├── 📄 README.md             # This documentation
└── 📄 LICENSE               # Apache 2.0 License
```

---

## 🎨 Interface Overview

The application features a **clean three-column layout**:

| Column | Purpose |
|--------|---------|
| **Left & Center** | Dual VAT calculators (20% & 5.5% default rates) |
| **Right** | Grand totals and timestamped activity log |

### 🔧 Customization Options
- VAT rates can be modified in the options tab
- Rates can also be hardcoded for specific business needs
- Interface scales well for different screen sizes

---

## 📄 License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Built iteratively** based on excellent user feedback
- Powered by **Python**, **tkinter**, and **PyInstaller**
- Special thanks to the open-source community for making powerful tools accessible


---

<div align="center">

**⭐ If this project helped you, consider giving it a star!**

** [Day after day I will walk and I will ...  ](https://www.youtube.com/watch?v=JZwPcPy04AQ) ** 🎸

</div>
