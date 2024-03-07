import pandas as pd

excel_file = 'subseccao.xlsx'

df = pd.read_excel(excel_file)

# df_municipios = df[['NUTS1 DSG','MUNICIPIO', 'MUNICIPIO DSG']].drop_duplicates()


# df_municipios = df_municipios.dropna(subset=['MUNICIPIO']).reset_index(drop=True)


# output_file = 'municipio-sql.txt'

# with open(output_file, 'w') as file:
#     for index, row in df_municipios.iterrows():
#         if row['NUTS1 DSG'] != 'Continente':
#             continue
#         municipio_id = str(int(row['MUNICIPIO']))
#         if len(municipio_id) == 3:
#             municipio_id = '0' + municipio_id
#         municipio_dsg = str(row['MUNICIPIO DSG'])
#         sql_command = f"UPDATE public.municipios SET dsg = '{municipio_dsg}' WHERE dtmn21 = '{municipio_id}';\n"
#         file.write(sql_command)

df_freg = df[['NUTS1 DSG','FREGUESIA', 'FREGUESIA DSG']].drop_duplicates()


df_freg = df_freg.dropna(subset=['FREGUESIA']).reset_index(drop=True)


output_file = 'FREGUESIA-sql.txt'

with open(output_file, 'w') as file:
    for index, row in df_freg.iterrows():
        if row['NUTS1 DSG'] != 'Continente':
            continue
        FREGUESIA_id = str((row['FREGUESIA']))
        if len(FREGUESIA_id) == 5:
            FREGUESIA_id = '0' + FREGUESIA_id
        FREGUESIA_dsg = str(row['FREGUESIA DSG'])
        sql_command = f"UPDATE public.freguesias SET dsg = '{FREGUESIA_dsg}' WHERE dtmnfr21 = '{FREGUESIA_id}';\n"
        file.write(sql_command)




print(f"SQL commands written to {output_file}")