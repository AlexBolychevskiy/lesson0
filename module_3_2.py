def send_email(message,recipient, *,sender = 'university.help@gmail.com'):
    variants = (".com", ".ru", ".net")
    a = recipient.endswith(variants)
    b = sender.endswith(variants)
    if '@' not in recipient and "@" not in sender or a is not True or b is not True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
              print("Нельзя отправить письмо самому себе!")
    elif sender =='university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender ='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')