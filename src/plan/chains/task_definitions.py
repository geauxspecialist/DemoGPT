import json
import re

ALL_TASKS = [
    {
        "name": "ui_input_text",
        "description": "Gets input from the user via a text field.",
        "good_at": "Retrieving text input from the user.",
        "input": "none",
        "output": "string",
        "purpose": "Collect user-entered text for further processing.",
    },
    {
        "name": "ui_input_file",
        "description": "Provide a mechanism for users to upload a file and return its path. The task involves creating a file upload widget and returning its file path",
        "good_at": "Enabling file uploads and making the file path available for doc_load",
        "input": "none",
        "output": "string",
        "purpose": "Getting local file path with upload file widget so that doc_load can use this path",
    },
    {
        "name": "ui_output_text",
        "description": "Shows text output to the user.",
        "good_at": "Showing text to the user.",
        "input": "string",
        "output": "none",
        "purpose": "Displaying textual information to the user.",
    },
    {
        "name": "prompt_chat_template",
        "description": "Generate any string output according to the given instruction by AI",
        "good_at": "Creating context-aware string, responses, role play, instructions, that can be generated by AI",
        "input": "string, context",
        "output": "string",
        "purpose":"Using AI to generate smart text output from given context or instruction",
    },
    {
        "name": "doc_loader",
        "description": "Load file content from path (txt or url or pdf file path or csv file path or powerpoint file path) and generate docs",
        "good_at": "Loading from external sources only from url or path not the content",
        "input":"path | url",
        "output":"Document",
        "purpose": "Loading external files",
    },
    {
        "name": "doc_to_string",
        "description": "Convert Document object to string",
        "good_at": "Converting Document object to string",
        "input":"Document object",
        "output":"String",
        "purpose": "Converting Document object to string",
    },
    {
        "name": "summarize",
        "description": "Summarize Document Objects",
        "good_at": "Summarizing long Document Objects",
        "input":"Document",
        "output":"string",
        "purpose": "Summarization of long Document Objects",
    },
    {
        "name": "path_to_content",
        "description": "Retrieve the content of the file from given path",
        "good_at": "Retrieving the content of the file from given path",
        "input":"string",
        "output":"string",
        "purpose": "Retrieving the content of the file from given path",
    },
    {
        "name": "hub_question_answering",
        "description": "Answer questions related to the file.",
        "good_at": "Question answering on files or documents.",
        "input":["string", "file"],
        "output":"string",
        "purpose": "Extracting and providing specific information from files in response to questions.",
    },
    {
        "name": "memory",
        "description": "Returns memory that could be attached as an input to any prompt_chat_template.",
        "good_at": "Memorizing the conversation history or context.",
        "input":"none",
        "output":"Memory",
        "purpose": "Storing and retrieving conversation history or contextual information.",
    },
    {
        "name": "prompt_list_parser",
        "description": "Transform the input text into a list.",
        "good_at": "Transforming text into a list.",
        "input":"string",
        "output":"list",
        "purpose": "Converting textual data into structured list format.",
    },
    {
        "name": "router",
        "description": "When there are multiple prompt_chat_template objects, it uses the appropriate one to answer the question.",
        "good_at": "Handling different types of questions that require different abilities.",
        "input":["*prompt_chat_template"],
        "output":"string",
        "purpose": "Routing queries to the appropriate handler based on context or type.",
    },
    {
        "name": "react",
        "description": "Answer questions that require external search on the web.",
        "good_at": "Answering questions that require Google search or other web searches.",
        "input":"string",
        "output":"string",
        "purpose": "Finding information online to answer user queries.",
    },
    {
        "name": "cpal_chain",
        "description": "Solve math problems end to end",
        "good_at": "Directly solving any math problems",
        "input":"string",
        "output":"string",
        "purpose": "Performing mathematical calculations and solving problems based on the input question",
    },
    {
        "name": "hub_bash",
        "description": "Do operations on the bash by running needed scripts on the terminal to apply the command.",
        "good_at": "Executing bash commands and providing results.",
        "input":"string",
        "output":"string",
        "purpose": "Running scripts or commands on the terminal and returning the output.",
    },
    {
        "name": "hub_meteo",
        "description": "Gives weather-related information from the question.",
        "good_at": "Answering weather-related questions.",
        "input":"string",
        "output":"string",
        "purpose": "Providing weather forecasts, conditions, and related information.",
    }
]

TASKS = ALL_TASKS[:7]  # first 7 of them has been implemented yet.

TASK_NAMES = [task["name"] for task in TASKS]

TASK_DESCRIPTIONS = json.dumps(TASKS, indent=4)

tasks = re.findall(r"\{(?:[^{}]|(?:\{[^{}]*\}))*\}", TASK_DESCRIPTIONS)

for task in tasks:
    changed = "{" + task + "}"
    TASK_DESCRIPTIONS = TASK_DESCRIPTIONS.replace(task, changed)