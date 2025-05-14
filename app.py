import pandas as pd
from shiny import App, ui, render

# Load the data and clean up column names
df = pd.read_csv("Movie_Data_File.csv")
df.columns = df.columns.str.strip()  # Strip any extra spaces from column names

# Define constants for column names – makes it easier to update later if needed
FILM_TITLE = "Film_title"
LANGUAGE = "Original_language"
DIRECTOR = "Director"

# Get unique options for the dropdowns
movie_titles = ["Show All"] + df[FILM_TITLE].dropna().unique().tolist()
languages = ["Show All"] + sorted(df[LANGUAGE].dropna().unique().tolist())
directors = ["Show All"] + sorted(df[DIRECTOR].dropna().unique().tolist())

# Create the UI – three dropdowns for filtering and a table to display the results
app_ui = ui.page_fluid(
    ui.h2("Movie Stats by Title, Language, and Director"),
    ui.row(
        ui.column(2, ui.input_select("title", "Select a Movie", choices=movie_titles)),
        ui.column(2, ui.input_select("language", "Select Language", choices=languages)),
        ui.column(2, ui.input_select("director", "Select Director", choices=directors)),
        ui.column(2, ui.input_text("search", "Search Movie Title"))
    ),
    ui.output_table("movie_table"),
    ui.tags.style("""
        table {
            width: 100%;
            text-align: center;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
    """)
)

def server(input, output, session):
    # Set up the server to handle the filters and display the table
    @output
    @render.table
    def movie_table():
        # Start with the whole dataset
        filtered_df = df

        # Apply filters one by one – we check if the user picked anything other than "Show All"
        filters = [
            (FILM_TITLE, input.title()),
            (LANGUAGE, input.language()),
            (DIRECTOR, input.director())
        ]

        for column, value in filters:
            if value != "Show All" and value:  # Only apply if the user selected a value
                filtered_df = filtered_df[filtered_df[column] == value]
        
        # If there’s a search term, filter by film title
        if input.search():
            filtered_df = filtered_df[filtered_df[FILM_TITLE].str.contains(input.search(), case=False, na=False)]
        
        # Return the top 50 results to avoid overwhelming the user
        return filtered_df.head(50)

# Set up the app with the UI and server logic
app = App(app_ui, server)

