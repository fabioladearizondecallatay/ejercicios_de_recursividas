def binary_search(list_numbers, element, start=0, end=None):

    """
    Performs a recursive binary search to find an element in an ordered list.

    Parametros:
        list_numbers (list): la lista ordenada de numeros.
        element (int): el elemento de busqueda de cada lista.
        start (int, optional): Indice de inicio para la busqueda. 
        end (int, optional): Indice de fin para la busqueda.

    Returns:
        int: el indice del elemento si encontrzado, -1 si no encontrado.
    """
    
    if end is None:
        end = len(list_numbers) - 1
    
    if start > end:
        return -1  #elemento no encontrado
    
    mid = (start + end) // 2
    
    if list_numbers[mid] == element:
        return mid
    elif list_numbers[mid] < element:
        return binary_search(list_numbers, element, mid + 1, end)
    else:
        return binary_search(list_numbers, element, start, mid - 1)

#pide al usuario que ingrese a lista ordenada y que buscar
list_numbers = input("Enter the ordered list of numbers separated by spaces: ").split()
list_numbers = [int(x) for x in list_numbers]  #convierte elementos a enteros
element_to_search = int(input("Enter the element you want to search for in the list: "))

#verifica que la lista esta ordenada
if list_numbers != sorted(list_numbers):
    print("Error: The entered list is not sorted.")
else:
    index = binary_search(list_numbers, element_to_search)
    if index != -1:
        print(f"The element {element_to_search} is found at index {index}.")
    else:
        print(f"The element {element_to_search} is not found in the list.")
