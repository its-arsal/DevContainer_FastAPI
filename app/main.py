from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Root"])
async def get_root():
    return {"message": "Welcome to FastAPI !"}


# Get item

# Add item

# Modify item

# Delete item
