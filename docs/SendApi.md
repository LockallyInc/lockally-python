# lockally.SendApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_messages_get**](SendApi.md#v1_messages_get) | **GET** /v1/messages | List outbound messages
[**v1_messages_id_delete**](SendApi.md#v1_messages_id_delete) | **DELETE** /v1/messages/{id} | Cancel a scheduled send
[**v1_messages_id_get**](SendApi.md#v1_messages_id_get) | **GET** /v1/messages/{id} | Get message status
[**v1_messages_stats_get**](SendApi.md#v1_messages_stats_get) | **GET** /v1/messages/stats | Aggregate delivery stats
[**v1_send_batch_post**](SendApi.md#v1_send_batch_post) | **POST** /v1/send/batch | Send a batch of emails
[**v1_send_post**](SendApi.md#v1_send_post) | **POST** /v1/send | Send an email


# **v1_messages_get**
> V1MessagesGet200Response v1_messages_get(status=status, sender=sender, q=q, since=since, cursor=cursor, limit=limit)

List outbound messages

Returns recent outbound messages for the calling tenant, sorted
newest first. Backs the send-status pill in the SvelteKit /sends
view and the outbound search box.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_messages_get200_response import V1MessagesGet200Response
from lockally.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lockally.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lockally.Configuration(
    host = "https://api.lockally.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (lk_live_<prefix>_<secret>): bearerAuth
configuration = lockally.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lockally.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lockally.SendApi(api_client)
    status = 'status_example' # str |  (optional)
    sender = 'sender_example' # str | Exact match against the `from` mailbox. (optional)
    q = 'q_example' # str | Free-text search across subject + sender. (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only messages queued at or after this RFC 3339 instant. (optional)
    cursor = 'cursor_example' # str | queued_at of the prior page boundary. Pass back the `next_cursor` returned by the previous call. (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List outbound messages
        api_response = api_instance.v1_messages_get(status=status, sender=sender, q=q, since=since, cursor=cursor, limit=limit)
        print("The response of SendApi->v1_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->v1_messages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **sender** | **str**| Exact match against the &#x60;from&#x60; mailbox. | [optional] 
 **q** | **str**| Free-text search across subject + sender. | [optional] 
 **since** | **datetime**| Only messages queued at or after this RFC 3339 instant. | [optional] 
 **cursor** | **str**| queued_at of the prior page boundary. Pass back the &#x60;next_cursor&#x60; returned by the previous call. | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**V1MessagesGet200Response**](V1MessagesGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of messages + optional next-page cursor. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_messages_id_delete**
> v1_messages_id_delete(id)

Cancel a scheduled send

Cancels a still-scheduled message (future queued_at). Already sending/sent → 409.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lockally.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lockally.Configuration(
    host = "https://api.lockally.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (lk_live_<prefix>_<secret>): bearerAuth
configuration = lockally.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lockally.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lockally.SendApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Cancel a scheduled send
        api_instance.v1_messages_id_delete(id)
    except Exception as e:
        print("Exception when calling SendApi->v1_messages_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cancelled. |  -  |
**404** | Resource not found under the calling tenant. |  -  |
**409** | Not cancellable (already sending or sent). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_messages_id_get**
> Message v1_messages_id_get(id)

Get message status

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.message import Message
from lockally.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lockally.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lockally.Configuration(
    host = "https://api.lockally.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (lk_live_<prefix>_<secret>): bearerAuth
configuration = lockally.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lockally.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lockally.SendApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get message status
        api_response = api_instance.v1_messages_id_get(id)
        print("The response of SendApi->v1_messages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->v1_messages_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**Message**](Message.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message record. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_messages_stats_get**
> MessageStats v1_messages_stats_get(var_from=var_from, to=to, domain=domain)

Aggregate delivery stats

Counts by delivery outcome (delivered/bounced/deferred/complaint) plus
rates over a window, from the delivery-event store. Privacy-first: this
reflects what receiving servers reported, NOT whether a human opened the
mail — Lockally does no open/click tracking.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.message_stats import MessageStats
from lockally.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lockally.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lockally.Configuration(
    host = "https://api.lockally.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (lk_live_<prefix>_<secret>): bearerAuth
configuration = lockally.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lockally.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lockally.SendApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Window start (default 7 days ago). (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Window end (default now). (optional)
    domain = 'domain_example' # str | Filter by sender domain. (optional)

    try:
        # Aggregate delivery stats
        api_response = api_instance.v1_messages_stats_get(var_from=var_from, to=to, domain=domain)
        print("The response of SendApi->v1_messages_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->v1_messages_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Window start (default 7 days ago). | [optional] 
 **to** | **datetime**| Window end (default now). | [optional] 
 **domain** | **str**| Filter by sender domain. | [optional] 

### Return type

[**MessageStats**](MessageStats.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stats. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_send_batch_post**
> V1SendBatchPost200Response v1_send_batch_post(idempotency_key, v1_send_batch_post_request)

Send a batch of emails

Sends up to 500 messages in one call. Each is validated and enqueued
independently — a bad message fails only its own slot (partial success,
HTTP 200). One `Idempotency-Key` header covers the batch; per-message
keys are derived as `<key>:<index>`.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_send_batch_post200_response import V1SendBatchPost200Response
from lockally.models.v1_send_batch_post_request import V1SendBatchPostRequest
from lockally.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lockally.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lockally.Configuration(
    host = "https://api.lockally.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (lk_live_<prefix>_<secret>): bearerAuth
configuration = lockally.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lockally.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lockally.SendApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | 
    v1_send_batch_post_request = lockally.V1SendBatchPostRequest() # V1SendBatchPostRequest | 

    try:
        # Send a batch of emails
        api_response = api_instance.v1_send_batch_post(idempotency_key, v1_send_batch_post_request)
        print("The response of SendApi->v1_send_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->v1_send_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | 
 **v1_send_batch_post_request** | [**V1SendBatchPostRequest**](V1SendBatchPostRequest.md)|  | 

### Return type

[**V1SendBatchPost200Response**](V1SendBatchPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-message results (partial success). |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_send_post**
> V1SendPost202Response v1_send_post(idempotency_key, v1_send_post_request)

Send an email

Submits an email for delivery via lockally. Returns 202 immediately
once the message is accepted into lockally's queue; the actual SMTP
submission to the recipient is async. Track delivery via
`GET /v1/messages/{id}` or webhook subscriptions for
`delivery.delivered` / `delivery.bounced` / `delivery.complaint`.

**Idempotency-Key required.** Per design L7 — any unique string per
send, 24-hour dedupe window. Repeated calls with the same key
return byte-exact the original response and do NOT create a
duplicate message.

**Sender authorisation.** `from` must be a non-disabled mailbox
owned by the calling tenant on a verified domain. Sending from
aliases is not yet supported.

**Rate cap.** Per-tenant `rate_cap_per_min` (returned on
`/v1/tenant`) is enforced — 429 with `Retry-After: 60` once tripped.

**Recipient warning.** Over 25 total recipients (To+Cc+Bcc) sets a
`warning` field in the response — large fan-outs queue noticeably
at scale. Hard cap is 100/send.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_send_post202_response import V1SendPost202Response
from lockally.models.v1_send_post_request import V1SendPostRequest
from lockally.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lockally.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lockally.Configuration(
    host = "https://api.lockally.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (lk_live_<prefix>_<secret>): bearerAuth
configuration = lockally.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lockally.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lockally.SendApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | 
    v1_send_post_request = lockally.V1SendPostRequest() # V1SendPostRequest | 

    try:
        # Send an email
        api_response = api_instance.v1_send_post(idempotency_key, v1_send_post_request)
        print("The response of SendApi->v1_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->v1_send_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | 
 **v1_send_post_request** | [**V1SendPostRequest**](V1SendPostRequest.md)|  | 

### Return type

[**V1SendPost202Response**](V1SendPost202Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Queued. |  * Idempotent-Replay - \&quot;true\&quot; when the response is replayed from the idempotency cache. <br>  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**429** | Per-tenant rate cap exceeded. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

