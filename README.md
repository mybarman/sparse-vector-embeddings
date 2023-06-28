# README

## Introduction
This codebase includes a FastAPI application that exposes an API to convert text into sparse embeddings.

It makes use of:
- Transformers library to load pretrained models and tokenizers
- Pydantic for data validation
- FastAPI for creating a web API
- Splade for creating sparse representations of text
- Pinecone for managing sparse values

## Usage
After installing all the necessary packages, you can start the FastAPI server by running:

```bash
uvicorn main:app --reload
```

You can then access the application at http://localhost:8000.

For calculating embeddings for a given text, make a POST request to http://localhost:8000/calculate-embeddings with a JSON payload like the following:

```json
{
  "text": "your text here"
}
```

The response will contain the sparse representation of your text as computed by the pretrained model.

Please note that the server and the endpoint paths may vary depending on your setup.

## Limits
SPLADE supports only 512 tokens at a time.

## Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request.

