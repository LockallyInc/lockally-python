# lockally.DistributionListsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_distribution_list**](DistributionListsApi.md#create_distribution_list) | **POST** /v1/distribution-lists | Create a distribution list
[**delete_distribution_list**](DistributionListsApi.md#delete_distribution_list) | **DELETE** /v1/distribution-lists/{address} | Delete a distribution list
[**get_distribution_list**](DistributionListsApi.md#get_distribution_list) | **GET** /v1/distribution-lists/{address} | Get a distribution list
[**list_distribution_lists**](DistributionListsApi.md#list_distribution_lists) | **GET** /v1/distribution-lists | List distribution lists
[**replace_distribution_list_members**](DistributionListsApi.md#replace_distribution_list_members) | **PUT** /v1/distribution-lists/{address}/members | Replace distribution list members


# **create_distribution_list**
> DistributionListDetail create_distribution_list(create_distribution_list_request)

Create a distribution list

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.create_distribution_list_request import CreateDistributionListRequest
from lockally.models.distribution_list_detail import DistributionListDetail
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
    api_instance = lockally.DistributionListsApi(api_client)
    create_distribution_list_request = lockally.CreateDistributionListRequest() # CreateDistributionListRequest | 

    try:
        # Create a distribution list
        api_response = api_instance.create_distribution_list(create_distribution_list_request)
        print("The response of DistributionListsApi->create_distribution_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionListsApi->create_distribution_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_distribution_list_request** | [**CreateDistributionListRequest**](CreateDistributionListRequest.md)|  | 

### Return type

[**DistributionListDetail**](DistributionListDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Distribution list created. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**409** | List address already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_distribution_list**
> delete_distribution_list(address)

Delete a distribution list

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
    api_instance = lockally.DistributionListsApi(api_client)
    address = 'address_example' # str | Distribution list email address

    try:
        # Delete a distribution list
        api_instance.delete_distribution_list(address)
    except Exception as e:
        print("Exception when calling DistributionListsApi->delete_distribution_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Distribution list email address | 

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

# **get_distribution_list**
> DistributionListDetail get_distribution_list(address)

Get a distribution list

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.distribution_list_detail import DistributionListDetail
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
    api_instance = lockally.DistributionListsApi(api_client)
    address = 'address_example' # str | Distribution list email address

    try:
        # Get a distribution list
        api_response = api_instance.get_distribution_list(address)
        print("The response of DistributionListsApi->get_distribution_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionListsApi->get_distribution_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Distribution list email address | 

### Return type

[**DistributionListDetail**](DistributionListDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Distribution list with full member list. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_distribution_lists**
> ListDistributionLists200Response list_distribution_lists()

List distribution lists

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_distribution_lists200_response import ListDistributionLists200Response
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
    api_instance = lockally.DistributionListsApi(api_client)

    try:
        # List distribution lists
        api_response = api_instance.list_distribution_lists()
        print("The response of DistributionListsApi->list_distribution_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionListsApi->list_distribution_lists: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDistributionLists200Response**](ListDistributionLists200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All distribution lists for the tenant. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_distribution_list_members**
> ReplaceDistributionListMembers200Response replace_distribution_list_members(address, replace_distribution_list_members_request)

Replace distribution list members

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.replace_distribution_list_members200_response import ReplaceDistributionListMembers200Response
from lockally.models.replace_distribution_list_members_request import ReplaceDistributionListMembersRequest
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
    api_instance = lockally.DistributionListsApi(api_client)
    address = 'address_example' # str | Distribution list email address
    replace_distribution_list_members_request = lockally.ReplaceDistributionListMembersRequest() # ReplaceDistributionListMembersRequest | 

    try:
        # Replace distribution list members
        api_response = api_instance.replace_distribution_list_members(address, replace_distribution_list_members_request)
        print("The response of DistributionListsApi->replace_distribution_list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionListsApi->replace_distribution_list_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Distribution list email address | 
 **replace_distribution_list_members_request** | [**ReplaceDistributionListMembersRequest**](ReplaceDistributionListMembersRequest.md)|  | 

### Return type

[**ReplaceDistributionListMembers200Response**](ReplaceDistributionListMembers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated member list. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

