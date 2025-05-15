# 🎬 Movie Stats Shiny App

This is a beginner-friendly Shiny app built in Python that allows you to explore a dataset of 10,000 movies from Letterboxd. You can filter the films by title and original language to see detailed statistics like release year, genres, runtime, ratings, and more.

## 🔍 Features

- Filter movies by title and original language
- Displays top 50 matching results
- Simple interactive table layout
- Built using [Shiny for Python](https://shiny.posit.co/py/) and `pandas`

## 📁 Project Structure

- `app.py` – The main Python file running the Shiny app
- `Movie_Data_File.csv` – The dataset used in the app

## 🚀 How to Run Locally

1. **Install Python 3.10+**
2. **Install required libraries**

Run the app 
shiny run --reload app.py

Open your browser and visit the localhost 

The app will automatically reload if you make changes to the code.

About This Project

This project was created as part of my learning journey in data storytelling and analytics. I’m exploring tools like Shiny, Streamlit, Power BI, and AI to make data more accessible and engaging. This app showcases how simple interactivity can bring a dataset to life, even as a beginner 

## My Approach 

In this project, I wanted to create a simple web app using Shiny in Python that allows users to filter and explore movie data. I started by loading the movie data from a CSV file using pandas.read_csv(). This is a straightforward way to work with data in Python, and since I was working with a file, it made sense to use this method to get everything into the app.

Once I had the data, I cleaned up the column names using str.strip() to remove any extra spaces. This ensures that I don’t run into errors when referencing column names later in the code.

For the filtering options, I focused on three main criteria: movie title, language, and director. I created the dropdown lists by selecting the unique values from each column in the dataset. First, I used dropna() to remove any missing data, then unique() to get distinct values. To make it easier for users, I sorted the options alphabetically using sorted(). I also added a "Show All" option to each dropdown so that users could reset their filter if they wanted to see the entire dataset again.

The filtering itself happens in the server() function. For each dropdown, I check if the user has selected a specific option or "Show All". If they chose something other than "Show All", I filter the data to match that selection. I also added a search box where users can search for movie titles, applying this filter if there’s text in the search input.

Finally, I wanted to make sure the user experience was smooth, so I displayed the filtered data in a table, showing only the top 50 results to avoid overwhelming the user with too many rows at once.

Overall, I wrote the code this way to make it easy for anyone to interact with and explore the movie data. It’s a straightforward approach that lets users filter and search based on their preferences, while keeping things simple and efficient.

```bash

