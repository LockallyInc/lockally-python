# lockally.AliasesApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_aliases_address_delete**](AliasesApi.md#v1_aliases_address_delete) | **DELETE** /v1/aliases/{address} | Delete an alias
[**v1_aliases_get**](AliasesApi.md#v1_aliases_get) | **GET** /v1/aliases | List aliases
[**v1_aliases_post**](AliasesApi.md#v1_aliases_post) | **POST** /v1/aliases | Create an alias


# **v1_aliases_address_delete**
> v1_aliases_address_delete(address)

Delete an alias

Hard-delete (no soft-delete window — aliases are cheap to recreate).

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
    api_instance = lockally.AliasesApi(api_client)
    address = 'address_example' # str | 

    try:
        # Delete an alias
        api_instance.v1_aliases_address_delete(address)
    except Exception as e:
        print("Exception when calling AliasesApi->v1_aliases_address_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

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

# **v1_aliases_get**
> V1AliasesGet200Response v1_aliases_get()

List aliases

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_aliases_get200_response import V1AliasesGet200Response
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
    api_instance = lockally.AliasesApi(api_client)

    try:
        # List aliases
        api_response = api_instance.v1_aliases_get()
        print("The response of AliasesApi->v1_aliases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->v1_aliases_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1AliasesGet200Response**](V1AliasesGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alias list. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_aliases_post**
> Alias v1_aliases_post(v1_aliases_post_request)

Create an alias

Creates an email alias. `alias_address` must be on a verified
tenant-owned domain and must not be the address of an existing mailbox
(live, suspended or deleted). `alias_target` must be an active mailbox
in the same workspace; forwarding to an address Lockally does not host
is not supported. The alias delivers as soon as the call returns.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.alias import Alias
from lockally.models.v1_aliases_post_request import V1AliasesPostRequest
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
    api_instance = lockally.AliasesApi(api_client)
    v1_aliases_post_request = lockally.V1AliasesPostRequest() # V1AliasesPostRequest | 

    try:
        # Create an alias
        api_response = api_instance.v1_aliases_post(v1_aliases_post_request)
        print("The response of AliasesApi->v1_aliases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AliasesApi->v1_aliases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_aliases_post_request** | [**V1AliasesPostRequest**](V1AliasesPostRequest.md)|  | 

### Return type

[**Alias**](Alias.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Alias created. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**409** | Alias address already exists, or is a mailbox&#39;s own address. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

