import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()

app.layout=html.Div(children=[
    html.H1(children='Hello Dash!!'),
    html.Div('Dash: lets try things to do thing'),
    dcc.Graph(id='example',
            figure={'data':[
            {'x':[1,2,3],'y':[4,1,2], 'type': 'bar', 'name':'SF'},
            {'x':[1,2,3],'y':[2,4,5], 'type': 'bar', 'name':'NC'},
            ],
                    'layout':{
                    'title': 'Bar plots first'
                    }
            }
    ),
    dcc.Graph(id='example1',
             figure={'data':[
             {'x':[1,2,3],'y':[4,1,2], 'type': 'scatter', 'name':'SF'},
             {'x':[1,2,3],'y':[2,4,5], 'type': 'scatter', 'name':'NC'},
             ],
                    'layout':{
                    'title': 'Scatter plots!'
                    }
             }
    )
])


if __name__ == '__main__':
    app.run_server()
