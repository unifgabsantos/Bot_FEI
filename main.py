from FEI import Bot,getAccounts
getAccounts()
def main():
    accounts = getAccounts()
    for account in accounts:
        Bot(account).start()
main()