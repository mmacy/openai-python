# OpenAI Python API library

[![PyPI version](https://img.shields.io/pypi/v/openai.svg)](https://pypi.org/project/openai/)

<!-- ---8<--- [start:get-started] -->

The OpenAI Python library provides access to the OpenAI REST API in Python applications. It includes type definitions for all request params and response fields and has clients for both synchronous and asynchronous operations powered by [httpx](https://github.com/encode/httpx).

The OpenAI Python library is generated from OpenAI's [OpenAPI specification](https://github.com/openai/openai-openapi) with [Stainless](https://stainlessapi.com/).

## Prerequisites

- [Python](https://www.python.org/) 3.7+
- [OpenAI API key](https://platform.openai.com/account/api-keys)

## Install the package

You can install the [openai](https://pypi.org/project/openai/) package from PyPi. For example, install with `pip`:

```sh
# Install from PyPI
pip install openai
```

## Migrate from earlier versions

Released on November 6th 2023, the OpenAI Python library was rewritten for version `1.0.0`.

If your project used a pre-v1 version of the library, see the [v1 migration guide](https://github.com/openai/openai-python/discussions/742) for information and scripts that can help you update your code.

<!-- ---8<--- [end:get-started] -->

## Connect

<!-- ---8<--- [start:connect] -->

To connect to the OpenAI API:

1. Populate an `OPENAI_API_KEY` environment variable with your [OpenAI API key](https://platform.openai.com/account/api-keys)
2. Create a synchronous or asynchronous `OpenAI` client object.


!!! Tip
    To reduce the risk of committing your OpenAI API key to source control, you can use [python-dotenv](https://pypi.org/project/python-dotenv/) and add `OPENAI_API_KEY="YOUR_API_KEY_HERE"` to your `.env` file.

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
    model="gpt-4o",
)
```

### Vision

With a hosted image:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": f"{img_url}"},
                },
            ],
        }
    ],
)
```

With the image as a base64 encoded string:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:{img_type};base64,{img_b64_str}"},
                },
            ],
        }
    ],
)
```

### Polling Helpers

When interacting with the API some actions such as starting a Run and adding files to vector stores are asynchronous and take time to complete. The SDK includes
helper functions which will poll the status until it reaches a terminal state and then return the resulting object.
If an API method results in an action that could benefit from polling there will be a corresponding version of the
method ending in '\_and_poll'.

For instance to create a Run and poll until it reaches a terminal state you can run:

```python
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
```

More information on the lifecycle of a Run can be found in the [Run Lifecycle Documentation](https://platform.openai.com/docs/assistants/how-it-works/run-lifecycle)

### Bulk Upload Helpers

When creating and interacting with vector stores, you can use polling helpers to monitor the status of operations.
For convenience, we also provide a bulk upload helper to allow you to simultaneously upload several files at once.

```python
sample_files = [Path("sample-paper.pdf"), ...]

batch = await client.vector_stores.file_batches.upload_and_poll(
    store.id,
    files=sample_files,
)
```

### Streaming helpers

The SDK also includes helpers to process streams and handle incoming events.

```python
with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
) as stream:
    for event in stream:
        # Print the text from text delta events
        if event.type == "thread.message.delta" and event.data.delta.content:
            print(event.data.delta.content[0].text)
```

More information on streaming helpers can be found in the dedicated documentation: [helpers.md](./helpers.md)

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
        model="gpt-4o",
    )


asyncio.run(main())
```

1. You can **omit** this parameter if the `OPENAI_API_KEY` environment variable is set and contains a valid key. By default, the [AsyncOpenAI()][src.openai.AsyncOpenAI] client attempts to read the `OPENAI_API_KEY` env var upon instantiation.

You can enable response streaming in the async client by including `stream=True` to the [AsyncCompletions.create()][src.openai.resources.chat.completions.AsyncCompletions.create] method:

```python
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

The async client uses the exact same interface.

```python
import asyncio
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
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)
```

We recommend you _avoid_ using this module-level client in your application code because:

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
    model="gpt-4o",
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
        model="gpt-4o",
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
|     422     | [`UnprocessableEntityError`][src.openai.UnprocessableEntityError] |
|     429     | [`RateLimitError`][src.openai.RateLimitError]                     |
|    >=500    | [`InternalServerError`][src.openai.InternalServerError]           |
|     N/A     | [`APIConnectionError`][src.openai.APIConnectionError]             |

## Request IDs

> For more information on debugging requests, see [these docs](https://platform.openai.com/docs/api-reference/debugging-requests)

All object responses in the SDK provide a `_request_id` property which is added from the `x-request-id` response header so that you can quickly log failing requests and report them back to OpenAI.

```python
completion = await client.chat.completions.create(
    messages=[{"role": "user", "content": "Say this is a test"}], model="gpt-4"
)
print(completion._request_id)  # req_123
```

Note that unlike other properties that use an `_` prefix, the `_request_id` property
*is* public. Unless documented otherwise, *all* other `_` prefix properties,
methods and modules are *private*.

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
            "content": "How can I get the name of the current day in JavaScript?",
        }
    ],
    model="gpt-4o",
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
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I list all files in a directory using Python?",
        }
    ],
    model="gpt-4o",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

<!-- ---8<--- [end:handle-errors] -->

## Advanced

### Logging

<!-- ---8<--- [start:debugging] -->

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `OPENAI_LOG` to `info`.

```shell
$ export OPENAI_LOG=info
```

Or to `debug` for more verbose logging.

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
    model="gpt-4o",
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
    model="gpt-4o",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

<!-- ---8<--- [end:debugging] -->

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) will be respected when making this
request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

<!-- ---8<--- [start:advanced] -->

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from openai import OpenAI, DefaultHttpxClient

client = OpenAI(
    # Or use the `OPENAI_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083/v1",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default, the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from openai import OpenAI

with OpenAI() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Microsoft Azure OpenAI

To use this library with [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview), use the `AzureOpenAI`
class instead of the `OpenAI` class.

!!! important

    The API surface of the Azure API differs from that of the core API. The static types for responses / params won't always be correct.

```py
from openai import AzureOpenAI

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    # https://learn.microsoft.com/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-07-01-preview",
    # https://learn.microsoft.com/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
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
print(completion.to_json())
```

In addition to the options provided in the base `OpenAI` client, the following options are provided:

- `azure_endpoint` (or the `AZURE_OPENAI_ENDPOINT` environment variable)
- `azure_deployment`
- `api_version` (or the `OPENAI_API_VERSION` environment variable)
- `azure_ad_token` (or the `AZURE_OPENAI_AD_TOKEN` environment variable)
- `azure_ad_token_provider`

An example of using the client with Microsoft Entra ID (formerly known as Azure Active Directory) can be found [here](https://github.com/openai/openai-python/blob/main/examples/azure_ad.py).

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/openai/openai-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import openai
print(openai.__version__)
```

<!-- ---8<--- [end:advanced] -->
