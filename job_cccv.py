import requests
from bs4 import BeautifulSoup
import pymssql  
from datetime import datetime


def main():
    link = "https://www.cccv.org.br/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

    requisicao = requests.get(link, headers=headers)
    #print(requisicao)

    site = BeautifulSoup(requisicao.text, "html.parser")

    titulo = site.find("title")
    dia = site.find("div", class_="date")
    #periodo = site.find("ul", class_="table-body linha middle-arabica")
    periodo = "2025/2026"
    a_dura = site.find_all("ul", class_="table-body linha bottom-arabica")
    a_rio = site.find_all("ul", class_="table-body linha middle-arabica")
    conilon = site.find_all("ul", class_="table-body linha bottom-conilon")

    txt_a_dura = a_dura[0].find_all("li")
    txt_a_rio = a_rio[1].find_all("li")
    txt_conilon = conilon[0].find_all("li")

    #print(titulo.get_text())
    #print("Dia:", dia.get_text().strip(), "-------", periodo.strip())
    #print(txt_a_dura[0].get_text(), "-------", txt_a_dura[1].get_text())
    #print(txt_a_rio[0].get_text(), "--------", txt_a_rio[1].get_text())
    #print(txt_conilon[0].get_text(), "--------------------------", txt_conilon[1].get_text())

          
    banco(dia.get_text().strip(), periodo, txt_a_dura[0].get_text(), txt_a_rio[0].get_text(), 
          txt_conilon[0].get_text(), txt_a_dura[1].get_text(), txt_a_rio[1].get_text(), txt_conilon[1].get_text())


def banco(dia, periodo, txt_a_dura, txt_a_rio, txt_conilon, a_dura, a_rio, conilon):
    # Informações de conexão
    server = ''  
    database = ''                 
    username = ''          
    password = ''                 

    # Conectando ao banco de dados com pymssql
    try:
        connection = pymssql.connect(
            server=server,
            user=username,
            password=password,
            database=database
        )
        print(f"Conexão bem-sucedida em: {datetime.now()}")
        

        # Criação do cursor para executar as consultas
        cursor = connection.cursor()

        # Incluindo o campo updated_at com GETDATE() no SQL
        cursor.execute("""
                       UPDATE dbo.cotacao_cafes 
                       SET data_vigencia = %s, periodo = %s, nome = %s, valor = %s, updated_at = GETDATE()
                       WHERE id = 1;
                       """, (dia, periodo, txt_a_dura, a_dura))

        cursor.execute("""
                       UPDATE dbo.cotacao_cafes 
                       SET data_vigencia = %s, periodo = %s, nome = %s, valor = %s, updated_at = GETDATE()
                       WHERE id = 2;
                       """, (dia, periodo, txt_a_rio, a_rio))

        cursor.execute("""
                       UPDATE dbo.cotacao_cafes 
                       SET data_vigencia = %s, periodo = %s, nome = %s, valor = %s, updated_at = GETDATE()
                       WHERE id = 3;
                       """, (dia, periodo, txt_conilon, conilon))

    except Exception as e:
        print(f"Erro de conexão em {datetime.now()}: {e}")

    finally:
        # Fechar a conexão
        if 'connection' in locals() and connection:
            connection.commit()
            connection.close()
            print("Conexão fechada.")


main()

