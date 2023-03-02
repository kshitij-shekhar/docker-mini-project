from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def root():
    return [{
        'name':'Kshitij',
        'email':'kshitij.s@ahduni.edu.in'
        }]
