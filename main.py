from csv_data import get_formatter_csv_data
from rate_by_company import get_rate_by_company
from winner import pick_winner

data = get_formatter_csv_data()
result = get_rate_by_company(data)
winner = pick_winner(result)

print(winner)
