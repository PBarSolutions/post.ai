import openpyxl
from src.tools.txt_reader import txt_read

def read_excel_data(filepath):

    wk = openpyxl.load_workbook(filepath)

    list_data = []

    info_negocio = wk['info_negocio']

    for row in info_negocio.iter_rows(min_row=2, values_only=True):

        dados = {
                'nome': row[0],
                'setor_atuacao': row[1],
                'publico_alvo': row[2],
                'tom_comunicacao': row[3],
            }

        list_data.append(dados)

    return list_data


def main():
    filepath_excel = './files/data.xlsx'
    filefreelas = './files/steps/freelancer.txt'

    freelas = txt_read(filefreelas)
    dados = read_excel_data(filepath_excel)


    freela = freelas.format(
        EMPRESA=dados['nome'],
        SETOR_ATUACAO=dados['setor_atuacao'],
        PUBLICO_ALVO=dados['publico_alvo'],
        TOM_COMUNICACAO=dados['tom_comunicacao'],
    )



    print("----------------Freelas----------------\n", freela)

    fileanal = './files/steps/analist.txt'
    anals = txt_read(fileanal)

    analist = anals.format(
        EMPRESA=dados['nome'],
        SETOR_ATUACAO=dados['setor_atuacao'],
        PUBLICO_ALVO=dados['publico_alvo'],
        TOM_COMUNICACAO=dados['tom_comunicacao'],
        REDE_SOCIAL='Facebook'
    )

    print("----------------Anal----------------\n", analist)




if __name__ == '__main__':
    main()