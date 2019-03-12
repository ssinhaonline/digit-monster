# Digit Monster


Digit Monster is a tool that offers easy prediction of handwritten numbers. It can be considered as a semi-productionized version of my [Digit Recognition Notebook][digit-recognition-notebook]. This project was heavily inspired by tutorials available at [PythonProgramming.net][python-programming-net-ml-tut1] and REST API in Python basics at [The Flask Mega-Tutorial][flask-mega-tutorial].

Usage:

Clone this repository:
```sh
$ git clone https://github.com/ssinhaonline/digit-monster.git
```
Use conda package manager to create environment and install dependencies. If you don't have Anaconda, you can download it [here][anaconda-download].
```sh
$ cd digit-monster
$ conda install --yes --file requirements.txt
```
Run the training module.
```sh
$ /path/to/executable/bin/python train.py
```
Wait till the execution completes. Verify the following lines in your output:
```
Epoch 1/3
60000/60000 [==============================] - 4s 68us/sample - loss: 0.2613 - acc: 0.9226
Epoch 2/3
60000/60000 [==============================] - 4s 66us/sample - loss: 0.1079 - acc: 0.9667
Epoch 3/3
60000/60000 [==============================] - 4s 65us/sample - loss: 0.0728 - acc: 0.9778
10000/10000 [==============================] - 0s 30us/sample - loss: 0.1049 - acc: 0.9664
0.10489846243094653
0.9664
Model saved at: models/digit-monster.model
```
Start your Flask server:
```sh
$ /path/to/executable/bin/flask run
```
Verify server has started with the following lines in console:
```
* Serving Flask app "digit_monster.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
POST to endpoint with CURL or Postman:
```
POST http://localhost:5000/digit-monster/v1.0/predict/
{
    "X" : [[["3D_IMAGE_ARRAY_SEE_EXAMPLE_BELOW"]]]
    "suggested_labels" : ["LABEL_ARRAY_SAME_SIZE_AS_X"]
}
```
Response format:
```
{
    "status" : "OK_OR_FAILED",
    "predicted_labels" : ["PREDICTED_LABELS"],
    "is_correct" : ["TRUE_OR_FALSE"]
}
```
  - Type some Markdown on the left
  - See HTML in the right
  - Magic


License
----

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [digit-recognition-notebook]: <https://github.com/ssinhaonline/pylot-vault/blob/master/tensor-flow/digit_recognition.ipynb>
   [python-programming-net-ml-tut1]: <https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/>
   [flask-mega-tutorial]: <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>
   [anaconda-download]: <https://www.anaconda.com/distribution/>
   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
