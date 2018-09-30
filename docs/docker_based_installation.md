## Docker-based installation
* make sure git is installed on your system
  * ```sudo apt-get update```
  * ```sudo apt-get install git-core```
* make sure python 3.5 is installed on your system
  * ```sudo apt-get install python3```
* make sure docker is installed on your system
  * [Get Docker CE for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* clone the repository
  * ```git clone https://github.com/Cyberlander/ActiveLearningPlatform```
* change to the repository containing the dockerfile
  * ```cd ActiveLearningPlatform/ProjektSprachverarbeitung```
* build the dockerfile
  * ```sudo docker build -t felixf/active-learning-platform .```
* run the dockerfile
  * ```sudo docker run -it -p 8000:8000 felixf/active-learning-platform```
