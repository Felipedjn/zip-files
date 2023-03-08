Script para zipar arquivos em massa. Construído em Python 3.10

# Descrição
O script compila em .zip arquivos de uma única extensão, o processo é o seguinte:
- Pega os arquivos da pasta e compila
- Exclui a pasta onde os arquivos estão
- Cria uma nova pasta com o mesmo nome

# Cuidados
O script exclui a pasta da qual ele compila, então faça um backup antes de testar!

# Instalação
instalar usando pip
- pip install os
- pip install zipfile
- pip install shutil
- pip install time

# Uso
O diretorio inserido terá que ser aquele em que os arquivos que você quer comprimir em zip estão

![image](https://user-images.githubusercontent.com/114688883/223839862-63a6ad04-56c7-4daf-b6f8-10b9e44a96ce.png)

Exemplo:
Meus arquivos estão na pasta "arquivos", meu caminho vai ser "C:/Users/Usuario/Desktop/arquivos" com a barra invertida

## Extensão dos arquivos
Com esse script só é possível compilar arquivos de um único tipo de extensão, para poder fazer com mais, precisara de alguns ajustes.

![image](https://user-images.githubusercontent.com/114688883/223840482-e01c152d-a37f-4072-b4c7-05512bf80e12.png)

Nessa linha, basta substituir "xml" pela extensão que quiser.

## Excluir e criar pasta

![image](https://user-images.githubusercontent.com/114688883/223841428-42378a63-b32c-4970-b2f5-7ab30516de6c.png)

A primeira linha exclui a pasta;
A segunda linha espera 2 segundos para poder processar;
A terceira linha cria outra pasta com o mesmo nome.

Caso não queira fazer esse processo, basta excluir as linhas.

