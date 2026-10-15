# lockally.SendApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_message**](SendApi.md#cancel_message) | **DELETE** /v1/messages/{id} | Cancel a scheduled send
[**get_message**](SendApi.md#get_message) | **GET** /v1/messages/{id} | Get message status
[**get_message_stats**](SendApi.md#get_message_stats) | **GET** /v1/messages/stats | Aggregate delivery stats
[**list_messages**](SendApi.md#list_messages) | **GET** /v1/messages | List outbound messages
[**send_email**](SendApi.md#send_email) | **POST** /v1/send | Send an email
[**send_email_batch**](SendApi.md#send_email_batch) | **POST** /v1/send/batch | Send a batch of emails


# **cancel_message**
> cancel_message(id)

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
        api_instance.cancel_message(id)
    except Exception as e:
        print("Exception when calling SendApi->cancel_message: %s\n" % e)
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

# **get_message**
> MessageDetail get_message(id)

Get message status

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.message_detail import MessageDetail
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
        api_response = api_instance.get_message(id)
        print("The response of SendApi->get_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->get_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**MessageDetail**](MessageDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message record with the content captured at send time. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_stats**
> MessageStats get_message_stats(var_from=var_from, to=to, domain=domain)

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
        api_response = api_instance.get_message_stats(var_from=var_from, to=to, domain=domain)
        print("The response of SendApi->get_message_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->get_message_stats: %s\n" % e)
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

# **list_messages**
> ListMessages200Response list_messages(status=status, sender=sender, q=q, since=since, cursor=cursor, limit=limit)

List outbound messages

Returns recent outbound messages for the calling tenant, sorted
newest first. Backs the send-status pill in the SvelteKit /sends
view and the outbound search box.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_messages200_response import ListMessages200Response
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
        api_response = api_instance.list_messages(status=status, sender=sender, q=q, since=since, cursor=cursor, limit=limit)
        print("The response of SendApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->list_messages: %s\n" % e)
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

[**ListMessages200Response**](ListMessages200Response.md)

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

# **send_email**
> SendEmail200Response send_email(idempotency_key, send_email_request)

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

**Sender authorisation.** `from` must be an address the calling
tenant owns on a verified domain. A mailbox always qualifies. On
business and combined accounts an **alias** qualifies too, so a
send-only address such as `no-reply@` need not be a billed seat.
An alias on an unverified domain, or one belonging to another
account, is refused with `403`. A catch-all creates no aliases and
so grants no sending rights.

**Rate cap.** Per-tenant `rate_cap_per_min` (returned on
`/v1/tenant`) is enforced — 429 with `Retry-After: 60` once tripped.

**Recipient warning.** Over 25 total recipients (To+Cc+Bcc) sets a
`warning` field in the response — large fan-outs queue noticeably
at scale. Hard cap is 100/send.

**Not every success is a 202.** Check the status code, not just the
body. A `200` means nothing was queued: either every recipient was
already suppressed, or the call used a test key and the send was
simulated. Both are successes, and neither produces a real delivery.
See the `200` response below.

**Warm-up headers.** While the platform is in its outbound warm-up
ramp, accepted sends carry `X-Warmup-Day`, `X-Warmup-Daily-Cap` and
`X-Warmup-Used-Today`. They describe a platform-wide cap shared by
every tenant, not your own allowance, and they disappear once the
ramp finishes. Hitting the cap returns 429.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.send_email200_response import SendEmail200Response
from lockally.models.send_email_request import SendEmailRequest
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
    send_email_request = lockally.SendEmailRequest() # SendEmailRequest | 

    try:
        # Send an email
        api_response = api_instance.send_email(idempotency_key, send_email_request)
        print("The response of SendApi->send_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | 
 **send_email_request** | [**SendEmailRequest**](SendEmailRequest.md)|  | 

### Return type

[**SendEmail200Response**](SendEmail200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted, but nothing was queued for real delivery. Two cases, told apart by &#x60;status&#x60;:  - &#x60;suppressed&#x60; — every recipient was on your suppression list, so   the send was dropped. Deliberately a success, not a retryable   error: retrying cannot change the outcome. There is no &#x60;id&#x60; or   &#x60;message_id&#x60;, because no message was created. Complaint and   bounce suppressions block every send; unsubscribe and manual   suppressions block only opt-in sends (&#x60;unsubscribe: true&#x60;). - &#x60;delivered&#x60; — the call used a test key (&#x60;lk_test_&#x60;). The message   is recorded and a &#x60;delivery.delivered&#x60; webhook fires with a   simulated &#x60;250 OK&#x60;, but nothing leaves the platform. Test sends   count against nothing: not your rate cap, allowance, send units,   the warm-up ramp, or your reputation.  |  -  |
**202** | Queued for delivery. |  * Idempotent-Replay - \&quot;true\&quot; when the response is replayed from the idempotency cache. <br>  * X-Warmup-Day - Present only during the platform&#39;s outbound warm-up ramp: which day of the ramp this send landed on. <br>  * X-Warmup-Daily-Cap - Warm-up ramp only: total messages the whole platform may send today, shared across all tenants. <br>  * X-Warmup-Used-Today - Warm-up ramp only: how much of that platform-wide cap was already used when this send was accepted. <br>  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**429** | Rate limited. Either your per-tenant &#x60;rate_cap_per_min&#x60;, or the platform-wide warm-up cap for the day (which resets at UTC midnight, so &#x60;Retry-After&#x60; can be hours rather than 60 seconds).  |  * Retry-After - 60 for the per-tenant cap; seconds until UTC midnight when the warm-up cap is what was hit. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_batch**
> SendEmailBatch200Response send_email_batch(idempotency_key, send_email_batch_request)

Send a batch of emails

Sends up to 500 messages in one call. Each is validated and enqueued
independently — a bad message fails only its own slot (partial success,
HTTP 200). One `Idempotency-Key` header covers the batch; per-message
keys are derived as `<key>:<index>`.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.send_email_batch200_response import SendEmailBatch200Response
from lockally.models.send_email_batch_request import SendEmailBatchRequest
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
    send_email_batch_request = lockally.SendEmailBatchRequest() # SendEmailBatchRequest | 

    try:
        # Send a batch of emails
        api_response = api_instance.send_email_batch(idempotency_key, send_email_batch_request)
        print("The response of SendApi->send_email_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SendApi->send_email_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | 
 **send_email_batch_request** | [**SendEmailBatchRequest**](SendEmailBatchRequest.md)|  | 

### Return type

[**SendEmailBatch200Response**](SendEmailBatch200Response.md)

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

