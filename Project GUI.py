import tkinter as tk
from tkinter import ttk, messagebox

class MobileRecharge:
    def __init__(self, mobile_number, operator, plan_name, plan_amount,
                 plan_validity, data_per_day, talktime, gst_rate=18):
        self.mobile_number = mobile_number
        self.operator = operator
        self.plan_name = plan_name
        self.plan_amount = plan_amount
        self.plan_validity = plan_validity
        self.data_per_day = data_per_day
        self.talktime = talktime
        self.gst_rate = gst_rate

    def gst_cal(self):
        return (self.plan_amount * self.gst_rate) / 100

    def total_cal(self):
        return self.plan_amount + self.gst_cal()

    def get_display_text(self):
        return f"""
Mobile Number : {self.mobile_number}
Operator      : {self.operator}
Plan Name     : {self.plan_name}

Plan Amount   : Rs. {self.plan_amount}
Validity      : {self.plan_validity}
Data / Day    : {self.data_per_day}
Talktime      : {self.talktime}

GST ({self.gst_rate}%) : Rs. {round(self.gst_cal(), 2)}
Total Amount  : Rs. {round(self.total_cal(), 2)}
"""


plans = {
    "Jio": [
        ("Monthly Plan", 299, "28 Days", "1.5 GB/day", "Unlimited"),
        ("Monthly High Data Plan", 399, "28 Days", "3 GB/day", "Unlimited"),
        ("Quarterly Plan", 799, "84 Days", "2 GB/day", "Unlimited"),
        ("Yearly Plan", 3599, "365 Days", "2.5 GB/day", "Unlimited")
    ],
    "Airtel": [
        ("Monthly Plan", 319, "30 Days", "1.5 GB/day", "Unlimited"),
        ("Monthly High Data Plan", 449, "30 Days", "3 GB/day", "Unlimited"),
        ("Quarterly Plan", 859, "84 Days", "2 GB/day", "Unlimited"),
        ("Yearly Plan", 3999, "365 Days", "2.5 GB/day", "Unlimited")
    ],
    "Vodafone": [
        ("Monthly Plan", 289, "28 Days", "1 GB/day", "Unlimited"),
        ("Monthly High Data Plan", 419, "28 Days", "3 GB/day", "Unlimited"),
        ("Quarterly Plan", 749, "84 Days", "1.5 GB/day", "Unlimited"),
        ("Yearly Plan", 3299, "365 Days", "2 GB/day", "Unlimited")
    ]
}

root = tk.Tk()
root.title("Mobile Recharge System")
root.geometry("450x550")

tk.Label(root, text="Mobile Recharge System", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Mobile Number").pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack(pady=5)

tk.Label(root, text="Select Operator").pack()
operator_var = tk.StringVar()
operator_menu = ttk.Combobox(root, textvariable=operator_var, state="readonly")
operator_menu['values'] = list(plans.keys())
operator_menu.pack(pady=5)

tk.Label(root, text="Select Plan").pack()
plan_var = tk.StringVar()
plan_menu = ttk.Combobox(root, textvariable=plan_var, state="readonly")
plan_menu.pack(pady=5)

# Output Label
output_label = tk.Label(root, text="", justify="left", bg="white", anchor="w")
output_label.pack(pady=10, fill="both", padx=10)



def update_plans(event):
    operator = operator_var.get()
    plan_list = [plan[0] for plan in plans[operator]]
    plan_menu['values'] = plan_list
    plan_menu.set("")


def recharge_action():
    mobile = mobile_entry.get()
    operator = operator_var.get()
    plan_name = plan_var.get()

  
    if not (len(mobile) == 10 and mobile.isdigit() and mobile[0] in "6789"):
        messagebox.showerror("Error", "Invalid Mobile Number")
        return

    if operator == "" or plan_name == "":
        messagebox.showerror("Error", "Please select operator and plan")
        return

    
    selected_plan = None
    for plan in plans[operator]:
        if plan[0] == plan_name:
            selected_plan = plan

    recharge = MobileRecharge(
        mobile, operator,
        selected_plan[0],
        selected_plan[1],
        selected_plan[2],
        selected_plan[3],
        selected_plan[4]
    )

    output_label.config(text=recharge.get_display_text())


def clear_fields():
    mobile_entry.delete(0, tk.END)
    operator_menu.set("")
    plan_menu.set("")
    output_label.config(text="")


tk.Button(root, text="Recharge", command=recharge_action, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)


operator_menu.bind("<<ComboboxSelected>>", update_plans)


root.mainloop()