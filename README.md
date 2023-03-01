create conda environment
"""
conda create -p venv python==3.7 -y

here -p means that venv will be created in the same project file and once we delete the project file 
the venv file also be deleted

-y means we accept all the condition

"""

activate venv the command is
"""
conda activate venv
       or
conda activate venv/
"""

install libraries
"""
pip install -r requirements.txt

"""

add file to github
```
if we want to add file with file name command is
git add file1
git add file2 file3 filen
if we want to add all the udated file and new file command is
git add .

```
how to check the created file is add to git or not command is
```
git status

it will tell us about the the file which is modified and which one is untracked

```
next is to commit the changes which will create version
```
git commit -m "message"
```
to see all the version available in git the command is
```
git log

```
to send changes /version to git command is
```
git push origin main
```
to check remote url
```
git remote -v

```
to check the branch of project
```
git branch

```
To setup CI/CD pipeline we need three information here
```
1.heroku_emailid = shinning.prakash@gmail.com
2.heroku_API_key = 78d95231-ef6d-4f22-870a-334fca41d151
3.heroku_app_name = flaskapp0101  

```
BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> .(comment: here . means location of docker file if it is located in same folder we write .)

```
note: image name for docker must be in lower case / tag name can be any thing you want

To list docker image command will be
```
docker images

```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image id>
here p means port number e means environment variable

```
to check running container in docker command is
```
docker ps

```
To stop docker container
```
docker stop <container_id>

```
Machine learning project
'''
here housing is the root folder where all the files and folders for the project resides
setup.py file is same as pip install -r requirements .txt
we do it by  "python setup.py install"

```
-e . will install all the libraries or packages in housing folder where ever there is  __init__ file 

so in requirements.txt file we mention -e . which will install internal packages.

```
install ipykernel
```
pip install ipykernel

```
```
any helper function we will write in util file like how to make pickle object
or how to load a model from pickle object
```


