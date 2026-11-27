def calculate_marks(marks):
    avg=sum(marks)/len(marks)
    high=max(marks)
    low=min(marks)
    return avg,high,low
marks=[99,80,100,50,99]
average,highest,lowest=calculate_marks(marks)
print("Average:",average)
print("High:",highest)
print("Low:",lowest)
