# parser
Hacker news parser

Пример запуска
python main.py -d 1 -p 8080 -i localhost -l https://news.ycombinator.com -m 100
или 
python main.py значения берутся из config.py
Параметры:

-l или --link сайт для парсинга
-i или --host интерфейс для api
-p или --port порт для api
-d или --debug дебаг режим
-m или --max_news макс. кол-во новостей для парсинга


