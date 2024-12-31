sexo = str(input('\033[mInforme o seu sexo[M/F]:\033[32m ')).upper().strip()[0]
if sexo != 'M' and sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[mDados inválidos. Por favor, informe seu sexo[M/F]: \033[32m')).upper().strip()[0]
if sexo == 'M':
    print('\033[mSexo masculino registrado com sucesso.')
else:
    print('\033[mSexo feminino registrado com sucesso.')
