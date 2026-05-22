# Personal Journal API

API REST desenvolvida com Django REST Framework utilizando autenticação JWT, permissões customizadas e controle de acesso por usuário.

---

# Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite
- Postman
- Git/GitHub

---

# Funcionalidades

- Cadastro de usuários
- Login com JWT
- Refresh Token
- Logout com blacklist
- CRUD completo de entradas do diário
- Rotas protegidas com autenticação
- Permissão para acessar apenas os próprios dados
- Rotas públicas
- Sistema de grupos (`Editor`)
- Endpoint `/api/auth/me/`

---

# Estrutura do Projeto

```bash
personal-journal-api/
│
├── accounts/
├── journal/
├── core/
├── venv/
├── manage.py
└── db.sqlite3
```

---

# Instalação

## 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/personal-journal-api.git
```

---

## 2. Entrar na pasta

```bash
cd personal-journal-api
```

---

## 3. Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

# Instalar dependências

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
```

---

# Rodar migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Criar super usuário

```bash
python manage.py createsuperuser
```

---

# Rodar servidor

```bash
python manage.py runserver
```

Servidor:

```text
http://127.0.0.1:8000/
```

---

# Endpoints

## Registro

### POST

```text
/api/auth/register/
```

### Body

```json
{
  "username": "maria",
  "email": "maria@email.com",
  "password": "senha1234"
}
```

---

# Login JWT

### POST

```text
/api/auth/login/
```

### Body

```json
{
  "username": "maria",
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

# Usuário logado

### GET

```text
/api/auth/me/
```

### Header

```text
Authorization: Bearer TOKEN
```

---

# Criar entrada

### POST

```text
/api/entries/
```

### Header

```text
Authorization: Bearer TOKEN
```

### Body

```json
{
  "title": "Minha primeira entrada",
  "content": "Hoje aprendi JWT",
  "mood": "happy",
  "is_public": true
}
```

---

# Listar entradas

### GET

```text
/api/entries/
```

---

# Entradas públicas

### GET

```text
/api/journal/public/
```

---

# Logout

### POST

```text
/api/auth/logout/
```

### Body

```json
{
  "refresh": "TOKEN_REFRESH"
}
```

---

# Segurança

O projeto utiliza:

- JWT Authentication
- IsAuthenticated
- Permissões customizadas
- Controle por proprietário (`IsOwner`)
- Groups do Django
- Blacklist de tokens

---

# Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

- APIs REST
- Autenticação JWT
- Django REST Framework
- Relacionamentos com User
- CRUD protegido
- Permissões e autorização
- Serializers
- ViewSets
- Rotas protegidas
- Git e GitHub

---

# Autor

Victor Laranjeira