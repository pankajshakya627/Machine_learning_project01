# Machine_learning_project01
My First Machine Learning Project

Requirements:

1. Github Account
2. Heroku accunt
3. VS Code IDE 
4. GIT cli


Creating conda environment
```
conda create -p venv python==3.7 -y
````
Activate the virtual environment
```
conda activate venv/
```
OR
```
conda activate venv
```
Once the environment is activated, you can install the dependencies using the following command:

```
pip install -r requirements.txt
```

> Note: To ignore file and folder from git we can write name of the folder/files in .gitignore file.

To ckeck the git status:
```
git staus
```
To create version/commit all changes by git:
```
git commit -m "message"
```
TO send/version changes to github:
```
git push origin main
```
To remove url from github:
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 ingredients:
1. Mail id of the user
2. HEROKU_API_KEY =  13af1ef-4abb-4658-a6be-e487342ab5d8
3. HEROKI_APP_NAME = machine-learning-project01

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be in lowercase.

To list docker images:
```
docker images
```

To remove the docker image:
```
docker rmi <image_name>:<tagname>
```
Run the docker image:
```
docker run -p <port_number>:<port_number> <image_name>:<tagname>
docker run -p 5000:5000 -e PORT=5000 image_id
```
To check the status of the docker image:
```
docker ps
```

To stop the docker container:
```
docker stop <container_id>
``` 

```
python setup.py install
```