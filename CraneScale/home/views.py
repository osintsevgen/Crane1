from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import datetime
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from ipywidgets import widgets, VBox, Layout, Button, Box, FloatText, Textarea, Dropdown, Label, IntSlider, HTML
from IPython.display import display


def home(request):
    def scatter():
        x1 = [1,2,3,4, 5,6,7]
        y1 = [30, 35, 25, 45,55,60,65]

        trace = go.Scatter(
            x=x1,
            y=y1
        )
        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis = dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)

        fig.update_xaxes(rangeslider_visible=True)

        for step in np.arange(min(x1), max(x1), 0.1):
            fig.add_trace(
                go.Scatter(
                    visible=False,
                    line=dict(color="#00CED1", width=6),
                    name="v = " + str(step),
                    x=x1,
                    y=y1))

        fig.data[20].visible = True
        # print(step)
        steps = []

        for i in range(len(fig.data)):
            step = dict(
                method="update",
                args=[{"visible": [False]*len(fig.data)}, {"title": "Slider switched to step: " + str(i)}],
            )
            step["args"][0]["visible"][i] = True
            steps.append(step)

        # print(step["args"])

        sliders = [dict(
            active=10,
            currentvalue={"prefix": "Frequency: "},
            pad={"t": 50},
            steps=steps,
            visible=True)]

        fig.update_layout(sliders=sliders)

        # month = [dict(
        #     active=10,
        #     activebgcolor='violet',
        #     bgcolor='yellow',
        #     currentvalue={"prefix": "Frequency: "},
        #     pad={"t": 50},
        #     # steps='stepdefaults',
        #     visible=True,
        #     # value=1.0,
        #     # min=1.0,
        #     # max=12.0,
        #     # step=1.0,
        #     # description='Month:',
        #     # coutinuous_update=False
        # )]
        #
        # fig.update_layout(sliders=month)


        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def widdgets():
        month = widgets.IntSlider(
            value=1.0,
            min=1.0,
            max=12.0,
            step=1.0,
            description='Month:',
            coutinuous_update=False
        )

        use_date = widgets.Checkbox(
            description='Date:',
            value=True,
        )

        container = widgets.HBox(children=[use_date, month])

        # textbox = widgets.Dropdown(
        #     description='Airline:  ',
        #     # value='1',
        #     options=df['НомерКрана'].unique().tolist()
        # )

        # origin = widgets.Dropdown(
        #     options=df['НомерКрана'].unique().tolist(),
        #     value='2',
        #     description='Origin Airport:  ',
        # )

        # trace1 = go.Scatter(x=list(cd1['ДатаВремя']), y=list(cd1['Скорость']), name="Скорость 1 крана",
        #                          line=dict(color="#33CFA5"), text=list(cd1['Скорость']), yaxis="y2")
        # trace2 = go.Scatter(x=list(cd2['ДатаВремя']), y=list(cd2['Скорость']), name="Скорость 2 крана",
        #                          line=dict(color="#F06A6A"), text=list(cd2['Скорость']), yaxis="y3")
        # g = go.FigureWidget(data=[plot()], layout=go.Layout(title=dict(text='Скорость разлива')))

        # def validate():
        #     # if origin.value in df['НомерКрана'].unique() and textbox.value in df['НомерКрана'].unique():
        #     if textbox.value in df['НомерКрана'].unique():
        #         return True
        #     else:
        #         return False
        #
        # def response(change):
        #     if validate():
        #         if use_date.value:
        #             filter_list = [i and j  for i, j in
        #                            zip(df['ДатаВремя'] == month.value, df['НомерКрана'] == textbox.value)]
        #             temp_df = df[filter_list]
        #
        #         else:
        #             filter_list = [i and j for i, j in
        #                            zip(df['ДатаВремя'] == month.value, df['НомерКрана'] == textbox.value)]
        #             temp_df = df[filter_list]
        #         x1 = temp_df['Скорость']
        #         x2 = temp_df['Вес']
        #         with g.batch_update():
        #             g.data[0].x = x1
        #             g.data[1].x = x2
        #             g.data[0].y = list(cd1['Скорость'])
        #             g.data[0].y = list(cd2['Скорость'])
        #             g.layout.barmode = 'overlay'
        #             g.layout.xaxis.title = 'Delay in Minutes'
        #             g.layout.yaxis.title = 'Number of Delays'

        # textbox.observe(response, names="value")
        # month.observe(response, names="value")
        # use_date.observe(response, names="value")

        # container2 = widgets.HBox([textbox, textbox])

        form_item_layout = Layout(
            display='flex',
            flex_flow='row',
            justify_content='space-between'
        )

        form_item = [
            Box([Label(value='Age of the captain'), IntSlider(min=40, max=60)], layout=form_item_layout),
            Box([Label(value='Egg style'), Dropdown(option=['Scrambled', 'Sunny side up', 'Over easy'])], layout=form_item_layout),
            Box([Label(value='Ship size'), FloatText()], layout=form_item_layout),
            Box([Label(value='Information'), Textarea(min=40, max=60)], layout=form_item_layout),
        ]

        form = Box(form_item, layout=Layout(
            display='flex',
            flex_flow='column',
            border='solid 2px',
            align_item='stretch',
            width='50%'
        ))
        # caption_size = 'h4'
        #
        # h = HTML(value='<{size}>Examples of <code>object_fit</code> with large image</size>'.format(size=caption_size))
        #
        # vb = VBox()
        # vb.children = [h, form]
        #
        #
        # slider=widgets.IntSlider()
        # text=widgets.IntText()
        # fig1 = widgets.HBox([slider, text])
        # fig2 = display(container)
        # plot_wid = plot(fig2, output_type='dict', include_plotlyjs=False)


        # fig2 = go.FigureWidget(data=[container], layout=go.Layout(title=dict(title='Simple Graph'), modebar='overlay'))
        # fig2 = go.FigureWidget(vb)

        # plot_wid = plot(fig2, output_type='div', include_plotlyjs=False)
        # plot_wid = plot(fig2, output_type='div', config={"displaylogo":False})
        # return plot_wid
        dropdown = widgets.Dropdown(options=[], description="Col")
        plot_area = widgets.Output()

        fig = go.Figure()

        # fig.update_layout(
        #     xaxis=dict(
        #         rangeselector=dict(
        #             buttons=list([
        #                 dict(step="all"),
        #                 dict(count=6,
        #                      label="6m",
        #                      step="month",
        #                      stepmode="todate")]
        #             ))))

        for step in np.arange(0, 5, 0.1):
            fig.add_trace(
                go.Scatter(
                    visible=False,
                    line=dict(color="#00CED1", width=6),
                    name="v = " + str(step),
                    x=np.arange(0, 10, 0.01),
                    y=np.sin(step*np.arange(0, 10, 0.01))))

        fig.data[10].visible = True

        steps = []

        for i in range(len(fig.data)):
            step = dict(
                method="update",
                args=[{"visible": [False]*len(fig.data)}, {"title": "Slider switched to step: " + str(i)}],
            )
            step["args"][0]["visible"][i] = True
            steps.append(step)


        sliders = [dict(
            active=10,
            currentvalue={"prefix": "Frequency: "},
            pad={"t": 50},
            steps=steps,
            visible=True)]

        fig.update_layout(sliders=sliders)

            # xaxis=dict(




        # output2=widgets.Output()


        return fig.to_html()







        # return plot_wid

    context ={
        'plot1': scatter(),
        'plot2': widdgets(),
    }

    return render(request, 'home/welcome.html', context)


