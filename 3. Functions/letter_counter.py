def count_letter(text, letter):
    count = 0
    for ch in text: #bierze każdy znak jeden po drugim, #ch w każdej obrocie pętli przbiera inną loiterke
        if ch == letter:
            count += 1 #jesli znajdzie e zwiększa wynik o 1
    return count