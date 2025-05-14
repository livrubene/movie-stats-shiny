import pandas as pd
from shiny import App, ui, render

df = pd.read_csv("Movie_Data_File.csv")
df.columns = df.columns.str.strip()

df = df[['Film_title', 'Director', 'Average_rating', 'Description', 'Original_language', 'Spoken_languages', 'Watches', 'Likes', 'Fans']].dropna()

movie_titles = ["Show All"] + df['Film_title'].unique().tolist()
languages = ["Show All"] + sorted(df['Original_language'].unique().tolist())
directors = ["Show All"] + sorted(df['Director'].dropna().unique().tolist())

app_ui = ui.page_fluid(
    ui.h2("Movie Stats by Title, Language, and Director"),
    ui.Tag("div", {"style": "display: flex; justify-content: flex-start; gap: 15px; align-items: center;"},
        ui.input_select("title", "Select a Movie", choices=movie_titles),
        ui.input_select("language", "Select Language", choices=languages),
        ui.input_select("director", "Select Director", choices=directors)
    ),
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
        
        if input.director() != "Show All":
            filtered_df = filtered_df[filtered_df["Director"] == input.director()]
        
        return filtered_df.head(50)

app = App(app_ui, server)
