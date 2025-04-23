# OpenAI API Integration

A simple FastAPI application that integrates with the OpenAI API to process text messages and get AI-generated responses.

## Features

- REST API endpoint for processing text messages
- Integration with OpenAI's GPT models
- Simple JSON-based request/response format

## Setup

1. Clone the repository
   ```
   git clone <repository-url>
   cd test-conversation-pipeline
   ```

2. Create a virtual environment and install dependencies
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Running the Application

Start the FastAPI server:
```
uvicorn main:app --reload --port 8080
```

The API will be available at `http://localhost:8080`.

## API Usage

### Process Text Endpoint

**Endpoint:** `POST /process`

**Request Body:**
```json
{
  "message": "Your text message here"
}
```

**Response:**
```json
{
  "response": "AI-generated response here"
}
```

## Testing

You can test the API using the included test script:
```
python test_api.py
```

Or with curl:
```
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello, how are you?"}' http://localhost:8080/process
``` 