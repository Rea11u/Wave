from PIL import Image
import numpy as np

# Загрузка изображения
encoded_image = Image.open('download/encoded_image.png')
pixels = np.array(encoded_image)

# Извлечение сообщения
binary_message = ''
for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        r, g, b = pixels[i, j]
        binary_message += str(r & 1)  # Извлечение наименьшего значащего бита

# Разбиваем бинарное сообщение на байты и преобразуем в символы
message_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
decoded_message = ''.join([chr(int(byte, 2)) for byte in message_bytes])

# Печатаем извлеченное сообщение
print(decoded_message)
