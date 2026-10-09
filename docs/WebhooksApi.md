# lockally.WebhooksApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_webhooks_get**](WebhooksApi.md#v1_webhooks_get) | **GET** /v1/webhooks | List webhooks
[**v1_webhooks_id_delete**](WebhooksApi.md#v1_webhooks_id_delete) | **DELETE** /v1/webhooks/{id} | Delete a webhook
[**v1_webhooks_id_patch**](WebhooksApi.md#v1_webhooks_id_patch) | **PATCH** /v1/webhooks/{id} | Update a webhook
[**v1_webhooks_post**](WebhooksApi.md#v1_webhooks_post) | **POST** /v1/webhooks | Create a webhook


# **v1_webhooks_get**
> V1WebhooksGet200Response v1_webhooks_get()

List webhooks

Returns the calling tenant's webhook subscriptions. Never returns
the signing secret — only metadata.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_webhooks_get200_response import V1WebhooksGet200Response
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
    api_instance = lockally.WebhooksApi(api_client)

    try:
        # List webhooks
        api_response = api_instance.v1_webhooks_get()
        print("The response of WebhooksApi->v1_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->v1_webhooks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1WebhooksGet200Response**](V1WebhooksGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook list. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_webhooks_id_delete**
> v1_webhooks_id_delete(id)

Delete a webhook

Hard-delete; cascades to `webhook_deliveries` history.

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
    api_instance = lockally.WebhooksApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a webhook
        api_instance.v1_webhooks_id_delete(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->v1_webhooks_id_delete: %s\n" % e)
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
**204** | Deleted. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_webhooks_id_patch**
> Webhook v1_webhooks_id_patch(id, v1_webhooks_id_patch_request)

Update a webhook

Supply at least one of `url`, `events`, `paused`. Setting `paused`
to `false` ALSO resets `consecutive_failures` to 0 — re-arms the
50-failure auto-pause counter.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_webhooks_id_patch_request import V1WebhooksIdPatchRequest
from lockally.models.webhook import Webhook
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
    api_instance = lockally.WebhooksApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    v1_webhooks_id_patch_request = lockally.V1WebhooksIdPatchRequest() # V1WebhooksIdPatchRequest | 

    try:
        # Update a webhook
        api_response = api_instance.v1_webhooks_id_patch(id, v1_webhooks_id_patch_request)
        print("The response of WebhooksApi->v1_webhooks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->v1_webhooks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **v1_webhooks_id_patch_request** | [**V1WebhooksIdPatchRequest**](V1WebhooksIdPatchRequest.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated webhook. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_webhooks_post**
> Webhook v1_webhooks_post(v1_webhooks_post_request)

Create a webhook

Subscribes a URL to one or more event types. Returns the
`signing_secret` ONCE in the response — store it immediately.
The dispatcher signs every outbound POST per design L3:

    X-Lockally-Signature: t=<unix>,v1=<hex(hmac_sha256(secret, t + "." + body))>

Verify on your end using HMAC-SHA256 with a 5-minute timestamp
window (replay protection). A reference verifier ships in
[internal/webhook](https://github.com/ucheigwedinma/lockally/blob/main/internal/webhook/sign.go).

Event names: see the [event catalogue](https://github.com/ucheigwedinma/lockally/blob/main/docs/v1-design.md#64-webhook-event-catalogue-v1).


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_webhooks_post_request import V1WebhooksPostRequest
from lockally.models.webhook import Webhook
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
    api_instance = lockally.WebhooksApi(api_client)
    v1_webhooks_post_request = lockally.V1WebhooksPostRequest() # V1WebhooksPostRequest | 

    try:
        # Create a webhook
        api_response = api_instance.v1_webhooks_post(v1_webhooks_post_request)
        print("The response of WebhooksApi->v1_webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->v1_webhooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_webhooks_post_request** | [**V1WebhooksPostRequest**](V1WebhooksPostRequest.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. &#x60;signing_secret&#x60; is in the response ONLY here. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

