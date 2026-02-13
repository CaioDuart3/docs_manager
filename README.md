# 🚀 Docs Manager

> Gestão inteligente de documentos: controle total sobre arquivos de qualquer extensão com uma camada colaborativa de comentários e gestão de privilégios de acesso

<div align="center">
    <img width=200px src="docs_manager\static\img\logotipo_fundo.svg"/>
</div>

<p align="center">Figura 1: Logo da Aplicação.</p>

## 📋 Sobre o Projeto

O projeto utiliza a arquitetura monolítica do Django para gerenciar o ciclo de vida de documentos e comentários, oferecendo uma interface intuitiva e níveis de acesso distintos para diferentes perfis de usuários.

### Funcionalidades Principais

* **Gestão de Acesso:** Autenticação para Superusuários e Usuários Comuns com restrições de permissões baseadas em perfil.
* **Painel Administrativo:** Interface de gerenciamento de usuários exclusiva para Superusuários.
* **Módulo de Documentos:** Listagem, upload, download, remoção e buscador integrado de arquivos.
* **Interatividade:** Sistema de criação e listagem de comentários em documentos.

## 🛠️ Tecnologias Utilizadas

* **Python 3.12** (Back-end)
* **Django 6.0.2** (Framework Back-end)
* **SQLite3** (Banco de dados)
* **HTML5, CSS3 e JavaScript** (Front-end)

---

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente de desenvolvimento em sua máquina.

### 1. Clonar o Repositório

```bash
git clone https://github.com/CaioDuart3/docs_manager
cd docs_manager

```

### 2. Configurar o Ambiente Virtual

```bash
# Criar o ambiente
python -m venv venv

# Ativar o ambiente (Windows)
venv\Scripts\activate

# Ativar o ambiente (Linux/macOS)
source venv/bin/activate

```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt

```

### 4. Configurações Iniciais (.env)

Crie um arquivo `.env` na raiz do projeto seguindo o modelo abaixo:

```env
# Chave secreta do Django
# Gere uma nova com: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY=sua-secret-key-aqui

# Configurações de Ambiente
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

```

### 5. Migrações e Superusuário

```bash
# Criar as tabelas no banco de dados
python manage.py migrate

# Criar administrador para gerenciar o sistema
python manage.py createsuperuser

```

### 6. Iniciar o Servidor

```bash
python manage.py runserver

```

O projeto estará disponível em `http://127.0.0.1:8000`.

---

## 📂 Estrutura de Pastas

```text
└─ docs_manager          // Raiz do projeto
    ├─ apps              // Módulos da aplicação
    │  ├─ documents      // Gestão de documentos e comentários
    │  │  ├─ static      // Assets específicos do app
    │  │  └─ templates   // Telas de documentos
    │  └─ users          // Gestão de usuários e autenticação
    │     └─ templates   // Telas de login/usuários
    ├─ docs_manager      // Configurações centrais do Django (Settings/URLs)
    └─ static            // Estilização e assets globais
        ├─ css
        └─ img

```

---

**Desenvolvido com ☕ por **Caio Duarte**