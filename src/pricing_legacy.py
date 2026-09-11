def calculate_discount(price, user_type, is_member):
    if user_type == "VIP":
        if is_member:
            return price * 0.80
        else:
            return price * 0.85
    elif user_type == "REGULAR":
        if is_member:
            return price * 0.90
        else:
            return price * 0.95
    else:
        return price