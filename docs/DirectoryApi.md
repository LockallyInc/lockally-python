# lockally.DirectoryApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_directory_activity**](DirectoryApi.md#get_directory_activity) | **GET** /v1/directory-activity | Get recent directory activity
[**get_directory_permissions**](DirectoryApi.md#get_directory_permissions) | **GET** /v1/directory-permissions | Get directory permission settings
[**get_directory_stats**](DirectoryApi.md#get_directory_stats) | **GET** /v1/directory-stats | Get directory statistics
[**get_gal_settings**](DirectoryApi.md#get_gal_settings) | **GET** /v1/gal-settings | Get Global Address List settings
[**rebuild_gal_index**](DirectoryApi.md#rebuild_gal_index) | **POST** /v1/gal-settings/rebuild-index | Rebuild the GAL search index
[**sync_gal**](DirectoryApi.md#sync_gal) | **POST** /v1/gal-settings/sync | Sync GAL with external directory sources
[**update_directory_permissions**](DirectoryApi.md#update_directory_permissions) | **PATCH** /v1/directory-permissions | Update directory permission settings
[**update_gal_settings**](DirectoryApi.md#update_gal_settings) | **PATCH** /v1/gal-settings | Update GAL settings


# **get_directory_activity**
> GetDirectoryActivity200Response get_directory_activity()

Get recent directory activity

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_directory_activity200_response import GetDirectoryActivity200Response
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
    api_instance = lockally.DirectoryApi(api_client)

    try:
        # Get recent directory activity
        api_response = api_instance.get_directory_activity()
        print("The response of DirectoryApi->get_directory_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->get_directory_activity: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDirectoryActivity200Response**](GetDirectoryActivity200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recent directory activity |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_permissions**
> DirectoryPermissions get_directory_permissions()

Get directory permission settings

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.directory_permissions import DirectoryPermissions
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
    api_instance = lockally.DirectoryApi(api_client)

    try:
        # Get directory permission settings
        api_response = api_instance.get_directory_permissions()
        print("The response of DirectoryApi->get_directory_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->get_directory_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DirectoryPermissions**](DirectoryPermissions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Directory permissions |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_stats**
> GetDirectoryStats200Response get_directory_stats()

Get directory statistics

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_directory_stats200_response import GetDirectoryStats200Response
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
    api_instance = lockally.DirectoryApi(api_client)

    try:
        # Get directory statistics
        api_response = api_instance.get_directory_stats()
        print("The response of DirectoryApi->get_directory_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->get_directory_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDirectoryStats200Response**](GetDirectoryStats200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Directory statistics |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gal_settings**
> GALSettings get_gal_settings()

Get Global Address List settings

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.gal_settings import GALSettings
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
    api_instance = lockally.DirectoryApi(api_client)

    try:
        # Get Global Address List settings
        api_response = api_instance.get_gal_settings()
        print("The response of DirectoryApi->get_gal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->get_gal_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GALSettings**](GALSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GAL settings |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild_gal_index**
> GALSettings rebuild_gal_index()

Rebuild the GAL search index

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.gal_settings import GALSettings
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
    api_instance = lockally.DirectoryApi(api_client)

    try:
        # Rebuild the GAL search index
        api_response = api_instance.rebuild_gal_index()
        print("The response of DirectoryApi->rebuild_gal_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->rebuild_gal_index: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GALSettings**](GALSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GAL settings after index rebuild |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_gal**
> GALSettings sync_gal()

Sync GAL with external directory sources

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.gal_settings import GALSettings
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
    api_instance = lockally.DirectoryApi(api_client)

    try:
        # Sync GAL with external directory sources
        api_response = api_instance.sync_gal()
        print("The response of DirectoryApi->sync_gal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->sync_gal: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GALSettings**](GALSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GAL settings after sync |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_directory_permissions**
> DirectoryPermissions update_directory_permissions(update_directory_permissions_request)

Update directory permission settings

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.directory_permissions import DirectoryPermissions
from lockally.models.update_directory_permissions_request import UpdateDirectoryPermissionsRequest
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
    api_instance = lockally.DirectoryApi(api_client)
    update_directory_permissions_request = lockally.UpdateDirectoryPermissionsRequest() # UpdateDirectoryPermissionsRequest | 

    try:
        # Update directory permission settings
        api_response = api_instance.update_directory_permissions(update_directory_permissions_request)
        print("The response of DirectoryApi->update_directory_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->update_directory_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_directory_permissions_request** | [**UpdateDirectoryPermissionsRequest**](UpdateDirectoryPermissionsRequest.md)|  | 

### Return type

[**DirectoryPermissions**](DirectoryPermissions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Directory permissions updated |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gal_settings**
> GALSettings update_gal_settings(update_gal_settings_request)

Update GAL settings

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.gal_settings import GALSettings
from lockally.models.update_gal_settings_request import UpdateGALSettingsRequest
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
    api_instance = lockally.DirectoryApi(api_client)
    update_gal_settings_request = lockally.UpdateGALSettingsRequest() # UpdateGALSettingsRequest | 

    try:
        # Update GAL settings
        api_response = api_instance.update_gal_settings(update_gal_settings_request)
        print("The response of DirectoryApi->update_gal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryApi->update_gal_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_gal_settings_request** | [**UpdateGALSettingsRequest**](UpdateGALSettingsRequest.md)|  | 

### Return type

[**GALSettings**](GALSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GAL settings updated |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

