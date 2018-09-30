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

## Next steps
* [User guide](https://github.com/Cyberlander/ActiveLearningPlatform/blob/master/docs/user_guide.md)
* [Installation/Admin guide](https://github.com/Cyberlander/ActiveLearningPlatform/blob/master/docs/installation_admin_guide.md)
* [Docker-based installation](https://github.com/Cyberlander/ActiveLearningPlatform/blob/master/docs/docker_based_installation.md)
