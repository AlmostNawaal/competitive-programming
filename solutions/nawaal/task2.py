from collections import deque

def predict_senate_winner(senate: str) -> str:
    n = len(senate)
    
    QR = deque()
    QD = deque()
    
    for i, party in enumerate(senate):
        if party == 'R':
            QR.append(i)
        else:
            QD.append(i)
            
    while QR and QD:
        r = QR.popleft()
        d = QD.popleft()
        
        if r < d:
            QR.append(r + n)
        else:
            QD.append(d + n)
            
    if QR:
        return "Radiant"
    else:
        return "Dire"

print(predict_senate_winner(input("Enter the senate string: ")))