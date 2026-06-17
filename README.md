# Desafio - b2bflow

Le contatos cadastrados no Supabase e envia mensagens personalizadas usando a Z-API.

## Setup da tabela (Supabase)

Execute no **SQL Editor** do seu projeto Supabase:

```sql
CREATE TABLE contacts (
  id    SERIAL PRIMARY KEY,
  name  TEXT NOT NULL,
  phone TEXT NOT NULL
);

INSERT INTO contacts (name, phone) VALUES
  ('Joao',  '5541999990001'),
  ('Maria', '5541999990002'),
  ('Pedro', '5541999990003');
```

> O campo `phone` deve conter apenas dígitos, incluindo código do país e DDD.
> Exemplo: `5541999990001` = Brasil (55) + DDD (41) + numero (999990001).

## Variaveis de ambiente

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

| Variavel            | Onde encontrar                                    |
|---------------------|---------------------------------------------------|
| `SUPABASE_URL`      | Supabase -> Settings -> API -> Project URL        |
| `SUPABASE_KEY`      | Supabase -> Settings -> API -> anon public key    |
| `ZAPI_INSTANCE_ID`  | Z-API -> sua instancia -> ID da instancia         |
| `ZAPI_TOKEN`        | Z-API -> sua instancia -> Token                   |
| `ZAPI_CLIENT_TOKEN` | Z-API -> Seguranca -> Security Token              |


## Como rodar

```bash
pip install -r requirements.txt
python3 main.py
```
