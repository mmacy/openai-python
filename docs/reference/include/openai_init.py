"""Snippets in this docstring are ingested by other documentation (including library docstrings) during the MkDocs build process.

# --8<-- [start:openai]
The [openai](https://pypi.org/project/openai/) package is the core library to install in Python projects that need
to call the [OpenAI REST API](https://platform.openai.com/docs/api-reference). It inclues modules for working with OpenAI
resources that provide access to its AI [models](https://platform.openai.com/docs/models),
including large language models (LLMs) like GPT-4 and models for working with images and audio. The `openai` package
provides both synchronous and asynchronous API clients, options to configure their behavior, and modules that provide
Python code with an API surface to interact with the OpenAI platform.

To get started, read the submodule descriptions in [`resources`][src.openai.resources] to determine which best fits your
project. For example, the [`resources.chat`][src.openai.resources.chat] submodule description indicates it's a good fit
for conversational chat-style interactions with an LLM like [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo).
Or, maybe you need the [`resources.audio`][src.openai.resources.audio] module to perform audio transcription,
translation, and speech synthesis in your app.

Once you've determined the resource to use, create an [`OpenAI`][src.openai.OpenAI] or [`AsyncOpenAI`][src.openai.AsyncOpenAI]
client instance and access the instance attribute for that resource on the client object. For example, if you instantiate
an `OpenAI` client object named `client`, youd access the [`OpenAI.chat`][src.openai.OpenAI.chat] instance attribute:

```python
from openai import OpenAI

# Reads API key from OPENAI_API_KEY environment variable
client = OpenAI()

# Use the `chat` resource to interact with the OpenAI chat completions endpoint
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)
```

For more information about the REST API this package talks to or to find client libraries for other programming
languages, see:

- [REST API reference documentation](https://platform.openai.com/docs/api-reference) for the OpenAPI REST API (platform.openai.com)
- [OpenAPI Description (OAD)](https://github.com/openai/openai-openapi) file for the OpenAPI REST API (GitHub)
- More [client libraries](https://platform.openai.com/docs/libraries) for the OpenAI API (platform.openai.com)
# --8<-- [end:openai]
"""
