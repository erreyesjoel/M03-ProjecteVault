import re

def check_password(pwd):
    # 1. Mínim 8 caràcters
    if len(pwd) < 8:
        return False
    
    # 2. Ha de tenir almenys un número
    if not any(char.isdigit() for char in pwd):
        return False
    
    # 3. Ha de tenir almenys una majúscula
    if not any(char.isupper() for char in pwd):
        return False
    
    # 4. No pot contenir la paraula "admin" (Blacklist check)
    if "admin" in pwd.lower():
        return False
    
    return True