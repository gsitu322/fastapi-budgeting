from enum import Enum

# These enums describes the types of categories we will have and will influence the calculations later.
class CategoryType(str, Enum):
    income = "Income"
    non_discretionary = "Non-Discretionary Expense"
    discretionary = "Discretionary Expense"
