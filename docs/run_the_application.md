## Run the application
* make sure git is installed on your system
* make sure python 3.5 is installed on your system
* make sure docker is installed on your system
* clone the repository
  * ```git clone https://github.com/Cyberlander/ActiveLearningPlatform```
* change to the repository containing the dockerfile
  * ```cd ActiveLearningPlatform/ProjektSprachverarbeitung```
* build the dockerfile
  * ```sudo docker build -t felixf/active-learning-platform .```
* run the dockerfile
  * ```sudo docker run -it -p 8000:8000 felixf/active-learning-platform```
