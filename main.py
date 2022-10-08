from Sort import counting_sort, counting_sort_task_3, radix_sort, radix_sort_task_3, radix_sort_task_3_2
from random import randint


print(10 // 3)

"""
Автоматичне введення в масив
"""


def auto_input():
    main_array = []
    number_of_elements = (input(f"Вкажіть кількість елементів в масиві: "))
    frame_min_number = 0
    frame_max_number = int(input(f"Вкажіть максимальне число яке може входити в масив: "))
    for i in range(int(number_of_elements)):
        main_array.append(randint(frame_min_number, frame_max_number))

    return main_array


main_array = auto_input()

"""
PART 1
"""

print(f"Вхідний масив                                : {main_array}")

print(f"Після сортування методом Підрахунку          : {counting_sort(main_array)}")

print(f"Після сортування методом Підрахунку обернений: {counting_sort_task_3(main_array)}")


"""
PART 2
"""
print("---------------------------------------------")


print(f"Вхідний масив                              : {main_array}")

print(f"Після сортування за розрядами              : {radix_sort(main_array)}")

print(f"Після сортування за розрядами обернений 3.1: {radix_sort_task_3(main_array)}")

print(f"Після сортування за розрядами обернений 3.2: {radix_sort_task_3_2(main_array)}")

print("---------------------------------------------")

