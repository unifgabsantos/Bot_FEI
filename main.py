from FEI import Bot,getAccounts
from os import system
def main():
    accounts = getAccounts()
    for account in accounts:
        Bot(account).start()
main()
system("pause")
