from random import randint, choice
from string import ascii_letters, digits
from math import gcd
from sqlite3 import connect

class RSAEncryption:
    def __init__(self):
        self.__p, self.__q = self.generate_distinct_primes()
        self.__n, self.__e, self.__d = self.generate_keys()
        self.__random_string = self.generate_random_string()

    def generate_keys(self):
        n = self.__p * self.__q
        phi_n = (self.__p - 1) * (self.__q - 1)
        e, d = self.generate_public_private_exponents(phi_n)
        return n, e, d

    def generate_public_private_exponents(self, phi_n):
        while True:
            e = randint(phi_n // 2, phi_n)
            if gcd(e, phi_n) == 1:
                d = self.modinv(e, phi_n)
                return e, d

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def generate_distinct_primes(self):
        while True:
            p = self.generate_random_prime(100, 1000)
            q = self.generate_random_prime(100, 1000)
            if p != q:
                return p, q

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_random_prime(self, a, b):
        while True:
            n = randint(a, b)
            if self.is_prime(n):
                return n

    def generate_random_string(self):
        return ''.join(choice(ascii_letters + digits + "@#$&") for _ in range(randint(30, 40)))

    def get_random_string(self):
        return self.__random_string

    def store_to_DB(self, encrypted_message, rail_fence_key):
        conn = connect("database.db")
        cursor = conn.cursor()
        self._encrypted = ' '.join(map(str, encrypted_message))
        insert_query = "INSERT INTO CipherData (encrypted, randomstring, keyN, keyE, keyD, rail_fence_key) VALUES (?, ?, ?, ?, ?, ?)"
        data = (self._encrypted, self.__random_string, self.__n, self.__e, self.__d, rail_fence_key)
        cursor.execute(insert_query, data)
        conn.commit()
        cursor.close()
        conn.close()

    def encrypt(self, message):
        initDB()
        rail_fence_key = randint(2, 5)
        rail_fence_cipher = RailFenceCipher(rail_fence_key)
        rail_fence_encrypted = rail_fence_cipher.encrypt(message)
        rsa_encrypted_integers = [pow(ord(char), self.__e, self.__n) for char in rail_fence_encrypted]
        self.store_to_DB(rsa_encrypted_integers, rail_fence_key)
        return {
            "status": "success",
            "message": self.__random_string
        }

    def decrypt(self, random_string):
        conn = connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT encrypted, keyN, keyE, keyD, rail_fence_key FROM CipherData WHERE randomstring = ?", (random_string,))
        result = cursor.fetchone()
        if result:
            encrypted_message, keyN, keyE, keyD, rail_fence_key = result
            rsa_encrypted_integers = [int(x) for x in encrypted_message.split()]
            rsa_decrypted = ''.join([chr(pow(char, keyD, keyN)) for char in rsa_encrypted_integers])
            rail_fence_cipher = RailFenceCipher(rail_fence_key)
            rail_fence_decrypted = rail_fence_cipher.decrypt(rsa_decrypted)
            return {
                "status": "success",
                "message": rail_fence_decrypted
            }
        else:
            return {
                "status": "failed",
                "message": "Not found in DB"
            }


class RailFenceCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        num_columns = len(plaintext)
        num_rows = self.key
        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
        
        direction, row = 1, 0
        for j in range(num_columns):
            matrix[row][j] = plaintext[j]
            row += direction

            if row == 0 or row == self.key - 1:
                direction *= -1
        
        cipher = ''
        for i in range(self.key):
            for j in range(num_columns):
                if matrix[i][j] != '':
                    cipher += matrix[i][j]
        return cipher

    def decrypt(self, ciphertext):
        num_columns = len(ciphertext)
        num_rows = self.key
        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
        
        direction, row = 1, 0
        for j in range(num_columns):
            matrix[row][j] = '*'
            row += direction

            if row == 0 or row == self.key - 1:
                direction *= -1
        
        index = 0
        for i in range(self.key):
            for j in range(num_columns):
                if matrix[i][j] == '*':
                    matrix[i][j] = ciphertext[index]
                    index += 1
        
        plaintext = ''
        direction, row = 1, 0
        for j in range(num_columns):
            plaintext += matrix[row][j]
            row += direction

            if row == 0 or row == self.key - 1:
                direction *= -1
        return plaintext

def initDB():
    conn = connect("database.db")

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CipherData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encrypted VARCHAR(200),
            randomstring VARCHAR(200),
            keyN INT,
            keyE INT,
            keyD INT,
            rail_fence_key INT,
            UNIQUE(encrypted)
        )
    ''')

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':

    initDB()
    
    rsa = RSAEncryption()

    while True:
        user_choice = input("Enter 'encrypt' or 'decrypt' to perform the respective operation: ").strip().lower()
        if user_choice == 'encrypt':
            message = input("Enter the message: ")

            rsa = RSAEncryption()

            cipher = rsa.encrypt(message)

            random_string = rsa.get_random_string()
            
        elif user_choice == 'decrypt':
            random_string = input("Enter the random string: ")

            decrypted_message = rsa.decrypt(random_string)
            if decrypted_message:
                print(decrypted_message)
        else:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")