
Эта программа - попытка создать простой инструмент для определения использования
памяти и затрат времени при работе тестируемых функций, работающих с массивами.
При разработке использовались сортировщики: пузырьковый, timsort и radixsort.

## Использование ##

При запуске предлагается выбрать файл со скриптом Python,  который содержит функцию 'sort' и
задать минимальное и максимальное количество элементов в массиве. После этого создаётся 10 наборов целых случайных чисел и сортируются. Результат можно увидеть в консоли и вывести в CSV
файл.

### Примечания ###

1. При сортировке пузырьком массивы размером более 10000 сортируются <b>очень</b> долго.
2. Строки 14 и 15 предусматривают использование функций с именем отличнм от <i>sort</i>.


