from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(string: str = "Hello World"):
    """
    This is a simple API that returns a string, its reverse, its length and whether it is a palindrome or not.
    """
    return {
        "string": string,
        "reverse": string[::-1],
        "length": len(string),
        "is_palindrome": string == string[::-1],
    }
