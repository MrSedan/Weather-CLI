# Weather CLI

Чтобы протестировать данный проект, необходимо:

1. Зарегистрироваться на https://weatherstack.com
2. Получить ключ API
3. Создать в корне проекта файл `.env`
4. Вставить ключ в созданный файл в формате

```
API=abcdef1234
```

## Работа с Python

Перейти в директорию с приложением на Python

```
cd python_app
```

Установить необходимые библиотеки

```
pip install -r requirements.txt
```

Запустить программу

```
python main.py
```

## Работа с Node.Js

Перейти в директорию с приложением на Node

```
cd node_app
```

Установить зависимости

```
npm i
```

Запустить программу с параметрами в виде `node index.js c <Город> <Единица измерения C, F или K>`

```
npm run weather Moscow c
```
