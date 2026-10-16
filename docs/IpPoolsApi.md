# lockally.IpPoolsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dedicated_ip_request**](IpPoolsApi.md#create_dedicated_ip_request) | **POST** /v1/dedicated-ip-requests | Request a dedicated IP
[**get_ip_assignment**](IpPoolsApi.md#get_ip_assignment) | **GET** /v1/ip-assignment | Get current IP assignment
[**list_dedicated_ip_requests**](IpPoolsApi.md#list_dedicated_ip_requests) | **GET** /v1/dedicated-ip-requests | List dedicated IP requests


# **create_dedicated_ip_request**
> DedicatedIPRequest create_dedicated_ip_request(create_dedicated_ip_request_request)

Request a dedicated IP

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.create_dedicated_ip_request_request import CreateDedicatedIPRequestRequest
from lockally.models.dedicated_ip_request import DedicatedIPRequest
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
    api_instance = lockally.IpPoolsApi(api_client)
    create_dedicated_ip_request_request = lockally.CreateDedicatedIPRequestRequest() # CreateDedicatedIPRequestRequest | 

    try:
        # Request a dedicated IP
        api_response = api_instance.create_dedicated_ip_request(create_dedicated_ip_request_request)
        print("The response of IpPoolsApi->create_dedicated_ip_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolsApi->create_dedicated_ip_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dedicated_ip_request_request** | [**CreateDedicatedIPRequestRequest**](CreateDedicatedIPRequestRequest.md)|  | 

### Return type

[**DedicatedIPRequest**](DedicatedIPRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dedicated IP request submitted. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**409** | A pending request already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_assignment**
> GetIPAssignment200Response get_ip_assignment()

Get current IP assignment

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_ip_assignment200_response import GetIPAssignment200Response
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
    api_instance = lockally.IpPoolsApi(api_client)

    try:
        # Get current IP assignment
        api_response = api_instance.get_ip_assignment()
        print("The response of IpPoolsApi->get_ip_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolsApi->get_ip_assignment: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIPAssignment200Response**](GetIPAssignment200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tenant&#39;s current outbound IP assignment. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dedicated_ip_requests**
> ListDedicatedIPRequests200Response list_dedicated_ip_requests()

List dedicated IP requests

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_dedicated_ip_requests200_response import ListDedicatedIPRequests200Response
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
    api_instance = lockally.IpPoolsApi(api_client)

    try:
        # List dedicated IP requests
        api_response = api_instance.list_dedicated_ip_requests()
        print("The response of IpPoolsApi->list_dedicated_ip_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolsApi->list_dedicated_ip_requests: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDedicatedIPRequests200Response**](ListDedicatedIPRequests200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dedicated IP request history. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

