import requests
import csv
import os

def get_cat_facts():
    url = 'https://cat-fact.herokuapp.com/facts/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        return response.json()
    except (requests.exceptions.HTTPError, Exception) as err:
        print(f'Houve um erro : {err}')  # Exibe o erro HTTP ou qualquer outro erro
        return None

def save_facts_to_csv(facts, filename='cat_facts.csv'):
    if facts:
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(facts[0].keys())  # Escreve o cabeçalho com os nomes das colunas
                for fact in facts:
                    writer.writerow(fact.values())  # Escreve os valores de cada fato
            print(f'O arquivo {filename} foi salvo com sucesso !')
        except IOError as e:
            print(f'Houve um erro ao salvar : {e}')

if __name__ == "__main__":
    cat_facts = get_cat_facts()
    if cat_facts:
        save_facts_to_csv(cat_facts)