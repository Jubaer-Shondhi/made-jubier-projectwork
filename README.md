# Project Plan

## Title
Analysis of police encounters in the United States

## Main Question

How do victims' age, gender, and threat level from the victim influence the frequency and outcomes of police encounters in the United States?

## Description

This project analyzes police encounters in the United States, focusing on how victims' age, gender, and perceived threat level influence the frequency and outcomes of these incidents. Despite a 1994 mandate, there remains no comprehensive federal record on police use of force, with estimates indicating 930 to 1,240 fatalities annually. Media-led databases, such as The Counted by The Guardian and The Washington Post’s tracking of police shootings, report thousands of fatalities since 2015. By examining these factors, this analysis aims to reveal patterns and contribute to informed discussions on law enforcement practices and public safety. The dataset includes over 7,700 records from 2015 to 2022, detailing victim demographics, incident circumstances, and geolocation data.

## Datasources


### Datasource1: 
* URL: https://www.kaggle.com/datasets/ramjasmaurya/us-police-shootings-from-20152022/data 
* Data Type: CSV
* Description: This dataset contains records of police shootings in the United States from 2015 to 2022. It includes details such as the date of the incident, manner of death, demographics of the individuals involved, and geographic location, providing insights into patterns and trends in police use of force.

### Datasource2: 
* Data URL: https://www.kaggle.com/datasets/ramjasmaurya/us-police-shootings-from-20152022/data 
* Data Type: CSV
* Description: This dataset includes details such as arms category,flee, body camera and providing insights into patterns and trends in police use of force.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Objective Definition and Dataset Selection
2. Data Collection and Pipeline Setup
3. Data Cleaning and Preprocessing
4. Data Analysis
5. Correlation and Trend Analysis
6. Visual Analysis
7. Reporting Findings
8. Presentation




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
