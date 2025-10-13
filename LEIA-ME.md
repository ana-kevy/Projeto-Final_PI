# Manual do Projeto Django – Primeiro Emprego

## 1. Visão Geral
O projeto gerencia vagas de emprego, empresas e usuários.

## 2. Pré-requisitos
- Python 3.11+
- Django 5+
- VS Code
- Git
- Ambiente virtual recomendado

## 3. Estrutura do Projeto
primeiro_emprego/
├── manage.py
├── db.sqlite3
├── primeiro_emprego/
├── usuario/
├── vagas/
└── empresa/

## 4. Funcionalidades Principais
### Usuário
- Registrar, Login/Logout
- Perfil e edição
- Mensagens de feedback

### Vagas
- Listar, criar, editar, excluir vagas

### Empresa
- Cadastrar empresas
- Gerenciar vagas

## 5. Como rodar no VS Code
1. Abra o terminal no VS Code: `Terminal → New Terminal`
2. Crie ambiente virtual:
```bash
python -m venv venv
Ative:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Instale dependências:
pip install -r requirements.txt

rodar migrations: 
python manage.py migrate
 
rodar servidor :
python manage.py runserver

Acesse http://127.0.0.1:8000/





