# lockally.SuppressionsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_suppressions_email_delete**](SuppressionsApi.md#v1_suppressions_email_delete) | **DELETE** /v1/suppressions/{email} | Remove a suppression
[**v1_suppressions_email_get**](SuppressionsApi.md#v1_suppressions_email_get) | **GET** /v1/suppressions/{email} | Check whether an address is suppressed
[**v1_suppressions_get**](SuppressionsApi.md#v1_suppressions_get) | **GET** /v1/suppressions | List suppressed recipients
[**v1_suppressions_post**](SuppressionsApi.md#v1_suppressions_post) | **POST** /v1/suppressions | Add a suppression


# **v1_suppressions_email_delete**
> v1_suppressions_email_delete(email)

Remove a suppression

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
    api_instance = lockally.SuppressionsApi(api_client)
    email = 'email_example' # str | 

    try:
        # Remove a suppression
        api_instance.v1_suppressions_email_delete(email)
    except Exception as e:
        print("Exception when calling SuppressionsApi->v1_suppressions_email_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

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
**204** | Removed. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_suppressions_email_get**
> Suppression v1_suppressions_email_get(email)

Check whether an address is suppressed

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.suppression import Suppression
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
    api_instance = lockally.SuppressionsApi(api_client)
    email = 'email_example' # str | 

    try:
        # Check whether an address is suppressed
        api_response = api_instance.v1_suppressions_email_get(email)
        print("The response of SuppressionsApi->v1_suppressions_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->v1_suppressions_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**Suppression**](Suppression.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppressed. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_suppressions_get**
> V1SuppressionsGet200Response v1_suppressions_get(reason=reason, cursor=cursor, limit=limit)

List suppressed recipients

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_suppressions_get200_response import V1SuppressionsGet200Response
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
    api_instance = lockally.SuppressionsApi(api_client)
    reason = 'reason_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List suppressed recipients
        api_response = api_instance.v1_suppressions_get(reason=reason, cursor=cursor, limit=limit)
        print("The response of SuppressionsApi->v1_suppressions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->v1_suppressions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reason** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**V1SuppressionsGet200Response**](V1SuppressionsGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppressions. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_suppressions_post**
> Suppression v1_suppressions_post(v1_suppressions_post_request)

Add a suppression

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.suppression import Suppression
from lockally.models.v1_suppressions_post_request import V1SuppressionsPostRequest
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
    api_instance = lockally.SuppressionsApi(api_client)
    v1_suppressions_post_request = lockally.V1SuppressionsPostRequest() # V1SuppressionsPostRequest | 

    try:
        # Add a suppression
        api_response = api_instance.v1_suppressions_post(v1_suppressions_post_request)
        print("The response of SuppressionsApi->v1_suppressions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->v1_suppressions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_suppressions_post_request** | [**V1SuppressionsPostRequest**](V1SuppressionsPostRequest.md)|  | 

### Return type

[**Suppression**](Suppression.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added. |  -  |
**400** | Malformed request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

