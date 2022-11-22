# Lecture notes for SLAM experiment

The script contains preparation and description of the experiment.
The following file contains some details about the idea behind the experiments

* [README_Experiment.md](README_Experiment.md)

## Design decisions

* All scripts are using Python 2.7.
* ROS is used as framework for the experiment with the robot.
* Jupyter-Notebook is used for preparation and example code.
* the folder `rvmrt_slam_lecture_modules` contains python modules used by Jupyter Notebooks
* Clear Output before saving to avoid committing output to git
* All documents used for experiments are written in Jupyter Notebooks to have one export script for all

## How to use the lecture notes

The script is written as [Jupyter Nodebook](LectureNotes.ipynb).

    # install jupyter notebook
    sudo apt-get -y install ipython ipython-notebook
    sudo -H pip install jupyter
    sudo -H pip install bresenham

The script can be opened using the script `start_notebook.sh`. ~~The script makes sure that the outputs are cleared after
saving and the git history is clean.~~ (Not yet implemented) Please clear outputs before saving to ensure a clean git history.

Some of the scripts inside the notebook import modules defined at [rvmrt_slam_lecture_notes/lecture_modules/](rvmrt_slam_lecture_notes/lecture_modules/).

## Run lecture notes inside Docker

Build docker image:

    sudo docker build -t rvmrt_lecture_notes .

Run docker container:

    sudo docker run -it -p 8888:8888 -v "$PWD:/home/jovyan/work/" rvmrt_lecture_notes

Open notebook in brower:

When running the docker container, there is console output like the following

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://(e5baf43b57e4 or 127.0.0.1):8888/?token=f22e7c34cff8298eb3acbebd086bd7ef80b9cd21b8ecb4d6

use 127.0.0.1 as ip address.

## Design notes for valid pdf export

* Maximale Zeilenlänge von 80 Zeichen in Code-Blöcken
* Bilder
  * Bilder als png. svg funktioniert (aktuell) nicht im Export, pdf nicht im eigentlichen Dokument
  * Leerzeile nach Bild, sofern dieses nicht in Text integriert werden soll
* Keine dokumentweite Hauptüberschrift, Kapitel mit höchstwertiger Überschrift beginnen (`# Kapitelüberschrift`)

## Export notes to pdf

Preparation:

* Set `%matplotlib inline` in first block.

Export:

```
RVMRT_EXPORT='True'
jupyter nbconvert --execute Preparation.ipynb --to pdf --template rvmrt_template.tplx
```
or when using Docker:
```
sudo docker run -it -rm -v "$PWD:/home/jovyan/work/" -e RVMRT_EXPORT='True' rvmrt_lecture_notes jupyter nbconvert --execute /home/jovyan/work/Preparation.ipynb --to pdf --template /home/jovyan/work/rvmrt_template.tplx
```

### Modify export templatex

LaTeX-Template: [rvmrt_template.tplx](rvmrt_template.tplx), 
Jupyter uses pandoc and jinja2 for generating LaTeX-Code

Tutorial for customizing export: https://nbconvert.readthedocs.io/en/latest/customizing.html

Tutorial for adding citations and export to print version: https://github.com/jupyter/nbconvert-examples/blob/master/citations/Tutorial.ipynb
