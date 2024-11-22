from datetime import datetime

def convert_date(date_string: str) -> str:
    """
    Konwertuje datę z formatu ISO 8601 na format 'DD.MM.YYYY HH:MM:SS'.

    :param date_string: Data w formacie 'YYYY-MM-DDTHH:MM:SS.sss±HHMM'
    :return: Data w formacie 'DD.MM.YYYY HH:MM:SS'
    """
    try:
        # Usunięcie części dotyczącej strefy czasowej (+HHMM) przed parsowaniem
        date_string = date_string.split('+')[0]

        # Parsowanie daty z milisekundami
        parsed_date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')

        # Formatowanie do 'DD.MM.YYYY HH:MM:SS'
        return parsed_date.strftime('%d.%m.%Y %H:%M:%S')

    except ValueError:
        # Obsługa przypadku bez milisekund
        try:
            parsed_date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
            return parsed_date.strftime('%d.%m.%Y %H:%M:%S')
        except ValueError:
            raise ValueError("Nieprawidłowy format daty")
        
'''
Przykład użycia
date_string = '2024-11-08T09:30:00.703+0100'
formatted_date = convert_date(date_string)
print(formatted_date)

wynik
08.11.2024 09:30:00
'''