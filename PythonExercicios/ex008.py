cores = {'branco':'\033[1;30m', 'vermelho':'\033[1;31m', 'azul':'\033[1;34m', 'ciano':'\033[1;36m', 'roxo':'\033[1;35m'}

nm = float(input('Digite um valor em metros: '))
ncm = nm * 100
nmm = nm * 1000
ndm = nm * 10
ndam = nm / 10
nhm = nm / 100
nkm = nm / 1000

print('{}Valor em metros: {}'.format(cores['roxo'] ,nm), end=' >>> ')
print('{}Valor em centímetros: {:.0f}'.format(cores['vermelho'], ncm), end=' >>> ')
print('{}Valor em milímetros: {:.0f}'.format(cores['azul'] ,nmm), end= '>>> ')
print('{}Valor em decímetros: {}. {}Valor em decâmetros: {}. {}Valor em hectômetros: {}. {}Valor em quilômetros: {}.'.format(cores['ciano'],ndm, cores['branco'],ndam, cores['roxo'],nhm, cores['vermelho'],nkm))

