check = [True, True, 1, 1, True]

if any(check):
    status = 'winner'
else:
    status = 'loser'

if status == "winner":
    winning_sum = 100
else:
    winning_sum = 10