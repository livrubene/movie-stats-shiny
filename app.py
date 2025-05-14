import pandas as pd
from shiny import App, ui, render

df = pd.read_csv("Movie_Data_File.csv")

df.columns = df.columns.str.strip()

movie_titles = ["Show All"] + df['Film_title'].dropna().unique().tolist()  
languages = ["Show All"] + sorted(df['Original_language'].dropna().unique().tolist())

df = df.drop(columns=['Cast'])

app_ui = ui.page_fluid(
    ui.h2("Movie Stats by Title and Language"),
    ui.input_select("title", "Select a Movie", choices=movie_titles),
    ui.input_select("language", "Select Language", choices=languages),
    ui.output_table("movie_table")
)

def server(input, output, session):
    @output
    @render.table
    def movie_table():
        filtered_df = df
        
        if input.title() != "Show All":
            filtered_df = filtered_df[filtered_df["Film_title"] == input.title()]
        
        if input.language() != "Show All":
            filtered_df = filtered_df[filtered_df["Original_language"] == input.language()]
        
        return filtered_df.head(50)

app = App(app_ui, server)
