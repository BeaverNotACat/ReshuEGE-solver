# РешуЕГЭ solver
Маленький парсер для спидрана тестов на [РешуЕГЭ](https://ege.sdamgia.ru/)

### Запуск
1.  Установите необходимые пакеты для Python
> pip install -r requirements.txt

2.  Укажите ваши настройки в setings.yml и создайте файл с ответами на тест
> answers.txt:
> 123
> 456
> 678

3. Запустите парсер, указав URL теста и имя файла с ответами
>   python run.py "https://ege.sdamgia.ru/test?id=49359682" answers.txt