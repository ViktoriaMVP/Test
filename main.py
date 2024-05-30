import random
import hashlib

# Генерация простого числа
def generate_prime():
    while True:
        prime_candidate = random.randint(2**10, 2**11)  # Генерация случайного числа
        if is_prime(prime_candidate):  # Проверка числа на простоту
            return prime_candidate

# Проверка числа на простоту
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Генерация ключей
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Задаем открытый ключ
    d = pow(e, -1, phi)  # Вычисляем закрытый ключ

    return ((e, n), (d, n))

# Шифрование сообщения
def encrypt(message, public_key):
    e, n = public_key
    encrypted = pow(message, e, n)
    return encrypted

# Расшифровка сообщения
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted = pow(encrypted_message, d, n)
    return decrypted

# Создание ЭЦП
def sign(message, private_key):
    d, n = private_key
    hashed_message = hashlib.sha256(message.encode()).digest()
    signature = pow(int.from_bytes(hashed_message, byteorder='big'), d, n)
    return signature

# Проверка ЭЦП
def verify(message, signature, public_key):
    e, n = public_key
    hashed_message = hashlib.sha256(message.encode()).digest()
    hashed_message_int = int.from_bytes(hashed_message, byteorder='big')
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == hashed_message_int

# Пример использования
def main():
    # 1. Генерация простых чисел
    prime = generate_prime()
    print("Сгенерированное простое число:", prime)

    # 2. Проверка числа на простоту
    print("Результат проверки на простоту:", is_prime(prime))

    # 3. Генерация ключей
    public_key, private_key = generate_keys()
    print("Открытый ключ (e, n):", public_key)
    print("Закрытый ключ (d, n):", private_key)

    # 4. Шифрование исходного сообщения
    message = input("Введите сообщение для шифрования: ")
    encrypted_message = encrypt(int.from_bytes(message.encode(), byteorder='big'), public_key)
    print("Зашифрованное сообщение:", encrypted_message)

    # 5. Создание и проверка ЭЦП
    signature = sign(message, private_key)
    print("ЭЦП:", signature)
    print("Проверка ЭЦП:", verify(message, signature, public_key))

    # 6. Расшифровка сообщения
    decrypted_message = decrypt(encrypted_message, private_key)
    decrypted_message_bytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big')
    decrypted_message_str = decrypted_message_bytes.decode('utf-8', errors='ignore')
    print("Расшифрованное сообщение:", decrypted_message_str)

if __name__ == "__main__":
    main()
    print("хехехех", 2+2*2)
