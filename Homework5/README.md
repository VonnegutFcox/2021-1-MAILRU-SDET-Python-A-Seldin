# 2021-1-MAILRU-SDET-Python-A-Seldin
### bash
total_number_of_requests
* считывает весь файл
* считает количество строк
* записывает получившееся значение в файл

total_number_of_requests_by_type
* итерируется по списку со всеми возможными типами запросов
* ищет в строках первые вхождения этих типов и считает их повторения в файле
* записывает получившееся значение в файл

top10
* итерируется по строкам файла
* сортирует эти значения по количеству вхождений url
* выводит первые 10
* записывает получившееся значение в файл

top5_4xx
* фильтрует все строки по регулярному выражению 4ХХ
* оставляет только уникальные значения
* сортирует по размеру запросов
* выводит первые 5
* записывает получившееся значение в файл

top5_5xx
* фильтрует все строки по регулярному выражению 5ХХ
* создает список всех пользователей
* сортирует по количеству запросов пользователя
* выводит первые 5
* записывает получившееся значение в файл

### python
total_number_of_requests.py
* расчитывает количество всех строк в файле
* записывает получившееся значение в файл

total_number_of_requests_by_type.py
* считывает файл
* итерируется по строкам
* ищет совпадение значения из списка всех типов запросов
* записывает получившиеся значения в словарь ключ="тип" значение="количество повторений"
* записывает получившееся значение в файл

top10.py
* считывает файл
* создает список из всех url
* сортирует список по количеству повторений url
* выводит первые 10
* записывает получившееся значение в файл

top5_4xx.py
* считывает файл
* создает список и строк, и фильтрует их по типу ответа 4ХХ
* сортирует список по числу размера запроса
* выводит первые 5
* записывает получившееся значение в файл

top5_5xx.py
* считывает файл
* создает список и строк
  * на основе него создает список из ip, и фильрует их по регулярному выражению 5ХХ
* сортирует список по числу запросов
* выводит первые 5
* записывает получившееся значение в файл