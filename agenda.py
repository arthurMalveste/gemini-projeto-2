from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']

def autenticar_google_calendar():
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=8080)  # usa o redirecionamento configurado
        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

def agendar_evento(titulo, data, hora_inicio, hora_fim):
    service = autenticar_google_calendar()
    evento = {
        'summary': titulo,
        'start': {
            'dateTime': f'{data}T{hora_inicio}:00',
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': f'{data}T{hora_fim}:00',
            'timeZone': 'America/Sao_Paulo',
        },
    }
    evento = service.events().insert(calendarId='primary', body=evento).execute()
    return f"✅ Evento criado!\n📆 {evento['summary']} em {data} das {hora_inicio} às {hora_fim}\n🔗 {evento.get('htmlLink')}"
