media_mobile =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

risultato= []

for i in range(len(media_mobile)):

    if i < n - 1: 
            
            media = sum(media_mobile[:i + 1]) / (i + 1) 
    else:   media = sum(media_mobile[i - n + 1:i + 1]) / n

    risultato.append(media)

print(risultato)