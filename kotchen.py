class RabbitProtectionError(SyntaxError):
    pass

def cook_dinner(action):
    if action == "beat":
        raise RabbitProtectionError(
            "Rabbit is too cute to be beaten", 
            ("forest_rpg.py", 42, 8, "rabbit.hit(damage=999)")
        )
    elif action == "eat":
        raise RabbitProtectionError(
            "Rabbit is too cute to be eaten", 
            ("kitchen.py", 100, 12, "shashlik.cook(rabbit)")
        )