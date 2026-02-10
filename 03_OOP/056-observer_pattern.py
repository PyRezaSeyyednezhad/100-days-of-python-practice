from abc import ABC, abstractmethod
from typing import List

# Example 1: Use Observer Pattern for Order Project
class Observer(ABC):
    @abstractmethod
    def update(self, new_status: str) -> None:
        pass


# Subject
class Order:
    def __init__(self):
        self._status: str = "created"
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def set_status(self, new_status: str) -> None:
        self._status = new_status
        self._notify()

    def _notify(self) -> None:
        for observer in self._observers:
            observer.update(self._status)


# Observers
class LoggerObserver(Observer):
    def update(self, new_status: str) -> None:
        print(f"[LOG] Order status changed to: {new_status}")


class EmailObserver(Observer):
    def update(self, new_status: str) -> None:
        print(f"[EMAIL] Sending email: Order is now '{new_status}'")


class UIObserver(Observer):
    def update(self, new_status: str) -> None:
        print(f"[UI] Updating UI with new status: {new_status}")


# if __name__ == "__main__":
#     order = Order()

#     logger = LoggerObserver()
#     email = EmailObserver()
#     ui = UIObserver()

#     order.subscribe(logger)
#     order.subscribe(email)
#     order.subscribe(ui)

#     order.set_status("paid")
#     print("----")
#     order.set_status("shipped")
#     print("----")
#     order.set_status("Jason")




class StockObserver(ABC):
    @abstractmethod
    def update(self, new_price: float) -> None:
        pass



# Subject
class StockSubject:
    def __init__(self):
        self._price: float = 0.0
        self._observers: List[StockObserver] = []
    
    def subscribe(self, observer: StockObserver) -> None:
        self._observers.append(observer)
    
    def unsubscribe(self, observer: StockObserver) -> None:
        self._observers.remove(observer)
    
    def _notify(self) -> None:
        for observer in self._observers:
            observer.update(self._price)
    
    def set_price(self, new_price):
        self._price = new_price
        self._notify()


# Observers

class StockLoggerObserver(StockObserver):
    def update(self, new_price: float) -> None:
        print(f"[STOCK LOG] Stock price updated to: {new_price}")


class StockLivePlotObserver(StockObserver):
    def update(self, new_price: float) -> None:
        print(f"[STOCK PLOT] Updating live plot with new price: {new_price}")


class StockWarningPriceObserver(StockObserver):
    def __init__(self, threshold: float):
        self._threshold = threshold
    
    def update(self, new_price: float) -> None:
        if new_price > self._threshold:
            print(f"[STOCK WARNING] Stock price {new_price} exceeds threshold {self._threshold}!")
        else:
            print(f"[STOCK WARNING] Stock price {new_price} is below threshold {self._threshold}.")

class StockAutoSellObserver(StockObserver):
    def __init__(self, threshold: float):
        self._threshold = threshold
    
    def update(self, new_price: float) -> None:
        if new_price < self._threshold:
            print(f"[STOCK AUTO-SELL] Stock price {new_price} is below threshold {self._threshold}. Selling stock!")
        else:
            print(f"[STOCK AUTO-SELL] Stock price {new_price} is above threshold {self._threshold}. No action taken.")

class StockSaveInFileObserver(StockObserver):
    def update(self, new_price: float) -> None:
        updated_text = f"The Price of Stock is {new_price}$.\n"
        with open("./files/Observer.txt", "a") as f1:
            f1.writelines(updated_text)
        
        print(f"[STOCK TEXT FILE] Updating text file with new price: {new_price}")


class StockSendMailInRange(StockObserver):
    def update(self, new_price) -> None:
        if new_price < 150.0 and new_price > 50.0:
            print(f"[STOCK EMAIL] Stock price {new_price} is below 150.0$ and above 50.0$. Email Sent!")
        elif new_price > 150:
            print(f"[STOCK EMAIL] Stock price {new_price} is above 150.0$. No action taken.")
        else:
            print(f"[STOCK EMAIL] Stock price {new_price} is below 50.0$. No action taken.")


if __name__ == "__main__":
    stock = StockSubject()

    logger = StockLoggerObserver()
    live_plot = StockLivePlotObserver()
    warning_price = StockWarningPriceObserver(threshold=150.0)
    auto_sell = StockAutoSellObserver(threshold=100.0)
    save_price = StockSaveInFileObserver()
    email_send = StockSendMailInRange()
    
    stock.subscribe(logger)
    stock.subscribe(live_plot)
    stock.subscribe(warning_price)
    stock.subscribe(auto_sell)
    stock.subscribe(save_price)
    stock.subscribe(email_send)

    stock.set_price(120)
    print("----")
    stock.set_price(160)
    print("----")
    stock.set_price(90)