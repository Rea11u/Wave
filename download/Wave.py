import struct

# Функция для восстановления исходного порядка байтов
def unshuffle_bytes(data, permutation):
    unshuffled = [0] * len(data)
    for i, p in enumerate(permutation):
        unshuffled[p] = data[i]
    return bytes(unshuffled)

# Функция расшифрования данных
def encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

# Чтение бинарного файла
with open('encrypted_flag.bin', 'rb') as f:
    # Чтение длины перестановки (известно из предыдущего скрипта, длина равна длине флага)
    permutation_length = 32  # Замените на реальную длину флага, если она изменится
    # Чтение перестановки
    permutation = struct.unpack(f'{permutation_length}i', f.read(permutation_length * 4))
    # Чтение перемешанного зашифрованного флага
    shuffled_flag = f.read()

# Восстановление исходного порядка байтов
encrypted_flag = unshuffle_bytes(shuffled_flag, permutation)

# Определение ключа (подобран вручную или с помощью анализа)
key = 42

# Расшифрование данных
flag_bytes = encrypt_decrypt(encrypted_flag, key)

# Преобразование байтов в строку
flag = flag_bytes.decode()
print(f'Recovered flag: {flag}')
