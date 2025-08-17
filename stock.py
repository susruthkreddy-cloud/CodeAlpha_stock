import csv
from datetime import datetime

def get_stock_prices():
    """
    Dictionary containing hardcoded stock prices
    Key concept: DICTIONARY usage
    """
    stock_prices = {
        "AAPL": 180.50,    # Apple Inc.
        "TSLA": 250.75,    # Tesla Inc.
        "GOOGL": 135.20,   # Alphabet Inc.
        "MSFT": 375.80,    # Microsoft Corp.
        "AMZN": 145.30,    # Amazon.com Inc.
        "META": 320.45,    # Meta Platforms Inc.
        "NVDA": 450.60,    # NVIDIA Corporation
        "NFLX": 425.90,    # Netflix Inc.
        "AMD": 110.25,     # Advanced Micro Devices
        "INTC": 45.85      # Intel Corporation
    }
    return stock_prices

def display_available_stocks(stock_prices):
    """
    Function to display available stocks and their prices
    Key concept: INPUT/OUTPUT operations
    """
    print("\n" + "=" * 60)
    print("           AVAILABLE STOCKS AND PRICES")
    print("=" * 60)
    print(f"{'Stock Symbol':<12} {'Stock Price':<15} {'Company'}")
    print("-" * 60)
    
    company_names = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.", 
        "GOOGL": "Alphabet Inc.",
        "MSFT": "Microsoft Corp.",
        "AMZN": "Amazon.com Inc.",
        "META": "Meta Platforms Inc.",
        "NVDA": "NVIDIA Corporation",
        "NFLX": "Netflix Inc.",
        "AMD": "Advanced Micro Devices",
        "INTC": "Intel Corporation"
    }
    
    for symbol, price in stock_prices.items():
        company = company_names.get(symbol, "Unknown Company")
        print(f"{symbol:<12} ${price:<14.2f} {company}")
    
    print("=" * 60)

def calculate_investment_value(portfolio, stock_prices):
    """
    Function to calculate total investment value
    Key concept: DICTIONARY operations and ARITHMETIC
    """
    total_value = 0
    investment_details = []
    
    print("\n" + "=" * 50)
    print("           INVESTMENT CALCULATION")
    print("=" * 50)
    print(f"{'Stock':<8} {'Quantity':<10} {'Price':<12} {'Total Value'}")
    print("-" * 50)
    
    for stock_symbol, quantity in portfolio.items():
        if stock_symbol in stock_prices:
            price = stock_prices[stock_symbol]
            stock_value = quantity * price
            total_value += stock_value
            
            # Store details for file saving
            investment_details.append({
                'stock': stock_symbol,
                'quantity': quantity,
                'price': price,
                'total_value': stock_value
            })
            
            print(f"{stock_symbol:<8} {quantity:<10} ${price:<11.2f} ${stock_value:.2f}")
        else:
            print(f"{stock_symbol:<8} {quantity:<10} {'NOT FOUND':<11} $0.00")
    
    print("-" * 50)
    print(f"{'TOTAL INVESTMENT VALUE:':<32} ${total_value:.2f}")
    print("=" * 50)
    
    return total_value, investment_details

def get_user_portfolio():
    """
    Function to get user input for stock portfolio
    Key concept: INPUT/OUTPUT operations and data validation
    """
    portfolio = {}
    
    print("\n" + "=" * 50)
    print("         BUILD YOUR STOCK PORTFOLIO")
    print("=" * 50)
    print("Enter your stock investments (type 'done' when finished)")
    print("Format: Enter stock symbol, then quantity")
    print("-" * 50)
    
    while True:
        # Get stock symbol
        stock_symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
        
        if stock_symbol == 'DONE':
            break
        
        if not stock_symbol:
            print("Please enter a valid stock symbol!")
            continue
        
        # Get quantity
        try:
            quantity = int(input(f"Enter quantity for {stock_symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0!")
                continue
        except ValueError:
            print("Please enter a valid number for quantity!")
            continue
        
        # Add to portfolio (or update if already exists)
        if stock_symbol in portfolio:
            portfolio[stock_symbol] += quantity
            print(f"Updated {stock_symbol}: Total quantity now {portfolio[stock_symbol]}")
        else:
            portfolio[stock_symbol] = quantity
            print(f"Added {stock_symbol}: {quantity} shares")
    
    return portfolio

def save_to_txt_file(portfolio, investment_details, total_value):
    """
    Function to save results to a text file
    Key concept: FILE HANDLING (TXT)
    """
    filename = f"investment_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write("STOCK INVESTMENT TRACKER SUMMARY\n")
            file.write("=" * 40 + "\n")
            file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 40 + "\n\n")
            
            file.write("PORTFOLIO DETAILS:\n")
            file.write("-" * 40 + "\n")
            file.write(f"{'Stock':<8} {'Qty':<6} {'Price':<10} {'Total Value'}\n")
            file.write("-" * 40 + "\n")
            
            for detail in investment_details:
                file.write(f"{detail['stock']:<8} {detail['quantity']:<6} "
                          f"${detail['price']:<9.2f} ${detail['total_value']:.2f}\n")
            
            file.write("-" * 40 + "\n")
            file.write(f"TOTAL INVESTMENT VALUE: ${total_value:.2f}\n")
            file.write("=" * 40 + "\n")
        
        print(f"\n✅ Results saved to: {filename}")
        return True
    except Exception as e:
        print(f"\n❌ Error saving to TXT file: {e}")
        return False

