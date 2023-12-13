# Proyecto de ejemplo Playwright + Pytest + Allure

Este proyecto contiene algunas pruebas sobre la sandbox de automatizacion del sitio de Practice-Automation

## Cómo probar localmente

Para probar este proyecto en tu entorno local, sigue estos pasos:

1. Clonar el repositorio a tu máquina local:

```bash
  git clone https://github.com/Gsirota01/playwright-python.git
```
2. Instalar python
    https://www.python.org/downloads/

3. Instalar dependencias y navegadores de Playwright
   ```bash
      pip install -r requirements.txt
      python -m playwright install --with-deps
   ```

4. Ejecutar las pruebas de Playwright
```bash
  pytest
```

5. Abrir el archivo de reporte de Allure
_**(Es necesario tener instalado allure)**_
```
allure serve reports/allure-results
```

## Integración con Github Actions
Si deseas ver este proyecto integrado con Github Actions o tienes alguna pregunta sobre cómo usarlo en ese entorno, te dejo mi mail a continuacion:
Correo electrónico: gabisirota@gmail.com
