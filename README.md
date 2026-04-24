## Лабораторная работа №2 по киберфизическим системам(Задание на Тройку)

### МАИ | 4 курс | 8 семестр

**Выполнил студент:** Слетюрин Кирилл Сергеевич

**Группа:** М8О-408Б-22

Инференс LLM через Ollama

## Используемый стек

- Python 3.10+
- requests
- Ollama
- Qwen2.5:0.5B

## Структура проекта

```bash
nlplab2/
 ├── main.py
 ├── report.csv
 ├── requirements.txt
 └── README.md
```

## Инструкция 

Установить Python 3.10+

Выполнить команды:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sudo snap install ollama
ollama pull qwen2.5:0.5b
ollama serve
python main.py

```

После выполнения будет создан файл report.csv

## Вывод

В рамках задания был развернут локальный сервер Ollama и загружена модель Qwen2.5:0.5B.

Был реализован Python-скрипт, который:

- отправляет HTTP-запросы к серверу Ollama;
- выполняет инференс модели на 10 заранее подготовленных запросах;
- получает ответы LLM;
- сохраняет результаты в файл `report.csv`.

Итогом работы является полностью настроенный локальный inference pipeline для взаимодействия с LLM через HTTP API.

