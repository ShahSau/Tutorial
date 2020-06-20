import dash
import dash_html_components as html
import dash_core_components as dcc

app=dash.Dash()
colors={'background':'#111111', 'text':'#7FDBFF'}

app.layout=html.Div(children=[
                     html.H1('Dash 2nd', style={'textAlign': 'center',
                                                'color':colors['text']}),
                     html.H6('me trying',style={'textAlign': 'center',
                                                'color':colors['text']}),


                dcc.Graph(id='example',
                        figure={'data':[
                            {'x':[1,2,3],'y':[4,1,2], 'type': 'bar', 'name':'SF'},
                            {'x':[1,2,3],'y':[2,4,5], 'type': 'bar', 'name':'NC'},
                            ],
                            'layout':{
                            'pg_bgcolor': colors['background'],
                            'paper_bgcolor':colors['background'],
                            'font':{'size': 24, 'color': colors['text']},
                            'title': 'Bar plots first'
                                }
                        }
                    )
#styling the layout
], style={'background':'#111111'})


if __name__ == '__main__':
    app.run_server()
