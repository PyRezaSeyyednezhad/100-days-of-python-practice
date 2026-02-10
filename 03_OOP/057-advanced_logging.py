import logging
from dataclasses import dataclass

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level to DEBUG
logger.setLevel(logging.DEBUG)

# Define a custom formatter with more details
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', style='%')
logging.basicConfig(filename="./files/advanced_logging.log", level=logging.DEBUG, format=formatter._fmt, datefmt=formatter.datefmt, filemode="a")


# Define a dataclass for the store application
@dataclass
class StoreApp:
    username: str
    password: str
    repeat_password: str
    user_wallet_value: float
    user_wallet_address: str
    
    def LoginAccount(self):
        logger.info(f"Attempting login for user: {self.username}")
        if self.password != self.repeat_password:
            logger.error("Password and repeat password do not match")
            return False
        else:
            logger.info("Login successful")
            return True
        
    
    def BuyItem(self, item_name, item_price):
        if self.LoginAccount():
            logger.info(f"User {self.username} is attempting to buy an item named '{item_name}' priced at {item_price}$")
            if self.user_wallet_value < item_price:
                logger.error("Insufficient funds to complete the purchase")
                return False
            else:
                self.user_wallet_value -= item_price
                logger.info(f"Purchase successful. Remaining wallet value: {self.user_wallet_value}$")
                return True
        else:
            logger.error("Login failed. Cannot proceed with the purchase")
            return False

    def SellItem(self, item_name, item_price):
        if self.LoginAccount():
            logger.info(f"User {self.username} is attempting to sell an item named '{item_name}' priced at {item_price}$")
            self.user_wallet_value += item_price
            logger.info(f"Sale successful. Updated wallet value: {self.user_wallet_value}$")
            return True
        else:
            logger.error("Login failed. Cannot proceed with the sale")
            return False
    
    def CheckWallet(self):
        if self.LoginAccount():
            logger.info(f"User {self.username} is checking their wallet value")
            logger.info(f"Current wallet value: {self.user_wallet_value}$")
            return self.user_wallet_value
        else:
            logger.error("Login failed. Cannot check wallet value")
            return None
    
    def CheckWalletAddress(self):
        if self.LoginAccount():
            logger.info(f"User {self.username} is checking their wallet address")
            logger.info(f"Current wallet address: {self.user_wallet_address}")
            return self.user_wallet_address
        else:
            logger.error("Login failed. Cannot check wallet address")
            return None
    
    def ChangeWalletAddress(self, new_address):
        if self.LoginAccount():
            logger.info(f"User {self.username} is attempting to change their wallet address to {new_address}")
            self.user_wallet_address = new_address
            logger.info(f"Wallet address updated successfully to: {self.user_wallet_address}")
            return self.user_wallet_address
        else:
            logger.error("Login failed. Cannot change wallet address")
            return None
    
    def ChangePassword(self, new_password, repeat_new_password):
        if self.LoginAccount():
            logger.info(f"User {self.username} is attempting to change their password")
            if new_password != repeat_new_password:
                logger.error("New password and repeat new password do not match")
                return False
            else:
                self.password = new_password
                self.repeat_password = repeat_new_password
                logger.info("Password updated successfully")
                return True
        else:
            logger.error("Login failed. Cannot change password")
            return False
    

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    repeat_password = input("Repeat password: ")
    userwalletvalue = 150000
    store_app = StoreApp(username, password, repeat_password, userwalletvalue, "0x1234567890abcdef")
    user_input = int(input(f"Enter a command (1. login, 2. buy, 3. sell, 4. check_wallet, 5. check_address, 6. change_address, 7. change_password, 8. exit): "))
    if user_input == 1:
        store_app.LoginAccount()
    elif user_input == 2:
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        store_app.BuyItem(item_name, item_price)
    elif user_input == 3:
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        store_app.SellItem(item_name, item_price)
    elif user_input == 4:
        store_app.CheckWallet()
    elif user_input == 5:
        store_app.CheckWalletAddress()
    elif user_input == 6:
        new_address = input("Enter new wallet address: ")
        store_app.ChangeWalletAddress(new_address)
    elif user_input == 7:
        new_password = input("Enter new password: ")
        repeat_new_password = input("Repeat new password: ")
        store_app.ChangePassword(new_password, repeat_new_password)
    elif user_input == 8:
        logger.info("Exiting the application")
    else:
        logger.warning(f"Invalid command entered: {user_input}")



if __name__ == "__main__":
    main()