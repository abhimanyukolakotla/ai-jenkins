from fastapi import FastAPI
import jenkins

app = FastAPI()

server = jenkins.Jenkins('http://host.docker.internal:8080', username='testuser', password='123456')
user = server.get_whoami()
version = server.get_version()

@app.get("/")
async def root():
    return {"message": 'Hello %s from Jenkins %s' % (user['fullName'], version)}

@app.get("/job/all")
async def jobs():
    jobs = server.get_jobs()
    return {"jobs": jobs}

@app.get("/job/{job}")
async def job_info(job):
    job = server.get_job_info(job)
    return job

@app.get("/job/{job}/{build}")
async def build_info(job, build: int):
    info = server.get_build_info(job, build)
    return info;


