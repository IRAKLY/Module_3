def send_email(message, recipient, *, sender="university.help@gmail.com"):
    domain_ = ('.com', '.ru', '.net')

    if ('@' in recipient and '@' in sender) and recipient.endswith(domain_) and sender.endswith(domain_):

        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.\n\t {message}")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.\n\t {message}")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')