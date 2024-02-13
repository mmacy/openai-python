# OpenAI Python API library

[![PyPI version](https://img.shields.io/pypi/v/openai.svg)](https://pypi.org/project/openai/)

<!-- ---8<--- [start:get-started] -->

The OpenAI Python library provides access to the OpenAI REST API in Python applications. It includes type definitions for all request params and response fields and has clients for both synchronous and asynchronous operations powered by [httpx](https://github.com/encode/httpx).

The OpenAI Python library is generated from OpenAI's [OpenAPI specification](https://github.com/openai/openai-openapi) with [Stainless](https://stainlessapi.com/).

## Prerequisites

- [Python](https://www.python.org/) 3.7+
- [OpenAI API key](https://platform.openai.com/account/api-keys)

## Install the package

You can the [openai](https://pypi.org/project/openai/) package from PyPi with `pip`:

```sh
# Install the package
pip install openai
```

## Migrate from earlier versions

Released on November 6th 2023, the OpenAI Python library was rewritten for version `1.0.0`.

If your project used a pre-v1 version of the library, see the [v1 migration guide](https://github.com/openai/openai-python/discussions/742) for information and scripts that can help you update your code.

<!-- ---8<--- [end:get-started] -->

## Connect

<!-- ---8<--- [start:connect] -->

To connect to the OpenAI API:

1. Populate an `OPENAI_API_KEY` environment variable with your [OpenAI API key](https://platform.openai.com/account/api-keys).
2. Create a synchronous or asynchronous `OpenAI` client object.

!!! Tip

    To reduce the risk of committing your OpenAI API key to source control, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/) and adding `OPENAI_API_KEY="YOUR_API_KEY_HERE"` to your `.env` file.

## Synchronous client

Create an instance of the [OpenAI][src.openai.OpenAI] client:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"), # (1)
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
```

1. You can **omit** this parameter if the `OPENAI_API_KEY` environment variable is set and contains a valid key. By default, the [OpenAI()][src.openai.OpenAI] client attempts to read the `OPENAI_API_KEY` env var upon instantiation.

To stream responses from the API, include `stream=True` in your call to [Completions.create()][src.openai.resources.chat.completions.Completions.create] method call:

```python
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True, # (1)
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

1. :material-chat: This enables response streaming through Server Side Events (SSE).

## Asynchronous client

Create an instance of the [AsyncOpenAI][src.openai.AsyncOpenAI] client and `await` each API call. Functionality between the synchronous and asynchronous clients is otherwise identical.

```python
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"), # (1)
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )


asyncio.run(main())
```

1. You can **omit** this parameter if the `OPENAI_API_KEY` environment variable is set and contains a valid key. By default, the [AsyncOpenAI()][src.openai.AsyncOpenAI] client attempts to read the `OPENAI_API_KEY` env var upon instantiation.

You can enable response streaming in the async client by including `stream=True` to the [AsyncCompletions.create()][src.openai.resources.chat.completions.AsyncCompletions.create] method:

```python
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main():
    stream = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True, # (1)
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())
```

1. :material-chat: This enables response streaming through Server Side Events (SSE).

## Module-level global client

Similar to pre-v1 versions of the library, there is also a module-level client available for use in REPLs, notebooks, and other scenarios requiring quick "local loop" iteration.

Do **NOT** use the module-level global client in production application code. Instead, create instances of [OpenAI][src.openai.OpenAI] or [AsyncOpenAI][src.openai.AsyncOpenAI] client objects as described earlier rather than relying on the global client.

```py
# WARNING: Use this client instantiation technique **only** in REPLs, notebooks,
#          or other scenarios requiring quick local-loop iteration.

import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = '...'

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://..."
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)
```

We recommend you _avoid_ using this module-level client your application code because:

- It can be difficult to reason about where client options are configured.
- It's impossible to change certain client options without causing the potential for race conditions.
- It's harder to mock for testing purposes.
- It's impossible to control cleanup of network connections.
<!-- ---8<--- [end:connect] -->

## Request types

<!-- ---8<--- [start:request-response] -->

Nested **request** parameters are Python [TypedDicts][typing.TypedDict].

For example, the user message in the following [`chat.completions.create()`][src.openai.resources.chat.completions.Completions.create] request is a [`ChatCompletionUserMessageParam`][src.openai.types.chat.chat_completion_user_message_param.ChatCompletionUserMessageParam], which has a base type of [`TypedDict`][typing.TypedDict]:

```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Can you generate an example JSON object describing a fruit?",
        }
    ],
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
)
```

### File upload request types

Request parameters that correspond to file uploads can be passed as [`bytes`][bytes], a [`PathLike`][os.PathLike] instance, or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()

client.files.create(
    file=Path("input.jsonl"),
    purpose="fine-tune",
)
```

The async client uses the same interface. If you pass a [`PathLike`][os.PathLike] instance, the file contents will be read asynchronously automatically.

## Response types

**Responses** are [Pydantic](https://docs.pydantic.dev) models that include their helper methods for things like:

- Serializing the object to JSON: [`example_response_object.model_dump_json`][src.openai.BaseModel.model_dump_json]`(indent=2, exclude_unset=True)`
- Converting the object to a dictionary: [`example_response_object.model_dump`][src.openai.BaseModel.model_dump]`(exclude_unset=True)`

!!! Tip

    Typed requests and responses enable type checking, autocompletion, and hover-help documentation in editors that support those features. In Visual Studio Code, for example, you can [enable type checking in Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) by setting `python.analysis.typeCheckingMode` to `basic` as described in that article's **Settings and Customization** section.

<!-- ---8<--- [end:request-response] -->

## Handling errors

<!-- ---8<--- [start:handle-errors] -->

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of [`openai.APIConnectionError`][src.openai.APIConnectionError] is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of [`openai.APIStatusError`][src.openai.APIStatusError] is raised, containing `status_code` and `response` properties.

All errors inherit from [`openai.APIError`][src.openai.APIError].

```python
import openai
from openai import OpenAI

client = OpenAI()

try:
    client.fine_tuning.jobs.create(
        model="gpt-3.5-turbo",
        training_file="file-abc123",
    )
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                                                        |
| :---------: | ----------------------------------------------------------------- |
|     400     | [`BadRequestError`][src.openai.BadRequestError]                   |
|     401     | [`AuthenticationError`][src.openai.AuthenticationError]           |
|     403     | [`PermissionDeniedError`][src.openai.PermissionDeniedError]       |
|     404     | [`NotFoundError`][src.openai.NotFoundError]                       |
|     409     | [`ConflictError`][src.openai.ConflictError]                       |
|     422     | [`UnprocessableEntityError`][src.openai.UnprocessableEntityError] |
|     429     | [`RateLimitError`][src.openai.RateLimitError]                     |
|    >=500    | [`InternalServerError`][src.openai.InternalServerError]           |
|     N/A     | [`APIConnectionError`][src.openai.APIConnectionError]             |

## Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.

Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from openai import OpenAI

# Configure the default for all requests:
client = OpenAI(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I get the name of the current day in Node.js?",
        }
    ],
    model="gpt-3.5-turbo",
)
```

## Timeouts

By default requests time out after 10 minutes. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from openai import OpenAI

# Configure the default for all requests:
client = OpenAI(
    # 20 seconds (default is 10 minutes)
    timeout=20.0,
)

# More granular control:
client = OpenAI(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I list all files in a directory using Python?",
        }
    ],
    model="gpt-3.5-turbo",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

<!-- ---8<--- [end:handle-errors] -->

## Advanced

### Logging

<!-- ---8<--- [start:debugging] -->

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `OPENAI_LOG` to `debug`.

```shell
$ export OPENAI_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, for example:

```py
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="gpt-3.5-turbo",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion)
```

These methods return an [`LegacyAPIResponse`](https://github.com/openai/openai-python/tree/main/src/openai/_legacy_response.py) object. This is a legacy class as we're changing it slightly in the next major version.

For the sync client this will mostly be the same with the exception
of `content` & `text` will be methods instead of properties. In the
async client, all methods will be async.

A migration script will be provided & the migration in general should
be smooth.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

As such, `.with_streaming_response` methods return a different [`APIResponse`](https://github.com/openai/openai-python/tree/main/src/openai/_response.py) object, and the async client returns an [`AsyncAPIResponse`](https://github.com/openai/openai-python/tree/main/src/openai/_response.py) object.

```python
with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

<!-- ---8<--- [end:debugging] -->

### Configuring the HTTP client

<!-- ---8<--- [start:advanced] -->

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/#client-instances) functionality

```python
import httpx
from openai import OpenAI

client = OpenAI(
    # Or use the `OPENAI_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

### Managing HTTP resources

By default, the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Microsoft Azure OpenAI

To use this library with [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview), use the `AzureOpenAI`
class instead of the `OpenAI` class.

!!! important

    The API surface of the Azure API differs from that of the core API. The static types for responses / params won't always be correct.

```py
from openai import AzureOpenAI

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-07-01-preview",
    # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-endpoint.openai.azure.com",
)

completion = client.chat.completions.create(
    model="deployment-name",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.model_dump_json(indent=2))
```

In addition to the options provided in the base `OpenAI` client, the following options are provided:

- `azure_endpoint` (or the `AZURE_OPENAI_ENDPOINT` environment variable)
- `azure_deployment`
- `api_version` (or the `OPENAI_API_VERSION` environment variable)
- `azure_ad_token` (or the `AZURE_OPENAI_AD_TOKEN` environment variable)
- `azure_ad_token_provider`

An example of using the client with Azure Active Directory can be found [here](https://github.com/openai/openai-python/blob/main/examples/azure_ad.py).

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/openai/openai-python/issues) with questions, bugs, or suggestions.

<!-- ---8<--- [end:advanced] -->
