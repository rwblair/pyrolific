from enum import Enum


class DynamicPaymentAction(str, Enum):
    DYNAMIC_PAYMENT = "DYNAMIC_PAYMENT"

    def __str__(self) -> str:
        return str(self.value)
