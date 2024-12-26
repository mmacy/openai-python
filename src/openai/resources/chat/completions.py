# File generated from our OpenAPI spec by Stainless.
""" --8<-- 'docs/reference/include/openai.resources.py:chat_completions' """
from __future__ import annotations

import inspect
from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx
import pydantic

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._streaming import Stream, AsyncStream
from ...types.chat import (
    ChatCompletionAudioParam,
    ChatCompletionReasoningEffort,
    completion_create_params,
)
from ..._base_client import make_request_options
from ...types.chat_model import ChatModel
from ...types.chat.chat_completion import ChatCompletion
from ...types.chat.chat_completion_chunk import ChatCompletionChunk
from ...types.chat.chat_completion_modality import ChatCompletionModality
from ...types.chat.chat_completion_tool_param import ChatCompletionToolParam
from ...types.chat.chat_completion_audio_param import ChatCompletionAudioParam
from ...types.chat.chat_completion_message_param import ChatCompletionMessageParam
from ...types.chat.chat_completion_reasoning_effort import ChatCompletionReasoningEffort
from ...types.chat.chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
from ...types.chat.chat_completion_prediction_content_param import ChatCompletionPredictionContentParam
from ...types.chat.chat_completion_tool_choice_option_param import ChatCompletionToolChoiceOptionParam

__all__ = ["Completions", "AsyncCompletions"]


