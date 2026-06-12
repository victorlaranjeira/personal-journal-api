# Personal Journal API

API REST desenvolvida com Django REST Framework para gerenciamento de entradas de diário, utilizando autenticação JWT, PostgreSQL em produção e deploy no Render.

## 🚀 Demonstração Online

### API Publicada

https://personal-journal-api-v08h.onrender.com

### Endpoint Público

https://personal-journal-api-v08h.onrender.com/api/journal/public/

### Repositório GitHub

https://github.com/victorlaranjeira/personal-journal-api

---

# 🛠 Tecnologias Utilizadas

- Python 3
- Django 6
- Django REST Framework
- JWT Authentication (SimpleJWT)
- PostgreSQL
- Render
- Gunicorn
- WhiteNoise
- Git
- GitHub
- Postman

---

# 📋 Funcionalidades

- Cadastro de usuários
- Login com JWT
- Refresh Token
- Endpoint de usuário autenticado
- CRUD de entradas do diário
- Rotas públicas e privadas
- Controle de permissões por usuário
- Deploy em produção
- Banco PostgreSQL hospedado no Render

---

# 📂 Estrutura do Projeto

```bash
personal-journal-api/
│
├── accounts/
├── journal/
├── core/
├── manage.py
├── requirements.txt
├── build.sh
├── README.md
└── .env
```

---

# ⚙️ Instalação Local

## Clonar o projeto

```bash
git clone https://github.com/victorlaranjeira/personal-journal-api.git
```

```bash
cd personal-journal-api
```

## Criar ambiente virtual

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar migrações

```bash
python manage.py migrate
```

## Criar superusuário

```bash
python manage.py createsuperuser
```

## Executar servidor

```bash
python manage.py runserver
```

Servidor local:

```text
http://127.0.0.1:8000
```

---

# 🔗 Endpoints

## Registro

### POST

```text
/api/auth/register/
```

### Body

```json
{
  "username": "teste",
  "email": "teste@email.com",
  "password": "senha1234"
}
```

---

## Login JWT

### POST

```text
/api/auth/login/
```

### Body

```json
{
  "username": "teste",
  "password": "senha1234"
}
```

### Resposta

```json
{
  "refresh": "TOKEN_REFRESH",
  "access": "TOKEN_ACCESS"
}
```

---

## Usuário autenticado

### GET

```text
/api/auth/me/
```

### Header

```text
Authorization: Bearer TOKEN_ACCESS
```

---

## Criar entrada

### POST

```text
/api/entries/
```

### Header

```text
Authorization: Bearer TOKEN_ACCESS
```

### Body

```json
{
  "title": "Minha primeira entrada",
  "content": "Hoje aprendi JWT no Django",
  "mood": "happy",
  "is_public": true
}
```

---

## Listar entradas do usuário

### GET

```text
/api/entries/
```

---

## Entradas públicas

### GET

```text
/api/journal/public/
```

---

# 🧪 Testes Realizados em Produção

### Cadastro Online

Usuário criado com sucesso através da API hospedada no Render.

### Login JWT

Token de acesso e refresh gerados corretamente.

### Autenticação

Validação realizada através do endpoint:

```text
/api/auth/me/
```

Retornando os dados do usuário autenticado.

### Endpoint Público

A rota:

```text
/api/journal/public/
```

retorna HTTP 200 OK em produção.

---

# ☁️ Deploy

O projeto foi publicado utilizando:

- Render Web Service
- PostgreSQL Render
- Gunicorn
- WhiteNoise
- Variáveis de ambiente

### Build Command

```bash
./build.sh
```

### Start Command

```bash
gunicorn core.wsgi:application
```

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

- APIs REST
- Django REST Framework
- JWT Authentication
- Serializers
- ViewSets
- Permissões customizadas
- PostgreSQL
- Deploy em produção
- Variáveis de ambiente
- Git e GitHub
- Integração com Render

---

# 👨‍💻 Autor

**Victor Laranjeira**

GitHub:
https://github.com/victorlaranjeira

LinkedIn:
https://www.linkedin.com/in/victorlaranjeira