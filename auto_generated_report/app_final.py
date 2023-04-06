# import libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import plotly.io as pio
import dash_table
import lorem
import pandas as pd
import pathlib
import pdfkit
import schedule
import datetime
import time
import os
# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

#load the data
supplyDemand = pd.read_csv(r'C:\Users\sempa\Documents\Auto_generate _report\auto_generated_report\data\supplyDemand.csv')

# create an app
app = dash.Dash(__name__)
app.title = "report generator"

fig=dcc.Graph(
        figure={
            "data": [
                go.Scatter(
                    x=supplyDemand["Demand, x"],
                    y=supplyDemand["Demand, y"],
                    hoverinfo="y",
                    line={"color": "red", "width": 1.5},
                    name="Demand",
                ),
                go.Scatter(
                    x=supplyDemand["Supply, x; Trace 2, x"],
                    y=supplyDemand["Supply, y; Trace 2, y"],
                    hoverinfo="y",
                    line={"color": "blue", "width": 1.5},
                    name="Supply",
                ),
            ],
            "layout": go.Layout(
                height=250,
                xaxis={
                    "range": [1988, 2015],
                    "showgrid": False,
                    "showticklabels": True,
                    "tickangle": -90,
                    "tickcolor": "#b0b1b2",
                    "tickfont": {"family": "Arial", "size": 9},
                    "tickmode": "linear",
                    "tickprefix": "1Q",
                    "ticks": "",
                    "type": "linear",
                    "zeroline": True,
                    "zerolinecolor": "#FFFFFF",
                },
                yaxis={
                    "autorange": False,
                    "linecolor": "#b0b1b2",
                    "nticks": 9,
                    "range": [-3000, 5000],
                    "showgrid": False,
                    "showline": True,
                    "tickcolor": "#b0b1b2",
                    "tickfont": {"family": "Arial", "size": 9},
                    "ticks": "outside",
                    "ticksuffix": " ",
                    "type": "linear",
                    "zerolinecolor": "#b0b1b2",
                },
                margin={"r": 10, "t": 5, "b": 0, "l": 40, "pad": 2},
                hovermode="closest",
                legend={
                    "x": 0.5,
                    "y": -0.4,
                    "font": {"size": 9},
                    "orientation": "h",
                    "xanchor": "center",
                    "yanchor": "bottom",
                },
            ),
        }
        # className="page-3m",
        

    )










# plot graph
def generate_plot():
    return fig


#app layout     
app.layout =  html.Div(
                    [ 
                          html.Div(
            [  
                html.Div(
                    [   
                        html.Div([html.H3("LOREM IPSUM")], className="page-2a"),
                        html.Div(
                            [    fig,
                                html.P(lorem.paragraph() , className="page-2b"),
                                html.P(lorem.paragraph() , className="page-2c"),
                                html.P(lorem.paragraph() , className="page-2c"),
                            ],
                            className="page-3",
                        ),
                        html.Div(
                            [
                                html.P(lorem.paragraph() , className="page-2b"),
                                html.P(lorem.paragraph() , className="page-2c"),
                            ],
                            className="page-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
        
                    ])
            # generate_plot()


    




# def generate_report():
    # image_file = 'graph.png'
    # pio.write_image(a, image_file)


    # # Convert the image to a PDF file and save it to a folder
    # pdf_file = 'C:/Users/sempa/Documents/report_storage/graph.pdf'
    # pdfkit.from_file(image_file, pdf_file, options={'dpi': 300})
def export_to_pdf():
    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".pdf"
    file_path = os.path.join("C:/Users/sempa/Generated_file", file_name)

    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm'
    }
    pdfkit.from_url('http://localhost:8050/', file_path, options=options)
    
# Run app and export PDF file every 10 seconds
if __name__ == '__main__':
    while True:
        app.run_server(debug=False)
        export_to_pdf()
        time.sleep(10)


