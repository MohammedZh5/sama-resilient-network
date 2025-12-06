from fastapi import FastAPI, HTTPException
import time
import random
import logging

app = FastAPI()

# Very simple mock DB connection simulation
def process_transaction(amount):
    # Chaos simulation: random delay or failure
    if random.random() < 0.1:
        raise ConnectionError("DB connection failed")
    
    # Business logic
    return {"status": "approved", "amount": amount, "timestamp": time.time()}


@app.get("/transfer")
def transfer(amount: float):
    attempts = 3
    for i in range(attempts):
        try:
            result = process_transaction(amount)
            logging.info(f"Transaction processed on attempt {i+1}")
            return result

        except Exception as e:
            logging.warning(f"Retry {i+1}: {e}")
            time.sleep(1 * (i + 1))

    logging.error("Transaction service unreachable after retry attempts.")
    raise HTTPException(status_code=503, detail="Service unavailable")

