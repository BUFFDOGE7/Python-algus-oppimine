EEK_TO_EUR_RATE = 15.6466

def convert_kroons_to_euros(kroons):
    """Convert Estonian kroons to euros"""
    euros = kroons / EEK_TO_EUR_RATE
    return round(euros, 2)

try:
    kroons = float(input("Enter amount in Estonian kroons (EEK): "))
    
    if kroons < 0:
        print("Error: Amount cannot be negative")
    else:
        euros = convert_kroons_to_euros(kroons)
        print(f"{kroons} EEK = {euros} EUR")
        
except ValueError:
    print("Error: Please enter a valid number")