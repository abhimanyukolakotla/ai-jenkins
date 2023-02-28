from fastapi import FastAPI
import os
from os.path import join, dirname
from dotenv import load_dotenv
import jenkins

load_dotenv()  # take environment variables from .env.

app = FastAPI()

<<<<<<< HEAD
server = jenkins.Jenkins('http://165.232.184.155:31001', username='testuser', password='123456')
=======
url = os.environ.get('JENKINS_URL')

server = jenkins.Jenkins(url, username=os.environ.get('USER_NAME'), password=os.environ.get('PASSWORD'))
>>>>>>> 1b816a8e156da56c9465d7e4e13409decfe417e2
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

@app.post("/build/{job}")
async def build_job(job: str, params: dict = None):
    return server.build_job(job, params)

@app.get("/buildInfo/{job}/{build}")
async def build_info(job: str, build: int):
    info = server.get_build_info(job, build)
    return info;

@app.get("/stopBuild/{job}/{build}")
async def stop_build(job: str, build: int):
    return server.stop_build(job, build)

@app.get("/lastStableBuild/{job}")
async def build_info(job: str):
    info = server.get_job_info(job)['lastStableBuild']
    return info;

@app.get("/artifact/{job}/{build}")
async def build_info(job: str, build: int):
    artifacts = server.get_build_info(job, build)["artifacts"]
    if (len(artifacts) > 0): 
        return '%s/job/%s/%s/artifact/%s' %(url, job, build, artifacts[0]['relativePath'])
    else :
        return '';

