#!/usr/bin/python3
from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 9999999999):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.pin

    def checkBalance(self):
        return self.balance

    def TarikTunai(self, nominal):
        self.balance -= nominal

    def SetorTunai(self, nominal):
        self.balance += nominal

    