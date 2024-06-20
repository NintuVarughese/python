def calculate(units):
    if units <= 200:
        bill = units * 0.50
    elif units <= 400:
        bill = 200 * 0.50 + (units - 200) * 0.65
    elif units <= 600:
        bill = 200 * 0.50 + 200 * 0.65 + (units - 400) * 0.80
    else:
        bill = 200 * 0.50 + 200 * 0.65 + 200 * 0.80 + (units - 600) * 1.00
    
    if bill > 400:
        surcharge = bill * 0.15
        bill += surcharge
    
    if bill < 100:
        bill = 100
    
    return bill

def main():
    print("welcom to electricity bill calculator")
    units = float(input("enter the number of unit consumed:"))
    total_bill = calculate(units)
    print(f"total amount : Rs. {total_bill:.2f}")
if __name__ == "__main__":
    main()