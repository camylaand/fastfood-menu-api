#  O Sabor Express

Uma API desenvolvida com **FastAPI** para consulta de cardápios de restaurantes fast-food como McDonald’s, Burger King, KFC, Pizza Hut, Wendy’s e outros.

Os dados são coletados a partir de uma fonte pública, organizados localmente em arquivos `.json` e disponibilizados por meio de uma API REST.

---

##  Funcionalidades

- Consulta de todos os cardápios disponíveis
- Filtro por restaurante específico
- Dados estruturados por `item`, `price` e `description`
- 100% local após a primeira coleta

---

##  Estrutura do Projeto

```
O-SABOR-EXPRESS/
├── app.py                  # Coleta os dados da API externa e salva localmente
├── main.py                 # API FastAPI que lê arquivos locais e responde as requisições
├── requirements.txt        # Dependências do projeto
├── .gitignore              # Arquivos e pastas ignoradas no Git
├── dados_restaurantes/     # Arquivos .json de cada restaurante
│   ├── McDonald’s.json
│   ├── Burger King.json
│   └── ...
```

---

##  Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/o-sabor-express.git
cd o-sabor-express
```

### 2. Crie o ambiente virtual e instale as dependências
```
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

### 3. Gere os dados locais (opcional)
```
python app.py
```

### 4. Rode a API
```
uvicorn main:app --reload
Acesse em: http://localhost:8000/docs
```
##  Endpoints

### `GET /api/hello`

Teste de conexão

**Resposta:**

```json
{ "Hello": "World" }
```

### `GET /api/restaurantes/`
```
Retorna todos os cardápios disponíveis
```

### `GET /api/restaurantes/?restaurante=Nome`
Retorna os itens apenas de um restaurante específico

**Exemplo:**
```bash
/api/restaurantes/?restaurante=Burger King
```
##  Requisitos

-  **Python 3.10+**
-  **FastAPI**
-  **Uvicorn**
-  **Requests**

---

## Fonte dos Dados

- Os cardápios são obtidos a partir da API pública mantida por Guilherme Lima:

- [https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json](https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json)

---

##  Autor

- Desenvolvido por **Camyla Andrade**  
- Projeto de prática com **FastAPI**
