class CustomerProfile:
    def __init__(self, user_id: int, email: str, password_hash: str, city: str, loyalty_points: int):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points


# 1. Ліквідація Stamp Coupling: передаються лише потрібні примітивні типи (city та weight_kg)
def calculate_delivery_cost(city: str, weight_kg: float) -> float:

    base_rate = 80.0 if city == "Ivano-Frankivsk" else 110.0
    return base_rate + (weight_kg * 15.0)

    base_rate = 50.0 if city == "Ivano-Frankivsk" else 110.0
    return base_rate + (weight_kg * 15.0)



# 2. Ліквідація Common Coupling та Control Coupling:
# - немає глобальної змінної GLOBAL_TAX_RATE; tax_rate передається явно (за замовчуванням 0.20)
# - немає mode_flag; стандартний розрахунок винесено в окрему функцію
def process_standard_invoice(
    amount: float,
    city: str,
    weight_kg: float,
    tax_rate: float = 0.20
) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


# Окрема функція для розрахунку без податку (не змінює жодного глобального стану)
def process_tax_exempt_invoice(
    amount: float,
    city: str,
    weight_kg: float
) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
