# encoding: utf-8

list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
list_2 = ['B', 'C', 'D', 'A', 'F', 'E', 'Z', 'M', 'N', 'J', 'K', 'L']
print(list_1)
print(list_2)

removed = set(list_1) - set(list_2)
added = set(list_2) - set(list_1)
print(f'Список "list_2" получился из списка "list_1" путем удаления эл.: {removed} и добавления эл.: {added}')
for element_2 in list_2:
    if element_2 in list_1:
        if list_1.index(element_2) == list_2.index(element_2):
            print(f'Элемент {element_2} находится на {list_1.index(element_2)} позиции в обоих списках.')
        elif list_1.index(element_2) - list_2.index(element_2) > 0:
            print(f'Элемент {element_2} в списке "list_2" находится на {list_1.index(element_2)} позиции со сдвигом '
                  f'влево на {list_1.index(element_2) - list_2.index(element_2)} поз. относительно списка "list_1"')
        else:
            print(f'Элемент {element_2} в списке "list_2" находится на {list_1.index(element_2)} позиции со сдвигом '
                  f'вправо на {list_2.index(element_2) - list_1.index(element_2)} поз. относительно списка "list_1"')
