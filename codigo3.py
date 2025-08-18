tem_wifi = False
tem_dados_moveis = True

O_celular_pode_se_conectar = tem_wifi or tem_dados_moveis

print(f'O celular pode se conectar a internet?{O_celular_pode_se_conectar} ')