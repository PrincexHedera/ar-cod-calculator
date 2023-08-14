import CSVtoDict

"""conveyor_belts = {1: 3200, 2: 3800, 3: 4200, 4: 5000,
                  5: 6000, 6: 7000, 7: 8000, 8: 8600,
                  9: 4000, 10: 1800, 11: 4000, 12: 3500,
                  13: 2800, 14: 4000, 15: 13000, 16: 11000,
                  17: 4000, 18: 4200, 19: 3800} """

"""def is_Valid(user_input, dictionary):
    seen_numbers = []
    for number in user_input.split():
        if number in seen_numbers:
            return False
        elif int(number) not in dictionary:
            return False
        else: 
            seen_numbers.append(number)
    return True """

def calculate_profits(dictionary):
    total = 0
    for key in dictionary: 
        total += dictionary[key]
    return total

def print_result(result):
    daily = result*12
    ad_multiplier = daily*1.5
    print("\nProfits:")
    print(f"Cod per hour: {format(result, ',')}")
    print(f"Daily earnings (12 hr): {format(daily, ',')}")
    print(f"Daily earnings with ad multiplier (×1.5): {format(ad_multiplier, ',')}")

def main():
    print("\t\tAnimal Resturant Buffet Calculator")
    print("-"*60)
    dict = CSVtoDict.read_file(CSVtoDict.facilities_csv, CSVtoDict.conveyer_belts)
    print(dict)
    profits = calculate_profits(CSVtoDict.conveyer_belts)
    print_result(profits)

    """while True: 
        try: 
            print("\t\tAnimal Resturant Buffet Calculator")
            print("-"*30)
            print("Enter the numbers of the facilities you own below in one line seperated by spaces.")
            user_input= input()
            break
        except ValueError:
            print("The input you entered is invalid. Please try again.")"""

    #condition = is_Valid(user_input)

    """if condition:
        hourly_earnings = calculate_profits(user_input)
        print_result(hourly_earnings)
    else: 
        print("Sorry, the numbers you entered have repeats or are out of range.")"""
    

main()