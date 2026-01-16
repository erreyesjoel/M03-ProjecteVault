import unittest
from vault_security import check_password

class TestVaultSecurity(unittest.TestCase):
    
    def test_password_length(self):
        # NIST recomana mínim 8. "abc" hauria de retornar False.
        self.assertFalse(check_password("abc"))
    
    def test_password_numbers(self):
        # Ha de fallar si no té números
        self.assertFalse(check_password("SoloLetras"))

    def test_password_uppercase(self):
        # Ha de fallar si no té majúscules
        self.assertFalse(check_password("sololower123"))

    def test_password_no_admin(self):
        # Ha de fallar si conté la paraula "admin" (insensible a majúscules)
        self.assertFalse(check_password("Admin12345"))
        
    def test_password_valid(self):
        # Aquesta hauria de ser True
        self.assertTrue(check_password("Vault@2025_Secure"))

if __name__ == '__main__':
    unittest.main()