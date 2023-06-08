from web3 import Web3
import requests

def infura_api(): #Connecting to Infura mainnet
    api = input("Insert Infura API: ")
    infura_access = f"https://mainnet.infura.io/v3/{api}"      #Will need to register for Infura API
    return infura_access

def valid_adrress(): #Validating ETH adress
    address_to_check = input("Input valid address: ")  #Try with this one 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
    print(f"Checking address {address_to_check}...")
    if Web3.is_address(address_to_check):
        address = address_to_check
        return address
        pass
    else:
        print("Invalid address")
        return valid_adrress()

def balance_checker(): #Checks ETH wallet balance
    web3 = Web3(Web3.HTTPProvider(infura_api()))
    web3.is_connected()
    balance = web3.eth.get_balance(valid_adrress())
    balance = web3.from_wei(balance, 'ether')
    return balance

def rates_calculator(): #Gets actual ETH/USDT rate from Binance
    rates_api = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    rate = requests.get(rates_api)
    rate = rate.json()
    rate = rate['price']
    return rate

while True:
    print(f"=================================================================")
    print(f"=================================================================")
    choice = input(f"      Welcome to Simple ETH wallet checker. "
                   f"\n {chr(62)} Enter C to check your balance in ETH and USTD. "
                   f"\n {chr(62)} Enter B to check your balance in ETH and USTD. "
                    "\nPlease choose: ")


    if choice.lower() == 'c':
        balance = balance_checker()
        rates = rates_calculator()
        print()
        print(f"=================================================================")
        print(f"=================================================================")
        print(f'Balance : {balance:.3f} ETH')
        print(f"Balance in USDT: {(float(balance) * float(rates)):.2f} \n"
              f"*at current rate {float(rates):.2f} USDT per ETH")
        print(f"=================================================================")
        print(f"=================================================================")
    elif choice.lower() == 'b':
        pass

    else:
        exit()


