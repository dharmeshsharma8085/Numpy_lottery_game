import numpy as np
participants = np.random.randint(1, 10001, size=10000)

lucky_numbers = np.random.choice(
    np.arange(1, 10001),
    size=10,
    replace=False
)

prize = 100000
print(f"Prize Pool: ₹{prize}")
winners = participants[np.isin(participants, lucky_numbers)]
print("Lucky Numbers:", lucky_numbers)
if len(winners) > 0:
    print(" Lottery Winners Found!")
    prize_per_winner = prize / len(winners)
    print(f"Prize per Winner: ₹{prize_per_winner:.2f}")
else:
    print(" No Winners Today!")
print("First 10 Winners:", winners[:10])
print("Unique Winning Numbers:", np.unique(winners))
print(f"Total Winners: {len(winners)}")
print(f"Winning Probability: {len(winners)/10000*100:.2f}%")