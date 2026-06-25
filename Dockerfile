FROM python:3.12-slim
WORKDIR /_final_project_
COPY ./requirements.txt /_final_project_/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /_final_project_/requirements.txt
COPY ./app /_final_project_/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]