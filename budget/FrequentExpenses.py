from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)
    spending_counter = collections.Counter(spending_categories)
    top5 = spending_counter.most_common(5)
    categories, count = zip(*top5)
    
plt.figure()
ax = plt.subplots()
plt.bar(categories, count)
plt.title('# of Purchases by Category')

plt.show()