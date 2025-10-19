# 💰 Expense Tracker with Input Validation
# ----------------------------------------
# This program allows users to add expenses, view all expenses,
# calculate the total, and filter by category.
# It also handles invalid inputs gracefully (e.g., letters instead of numbers).


"""
Expense Tracker ++
------------------
Adds:
  • Auto save/load (JSON)
  • Date on each expense
  • Category summary
  • CSV export
  • Optional pie chart (matplotlib if installed)

Notes:
  • No external deps required for core features.
  • Pie chart needs matplotlib. If not installed, the program will continue without it.
"""

from __future__ import annotations
import json
import csv
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Iterable

# Try to import matplotlib for the pie chart; continue gracefully if missing.
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except Exception:
    MATPLOTLIB_AVAILABLE = False


# ---------- Core CRUD ----------

def add_expense(expenses: List[Dict], amount: float, category: str, date_str: str | None = None, note: str = "") -> None:
    """
    Add a new expense entry.
    - amount: positive float
    - category: non-empty string
    - date_str: 'YYYY-MM-DD' (optional). If None/invalid, use today's date.
    - note: short optional text for context
    """
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        # Validate date; fallback to today if invalid
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("⚠️  Invalid date format. Using today's date instead.")
            date_str = datetime.now().strftime("%Y-%m-%d")

    expenses.append({
        'amount': float(amount),
        'category': category.strip(),
        'date': date_str,
        'note': note.strip()
    })


def print_expenses(expenses: Iterable[Dict]) -> None:
    """
    Print a formatted list of expenses.
    Accepts either a list or any iterable (e.g., a filter object).
    """
    found = False
    for e in expenses:
        print(f"- ${e['amount']:.2f} | {e['category']} | {e['date']} | {e.get('note','')}")
        found = True
    if not found:
        print("No expenses found.")


def total_expenses(expenses: List[Dict]) -> float:
    """Return the sum of all expense amounts."""
    return sum(map(lambda e: e['amount'], expenses))


def filter_expenses_by_category(expenses: List[Dict], category: str) -> Iterable[Dict]:
    """Case-insensitive category filter."""
    return filter(lambda e: e['category'].lower() == category.lower(), expenses)


# ---------- Persistence ----------

def save_expenses(expenses: List[Dict], filename: str = "expenses.json") -> None:
    """Save expenses to JSON (called on exit and also available via menu)."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(expenses, f, ensure_ascii=False, indent=2)
        print(f"💾 Saved {len(expenses)} expenses to {filename}.")
    except Exception as ex:
        print(f"❌ Failed to save to {filename}: {ex}")


def load_expenses(filename: str = "expenses.json") -> List[Dict]:
    """Load expenses from JSON (called on start)."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Light validation: ensure keys exist
            cleaned = []
            for e in data:
                if all(k in e for k in ("amount", "category", "date")):
                    cleaned.append({
                        "amount": float(e["amount"]),
                        "category": str(e["category"]),
                        "date": str(e["date"]),
                        "note": str(e.get("note", "")),
                    })
            print(f"📥 Loaded {len(cleaned)} expenses from {filename}.")
            return cleaned
    except FileNotFoundError:
        print("ℹ️  No previous data found. Starting fresh.")
        return []
    except Exception as ex:
        print(f"❌ Failed to load {filename}: {ex}")
        return []


# ---------- Analytics / Output ----------

def category_summary(expenses: List[Dict]) -> Dict[str, float]:
    """Return a dict of total spent per category."""
    summary = defaultdict(float)
    for e in expenses:
        summary[e['category']] += e['amount']
    return dict(summary)


def print_category_summary(expenses: List[Dict]) -> None:
    """Nicely print the totals per category."""
    summary = category_summary(expenses)
    if not summary:
        print("No expenses to summarize.")
        return
    print("\n--- Category Summary ---")
    for cat, total in sorted(summary.items(), key=lambda kv: (-kv[1], kv[0].lower())):
        print(f"{cat}: ${total:.2f}")
    print("------------------------")


def export_to_csv(expenses: List[Dict], filename: str = "expenses.csv") -> None:
    """Export all expenses to CSV."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["amount", "category", "date", "note"])
            writer.writeheader()
            for e in expenses:
                writer.writerow(e)
        print(f"📄 Exported {len(expenses)} expenses to {filename}.")
    except Exception as ex:
        print(f"❌ Failed to export CSV: {ex}")


def plot_category_pie(expenses: List[Dict]) -> None:
    """
    Show a pie chart of spending by category.
    Requires matplotlib. If unavailable or no data, prints a message.
    """
    if not MATPLOTLIB_AVAILABLE:
        print("📉 Pie chart not available (matplotlib not installed).")
        print("Tip: pip install matplotlib")
        return

    summary = category_summary(expenses)
    if not summary:
        print("No data to chart.")
        return

    labels = list(summary.keys())
    sizes = list(summary.values())

    try:
        # One chart, no custom colors (keeps things simple and clean).
        plt.figure()
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.title("Spending by Category")
        plt.axis("equal")  # equal aspect ratio ensures pie is drawn as a circle.
        plt.show()
    except Exception as ex:
        print(f"❌ Failed to render chart: {ex}")


# ---------- CLI Helpers ----------

def input_menu_choice(prompt: str, valid: List[str]) -> str:
    """Ask for a menu choice and validate against provided list."""
    choice = input(prompt).strip()
    if choice not in valid:
        print(f"❌ Invalid choice. Please enter one of: {', '.join(valid)}")
        return ""
    return choice


def input_amount(prompt: str = "Enter amount: ") -> float | None:
    """Get a positive float amount from user, or None on validation failure."""
    raw = input(prompt).strip()
    try:
        amt = float(raw)
        if amt < 0:
            print("❌ Amount cannot be negative.")
            return None
        return amt
    except ValueError:
        print("❌ Invalid input. Please enter a valid number for amount.")
        return None


def main():
    expenses: List[Dict] = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Show category summary")
        print("6. Export all expenses to CSV")
        print("7. Show pie chart by category")
        print("8. Save now")
        print("9. Exit")

        choice = input_menu_choice("Enter your choice (1-9): ", [str(i) for i in range(1, 10)])
        if not choice:
            continue  # invalid, re-loop

        if choice == "1":
            amt = input_amount()
            if amt is None:
                continue
            category = input("Enter category: ").strip()
            if not category:
                print("❌ Category cannot be empty. Try again.")
                continue
            # Optional note and date (date defaults to today if left blank)
            note = input("Enter note (optional): ").strip()
            date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
            add_expense(expenses, amt, category, date_str=date_str or None, note=note)
            print(f'✅ Added ${amt:.2f} in "{category}".')

        elif choice == "2":
            print("\n--- All Expenses ---")
            print_expenses(expenses)

        elif choice == "3":
            print("\n--- Total Expenses ---")
            print(f"Total: ${total_expenses(expenses):.2f}")

        elif choice == "4":
            category = input("Enter category to filter: ").strip()
            print(f'\n--- Expenses for "{category}" ---')
            filtered = list(filter_expenses_by_category(expenses, category))
            print_expenses(filtered)

        elif choice == "5":
            print_category_summary(expenses)

        elif choice == "6":
            export_to_csv(expenses)

        elif choice == "7":
            plot_category_pie(expenses)

        elif choice == "8":
            save_expenses(expenses)

        elif choice == "9":
            # Auto-save on exit
            save_expenses(expenses)
            print("👋 Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()