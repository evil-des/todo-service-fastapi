# Todo Service

Это полнофункциональный проект для управления задачами, включающий бэкенд на FastAPI с SQLAlchemy и фронтенд на Vue 3 с Tailwind CSS. Проект также использует Docker для контейнеризации, что позволяет легко разворачивать приложение в разных средах.

---

## Особенности

- **Бэкенд (FastAPI):**
  - CRUD операции для задач (создание, чтение, обновление, удаление).
  - Аутентификация и авторизация пользователей.
  - Валидация входящих данных с помощью Zod.
  - Интеграция с PostgreSQL через SQLAlchemy.
  - Документация API (Swagger / OpenAPI).

- **Фронтенд (Vue 3 + Tailwind CSS):**
  - Адаптивный интерфейс для отображения списка задач.
  - Возможность добавления, редактирования и удаления задач.
  - Фильтрация задач по статусу и сортировка по дате создания.
  - Удобный UX с использованием компонентных решений (например, TaskCard, AuthForm).

- **Docker:**
  - Контейнеризация бэкенда, Nginx и базы данных.
  - Прокси-сервер Nginx для объединения фронтенда и бэкенда через единый порт.
  - Легкое развертывание в разных средах (локально, Docker).

---

## Технологии

- **Бэкенд:**  
  - FastAPI  
  - SQLAlchemy  
  - Alembic (миграции базы данных)
  - Pydantic v2 (валидация данных)  
  - PostgreSQL

- **Фронтенд:**  
  - Vue 3
  - Tailwind CSS
  - Zod (валидация данных)  
  - Pinia (управление состоянием)
  
- **Инфраструктура:**  
  - Docker / Docker Compose  
  - Nginx (обратное проксирование)

---

## Установка и запуск

### Локальный запуск с Docker Compose

1. **Настройка переменных окружения:**

   Создайте файл `.env` в корне проекта, например:
   ```env
   NGINX_PORT=80
   BACKEND_PORT=8000
   FRONTEND_PORT=3000

   POSTGRES_USER=youruser
   POSTGRES_PASSWORD=yourpassword
   POSTGRES_DB=todoservice

   JWT_KEY=your_secret_key
   DEBUG=True
   ```
2. **Запуск Docker Compose (в корне проекта):**
```shell 
docker-compose up -d --build
```
3. **Запуск фронтенда:**
```shell 
cd frontend
npm install
npm run dev
```
4. В браузере откройте http://localhost (для NGINX_PORT=80)