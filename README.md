# Enviar arquivo de Workmap 
O código foi desenvolvido utilizando Python, afim de automatizar o envio do workmap para vários destinatários.
  

# Configuração

## Ambiente Virtual
Para executar o projeto em um abiente virtual é preciso criar uma env:
<br>
1º Instalar o env em sua máquina para isso utilize o comando :
```
pip install venv
```
2º Criar sua máquina virtual:
```
python3 -m venv nome_maquina_virtual-env
```
3º Escolha o comando de acordo com seu sistema opercional:
#### Para Windows:
```
nome_maquina_virtual-env\Scripts\activate.bat
```
#### Para Unix ou no MacOS:
```
source nome_maquina_virtual-env/bin/activate
```

## Instalando Dependências
Use o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.
```bash
pip install -r requirements.txt
```

## Arquivo de Configuração
Para executar o projeto é necessário criar um arquivo `config.yaml` na raiz do projeto. Segue exemplo de estrutura do arquivo:

```yaml

email:
  remetente: '' # endereço do remetente
  senha: '' # senha do remetente

```

# Inicializando

Para executar o robô basta executar o comando :

```
pyhton main.py
