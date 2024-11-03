# Project Plan

## Title
<!-- Give your project a short title. -->
Awesome MADE project.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Does writing an example question help students write better project plans?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
XY is an important problem, because... This projects analyzes XY, using method A. The results can give insights into...

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: ExampleSource
* Metadata URL: https://mobilithek.info/offers/-6901989592576801458
* Data URL: https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv
* Data Type: CSV

Short description of the DataSource.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/made-template/issues/1



# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
