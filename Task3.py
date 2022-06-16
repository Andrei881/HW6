def rot13(text: str, decode=False) -> str:
    text = text.upper()
    abc = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dict = [""]*len(abc)
    shift = 13
    for i in range(len(abc)):
        dict[i] = abc[(i + shift) % len(abc)]
    encoded_text = [""]*len(text)
    for i in range(len(text)):
        if not text[i] in abc:
            encoded_text[i] = text[i]
        else:
            encoded_text[i] = abc[dict.index(text[i])] if decode else dict[abc.index(text[i])]

    return "".join(encoded_text)


text = "Привет!Как жизнь?"

encoded_text = rot13(text)
print(f"Закодированное сообщение: {encoded_text}")

decoded_text = rot13(encoded_text, decode=True)
print(f"Исходное сообщение: {decoded_text}")