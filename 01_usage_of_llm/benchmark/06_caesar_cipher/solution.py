def caesar_cipher(s: str, shift: int) -> str:
    result = ""
    shift = shift % 26  # Appliquer le modulo 26 pour gérer les décalages négatifs ou supérieurs à 25
    
    for char in s:
        if char.isalpha():
            # Déterminer si le caractère est une majuscule ou une minuscule
            is_upper = char.isupper()
            # Convertir le caractère en minuscule pour le traitement
            char_lower = char.lower()
            # Calculer la nouvelle position après décalage
            new_pos = (ord(char_lower) - ord('a') + shift) % 26
            # Convertir le caractère en majuscule si nécessaire
            new_char = chr(ord('a') + new_pos) if not is_upper else chr(ord('A') + new_pos)
            result += new_char
        else:
            # Conserver les caractères non alphabétiques inchangés
            result += char
    return result