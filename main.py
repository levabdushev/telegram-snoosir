# complaint_bot.py
import json
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_json_file(file_path):
    """Читает JSON-файл и возвращает его содержимое."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат файла {file_path}")
        exit(1)

def create_complaint(username, user_id, reason, chat_link, message_link):
    """Формирует текст жалобы на английском языке."""
    return f"""Hello Telegram Support,

I would like to report a user @{username if username != 'none' else 'none'} (User ID: {user_id}).
The user has violated the rule: "{reason}".
Chat where the violation occurred: {chat_link}
Link to the message violating the rule: {message_link}

Please take action regarding this user as soon as possible.

Best regards,
[Your Name]"""

def send_email(email, password, recipient, complaint_text):
    """Отправляет email с жалобой."""
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = 'Complaint about Telegram User'
    msg.attach(MIMEText(complaint_text, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, recipient, msg.as_string())
        server.quit()
        print(f"Жалоба отправлена с {email} на {recipient}")
    except Exception as e:
        print(f"Ошибка при отправке с {email} на {recipient}: {e}")

def main():
    # Загрузка данных из JSON-файлов
    gmails = load_json_file('gmails.json')
    wheresend = load_json_file('wheresend.json')

    # Запрос данных у пользователя
    username = input("Введите username пользователя (@username) или 'none', если его нет: ")
    user_id = input("Введите ID пользователя в Telegram: ")
    reason = input("Введите причину жалобы (нарушение правил Telegram): ")
    chat_link = input("Введите ссылку на чат, где произошло нарушение: ")
    message_link = input("Введите ссылку на сообщение, нарушающее правила: ")

    # Формирование жалобы
    complaint_text = create_complaint(username, user_id, reason, chat_link, message_link)
    print("\nСформированная жалоба:\n")
    print(complaint_text)

    # Параметры отправки
    total_time = 5 * 60  # 5 минут
    interval = 30  # 30 секунд
    iterations = total_time // interval  # 10 итераций

    print(f"\nОтправка жалоб началась. Будет отправлено {iterations} раз с интервалом 30 секунд.")

    # Отправка жалоб
    for i in range(iterations):
        print(f"\nОтправка #{i+1}...")
        for gmail in gmails:
            email = gmail['email']
            password = gmail['password']
            for recipient in wheresend:
                send_email(email, password, recipient, complaint_text)
        
        if i < iterations - 1:  # Не ждем после последней отправки
            print(f"Ожидание {interval} секунд до следующей отправки...")
            time.sleep(interval)

    print("\nОтправка завершена!")

if __name__ == "__main__":
    main()