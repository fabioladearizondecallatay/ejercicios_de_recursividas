def sort_tiles(tiles):
    #cuenta la frecuencia de los colores
    frequency = {'red': 0, 'green': 0, 'blue': 0}
    for tile in tiles:
        if tile == 'red':
            frequency['red'] += 1
        elif tile == 'green':
            frequency['green'] += 1
        elif tile == 'blue':
            frequency['blue'] += 1

    #genera la secuencia ordenada
    order = []
    for color, count in frequency.items():
        order.extend([color] * count)

    return order

#pide al usuario las fichas 
tiles = input("Enter the tiles separated by spaces (red, green, blue): ").split()

#verifica que las fichas ingresadas son validas
valid_colors = {'red', 'green', 'blue'}
if not all(tile in valid_colors for tile in tiles):
    print("Error: The entered tiles are not valid. Please enter only 'red', 'green', or 'blue'.")
else:
    #ordena las fichas
    order = sort_tiles(tiles)
    print("Original order of tiles:", tiles)
    print("Sorted tiles:", order)
