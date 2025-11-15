import pandas as pd
import matplotlib.pyplot as plt


def load_transactions(csv_path):
    """
    Load transactions from a CSV file.
    The CSV should have columns: Date, Description, Amount.
    """
    df = pd.read_csv(csv_path)
    return df


def categorize_expenses(df, category_map):
    """
    Assign categories to transactions based on a mapping of description keywords to categories.
    Any descriptions not found in the mapping will be labeled as 'Other'.
    """
    df['Category'] = df['Description'].map(category_map).fillna('Other')
    return df


def summarize_spending(df):
    """
    Summarize total spending by category.
    Returns a pandas Series sorted by total spending descending.
    """
    summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    return summary


def plot_spending(summary):
    """
    Plot a bar chart of spending by category using matplotlib.
    """
    summary.plot(kind='bar')
    plt.title('Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Spending')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Example usage:
    # Provide the path to a CSV file with columns: Date, Description, Amount
    csv_path = input("Enter path to transactions CSV: ")
    df = load_transactions(csv_path)
    # Example category_map: a dictionary mapping descriptions or merchants to categories
    category_map = {
        'Groceries': 'Food',
        'Supermarket': 'Food',
        'Rent': 'Housing',
        'Utilities': 'Bills',
        # Add more mappings as needed
    }
    df = categorize_expenses(df, category_map)
    summary = summarize_spending(df)
    print("Spending Summary:")
    print(summary)
    plot_spending(summary)
