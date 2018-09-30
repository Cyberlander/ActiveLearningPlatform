## Installation/admin guide
* make sure git is installed on your system
  * ```sudo apt-get update```
  * ```sudo apt-get install git-core```
* make sure python 3.5 is installed on your system
  * ```sudo apt-get install python3```
* make sure docker is installed on your system
  * [Get Docker CE for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* clone the repository
  * ```git clone https://github.com/Cyberlander/ActiveLearningPlatform```
* change to the directory where to place the word2vec model
  * ```cd ActiveLearningPlatform/ProjektSprachverarbeitung/resources/word2vec```
* install wget if necessary
  * ```sudo apt-get install wget```
* download the german word2vec model
  * ```wget http://cloud.devmount.de/d2bc5672c523b086/german.model```
* change to the project root directory (ActiveLearningPlatform/ProjektSprachverarbeitung)
* start the background task scheduler
  * ```python3 manage.py process_tasks```
* start the background task scheduler
  * ```python3 manage.py runserver```
