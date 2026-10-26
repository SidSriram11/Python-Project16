def compute_balance(amount_given, cost):
    balance = amount_given - cost
    return balance

rate = 30
print("--- METRED PARKING ASSISTANT ---")
print(f"Fee required: {rate} credits.")
print("We take denominations of: 1, 5, 10, 25\n")

sum_received = 0
piece_count = 0

while True:
    piece = int(input("Please drop in a coin (1, 5, 10, or 25): "))

    if piece != 1 and piece != 5 and piece != 10 and piece != 25:
        print("Unrecognised coin type. Please re-enter.\n")
        continue

    sum_received += piece
    piece_count += 1
    print(f"Added {piece}. Current balance deposited: {sum_received}\n")

    if sum_received >= rate:
        print("Required amount met!\n")
        break

dispensed_funds = compute_balance(sum_received, rate)

print("Dispensing permit now...")

if dispensed_funds == 0:
    pass
else:
    print(f"Your change amounts to: {dispensed_funds} credits")

print("\n--- TRANSACTION OVERVIEW ---")
print("Required Fee:", rate)
print("Items Deposited:", piece_count)
print("Grand Total:", sum_received)
print("Returned Cash:", dispensed_funds)
print("----------------------------")
print("Process finalized. Have a great day!")
