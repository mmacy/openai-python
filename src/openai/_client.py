# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    is_mapping,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import OpenAIError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "OpenAI",
    "AsyncOpenAI",
    "Client",
    "AsyncClient",
]


class OpenAI(SyncAPIClient):
    """Primary synchronous client interface for interacting with the services (resources) provided by the OpenAI API.

        An instance of the `OpenAI` class is the top-level object you interact with to make synchronous calls to the
        OpenAI API. The client provides access to OpenAI's services, or *resources*, like text completion, chat,
        embeddings, image and audio processing, and managing the files used by these resources.

        The API authenticates requests to its endpoints by validating your API key, which you provide to the `OpenAI`
        client object in one of two ways:

        :material-checkbox-marked-circle-outline: **Set an  environment variable** named `OPENAI_API_KEY` that contains
        your API key and then instantiate the client *without* passing the `api_key` parameter. This is the preferred
        method.

        :material-alert: **Pass the `api_key` parameter explicitly** when you instantiate the client object. Choose this
        method *only* if you're unwilling or unable to use a more secure method like setting the `OPENAI_API_KEY`
        environment variable.

        Danger:
            To prevent unauthorized access to OpenAI services, securely manage credentials like your OpenAI API key.

        Examples:
            The following code snippets each create an instance of the `OpenAI` class ready to call the API. To interact
            with an OpenAI service (a [`resource`][src.openai.resources] in the API), you access the appropriate
            attribute on the initialized client object and call the the methods provided by that resource.

        - Create client using **inferred API key** ⁠— The API key is obtained by the `OpenAI` client automatically from
            the `OPENAI_API_KEY` environment variable if you *omit* the `api_key` constructor argument.

            ```python
            from openai import OpenAI

            # Instantiate the client with NO 'api_key' param so the client will
            # read the OPENAI_API_KEY variable from the environment automatically
            client = OpenAI()
            ```

        - Create client using **explicit API key** ⁠— Passing the API key explicitly directs the `OpenAI` client to use
            that key instead of the `OPENAI_API_KEY` environment variable (if set).

            :material-alert: This instantiation method can pose an increased **security risk**. For example, by
            instantiating the client this way in your code, it's easier to accidentally commit your API key to version
            control, which you should *never* do.

            ```python
            from openai import OpenAI

            # !!! USE WITH CAUTION !!!

            # Instantiate the client and pass the API key explicitly
            client = OpenAI(api_key='your_api_key_here')
            ```
    """
    completions: resources.Completions
    chat: resources.Chat
    embeddings: resources.Embeddings
    files: resources.Files
    images: resources.Images
    audio: resources.Audio
    moderations: resources.Moderations
    models: resources.Models
    fine_tuning: resources.FineTuning
    beta: resources.Beta
    with_raw_response: OpenAIWithRawResponse
    with_streaming_response: OpenAIWithStreamedResponse

    # client options
    api_key: str
    organization: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Initializes a new instance of the OpenAI client for making synchronous API requests.

        Args:
            api_key (str | None, optional): The API key used for authenticating requests to OpenAI. If not provided, the
                client attempts to retrieve the API key from the `OPENAI_API_KEY` environment variable. Defaults to None.
            organization (str | None, optional): The ID of the organization under which the API calls are made. This is
                optional and typically used for OpenAI services that require organization-level access control. If not
                provided, the client attempts to retrieve the organization ID from the `OPENAI_ORG_ID` environment
                variable. Defaults to None.
            base_url (str | httpx.URL | None, optional): The base URL for the OpenAI API. This allows for custom API
                endpoints like those used for testing or specific API versions. If not provided, defaults to the
                official OpenAI API URL.
            timeout (Union[float, Timeout, None, NotGiven], optional): The timeout for API requests. This can be
                specified as a float representing seconds, a `httpx.Timeout` object for fine-grained control, or `None`
                to use the default timeout. Defaults to `NOT_GIVEN`, which utilizes the `httpx` default timeout settings.
            max_retries (int, optional): The maximum number of retries for failed requests. This can help handle
                transient network issues or rate limit errors gracefully. Defaults to a predefined constant
                `DEFAULT_MAX_RETRIES`.
            default_headers (Mapping[str, str] | None, optional): Default headers to include with every request. This
                can be used to set global headers like `User-Agent` or custom headers required for integration.
                Defaults to None.
            default_query (Mapping[str, object] | None, optional): Default query parameters to include with every
                request. This is useful for setting global parameters that should be included in all API calls. Defaults
                to None.
            http_client (httpx.Client | None, optional): An instance of `httpx.Client` to be used for making HTTP
                requests. This allows for custom configuration of the HTTP client, like setting proxies or client-side
                SSL certificates. If not provided, a default `httpx.Client` instance is used. Defaults to None.
            _strict_response_validation (bool, optional): Enables or disables strict validation of API responses against
                the expected schema. This is primarily used for development and debugging purposes to ensure the API
                responses match the expected format. Note that this argument may be removed or changed in future releases.
                Defaults to False.

        Raises:
            OpenAIError: If neither the `api_key` is provided nor the `OPENAI_API_KEY` environment variable is set,
                indicating that the client's requests to the OpenAI API would fail authentication.
        """
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY")
        if api_key is None:
            raise OpenAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable"
            )
        self.api_key = api_key

        if organization is None:
            organization = os.environ.get("OPENAI_ORG_ID")
        self.organization = organization

        if base_url is None:
            base_url = os.environ.get("OPENAI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openai.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

        self.completions = resources.Completions(self)
        self.chat = resources.Chat(self)
        self.embeddings = resources.Embeddings(self)
        self.files = resources.Files(self)
        self.images = resources.Images(self)
        self.audio = resources.Audio(self)
        self.moderations = resources.Moderations(self)
        self.models = resources.Models(self)
        self.fine_tuning = resources.FineTuning(self)
        self.beta = resources.Beta(self)
        self.with_raw_response = OpenAIWithRawResponse(self)
        self.with_streaming_response = OpenAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "OpenAI-Organization": self.organization if self.organization is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            organization=organization or self.organization,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)

client = OpenAI()
class AsyncOpenAI(AsyncAPIClient):
    completions: resources.AsyncCompletions
    chat: resources.AsyncChat
    embeddings: resources.AsyncEmbeddings
    files: resources.AsyncFiles
    images: resources.AsyncImages
    audio: resources.AsyncAudio
    moderations: resources.AsyncModerations
    models: resources.AsyncModels
    fine_tuning: resources.AsyncFineTuning
    beta: resources.AsyncBeta
    with_raw_response: AsyncOpenAIWithRawResponse
    with_streaming_response: AsyncOpenAIWithStreamedResponse

    # client options
    api_key: str
    organization: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async openai client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `OPENAI_API_KEY`
        - `organization` from `OPENAI_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY")
        if api_key is None:
            raise OpenAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable"
            )
        self.api_key = api_key

        if organization is None:
            organization = os.environ.get("OPENAI_ORG_ID")
        self.organization = organization

        if base_url is None:
            base_url = os.environ.get("OPENAI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openai.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

        self.completions = resources.AsyncCompletions(self)
        self.chat = resources.AsyncChat(self)
        self.embeddings = resources.AsyncEmbeddings(self)
        self.files = resources.AsyncFiles(self)
        self.images = resources.AsyncImages(self)
        self.audio = resources.AsyncAudio(self)
        self.moderations = resources.AsyncModerations(self)
        self.models = resources.AsyncModels(self)
        self.fine_tuning = resources.AsyncFineTuning(self)
        self.beta = resources.AsyncBeta(self)
        self.with_raw_response = AsyncOpenAIWithRawResponse(self)
        self.with_streaming_response = AsyncOpenAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "OpenAI-Organization": self.organization if self.organization is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            organization=organization or self.organization,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)


class OpenAIWithRawResponse:
    def __init__(self, client: OpenAI) -> None:
        self.completions = resources.CompletionsWithRawResponse(client.completions)
        self.chat = resources.ChatWithRawResponse(client.chat)
        self.embeddings = resources.EmbeddingsWithRawResponse(client.embeddings)
        self.files = resources.FilesWithRawResponse(client.files)
        self.images = resources.ImagesWithRawResponse(client.images)
        self.audio = resources.AudioWithRawResponse(client.audio)
        self.moderations = resources.ModerationsWithRawResponse(client.moderations)
        self.models = resources.ModelsWithRawResponse(client.models)
        self.fine_tuning = resources.FineTuningWithRawResponse(client.fine_tuning)
        self.beta = resources.BetaWithRawResponse(client.beta)


class AsyncOpenAIWithRawResponse:
    def __init__(self, client: AsyncOpenAI) -> None:
        self.completions = resources.AsyncCompletionsWithRawResponse(client.completions)
        self.chat = resources.AsyncChatWithRawResponse(client.chat)
        self.embeddings = resources.AsyncEmbeddingsWithRawResponse(client.embeddings)
        self.files = resources.AsyncFilesWithRawResponse(client.files)
        self.images = resources.AsyncImagesWithRawResponse(client.images)
        self.audio = resources.AsyncAudioWithRawResponse(client.audio)
        self.moderations = resources.AsyncModerationsWithRawResponse(client.moderations)
        self.models = resources.AsyncModelsWithRawResponse(client.models)
        self.fine_tuning = resources.AsyncFineTuningWithRawResponse(client.fine_tuning)
        self.beta = resources.AsyncBetaWithRawResponse(client.beta)


class OpenAIWithStreamedResponse:
    def __init__(self, client: OpenAI) -> None:
        self.completions = resources.CompletionsWithStreamingResponse(client.completions)
        self.chat = resources.ChatWithStreamingResponse(client.chat)
        self.embeddings = resources.EmbeddingsWithStreamingResponse(client.embeddings)
        self.files = resources.FilesWithStreamingResponse(client.files)
        self.images = resources.ImagesWithStreamingResponse(client.images)
        self.audio = resources.AudioWithStreamingResponse(client.audio)
        self.moderations = resources.ModerationsWithStreamingResponse(client.moderations)
        self.models = resources.ModelsWithStreamingResponse(client.models)
        self.fine_tuning = resources.FineTuningWithStreamingResponse(client.fine_tuning)
        self.beta = resources.BetaWithStreamingResponse(client.beta)


class AsyncOpenAIWithStreamedResponse:
    def __init__(self, client: AsyncOpenAI) -> None:
        self.completions = resources.AsyncCompletionsWithStreamingResponse(client.completions)
        self.chat = resources.AsyncChatWithStreamingResponse(client.chat)
        self.embeddings = resources.AsyncEmbeddingsWithStreamingResponse(client.embeddings)
        self.files = resources.AsyncFilesWithStreamingResponse(client.files)
        self.images = resources.AsyncImagesWithStreamingResponse(client.images)
        self.audio = resources.AsyncAudioWithStreamingResponse(client.audio)
        self.moderations = resources.AsyncModerationsWithStreamingResponse(client.moderations)
        self.models = resources.AsyncModelsWithStreamingResponse(client.models)
        self.fine_tuning = resources.AsyncFineTuningWithStreamingResponse(client.fine_tuning)
        self.beta = resources.AsyncBetaWithStreamingResponse(client.beta)


Client = OpenAI

AsyncClient = AsyncOpenAI
