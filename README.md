# Active Learning Platform
This project is a  Django full stack web application with the focus on active learning.

## What is active learning?
Active learning is a process to train machine learning algorithms more efficiently.
In the first step a pre-trained machine learning algorithm predicts
probabilities for unlabeled data points. These predictions give an insight about
how sure the algorithm is about a specific data point. This gives us the the
opportunity to preselect these data points and label them. The machine learning algorithm
learns more from these data points.

## How does it work on this concrete platform?
The backend of this web application offers a REST API for interaction with the server.
There is a SQLite database with 3 tables. The largest table contains 100 000 unlabeled
comments which is a subset of the [One Million Posts Corpus](https://ofai.github.io/million-post-corpus/),
which are user comments submitted on an Austrian newspaper website. The second table
contains all the comments which are labeled by the user of this platform. Between
them there is the so called Staging table. This table contains comments about which
the machine learning algorithm is unsure about. The frontend gets its data from
this staging table.

## How to start the platform without docker?
### Windows
* make sure git is installed on your system
* make sure python 3.5 is installed on your system
* clone the repository
  * ```git clone https://github.com/Cyberlander/ActiveLearningPlatform```
* download the german word embeddings word to vec from [this site](http://cloud.devmount.de/d2bc5672c523b086/german.model)
* place the file german.model in this location: ProjektSprachverarbeitung/resources/word2vec
* change into the ProjektSprachverarbeitung root directory and install the python requirements
  * ```pip install -r requirements.txt```
* start the queue for the background tasks:
  * ```python manage.py process_tasks```
* start the platform:
  * ```python manage.py runserver```

## User Manual
Open an web browser and type ```localhost:8000``` into the browser address bar
Now you should see the following web page:
### Get a comment
When you open the page for the first time there isn't any comment loaded yet.
Click on the blue button in the middle of the page to retrieve a new comment.

### Label a comment
Below the actual comment you will find three litte buttons with good, neutral and
bad on it.  Use them to label the comment. You will see that the border of the
comment will change according to the label. Now there appears another blue button
in the middle "Save labeled comment". Press it to store the comment in the backend
table and retrieve another unlabeled one.

### See database statistics