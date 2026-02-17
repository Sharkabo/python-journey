from abc import ABC, abstractmethod
from typing import Any  

class PaymentGateway(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def connect(self, api_key: str) -> Any:
        pass

    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class PaypalGateway(PaymentGateway):
    def __init__(self, paypal_id) -> None:
        super().__init__()
        self.paypal_id = paypal_id
    
    def connect(self, api_key: str) -> Any:
        return f"API: {api_key}"
    
    def process_payment(self, amount: float) -> bool:
        payment_completed: bool
        if amount > 0:
            payment_completed= True
        else:
            payment_completed= False
        
        return payment_completed

class StripeGateway(PaymentGateway):
    def __init__(self, stripe_id) -> None:
        super().__init__()
        self.stripe_id = stripe_id
    
    def connect(self, api_key: str) -> Any:
        return f"API: {api_key}"
    
    def process_payment(self, amount: float) -> bool:
        payment_completed: bool
        if amount > 0:
            payment_completed= True
        else:
            payment_completed= False
        
        return payment_completed