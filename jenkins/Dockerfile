FROM jenkins/jenkins:lts
USER root
RUN apt-get update
RUN apt-get install -y ansible
USER jenkins
EXPOSE 80