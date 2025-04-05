
# 📊 Django Python Web

Projeto web desenvolvido com Django que implementa uma aplicação de enquetes. Usuários podem votar em perguntas e visualizar os resultados. Ideal para fins didáticos e estudos com o framework Django.

---

## 🔧 Tecnologias Utilizadas

- **Python 3.10+**
- **Django 4.x**
- **SQLite** (banco de dados padrão do Django)

---

## 📁 Estrutura do Projeto

```
Django-Python-Web-main/
└── mysite/
    ├── manage.py                  # Utilitário de linha de comando do Django
    ├── mysite/                    # Diretório de configurações do projeto
    │   ├── settings.py            # Configurações gerais
    │   ├── urls.py                # Rotas principais
    │   └── ...
    └── polls/                     # Aplicação de enquetes
        ├── models.py             # Definição dos modelos (Pergunta e Opção)
        ├── views.py              # Lógica das views
        ├── urls.py               # Rotas da aplicação
        └── admin.py              # Registro de modelos no admin
```

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/Django-Python-Web.git
cd Django-Python-Web-main/mysite
```

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**

```bash
pip install django
```

4. **Aplique as migrações:**

```bash
python manage.py migrate
```

5. **(Opcional) Crie um superusuário:**

```bash
python manage.py createsuperuser
```

6. **Inicie o servidor de desenvolvimento:**

```bash
python manage.py runserver
```

> Acesse: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Funcionalidades

- Cadastro e gerenciamento de enquetes no admin
- Listagem de perguntas ativas
- Votação em opções
- Visualização de resultados

---

## 🔐 Acesso ao Painel Administrativo

Após criar um superusuário, acesse:

[http://localhost:8000/admin](http://localhost:8000/admin)

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Sinta-se livre para usar, estudar e modificar!

---

## 🙋 Sobre

Este projeto tem fins educacionais e serve como base para aprender os fundamentos de aplicações web com Django.
