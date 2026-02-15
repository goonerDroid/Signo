import os
import base64
import json
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=OPENAI_API_KEY)

# --------------------------------------------------
# FastAPI Setup
# --------------------------------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Health Check
# --------------------------------------------------


@app.get("/")
def health_check():
    return {"status": "Signo backend running"}

# --------------------------------------------------
# Analyze Endpoint
# --------------------------------------------------


@app.post("/analyze")
async def analyze_sign(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        if not contents:
            raise HTTPException(status_code=400, detail="Empty file uploaded")

        base64_image = base64.b64encode(contents).decode("utf-8")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """
You are an AI that analyzes signboard images.

Perform the following tasks:
1. Extract the exact visible text from the sign.
2. Detect the language.
3. Translate it to English.
4. If relevant to Quebec (Canada), explain any cultural or legal context.
5. Provide a confidence score between 0 and 1.

Return strictly valid JSON in this format:

{
  "extracted_text": "",
  "detected_language": "",
  "translation": "",
  "quebec_context": "",
  "confidence": 0.0
}
"""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=500,
        )

        raw_content = response.choices[0].message.content.strip()

        print("🔎 Raw Model Output:\n", raw_content)  # Debug log

        # --------------------------------------------------
        # Remove markdown code fences if present
        # --------------------------------------------------

        if raw_content.startswith("```"):
            raw_content = raw_content.replace("```json", "")
            raw_content = raw_content.replace("```", "")
            raw_content = raw_content.strip()

        try:
            result_json = json.loads(raw_content)
        except json.JSONDecodeError as e:
            raise HTTPException(
                status_code=500,
                detail=f"JSON parsing failed: {str(e)}"
            )

        return result_json

    except HTTPException as http_error:
        raise http_error

    except Exception as e:
        print("❌ Internal Error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# Optional Direct Run
# --------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
