## User guide
Open an web browser and type ```0.0.0.0:8000``` into the browser address bar
Now you should see the following web page:
![alt text](https://github.com/Cyberlander/ActiveLearningPlatform/blob/master/images/start_page.png "Logo Title Text 2")
### Get a comment
When you open the page for the first time there isn't any comment loaded yet.
Click on the blue button in the middle of the page to retrieve a new comment.

### Label a comment
Below the actual comment you will find three litte buttons with good, neutral and
bad on it.  Use them to label the comment. You will see that the border of the
comment will change according to the label.

### Save the labeled comment to database
If you have labeled a comment as described in the section above,
there appears another blue button in the middle  with the text "Save labeled comment".
Press it to store the comment in the backend table and retrieve another unlabeled one.

### Show the predictions of the neural network
Click on "show estimator predictions" to see the neural network outputs for the
three possible labels.

### See database statistics
You can see some statistics when you click on the left link "show database statistics".
This will open an bootstrap modal with some entries.
You can see how many unlabeled comments are in the corresponding table. It also shows
you how many comments are staging area, waiting for a user to be labeled. The third
entry shows you how many comments are already labeled by users.

### Fill staging area
The staging area is the table, where the comments are stored which have more value
for neural network training because it is unsure about them. You can fill it by hand
if you click on the corresponding text. This will start the selection process where
the neural network looks at 100 unlabeled comments and stores the most promising of them
in the staging area.

### Train neural network
This will give a background task to the scheduler which will train the network
on the new labeled comments.
