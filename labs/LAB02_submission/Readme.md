# Lab 2 Submission README

## Student Information
- Name: Lewis Campbell
- Date: [2026-03-31]

## Deliverables Included
- `inference_api/Dockerfile`
- `preprocessor/Dockerfile`
- `inference_api/app.py` (with `/health` and `/stats`)
- `sample_classifications_20.jsonl` (first 20 lines from logs)
- `Reflection.md`

## Docker Build Commands Used

### Inference API
```bash
docker build -t inference-api ./labs/LAB02_submission/inference_api
```

### Preprocessor
```bash
docker build -t preprocessor ./labs/LAB02_submission/preprocessor
```

## Docker Run Commands Used

### Inference API Container
```bash
docker run -d --name inference-api -p 8000:8000 -v $(pwd)/logs:/logs inference-api
```

### Preprocessor Container
```bash
docker run -d --name preprocessor -v $(pwd)/incoming:/incoming -e API_URL=http://host.docker.internal:8000 preprocessor

```

## Brief Explanation: How the Containers Communicate
The preprocessor docker container calls the inference API's "predict" endpoint by sending an http request with each new product image it detects. We tell it where to send this http request using the 'API_URL' variable. Images persist on the host through a volume mount to 'incoming', and the classification logs persist through a volume mount to 'logs'. That way, our data survives even if the containers are stopped for some reason. The reason `localhost` can be tricky inside containers is because each container has its own isolated network, so when we use the term 'localhost', it will refer to the container, not the machine, so the preprocessor will be unable to reach the port outside itself without using `host.docker.internal`. Alternatively we could also put both containers on the Docker network and the would be able to communicate through that.

Points to cover:
- Which container calls which endpoint.
- How the preprocessor knows where to find the inference API.
- How images and logs persist using mounted host folders.
- Why `localhost` can be tricky inside containers.

