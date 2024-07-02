FROM python:3.11

WORKDIR /app

RUN pip install flake8==3.9.2 flake8-import-order==0.18.1 \
    flake8-polyfill==1.0.2 pep8-naming==0.11.1

COPY ./ /app/

CMD ["flake8", ".", "--exclude=.venv,venv,__pycache__,*/alembic/versions/*"]