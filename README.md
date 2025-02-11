# Weather CLI

Чтобы протестировать данный проект, необходимо:

1. Зарегистрироваться на <https://weatherstack.com>
2. Получить ключ API
3. Создать в корне проекта файл `.env`
4. Вставить ключ в созданный файл в формате
5. Запустить веб-сервер. Описание запуска указано в разделе [Веб-сервер](#веб-сервер)

```
API=abcdef1234
```

## Работа с Python

Перейти в директорию с приложением на Python

```sh
cd python_app
```

Установить необходимые библиотеки

```sh
pip install -r requirements.txt
```

Запустить программу

```sh
python main.py
```

## Работа с Node.Js

Перейти в директорию с приложением на Node

```sh
cd node_app
```

Установить зависимости

```sh
npm i
```

Запустить программу с параметрами в виде `node index.js c <Город> <Единица измерения C, F или K>`

```sh
npm run weather Moscow c
```

---

# Веб-сервер

Для работы также необходим веб-сервер, который запускается из папки `server`:
```sh
cd server
```
Для запуска необходимо установить необходимые библиотеки.
```sh
pip install -r requirements.txt
```
Запуск сервера:
```sh
python main.py
```
У сервера есть Swagger, доступный по адресу `http://localhost:5000/swagger`, в котором описаны методы сервера.
