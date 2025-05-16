from gemini import perguntar_ao_bot
from agenda import agendar_evento

def main():
    print("🤖 Assistente Doméstica iniciada. Digite sua dúvida, ou use o prefixo 'AGENDA:'")
    print("Exemplo: AGENDA: Faxina, 2025-05-20, 14:00, 16:00\n")
    

    while True:
        entrada = input("Você: ")

        if entrada.upper().startswith("AGENDA:"):
            try:
                dados = entrada[7:].strip().split(",")
                if len(dados) != 4:
                    raise ValueError("Formato incorreto. Use: AGENDA: título, data, hora_início, hora_fim")

                titulo, data, inicio, fim = [d.strip() for d in dados]
                resposta = agendar_evento(titulo, data, inicio, fim)
                print(resposta)
            except Exception as e:
                print("⚠️ Erro ao agendar. Verifique o formato.")
                print(e)

        else:
            resposta = perguntar_ao_bot(entrada)
            print("🤖 Assistente:", resposta)

if __name__ == "__main__":
    main()