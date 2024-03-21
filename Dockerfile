FROM python:3.9
ADD main.py .
ADD matrix_mult.py .
CMD ["python", "./main.py"]