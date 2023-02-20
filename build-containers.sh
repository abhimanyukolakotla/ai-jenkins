docker build -t aidebugops-jenkins -f jenkins/Dockerfile jenkins
docker build -t aidebugops-backend -f node-jenkins/Dockerfile node-jenkins
docker build -t aidebugops-chatbot -f chatbot/Dockerfile chatbot
docker build -t aidebugops-py-backend -f py-jenkins/Dockerfile py-jenkins

docker tag aidebugops-chatbot registry.digitalocean.com/docr-dailybhajans-registry/aidebugops-chatbot
docker tag aidebugops-backend registry.digitalocean.com/docr-dailybhajans-registry/aidebugops-backend
docker tag aidebugops-jenkins registry.digitalocean.com/docr-dailybhajans-registry/aidebugops-jenkins


#docker push registry.digitalocean.com/docr-dailybhajans-registry/aidebugops-chatbot
#docker push registry.digitalocean.com/docr-dailybhajans-registry/aidebugops-backend
#docker push registry.digitalocean.com/docr-dailybhajans-registry/aidebugops-jenkins