# tiny-fastapi-app

This is just the tiniest app, used as a demonstrator for
ACR and Python/FastAPI, which I have not used before. It 
comes with included swagger-support, unlike Flask.

build with:
docker build -t my-fastapi-app .

run with:
docker run -d --name fastapi_container -p 8000:8000 -v ${PWD}:/app my-fastapi-app uvicorn app:app --host 0.0.0.0 --port 8000 --reload

OBS: --reload flag for allowing changes during dev!