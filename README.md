# CHIHO_BOT

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Salary Calculator Bot - это Telegram-бот для подсчета зарплаты сотрудников. Бот позволяет вводить рабочие часы и почасовую ставку для каждого сотрудника и автоматически рассчитывает их зарплату.

## Возможности

- Регистрация сотрудников
- Ввод рабочих часов
- Установка почасовой ставки
- Подсчет зарплаты

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/slon-hk/chiho_bot.git
    cd chiho_bot
    ```

2. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

3. Создайте файл `.env` и добавьте в него ваш Telegram Bot API Token:

    ```env
    BOT_TOKEN=your_telegram_bot_token
    ```

4. Запустите бота:

    ```sh
    python3 main.py
    ```


## Технические детали

### Структура проекта

```plaintext
chiho_bot/
│
├── bot.py               # Основной файл бота
├── handlers.py          # Обработчики команд
├── database.py          # Работа с базой данных
├── requirements.txt     # Зависимости проекта
├── .env                 # Файл для хранения секретов (не добавлять в репозиторий)
└── README.md            # Документация
