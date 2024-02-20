"""Snippets in this docstring are ingested by other documentation (including library docstrings) during the MkDocs build process.

# --8<-- [start:openai]
The [openai](https://pypi.org/project/openai/) package is the core library to install in Python projects that need
to call the [OpenAI REST API](https://platform.openai.com/docs/api-reference). It inclues modules for working with OpenAI
resources that provide access to its AI [models](https://platform.openai.com/docs/models),
including large language models (LLMs) like GPT-4 and models for working with images and audio. The `openai` package
provides both synchronous and asynchronous API clients, their configuration options, and modules that provide the API
surface for interacting with the services in the OpenAI platform.

To get started, check out the documentation for the module representing the [resource][src.openai.resources] you're interested in using for your
project. For example, the [`resources.chat.completions`][src.openai.resources.chat.completions] module is what you'd use
for conversational chat-style interactions with an LLM like [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo).
Or, maybe you want the [`resources.audio`][src.openai.resources.audio] module for performing audio transcription, translation, and
speech synthesis in your app.

The documentation for the library's main client classes, [`OpenAI`][src.openai.OpenAI] and
[`AsyncOpenAI`][src.openai.AsyncOpenAI], is another good place to start. Those clients are the primary contact points for
your code working with any of the resources available on OpenAI API endpoints.

For more information about the REST API this package talks to or to find client libraries for other programming
languages, see:

- [Reference documentation](https://platform.openai.com/docs/api-reference) for the OpenAPI REST API (platform.openai.com)
- [OpenAPI Description (OAD)](https://github.com/openai/openai-openapi) file for the OpenAPI REST API (GitHub)
- More [client libraries](https://platform.openai.com/docs/libraries) for the OpenAI API (platform.openai.com)
# --8<-- [end:openai]
"""
