import csv
from datetime import datetime
from collections import defaultdict
FILE = "expenses.csv"
def init():
    try:
        with open(FILE, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "type", "category", "amount"])
    except FileExistsError:
        pass
def add_entry():
    date = input("Date (YYYY-MM-DD, blank = today): ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    typ = input("Type (income/expense): ").strip().lower()
    category = input("Category: ").strip()
    amount = input("Amount: ").strip()
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, typ, category, amount])
    print("Entry added!")
def show_all():
    with open(FILE) as f:
        for row in csv.reader(f):
            print(row)
def monthly_summary():
    month = input("Enter month (1–12): ").strip()
    year = input("Enter year (YYYY): ").strip()
    total_income = 0
    total_expense = 0
    category_sum = defaultdict(float)
    with open(FILE) as f:
        reader = csv.DictReader(f)
        for r in reader:
            d = r["date"]
            if d.startswith(f"{year}-{int(month):02d}"):
                amt = float(r["amount"])
                key = r["category"]
                if r["type"] == "income":
                    total_income += amt
                    category_sum[key] += amt
                else:
                    total_expense += amt
                    category_sum[key] -= amt
    print("\n=== MONTHLY SUMMARY ===")
    print("Total Income :", total_income)
    print("Total Expense:", total_expense)
    print("Category Breakdown:")
    for k, v in category_sum.items():
        print(f"  {k}: {v}")
    print("=======================\n")
def menu():
    init()
    while True:
        print("\n1. Add Entry")
        print("2. Show All")
        print("3. Monthly Summary")
        print("4. Exit\n")
        choice = input("Choose option: ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            show_all()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            break
        else:
            print("Invalid option!")
menu()