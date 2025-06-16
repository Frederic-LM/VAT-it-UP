#!/usr/bin/env python3

# --- Import necessary libraries ---
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# --- Main Application Class ---
class VatCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VAT Invoicing Dashboard")
        self.root.geometry("1000x420") 
        self.root.resizable(False, False)

        # --- Core VAT Rate Variables ---
        self.vat_rate_1 = 20.0
        self.vat_rate_2 = 5.5

        # --- Variable Initialization ---
        self.price_ttc_1_var = tk.StringVar()
        self.ht_1_var = tk.StringVar(value="0.00 €")
        self.vat_1_var = tk.StringVar(value="0.00 €")
        self.current_ttc_1, self.current_ht_1, self.current_vat_1 = 0.0, 0.0, 0.0
        
        # --- REMOVED THE UNUSED StringVars for the LabelFrame titles ---

        self.price_ttc_2_var = tk.StringVar()
        self.ht_2_var = tk.StringVar(value="0.00 €")
        self.vat_2_var = tk.StringVar(value="0.00 €")
        self.current_ttc_2, self.current_ht_2, self.current_vat_2 = 0.0, 0.0, 0.0
        
        self.total_ttc, self.total_ht, self.total_vat = 0.0, 0.0, 0.0
        self.total_ttc_var = tk.StringVar(value="0.00 €")
        self.total_ht_var = tk.StringVar(value="0.00 €")
        self.total_vat_var = tk.StringVar(value="0.00 €")

        self.options_vat1_var = tk.StringVar(value=str(self.vat_rate_1))
        self.options_vat2_var = tk.StringVar(value=str(self.vat_rate_2))
        self.options_status_var = tk.StringVar()

        self.price_ttc_1_var.trace_add("write", self.calculate_vat1)
        self.price_ttc_2_var.trace_add("write", self.calculate_vat2)

        self.configure_styles()
        self.create_widgets()
        
        self.update_dashboard_labels()
        self.calculate_vat1()
        self.calculate_vat2()

    def configure_styles(self):
        style = ttk.Style(self.root)
        style.configure("TLabel", padding=5, font=('Segoe UI', 10))
        style.configure("Total.TLabel", font=('Segoe UI', 10, 'bold'))
        style.configure("TEntry", padding=5, font=('Segoe UI', 10))
        style.configure("TLabelframe.Label", font=('Segoe UI', 11, 'bold'))
        style.configure("Header.TLabel", font=('Segoe UI', 12, 'bold'))
        style.configure("TButton", font=('Segoe UI', 10))
        style.configure("Success.TLabel", foreground="green")
        style.configure("Error.TLabel", foreground="red")

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        dashboard_tab = ttk.Frame(notebook, padding="5")
        options_tab = ttk.Frame(notebook, padding="15")
        notebook.add(dashboard_tab, text="Dashboard")
        notebook.add(options_tab, text="Options")
        self.create_dashboard_tab(dashboard_tab)
        self.create_options_tab(options_tab)

    def create_dashboard_tab(self, parent):
        parent.columnconfigure(0, weight=3); parent.columnconfigure(1, weight=3)
        parent.columnconfigure(2, weight=2); parent.rowconfigure(0, weight=1)

        left_panel = ttk.Frame(parent)
        left_panel.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew", padx=(0, 10))
        left_panel.columnconfigure(0, weight=1); left_panel.columnconfigure(1, weight=1)

        # --- FIX: Store LabelFrames as instance variables (self.frame1) and remove textvariable ---
        self.frame1 = ttk.LabelFrame(left_panel, padding=10)
        self.frame1.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        self.create_vat_card(self.frame1, self.price_ttc_1_var, self.ht_1_var, self.vat_1_var, self.add_to_totals_1)

        self.frame2 = ttk.LabelFrame(left_panel, padding=10)
        self.frame2.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        self.create_vat_card(self.frame2, self.price_ttc_2_var, self.ht_2_var, self.vat_2_var, self.add_to_totals_2)
        
        totals_frame = ttk.LabelFrame(left_panel, text="Grand Totals", padding=10)
        totals_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(10, 0))
        self.create_totals_section(totals_frame)

        log_frame = ttk.LabelFrame(parent, text="Activity Log", padding=10)
        log_frame.grid(row=0, column=2, rowspan=2, sticky="ns")
        self.create_log_widgets(log_frame)

    def create_options_tab(self, parent):
        parent.columnconfigure(1, weight=1)
        ttk.Label(parent, text="Set Custom VAT Rates", font=('Segoe UI', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        ttk.Label(parent, text="VAT Rate 1 (%):").grid(row=1, column=0, sticky="w", padx=5)
        ttk.Entry(parent, textvariable=self.options_vat1_var, width=10).grid(row=1, column=1, sticky="w", padx=5)
        ttk.Label(parent, text="VAT Rate 2 (%):").grid(row=2, column=0, sticky="w", padx=5, pady=10)
        ttk.Entry(parent, textvariable=self.options_vat2_var, width=10).grid(row=2, column=1, sticky="w", padx=5, pady=10)
        ttk.Button(parent, text="Apply Changes", command=self.apply_new_vat_rates).grid(row=3, column=1, sticky="w", padx=5, pady=20)
        ttk.Label(parent, textvariable=self.options_status_var).grid(row=4, column=0, columnspan=2, sticky="w", padx=5)

    def create_vat_card(self, parent, price_var, ht_var, vat_var, add_command):
        parent.columnconfigure(1, weight=1)
        ttk.Label(parent, text="Price (TTC):").grid(row=0, column=0, sticky="w", padx=(0, 5))
        ttk.Entry(parent, textvariable=price_var, width=15).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(parent, text="+ to Total", command=add_command, width=10).grid(row=0, column=2, sticky="e")
        ttk.Separator(parent, orient='horizontal').grid(row=1, column=0, columnspan=3, sticky='ew', pady=10)
        ttk.Label(parent, text="Price (HT):").grid(row=2, column=0, sticky="w")
        ttk.Label(parent, textvariable=ht_var, style="Total.TLabel").grid(row=2, column=2, sticky="e")
        ttk.Label(parent, text="VAT Amount:").grid(row=3, column=0, sticky="w")
        ttk.Label(parent, textvariable=vat_var, style="Total.TLabel").grid(row=3, column=2, sticky="e")

    def create_totals_section(self, parent):
        parent.columnconfigure(1, weight=1)
        ttk.Label(parent, text="Total Price (HT):").grid(row=0, column=0, sticky="w")
        ttk.Label(parent, textvariable=self.total_ht_var, style="Total.TLabel").grid(row=0, column=1, sticky="e")
        ttk.Label(parent, text="Total VAT:").grid(row=1, column=0, sticky="w")
        ttk.Label(parent, textvariable=self.total_vat_var, style="Total.TLabel").grid(row=1, column=1, sticky="e")
        ttk.Label(parent, text="Total Price (TTC):", font=('Segoe UI', 11, 'bold')).grid(row=2, column=0, sticky="w", pady=(5,0))
        ttk.Label(parent, textvariable=self.total_ttc_var, style="Header.TLabel").grid(row=2, column=1, sticky="e", pady=(5,0))
        ttk.Button(parent, text="Reset All", command=self.reset_all).grid(row=3, column=1, sticky="e", pady=(15, 0))

    def create_log_widgets(self, parent):
        self.log_text = tk.Text(parent, width=45, wrap=tk.WORD, font=('Courier New', 9), state=tk.DISABLED)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def apply_new_vat_rates(self):
        try:
            new_rate1 = float(self.options_vat1_var.get().replace(',', '.'))
            new_rate2 = float(self.options_vat2_var.get().replace(',', '.'))
            if not (0 <= new_rate1 <= 100 and 0 <= new_rate2 <= 100):
                raise ValueError("Rates must be between 0 and 100.")
            self.vat_rate_1 = new_rate1
            self.vat_rate_2 = new_rate2
            self.update_dashboard_labels()
            self.calculate_vat1()
            self.calculate_vat2()
            self.options_status_var.set("Settings applied successfully!")
            self.root.after(3000, lambda: self.options_status_var.set(""))
        except ValueError as e:
            self.options_status_var.set(f"Error: Invalid input. {e}")

    # --- FIX: Update this method to use .config() instead of a StringVar ---
    def update_dashboard_labels(self):
        """Updates the titles of the VAT calculator cards using .config()"""
        self.frame1.config(text=f"Item at {self.vat_rate_1}% VAT")
        self.frame2.config(text=f"Item at {self.vat_rate_2}% VAT")
    
    # --- All other methods from here are correct and largely unchanged ---
    def calculate_vat1(self, *args):
        try:
            price_ttc = float(self.price_ttc_1_var.get().replace(',', '.'))
            divisor = 1 + (self.vat_rate_1 / 100.0)
            price_ht = price_ttc / divisor; vat_amount = price_ttc - price_ht
            self.current_ttc_1, self.current_ht_1, self.current_vat_1 = price_ttc, price_ht, vat_amount
            self.ht_1_var.set(f"{price_ht:.2f} €"); self.vat_1_var.set(f"{vat_amount:.2f} €")
        except (ValueError, TypeError):
            self.current_ttc_1, self.current_ht_1, self.current_vat_1 = 0.0, 0.0, 0.0
            self.ht_1_var.set("0.00 €"); self.vat_1_var.set("0.00 €")
    
    def calculate_vat2(self, *args):
        try:
            price_ttc = float(self.price_ttc_2_var.get().replace(',', '.'))
            divisor = 1 + (self.vat_rate_2 / 100.0)
            price_ht = price_ttc / divisor; vat_amount = price_ttc - price_ht
            self.current_ttc_2, self.current_ht_2, self.current_vat_2 = price_ttc, price_ht, vat_amount
            self.ht_2_var.set(f"{price_ht:.2f} €"); self.vat_2_var.set(f"{vat_amount:.2f} €")
        except (ValueError, TypeError):
            self.current_ttc_2, self.current_ht_2, self.current_vat_2 = 0.0, 0.0, 0.0
            self.ht_2_var.set("0.00 €"); self.vat_2_var.set("0.00 €")

    def add_to_totals_1(self):
        if self.current_ttc_1 > 0:
            self.log_activity(f"Added {self.current_ttc_1:.2f} € (VAT @ {self.vat_rate_1}%)")
            self.total_ttc += self.current_ttc_1; self.total_ht += self.current_ht_1
            self.total_vat += self.current_vat_1; self.update_totals_display()
    
    def add_to_totals_2(self):
        if self.current_ttc_2 > 0:
            self.log_activity(f"Added {self.current_ttc_2:.2f} € (VAT @ {self.vat_rate_2}%)")
            self.total_ttc += self.current_ttc_2; self.total_ht += self.current_ht_2
            self.total_vat += self.current_vat_2; self.update_totals_display()

    def log_activity(self, message):
        self.log_text.config(state=tk.NORMAL); timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n"); self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def reset_all(self):
        self.total_ttc, self.total_ht, self.total_vat = 0.0, 0.0, 0.0; self.update_totals_display()
        self.log_text.config(state=tk.NORMAL); self.log_text.delete('1.0', tk.END)
        self.log_text.config(state=tk.DISABLED); self.log_activity("Dashboard cleared.")

    def update_totals_display(self):
        self.total_ttc_var.set(f"{self.total_ttc:.2f} €"); self.total_ht_var.set(f"{self.total_ht:.2f} €")
        self.total_vat_var.set(f"{self.total_vat:.2f} €")

if __name__ == "__main__":
    app_root = tk.Tk()
    app = VatCalculatorApp(app_root)
    app_root.mainloop()
