import os
import time
from textwrap import dedent

import dash

# import dash_html_components as html
# import dash_core_components as dcc
from dash import html, dcc

# from dash import callback_context
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from PIL import Image
from openaiClient import gpt3

chat_obj = gpt3()


def Header(name, app):
    title_style = {
        "margin-top": 10,
        "margin-bottom": 10,
        "font-family": "Arial, sans-serif",
        "font-weight": "bold",
        "color": "#2C3E50",  # Dark blue color
    }

    logo_style = {
        "float": "right",
        "height": 50,
        "margin-top": 10,
        "margin-bottom": 10,
        "transition": "transform 0.2s",  # Smooth transition for hover effect
    }

    row_style = {
        "background-color": "#ECF0F1",  # Light gray color
        "padding": "10px 20px",
        "border-radius": "5px",
        "box-shadow": "2px 3px 8px rgba(0, 0, 0, 0.1)",  # Subtle shadow
    }

    title = html.H1(name, style=title_style)
    logo = html.Img(
        src=app.get_asset_url("logo.png"), style=logo_style, className="logo-hover"
    )
    return dbc.Row(
        [dbc.Col(title, md=8), dbc.Col(logo, md=4)],
        # style=row_style,
    )


def textbox(text, box="AI", name="Philippe", additional_class=""):
    text = text.replace(f"{name}:", "").replace("You:", "")
    style = {
        "max-width": "60%",
        "width": "max-content",
        "padding": "5px 10px",
        "border-radius": 25,
        "margin-bottom": 20,
    }

    if box == "user":
        style["margin-left"] = "auto"
        style["margin-right"] = 0
        return dbc.Card(
            text,
            style=style,
            body=True,
            color="primary",
            inverse=True,
            className=additional_class,
        )

    elif box == "AI":
        style["margin-left"] = 0
        style["margin-right"] = "auto"
        thumbnail = html.Img(
            src=app.get_asset_url("bot.png"),
            style={
                "border-radius": 50,
                "height": 36,
                "margin-right": 5,
                "float": "left",
            },
        )
        textbox = dbc.Card(text, style=style, body=True, color="light", inverse=False)
        return html.Div(
            [
                thumbnail,
                dbc.Card(
                    text,
                    style=style,
                    body=True,
                    color="light",
                    inverse=False,
                    className=additional_class,
                ),
            ]
        )

    else:
        raise ValueError("Incorrect option for `box`.")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "./styles.css"])
server = app.server

IMAGES = {"Philippe": app.get_asset_url("bot.png")}

conversation = html.Div(
    html.Div(id="display-conversation"),
    style={
        "overflow-y": "auto",
        "display": "flex",
        "height": "calc(90vh - 132px)",
        "flex-direction": "column-reverse",
    },
)

controls = dbc.Row(
    [
        dbc.Col(
            dbc.Input(
                id="user-input", placeholder="Write to the chatbot...", type="text"
            ),
            style={"flex": "8"},  # Use flex for proportional widths,
        ),
        dbc.Col(
            dbc.Button("Submit", id="submit"),
            style={
                "flex": "1",
                "maxWidth": "100px",
            },  # max width to limit the button width
        ),
    ],
    style={"display": "flex"},
)  # Display flex for parent to control children's width


app.layout = dbc.Container(
    fluid=False,
    children=[
        Header("avicii The Chatbot", app),
        # title_bar,
        dcc.Dropdown(
            id="model-choice",
            options=[
                {"label": "OpenAI GPT", "value": "api"},
                {"label": "Local GPT", "value": "local"},
            ],
            value="api",  # Default value
            clearable=False,  # Prevents the user from clearing the selection
        ),
        html.Hr(),
        dcc.Store(id="store-conversation", data=""),
        conversation,
        controls,
        dbc.Spinner(html.Div(id="loading-component")),
    ],
)


def get_ai_response():
    # time.sleep(2)  # Simulate delay
    return "This is the AI response"


@app.callback(
    [
        Output("store-conversation", "data"),
        Output("display-conversation", "children"),
        Output("user-input", "value"),
    ],
    [
        Input("model-choice", "value"),
        Input("submit", "n_clicks"),
        Input("user-input", "n_submit"),
    ],
    [State("user-input", "value"), State("store-conversation", "data")],
)
def update_conversation(
    model_choice_value, n_clicks, n_submit, user_input, chat_history
):
    ctx = dash.callback_context

    if not ctx.triggered:
        return dash.no_update

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if triggered_id == "model-choice":
        return "", [], ""  # Clear the chat and the input field

    elif triggered_id in ["submit", "user-input"]:
        if not user_input:
            return dash.no_update

        name = "Philippe"
        updated_chat = (
            chat_history + f"You: {user_input}<split>{name}: Typing...<split>"
        )
        model_output = chat_obj.get_response(user_input, model_choice_value)
        updated_chat = updated_chat.replace(
            f"{name}: Typing...", f"{name}: {model_output}"
        )

        messages = updated_chat.split("<split>")[:-1]
        chat_bubbles = [
            textbox(message, box="user" if i % 2 == 0 else "AI")
            for i, message in enumerate(messages)
        ]

        return updated_chat, chat_bubbles, ""  # Clear the input field after processing

    else:
        return dash.no_update


# @app.callback(
#     [Output("store-conversation", "data"), Output("display-conversation", "children")],
#     [Input("model-choice", "value"), Input("submit", "n_clicks")],
#     [State("user-input", "value"), State("store-conversation", "data")]
# )
# def update_conversation(model_choice_value, n_clicks, user_input, chat_history):
#     ctx = dash.callback_context

#     if not ctx.triggered:
#         # If callback was not triggered by user interaction, do not update
#         raise dash.exceptions.PreventUpdate

#     # Determine which input was triggered
#     triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

#     if triggered_id == "model-choice":
#         # If the dropdown value changed, reset the chat history
#         return "", []  # Clear both the store and the display

#     elif triggered_id == "submit":
#         # If the submit button was pressed, process the chat
#         if not user_input:
#             # If no user input, do not update
#             raise dash.exceptions.PreventUpdate

#         name = "Philippe"
#         updated_chat = chat_history + f"You: {user_input}<split>{name}: Typing...<split>"
#         model_output = chat_obj.get_response(user_input, model_choice_value)
#         updated_chat = updated_chat.replace(f"{name}: Typing...", f"{name}: {model_output}")

#         # Split the updated chat history to create chat bubbles
#         messages = updated_chat.split("<split>")[:-1]
#         chat_bubbles = []
#         for i, message in enumerate(messages):
#             chat_bubbles.append(textbox(message, box="user" if i % 2 == 0 else "AI"))

#         return updated_chat, chat_bubbles

#     else:
#         raise dash.exceptions.PreventUpdate

if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0")
