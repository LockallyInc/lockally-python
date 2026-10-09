# lockally.AddOnsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_add_on**](AddOnsApi.md#activate_add_on) | **POST** /v1/add-ons/{name}/activate | Activate an add-on
[**cancel_add_on**](AddOnsApi.md#cancel_add_on) | **POST** /v1/add-ons/{name}/cancel | Cancel an add-on
[**get_add_on_status**](AddOnsApi.md#get_add_on_status) | **GET** /v1/add-ons/{name} | Get add-on status
[**list_add_ons**](AddOnsApi.md#list_add_ons) | **GET** /v1/add-ons | List add-ons


# **activate_add_on**
> ActivateAddOn200Response activate_add_on(name)

Activate an add-on

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.activate_add_on200_response import ActivateAddOn200Response
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
    api_instance = lockally.AddOnsApi(api_client)
    name = 'name_example' # str | Add-on key

    try:
        # Activate an add-on
        api_response = api_instance.activate_add_on(name)
        print("The response of AddOnsApi->activate_add_on:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnsApi->activate_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Add-on key | 

### Return type

[**ActivateAddOn200Response**](ActivateAddOn200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add-on activated. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_add_on**
> cancel_add_on(name)

Cancel an add-on

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
    api_instance = lockally.AddOnsApi(api_client)
    name = 'name_example' # str | Add-on key

    try:
        # Cancel an add-on
        api_instance.cancel_add_on(name)
    except Exception as e:
        print("Exception when calling AddOnsApi->cancel_add_on: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Add-on key | 

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
**204** | No content |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_add_on_status**
> GetAddOnStatus200Response get_add_on_status(name)

Get add-on status

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_add_on_status200_response import GetAddOnStatus200Response
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
    api_instance = lockally.AddOnsApi(api_client)
    name = 'name_example' # str | Add-on key

    try:
        # Get add-on status
        api_response = api_instance.get_add_on_status(name)
        print("The response of AddOnsApi->get_add_on_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnsApi->get_add_on_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Add-on key | 

### Return type

[**GetAddOnStatus200Response**](GetAddOnStatus200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add-on eligibility and activation state. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_add_ons**
> ListAddOns200Response list_add_ons()

List add-ons

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_add_ons200_response import ListAddOns200Response
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
    api_instance = lockally.AddOnsApi(api_client)

    try:
        # List add-ons
        api_response = api_instance.list_add_ons()
        print("The response of AddOnsApi->list_add_ons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnsApi->list_add_ons: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAddOns200Response**](ListAddOns200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available add-ons and their activation state. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

