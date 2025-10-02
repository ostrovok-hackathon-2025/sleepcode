# Друзья рекомендуют (Ostrovok Hackathon 2025)

Прототип сервиса персонализированных рекомендаций отелей на основе отзывов друзей.

## Быстрый старт

```bash
cp .env.example .env
docker compose up --build
```

Открыть: [http://localhost:8080](http://localhost:8080)

## Что внутри
- Django 5 + PostgreSQL
- Автоматические миграции и сидирование при старте
- Простой фронтенд на Django templates (Bootstrap)
- Фильтр «Показать только рекомендованные друзьями»

## Тестовые данные
- Пользователь admin/admin123
- Юзеры: alice, bob, charlie
- Демо-отели: Москва, Париж, Стамбул
- Отзывы: bob про Москву, charlie про Стамбул

## Маршруты
- `/` — список отелей
- `/health` — healthcheck (JSON)
- `/admin/` — админка
