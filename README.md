# Test CI/CD Repository

Questo repository è utilizzato per testare e sperimentare con GitHub Actions, il sistema di automazione e CI/CD integrato in GitHub.

## Struttura del Repository

```
.github/
  └── workflows/          # Directory per i file di configurazione delle GitHub Actions
src/                     # Directory per il codice sorgente
tests/                   # Directory per i test
```

## GitHub Actions

Le GitHub Actions sono uno strumento di automazione che permette di:
- Eseguire test automatici
- Fare build automatiche
- Fare deploy automatici
- Automatizzare qualsiasi processo di sviluppo

I workflow sono definiti in file YAML nella directory `.github/workflows/`.

## Come Iniziare

1. I workflow possono essere attivati da vari eventi:
   - Push su un branch
   - Pull request
   - Release
   - Schedule (cron jobs)
   - Eventi manuali (workflow_dispatch)

2. Per creare un nuovo workflow:
   - Crea un nuovo file `.yml` nella directory `.github/workflows/`
   - Definisci gli eventi trigger
   - Configura i job e i step necessari

## Note

Questo repository è utilizzato per scopi di test e apprendimento delle GitHub Actions. 