class Completions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/openai/openai-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/openai/openai-python#with_streaming_response
        """
        return CompletionsWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """Creates a model response for the given chat conversation.

        Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: ID of the model to use. See the
              [model endpoint compatibility](https://platform.openai.com/docs/models#model-endpoint-compatibility)
              table for details on which models work with the Chat API.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o1 series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Developer-defined tags and values used for filtering completions in the
              [dashboard](https://platform.openai.com/chat-completions).

          modalities: Output types that you would like the model to generate for this request. Most
              models are capable of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          reasoning_effort: **o1 models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the latency tier to use for processing the request. This parameter is
              relevant for customers subscribed to the scale tier service:

              - If set to 'auto', and the Project is Scale tier enabled, the system will
                utilize scale tier credits until they are exhausted.
              - If set to 'auto', and the Project is not Scale tier enabled, the request will
                be processed using the default service tier with a lower uptime SLA and no
                latency guarentee.
              - If set to 'default', the request will be processed using the default service
                tier with a lower uptime SLA and no latency guarentee.
              - When not set, the default behavior is 'auto'.

              When this parameter is set, the response body will include the `service_tier`
              utilized.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: Literal[True],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionChunk]:
        """Creates a model response for the given chat conversation.

        Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: ID of the model to use. See the
              [model endpoint compatibility](https://platform.openai.com/docs/models#model-endpoint-compatibility)
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o1 series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Developer-defined tags and values used for filtering completions in the
              [dashboard](https://platform.openai.com/chat-completions).

          modalities: Output types that you would like the model to generate for this request. Most
              models are capable of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          reasoning_effort: **o1 models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the latency tier to use for processing the request. This parameter is
              relevant for customers subscribed to the scale tier service:

              - If set to 'auto', and the Project is Scale tier enabled, the system will
                utilize scale tier credits until they are exhausted.
              - If set to 'auto', and the Project is not Scale tier enabled, the request will
                be processed using the default service tier with a lower uptime SLA and no
                latency guarentee.
              - If set to 'default', the request will be processed using the default service
                tier with a lower uptime SLA and no latency guarentee.
              - When not set, the default behavior is 'auto'.

              When this parameter is set, the response body will include the `service_tier`
              utilized.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: bool,
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """Creates a model response for the given chat conversation.

        Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: ID of the model to use. See the
              [model endpoint compatibility](https://platform.openai.com/docs/models#model-endpoint-compatibility)
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o1 series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Developer-defined tags and values used for filtering completions in the
              [dashboard](https://platform.openai.com/chat-completions).

          modalities: Output types that you would like the model to generate for this request. Most
              models are capable of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          reasoning_effort: **o1 models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the latency tier to use for processing the request. This parameter is
              relevant for customers subscribed to the scale tier service:

              - If set to 'auto', and the Project is Scale tier enabled, the system will
                utilize scale tier credits until they are exhausted.
              - If set to 'auto', and the Project is not Scale tier enabled, the request will
                be processed using the default service tier with a lower uptime SLA and no
                latency guarentee.
              - If set to 'default', the request will be processed using the default service
                tier with a lower uptime SLA and no latency guarentee.
              - When not set, the default behavior is 'auto'.

              When this parameter is set, the response body will include the `service_tier`
              utilized.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """Creates a model response for the given chat conversation, tailored by a variety of customizable parameters.

        This method allows for detailed control over the chat completion process, including model selection,
        response formatting, and dynamic interaction through streaming.

        Args:
            messages (Iterable[ChatCompletionMessageParam]):
                Messages comprising the conversation so far. Example Python code available at
                [How to format inputs to ChatGPT models](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).
            model (str | Literal[...]):
                ID of the model to use. Refer to the [model endpoint compatibility](https://platform.openai.com/docs/models/model-endpoint-compatibility)
                table for details on which models are compatible with the Chat API.
            stream (Literal[True]):
                If True, enables streaming of message deltas. Tokens are sent as server-sent events as they become available,
                terminating with a `data: [DONE]` message. See [Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
                for more on this format and [How to stream completions](https://cookbook.openai.com/examples/how_to_stream_completions)
                for example Python code.
            frequency_penalty (Optional[float], default=NOT_GIVEN):
                Adjusts token generation frequency to discourage repetition, with a range between -2.0 and 2.0.
                More details at [frequency and presence penalties](https://platform.openai.com/docs/guides/text-generation/parameter-details).
            function_call (completion_create_params.FunctionCall, optional):
                Deprecated in favor of `tool_choice`. Controls the function call behavior within the model.
            functions (Iterable[completion_create_params.Function], optional):
                Deprecated in favor of `tools`. Lists functions the model can call.
            logit_bias (Optional[Dict[str, int]], default=NOT_GIVEN):
                Modifies the likelihood of specified tokens. Accepts a dict mapping token IDs to bias values (-100 to 100).
            logprobs (Optional[bool], default=NOT_GIVEN):
                Includes log probabilities of output tokens when True. Not available for `gpt-4-vision-preview`.
            max_tokens (Optional[int], default=NOT_GIVEN):
                Sets the maximum token count for the chat completion. See [How to count tokens with TikToken](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
                for token counting examples.
            n (Optional[int], default=NOT_GIVEN):
                Number of chat completion choices to generate for each message. Affects cost.
            presence_penalty (Optional[float], default=NOT_GIVEN):
                Adjusts for token presence to promote topic diversity, with a range between -2.0 and 2.0.
            response_format (completion_create_params.ResponseFormat, optional):
                Specifies the model output format, compatible with GPT-4 Turbo and GPT-3.5 Turbo models newer than
                `gpt-3.5-turbo-1106`. JSON mode ensures valid JSON output.
            seed (Optional[int], default=NOT_GIVEN):
                Seeds the RNG for deterministic outputs. Beta feature.
            stop (Union[Optional[str], List[str]], default=NOT_GIVEN):
                Sequences indicating when to halt token generation.
            temperature (Optional[float], default=NOT_GIVEN):
                Controls output randomness. Recommended to adjust this or `top_p`, but not both.
            tool_choice (ChatCompletionToolChoiceOptionParam, optional):
                Selects a tool or function for the model to use.
            tools (Iterable[ChatCompletionToolParam], optional):
                Specifies available tools for the model, currently limited to functions.
            top_logprobs (Optional[int], default=NOT_GIVEN):
                Returns top log probabilities for each token position. Requires `logprobs` to be True.
            top_p (Optional[float], default=NOT_GIVEN):
                Nucleus sampling parameter, considering only the top probability mass for generation.
            user (str | NotGiven):
                Unique identifier for the end-user, assisting in abuse monitoring. Learn more at
                [End-user IDs](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
            extra_headers (Headers, optional):
                Additional HTTP headers for the request.
            extra_query (Query, optional):
                Additional query parameters for the request.
            extra_body (Body, optional):
                Additional body content for the request.
            timeout (float | httpx.Timeout | None | NotGiven, default=NOT_GIVEN):
                Custom timeout for this request, overriding the default settings.

        Returns:
            Stream[ChatCompletionChunk]: A stream of chat completion chunks for real-time interaction.

        Examples:
            >>> create(
            ...     messages=[{"role": "user", "content": "Hello, world!"}],
            ...     model="gpt-3.5-turbo",
            ...     stream=True,
            ...     frequency_penalty=0.5,
            ...     # Additional parameters...
            ... )
            <Stream of ChatCompletionChunk>
        """
        validate_response_format(response_format)
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )


class AsyncCompletions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/openai/openai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/openai/openai-python#with_streaming_response
        """
        return AsyncCompletionsWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """Creates a model response for the given chat conversation.

        Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: ID of the model to use. See the
              [model endpoint compatibility](https://platform.openai.com/docs/models#model-endpoint-compatibility)
              table for details on which models work with the Chat API.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o1 series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Developer-defined tags and values used for filtering completions in the
              [dashboard](https://platform.openai.com/chat-completions).

          modalities: Output types that you would like the model to generate for this request. Most
              models are capable of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          reasoning_effort: **o1 models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the latency tier to use for processing the request. This parameter is
              relevant for customers subscribed to the scale tier service:

              - If set to 'auto', and the Project is Scale tier enabled, the system will
                utilize scale tier credits until they are exhausted.
              - If set to 'auto', and the Project is not Scale tier enabled, the request will
                be processed using the default service tier with a lower uptime SLA and no
                latency guarentee.
              - If set to 'default', the request will be processed using the default service
                tier with a lower uptime SLA and no latency guarentee.
              - When not set, the default behavior is 'auto'.

              When this parameter is set, the response body will include the `service_tier`
              utilized.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: Literal[True],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionChunk]:
        """Creates a model response for the given chat conversation.

        Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: ID of the model to use. See the
              [model endpoint compatibility](https://platform.openai.com/docs/models#model-endpoint-compatibility)
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o1 series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Developer-defined tags and values used for filtering completions in the
              [dashboard](https://platform.openai.com/chat-completions).

          modalities: Output types that you would like the model to generate for this request. Most
              models are capable of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          reasoning_effort: **o1 models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the latency tier to use for processing the request. This parameter is
              relevant for customers subscribed to the scale tier service:

              - If set to 'auto', and the Project is Scale tier enabled, the system will
                utilize scale tier credits until they are exhausted.
              - If set to 'auto', and the Project is not Scale tier enabled, the request will
                be processed using the default service tier with a lower uptime SLA and no
                latency guarentee.
              - If set to 'default', the request will be processed using the default service
                tier with a lower uptime SLA and no latency guarentee.
              - When not set, the default behavior is 'auto'.

              When this parameter is set, the response body will include the `service_tier`
              utilized.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: bool,
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """Creates a model response for the given chat conversation.

        Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: ID of the model to use. See the
              [model endpoint compatibility](https://platform.openai.com/docs/models#model-endpoint-compatibility)
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.
              [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o1 series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Developer-defined tags and values used for filtering completions in the
              [dashboard](https://platform.openai.com/chat-completions).

          modalities: Output types that you would like the model to generate for this request. Most
              models are capable of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          reasoning_effort: **o1 models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the latency tier to use for processing the request. This parameter is
              relevant for customers subscribed to the scale tier service:

              - If set to 'auto', and the Project is Scale tier enabled, the system will
                utilize scale tier credits until they are exhausted.
              - If set to 'auto', and the Project is not Scale tier enabled, the request will
                be processed using the default service tier with a lower uptime SLA and no
                latency guarentee.
              - If set to 'default', the request will be processed using the default service
                tier with a lower uptime SLA and no latency guarentee.
              - When not set, the default behavior is 'auto'.

              When this parameter is set, the response body will include the `service_tier`
              utilized.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[ChatCompletionModality]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: ChatCompletionReasoningEffort | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """Generates a chat completion by submitting a conversation history and model parameters, supporting various configurations to tailor the chat completion process, including penalties, response formats, and streaming outputs.

        Returns:
            AsyncStream[ChatCompletionChunk]: Stream of chat completion chunks for incremental output consumption.
            ChatCompletion: An object containing the generated chat completion and other relevant details, such as
                            the chosen tokens and any associated metadata.

        Raises:
            OpenAIError: If there's an issue with API request or parsing the response.

        Examples:
        ```python
        completion = client.Completions().create(
            messages=[{"role": "user", "content": "Tell me a joke."}],
            model="text-davinci-003",
            max_tokens=60
        )
        print(completion.choices[0].text)
        ```

        ```python
        completion = client.Completions().create(
            messages=[{"role": "user", "content": "How do you make a latte?"}],
            model="gpt-3.5-turbo",
            max_tokens=150
        )
        print(completion.choices[0].text)
        ```

        ```python
        async with client.AsyncCompletions().create(
            messages=[{"role": "user", "content": "What's the weather like in Tokyo?"}],
            model="text-davinci-003",
            frequency_penalty=0.5,
            presence_penalty=0.5
        ) as stream:
            async for chunk in stream:
                print(chunk.text)
        ```

        Args:
            messages (Iterable[ChatCompletionMessageParam]): A sequence of message objects that make up the
                conversation so far. Each message is a dictionary that should include the keys `role` and
                `content`, where `role` is either `user` or `assistant`, indicating who is speaking, and
                `content` is a string containing the message text. This parameter is essential for
                constructing the conversational context for the model's response.
            model (Union[str, Literal[...]]): The model ID of the OpenAI GPT model to use for generating the chat
                completion. This parameter specifies which version of the model to use, for example,
                `text-davinci-003` for general-purpose completions or `gpt-3.5-turbo` for optimized
                performance. The choice of model affects the quality, style, and capabilities of the
                generated content.
            stream (Optional[bool]): Whether the response should be streamed. Streaming can be useful for
                receiving responses as they are generated, especially for long completions. This approach
                enables real-time interaction and processing of the model's output.
            frequency_penalty (Optional[float]): Adjusts the likelihood of the model repeating the same line
                verbatim. Values can range from -2.0 to 2.0, with positive values making repeats less likely.
                This parameter helps in controlling the diversity of the generated text.
            function_call (Optional[FunctionCall]): Deprecated. Originally used to specify whether the model
                should execute a function call. While it is still accepted for backward compatibility, the
                `tool_choice` parameter is recommended for new implementations.
            functions (Optional[Iterable[Function]]): Deprecated. Originally provided a list of functions the
                model could choose to call during generation. Like `function_call`, this parameter has been
                superseded by `tools`.
            logit_bias (Optional[Dicst[str, int]]): Modifies token likelihood, mapping token IDs to bias values
                (-100 to 100), influencing selection. This mechanism allows for fine-tuning the presence or
                avoidance of specific words or phrases in the generated text.
            logprobs (Optional[bool]): Whether to return the log probabilities of the tokens generated in the
                completion. Useful for model introspection and understanding the model's decision-making
                process. Note: This feature might not be available for all models.
            max_tokens (Optional[int]): The maximum number of tokens to generate in the completion. This limit
                includes the tokens in the prompt. Careful management of this parameter is crucial for
                controlling the length and computational cost of model operations.
            n (Optional[int]): The number of completions to generate for each prompt. Higher values allow for
                more diversity in the responses but increase computational cost. Balancing this parameter
                is key to achieving desired output variability while managing resource use.
            presence_penalty (Optional[float]): Encourages new content by penalizing token presence, with values
                from -2.0 to 2.0. This parameter influences the model to explore new topics and ideas,
                enhancing the creativity and variability of the output.
            response_format (Optional[ResponseFormat]): Specifies how the model's responses should be formatted.
                For example, responses can be structured as plain text, JSON objects, or other formats
                depending on the model's capabilities. This flexibility allows for tailored outputs to suit
                different applications and processing needs.
            seed (Optional[int]): Seed for deterministic randomness, ensuring same inputs yield consistent
                outputs. This feature is beneficial for reproducibility and debugging purposes, allowing
                users to obtain the same results from identical requests.
            stop (Optional[Union[str, List[str]]]): Sequences where the API will stop generating further tokens.
                This can be used to indicate the end of a message or section, providing a mechanism to
                control the scope and completion of the generated content.
            temperature (Optional[float]): Controls the randomness of the output. A lower temperature results in
                more deterministic output, while a higher temperature results in more diversity. Adjusting
                this parameter allows users to balance between predictability and creativity in the model's
                responses.
            tool_choice (Optional[ToolChoiceOptionParam]): Specifies which tool the model should use if it
                decides to make an external call. This replaces `function_call` and offers more granular
                control over the model's interactive capabilities.
            tools (Optional[Iterable[ToolParam]]): Lists tools available for response generation, including
                functions and APIs. This parameter expands the model's ability to incorporate external data
                and functionalities into its responses, broadening the scope of possible applications.
            top_logprobs (Optional[int]): Specifies the number of top logits to return, providing insight into
                the model's decision-making process. This information can be valuable for analyzing the
                model's preferences and the statistical distribution of its predictions.
            top_p (Optional[float]): Nucleus sampling strategy focusing on top P% probability mass, influencing
                token selection. This parameter adjusts the scope of the token set considered at each step,
                effectively adjusting the diversity and unpredictability of the output. A balance between
                coherence and variety can be achieved by tuning this parameter.
            user (Optional[str]): Identifies the end user of the API, aiding in monitoring usage patterns and
                detecting potential misuse. This parameter helps maintain the security and integrity of the
                system, ensuring that the API is used responsibly and in accordance with OpenAI's guidelines.
                [End user identification best practices](https://platform.openai.com/docs/guides/safety-best-practices/end user-ids)
            extra_headers (Optional[Headers]): Additional HTTP headers to send with the request. This allows for
                customizing the request headers for scenarios that require specific HTTP header entries.
            extra_query (Optional[Query]): Extra query parameters for the request URL. These parameters are
                appended to the URL query string, providing a flexible way to extend the request with
                additional data.
            extra_body (Optional[Body]): Additional body parameters to include in the POST request. This can be
                used to pass extra information that is not covered by the standard parameters.
            timeout (Optional[float | httpx.Timeout]): Custom timeout for the request, overriding the default.
                Setting this parameter ensures that operations adhere to specific timing requirements,
                preventing excessively long waits or premature termination of requests.
        """
        validate_response_format(response_format)
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )


class CompletionsWithRawResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = _legacy_response.to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithRawResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsWithStreamingResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithStreamingResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )


def validate_response_format(response_format: object) -> None:
    if inspect.isclass(response_format) and issubclass(response_format, pydantic.BaseModel):
        raise TypeError(
            "You tried to pass a `BaseModel` class to `chat.completions.create()`; You must use `beta.chat.completions.parse()` instead"
        )
