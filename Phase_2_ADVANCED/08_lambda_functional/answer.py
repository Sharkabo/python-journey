transactions = [
    {"id": 101, "amount": 1500, "type": "credit", "status": "completed"},
    {"id": 102, "amount": 500, "type": "debit", "status": "pending"},
    {"id": 103, "amount": 2000, "type": "credit", "status": "completed"},
    {"id": 104, "amount": 100, "type": "debit", "status": "completed"}
]

completed_debit = list(map(lambda x: f"${x["amount"]:.2f}", sorted(filter(lambda x: x['type'] == 'debit' and x['status'] == 'completed' , transactions), key = lambda t: t["amount"], reverse= True)))