# lockally.AiApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_ai_config_get**](AiApi.md#v1_ai_config_get) | **GET** /v1/ai-config | Read the tenant&#39;s AI configuration
[**v1_ai_config_put**](AiApi.md#v1_ai_config_put) | **PUT** /v1/ai-config | Configure the AI tier
[**v1_billing_ai_units_checkout_post**](AiApi.md#v1_billing_ai_units_checkout_post) | **POST** /v1/billing/ai-units/checkout | Buy prepaid AI units
[**v1_threads_thread_id_classify_post**](AiApi.md#v1_threads_thread_id_classify_post) | **POST** /v1/threads/{threadID}/classify | LLM-classify a thread


# **v1_ai_config_get**
> object v1_ai_config_get()

Read the tenant's AI configuration

Mode (off/byok/units), model, masked key hint, AI-unit balance, whether the units tier is available on this deployment.

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
    api_instance = lockally.AiApi(api_client)

    try:
        # Read the tenant's AI configuration
        api_response = api_instance.v1_ai_config_get()
        print("The response of AiApi->v1_ai_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->v1_ai_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI config |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ai_config_put**
> object v1_ai_config_put()

Configure the AI tier

Body: {"mode": "off|byok|units", "model": "...", "anthropic_key": "sk-ant-..."}. BYOK keys are stored AES-256-GCM encrypted; the cleartext is never returned. Omit anthropic_key to keep the stored one.

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
    api_instance = lockally.AiApi(api_client)

    try:
        # Configure the AI tier
        api_response = api_instance.v1_ai_config_put()
        print("The response of AiApi->v1_ai_config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->v1_ai_config_put: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_billing_ai_units_checkout_post**
> object v1_billing_ai_units_checkout_post()

Buy prepaid AI units

Body: {"bundle": "100|500|2000"}. One classification = one unit; bundles expire after 6 months. Admin session required. 503 until Paystack billing is configured.

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
    api_instance = lockally.AiApi(api_client)

    try:
        # Buy prepaid AI units
        api_response = api_instance.v1_billing_ai_units_checkout_post()
        print("The response of AiApi->v1_billing_ai_units_checkout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->v1_billing_ai_units_checkout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paystack authorization URL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_threads_thread_id_classify_post**
> object v1_threads_thread_id_classify_post(thread_id, refresh=refresh)

LLM-classify a thread

Returns {intent, urgency, summary, suggested_action} via the tenant's AI tier (BYOK or prepaid units — see /v1/ai-config). Cached per thread state: unchanged threads return the cache free; ?refresh=true forces a re-run. A failed model call charges nothing. 402 when the AI tier is off.

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
    api_instance = lockally.AiApi(api_client)
    thread_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    refresh = True # bool |  (optional)

    try:
        # LLM-classify a thread
        api_response = api_instance.v1_threads_thread_id_classify_post(thread_id, refresh=refresh)
        print("The response of AiApi->v1_threads_thread_id_classify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->v1_threads_thread_id_classify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**|  | 
 **refresh** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Classification |  -  |
**402** | AI tier not enabled / out of units |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

