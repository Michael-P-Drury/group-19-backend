from ollama import AsyncClient
import time
from cerebras.cloud.sdk import AsyncCerebras
import os
from dotenv import load_dotenv

load_dotenv()


async def invoke_genai(prompt, model_id, temperature):

    try:
        start = time.time()
        
        client = AsyncCerebras(api_key=os.getenv('CEREBRAS_API_KEY'))

        response = await client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )

        response = response.choices[0].message.content

        end = time.time()
        time_taken = end - start

        return {'response': response, 'time_taken': time_taken}

    except Exception as e:
        print(f"A genai error occurred: {e}")

        return {'response': None, 'time_taken': None}