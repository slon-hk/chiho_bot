# CHIHO_BOT

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

CHIHO_BOT - это Telegram-бот для подсчета зарплаты сотрудников. Бот позволяет вводить рабочие часы и почасовую ставку для каждого сотрудника и автоматически рассчитывает их зарплату.

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
├── db.py                # Работа с базой данных
├── keyboard.py          # Работа с клавитурой бота
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация
```


# CHIHO_BOT

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

CHIHO_BOT is a Telegram bot for calculating employees' salaries. The bot allows you to input working hours and hourly rate for each employee and automatically calculates their salary.

## Features

-Employee registration
-Input of working hours
-Setting hourly rate
-Salary calculation

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/slon-hk/chiho_bot.git
    cd chiho_bot
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a .env file and add your Telegram Bot API Token:

    ```env
    BOT_TOKEN=your_telegram_bot_token
    ```

4. Run the bot:

    ```sh
    python3 main.py
    ```

## Technical Details

### Project Structure

```plaintext
chiho_bot/
│
├── bot.py               # Main bot file
├── handlers.py          # Command handlers
├── db.py                # Database operations
├── keyboard.py          # Bot keyboard operations
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```