def save_to_csv_file(investment_details, total_value):
    """
    Function to save results to a CSV file
    Key concept: FILE HANDLING (CSV)
    """
    filename = f"investment_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(['Date', 'Stock_Symbol', 'Quantity', 'Price_Per_Share', 'Total_Value'])
            
            # Write investment data
            current_date = datetime.now().strftime('%Y-%m-%d')
            for detail in investment_details:
                writer.writerow([
                    current_date,
                    detail['stock'],
                    detail['quantity'],
                    detail['price'],
                    detail['total_value']
                ])
            
            # Write total row
            writer.writerow(['', 'TOTAL', '', '', total_value])
        
        print(f"✅ CSV data saved to: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving to CSV file: {e}")
        return False

def main_menu():
    """
    Main function to run the stock tracker
    Key concept: PROGRAM FLOW and MENU SYSTEM
    """
    print("=" * 60)
    print("           SIMPLE STOCK INVESTMENT TRACKER")
    print("=" * 60)
    print("Track your stock investments with real-time calculations!")
    
    # Get hardcoded stock prices (Dictionary)
    stock_prices = get_stock_prices()
    
    while True:
        print("\n" + "=" * 40)
        print("              MAIN MENU")
        print("=" * 40)
        print("1. View Available Stocks")
        print("2. Create New Portfolio")
        print("3. Quick Investment Calculator")
        print("4. Exit")
        print("-" * 40)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            display_available_stocks(stock_prices)
        
        elif choice == '2':
            # Get user portfolio
            portfolio = get_user_portfolio()
            
            if not portfolio:
                print("\n⚠️  No stocks added to portfolio!")
                continue
            
            # Calculate investment value
            total_value, investment_details = calculate_investment_value(portfolio, stock_prices)
            
            # Ask to save results
            save_choice = input("\nWould you like to save the results? (y/n): ").lower().strip()
            
            if save_choice in ['y', 'yes']:
                print("\nChoose file format:")
                print("1. Text file (.txt)")
                print("2. CSV file (.csv)")
                print("3. Both formats")
                
                format_choice = input("Select format (1-3): ").strip()
                
                if format_choice == '1':
                    save_to_txt_file(portfolio, investment_details, total_value)
                elif format_choice == '2':
                    save_to_csv_file(investment_details, total_value)
                elif format_choice == '3':
                    save_to_txt_file(portfolio, investment_details, total_value)
                    save_to_csv_file(investment_details, total_value)
                else:
                    print("Invalid choice. Results not saved.")
        
        elif choice == '3':
            print("\n" + "=" * 40)
            print("        QUICK CALCULATOR")
            print("=" * 40)
            
            try:
                symbol = input("Enter stock symbol: ").strip().upper()
                if symbol not in stock_prices:
                    print(f"❌ Stock {symbol} not found!")
                    continue
                
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("❌ Quantity must be greater than 0!")
                    continue
                
                price = stock_prices[symbol]
                total = quantity * price
                
                print(f"\n📊 CALCULATION RESULT:")
                print(f"Stock: {symbol}")
                print(f"Price per share: ${price:.2f}")
                print(f"Quantity: {quantity}")
                print(f"Total investment: ${total:.2f}")
                
            except ValueError:
                print("❌ Please enter a valid number for quantity!")
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '4':
            print("\n👋 Thank you for using Stock Investment Tracker!")
            print("Happy investing! 📈")
            break
        
        else:
            print("❌ Invalid choice. Please select 1-4.")

# Run the program
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
