"""
Mini Bank System (Python, OOP, Design Patterns, Logging)
- Factory Pattern for account creation
- Observer Pattern for event notifications
- Advanced structured logging
- Context Manager for safe resource handling
"""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Protocol, Optional

# -------------------------
# Logging (Advanced)
# -------------------------
logger = logging.getLogger("mini_bank_system")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

file_handler = logging.FileHandler("./files/mini_bank_system.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# -------------------------
# Domain Models
# -------------------------
@dataclass
class Transaction:
    tx_id: int
    tx_type: str  # deposit, withdraw, transfer
    amount: float
    timestamp: datetime
    status: str   # success, failed
    message: str


class Account(ABC):
    def __init__(self, account_id: int, owner: str, initial_balance: float):
        self.account_id = account_id
        self.owner = owner
        self._balance = float(initial_balance)
        self._transactions: List[Transaction] = []

    @property
    def balance(self) -> float:
        return self._balance

    @abstractmethod
    def account_type(self) -> str:
        pass

    def _record_tx(self, tx: Transaction) -> None:
        self._transactions.append(tx)

    def deposit(self, amount: float, tx_id: int) -> None:
        if amount <= 0:
            logger.error("Deposit amount must be positive")
            self._record_tx(Transaction(tx_id, "deposit", amount, datetime.now(), "failed", "Invalid amount"))
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        logger.info(f"[{self.account_type}] Deposit {amount}$ to {self.owner} (id={self.account_id}). New balance={self._balance}$")
        self._record_tx(Transaction(tx_id, "deposit", amount, datetime.now(), "success", "Deposit completed"))

    def withdraw(self, amount: float, tx_id: int) -> None:
        if amount <= 0:
            logger.error("Withdrawal amount must be positive")
            self._record_tx(Transaction(tx_id, "withdraw", amount, datetime.now(), "failed", "Invalid amount"))
            raise ValueError("Withdrawal amount must be positive")

        if self._balance < amount:
            logger.warning(f"[{self.account_type}] Insufficient funds for {self.owner} (id={self.account_id})")
            self._record_tx(Transaction(tx_id, "withdraw", amount, datetime.now(), "failed", "Insufficient funds"))
            raise RuntimeError("Insufficient funds")

        self._balance -= amount
        logger.info(f"[{self.account_type}] Withdraw {amount}$ from {self.owner} (id={self.account_id}). New balance={self._balance}$")
        self._record_tx(Transaction(tx_id, "withdraw", amount, datetime.now(), "success", "Withdraw completed"))

    def transfer_to(self, target: "Account", amount: float, tx_id: int) -> None:
        if target is self:
            raise ValueError("Cannot transfer to the same account")

        self.withdraw(amount, tx_id)
        target.deposit(amount, tx_id)
        logger.info(f"Transfer {amount}$ from {self.owner} (id={self.account_id}) to {target.owner} (id={target.account_id})")

    def transactions(self) -> List[Transaction]:
        return list(self._transactions)


class SavingsAccount(Account):
    @property
    def account_type(self) -> str:
        return "Savings"


class CheckingAccount(Account):
    @property
    def account_type(self) -> str:
        return "Checking"


class BusinessAccount(Account):
    @property
    def account_type(self) -> str:
        return "Business"


# -------------------------
# Factory Pattern
# -------------------------
class AccountFactory(ABC):
    @abstractmethod
    def create(self, account_id: int, owner: str, initial_balance: float) -> Account:
        pass


class SavingsAccountFactory(AccountFactory):
    def create(self, account_id: int, owner: str, initial_balance: float) -> Account:
        return SavingsAccount(account_id, owner, initial_balance)


class CheckingAccountFactory(AccountFactory):
    def create(self, account_id: int, owner: str, initial_balance: float) -> Account:
        return CheckingAccount(account_id, owner, initial_balance)


class BusinessAccountFactory(AccountFactory):
    def create(self, account_id: int, owner: str, initial_balance: float) -> Account:
        return BusinessAccount(account_id, owner, initial_balance)


# -------------------------
# Observer Pattern
# -------------------------
class Observer(Protocol):
    def update(self, event: str) -> None:
        pass


class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, event: str) -> None:
        for obs in self._observers:
            obs.update(event)


class LoggerObserver:
    def update(self, event: str) -> None:
        logger.info(f"[Observer:Logger] {event}")


class EmailObserver:
    def update(self, event: str) -> None:
        logger.info(f"[Observer:Email] Email sent for event: {event}")


class AnalyticsObserver:
    def update(self, event: str) -> None:
        logger.info(f"[Observer:Analytics] Event recorded: {event}")


# -------------------------
# Context Manager (Storage Simulation)
# -------------------------
class TransactionStorage:
    def __enter__(self):
        logger.info("Opening transaction storage")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            logger.error(f"Storage error: {exc}")
        logger.info("Closing transaction storage")
        return False 

# -------------------------
# Application Facade
# -------------------------
class BankSystem(Subject):
    def __init__(self):
        super().__init__()
        self._tx_seq = 1

    def _next_tx_id(self) -> int:
        tx_id = self._tx_seq
        self._tx_seq += 1
        return tx_id

    def deposit(self, acc: Account, amount: float) -> None:
        tx_id = self._next_tx_id()
        acc.deposit(amount, tx_id)
        self.notify(f"Deposit {amount}$ to {acc.owner} ({acc.account_type})")

    def withdraw(self, acc: Account, amount: float) -> None:
        tx_id = self._next_tx_id()
        acc.withdraw(amount, tx_id)
        self.notify(f"Withdraw {amount}$ from {acc.owner} ({acc.account_type})")

    def transfer(self, src: Account, dst: Account, amount: float) -> None:
        tx_id = self._next_tx_id()
        src.transfer_to(dst, amount, tx_id)
        self.notify(f"Transfer {amount}$ from {src.owner} to {dst.owner}")


# -------------------------
# UI
# -------------------------
def main():
    bank = BankSystem()
    bank.subscribe(LoggerObserver())
    bank.subscribe(EmailObserver())
    bank.subscribe(AnalyticsObserver())

    savings_factory = SavingsAccountFactory()
    checking_factory = CheckingAccountFactory()

    alice = savings_factory.create(1, "Alice", 1000.0)
    bob = checking_factory.create(2, "Bob", 300.0)

    with TransactionStorage():
        bank.deposit(alice, 200.0)
        bank.withdraw(alice, 150.0)
        bank.transfer(alice, bob, 250.0)

        try:
            bank.withdraw(bob, 100.0) 
        except Exception as e:
            logger.error(f"Operation failed: {e}")

    logger.info(f"Alice final balance: {alice.balance}$")
    logger.info(f"Bob final balance: {bob.balance}$")


if __name__ == "__main__":
    main()
