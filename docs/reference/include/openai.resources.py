"""Snippets in this docstring are ingested by other documentation (including library docstrings) during the MkDocs build process.

# --8<-- [start:resources]
The `resources` module aggregates classes and functions for interacting with the OpenAI API into several submodules,
each representing a specific resource or feature of the API.

The submodules' classes mirror the structure of the API's endpoints and offer synchronous and asynchronous
communication with the API.

Each resource is accessible as an attribute on the [`OpenAI`][src.openai.OpenAI] and [`AsyncOpenAI`][src.openai.AsyncOpenAI]
clients. To work with a resource, initialize an instance of one of the clients and access the resource as an attribute
on the client instance. For example, to work with the `chat` resource, create an instance of the `OpenAI` client and
access the attributes and methods on `your_client_instance.chat`.
# --8<-- [end:resources]

# --8<-- [start:audio]
The `audio` module provides classes for handling various audio processing operations, including transcription of audio to text, translation of spoken content, and speech synthesis.

This module supports synchronous and asynchronous operations, and offers interfaces for direct interaction with audio data, as well as handling of raw and streaming responses. Designed for applications that require audio input processing like automated transcription services, real-time translation of spoken language, and generating spoken content from text.
# --8<-- [end:audio]

# --8<-- [start:beta]
The `beta` modules provides a unified interface for accessing beta features of the API, encapsulating synchronous and asynchronous access to resources in beta.

The module aggregates the beta functionalities related to features like yet considered generally available (GA), offering a simplified entry point for interacting with these resources. It is designed to facilitate easy access to the cutting-edge features still under development, enabling developers to experiment with and leverage new capabilities before they become GA.
# --8<-- [end:beta]

# --8<-- [start:chat]
The `chat` module provides classes for creating and managing chat sessions that leverage OpenAI's language models to generate conversational responses.

The module supports both synchronous and asynchronous operations, offering interfaces for direct interaction with the completion endpoints tailored for chat applications. Designed for developers looking to integrate AI-powered chat functionalities into their applications and features like raw and streaming response handling for more flexible integration.
# --8<-- [end:chat]

# --8<-- [start:chat_completions]
The `chat.completions` module provides access to the chat completions endpoint of the OpenAI API. It supports
the latest models including `gpt-4`, `gpt-4-turbo-preview`, `gpt-4-vision-preview`, `gpt-4-32k`, `gpt-3.5-turbo`,
and their respective dated model releases, along with fine-tuned versions of `gpt-3.5-turbo`.

This module interacts with the `/v1/chat/completions` endpoint and replaces the the legacy [`resources.completions`][src.openai.resources.completions] module. You're *strongly encouraged* to migrate existing applications that use the legacy `resources.completions` module to this one before the expected [deprecation](https://platform.openai.com/docs/deprecations) of the `/v1/completions` endpoint.
# --8<-- [end:chat_completions]

# --8<-- [start:completions]
The `completions` module provides access to the legacy completions endpoint of the OpenAI API. Use the [`chat.completions`][src.openai.resources.chat.completions] module instead for new applications.

This module interacts with a [legacy](https://platform.openai.com/docs/deprecations) endpoint,  `/v1/completions`, indicating that the endpoint no longer receives updates and is expected to be deprecated. This module is for use only in applications that require compatibility with the legacy endpoint and should **not** be used for new projects.

You're *strongly encouraged* to migrate existing applications to the [`chat.completions`][src.openai.resources.chat.completions] module⁠—which interacts with the current (non-legacy) `/v1/chat/completions` endpoint—prior to the [deprecation](https://platform.openai.com/docs/deprecations) of the `/v1/completions` endpoint.
# --8<-- [end:completions]

# --8<-- [start:embeddings]
The `embeddings` module provides classes for creating embeddings from text inputs using OpenAI's models and supports both synchronous and asynchronous operations as well as the handling of raw responses and streaming response capabilities.

The module is appropriate for use in applications that require semantic analysis of text, like similarity searches, text clustering, and other natural language processing tasks that can benefit from high-dimensional vector representations of text.
# --8<-- [end:embeddings]

# --8<-- [start:files]
The `files` module provides classes for uploading, retrieving, listing, and deleting files used across various OpenAI API endpoints.

The module supports both synchronous and asynchronous operations, along with handling of raw responses and streaming of file content. Designed for use cases that involve managing large datasets or files for purposes like fine-tuning models or using assistants, this module facilitates the efficient handling of file-related operations on the OpenAI platform.
# --8<-- [end:files]

# --8<-- [start:fine_tuning]
The `fine_tuning` module provides classes for handling fine-tuning operations, including the initiation, management, and retrieval of fine-tuning jobs.

The module supports synchronous and asynchronous operations, offering interfaces for working with jobs directly, as well as with raw or streaming responses. Designed for use in applications requiring custom model training on specific datasets to improve model performance for tailored tasks.
# --8<-- [end:fine_tuning]

# --8<-- [start:fine_tuning_jobs]
The `jobs` module provides synchronous and asynchronous access to fine-tuning job resources and enables you to create, retrieve, list, and cancel fine-tuning jobs and list the events associated with them.

Fine-tuning jobs allow you to customize pre-trained models with your own datasets, optimizing performance for specific tasks or improving understanding of particular data types. The classes in the `jobs` module includes methods for managing fine-tuning jobs, like creating a new job, fetching  details of an existing job, listing all jobs, canceling a job, and listing events associated with a job.
# --8<-- [end:fine_tuning_jobs]

# --8<-- [start:images]
The `image` module provides functionality for creating variations of images, editing images based on textual prompts, and generating new images from prompts using specified models.

The module supports both synchronous and asynchronous operations, with capabilities for handling raw responses and streaming. Suitable for applications requiring dynamic image generation or modification through the OpenAI API, this module leverages models like DALL-E to interpret text prompts into visual content.
# --8<-- [end:images]

# --8<-- [start:models]
The `models` module facilitates the retrieval, listing, and deletion of models on the OpenAI platform and supports both synchronous and asynchronous operations.

The module enables developers to interact with models, providing functionalities like fetching detailed information about a specific model, listing all available models, and deleting fine-tuned models.
# --8<-- [end:models]

# --8<-- [start:moderations]
The `moderations` module provides functionality to submit text for moderation to determine whether it violates OpenAI's content policy.

Moderation is particularly useful for developers looking to ensure the content generated or processed by their applications adheres to OpenAI's content policy. By leveraging the content moderation models provided by OpenAI, applications can automatically classify and filter out text that might be considered harmful or inappropriate.
# --8<-- [end:moderations]

# --8<-- [start:assistants]
The `assistants` module offers functionalities to create, retrieve, update, list, and delete Assistants. Assistants are AI models configured to perform specific tasks based on instructions, files, and other parameters.
# --8<-- [end:assistants]

# --8<-- [start:threads]
The `threads` module facilitates the creation, retrieval, update, deletion, and execution of Threads. Threads represent a series of messages or interactions with an assistant and support a conversational context or a sequence of operations.
# --8<-- [end:threads]
"""