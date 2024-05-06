import requests
import auth
import json
import time
from datetime import date


def main():
    # В заголовках используется Personal Access Token, получить его можно в настройках профиля
    # Данные для авторизации забираются из файла auth.py
    headers = {'X-Auth-Token': auth.auth_token, 'X-User-Id': auth.user_id, "Content-type": "application/json"}
    # Зацикливаем скрипт на бесконечность
    while True:
        # Задаем дату для логов
        today = date.today()
        date_format = today.strftime("%d/%m/%Y")
        # Делаем запрос на блокировку
        request_result = requests.post(auth.url + "/users.deactivateIdle", headers=headers,
                                       json={"daysIdle": auth.days_iddle, "role": "user"})
        # Форматируем результат
        format_result = json.loads(request_result.content)
        # Выводим сообщение в лог
        print(
            f'{date_format} Operation result: {format_result["success"]}, number of users blocked: {format_result["count"]}')
        # Спим 24 часа
        time.sleep(86400)  # 86400
    pass


if __name__ == '__main__':
    main()
