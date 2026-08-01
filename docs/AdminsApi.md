# lockally.AdminsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_admins_get**](AdminsApi.md#v1_admins_get) | **GET** /v1/admins | List tenant admins
[**v1_admins_id_delete**](AdminsApi.md#v1_admins_id_delete) | **DELETE** /v1/admins/{id} | Delete an admin
[**v1_admins_id_patch**](AdminsApi.md#v1_admins_id_patch) | **PATCH** /v1/admins/{id} | Update an admin
[**v1_admins_post**](AdminsApi.md#v1_admins_post) | **POST** /v1/admins | Invite a new admin


# **v1_admins_get**
> V1AdminsGet200Response v1_admins_get()

List tenant admins

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_admins_get200_response import V1AdminsGet200Response
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
    api_instance = lockally.AdminsApi(api_client)

    try:
        # List tenant admins
        api_response = api_instance.v1_admins_get()
        print("The response of AdminsApi->v1_admins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->v1_admins_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1AdminsGet200Response**](V1AdminsGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Admin list. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_admins_id_delete**
> v1_admins_id_delete(id)

Delete an admin

Hard-delete. Cascade-drops the admin's sessions (immediate
revocation). Same safety rails as PATCH disabled=true.


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
    api_instance = lockally.AdminsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an admin
        api_instance.v1_admins_id_delete(id)
    except Exception as e:
        print("Exception when calling AdminsApi->v1_admins_id_delete: %s\n" % e)
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
**409** | Self-delete on session bearer, or last-admin safeguard. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_admins_id_patch**
> AdminFull v1_admins_id_patch(id, v1_admins_id_patch_request)

Update an admin

Supply at least one of `password`, `display_name`, `role`, `disabled`.

**Safety rails.** A session bearer (adm_sess_*) cannot disable
itself — use another admin or an API key (which bypasses the
self-rail). Disabling the last active admin returns 409 to prevent
orphaning the tenant from its console.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.admin_full import AdminFull
from lockally.models.v1_admins_id_patch_request import V1AdminsIdPatchRequest
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
    api_instance = lockally.AdminsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    v1_admins_id_patch_request = lockally.V1AdminsIdPatchRequest() # V1AdminsIdPatchRequest | 

    try:
        # Update an admin
        api_response = api_instance.v1_admins_id_patch(id, v1_admins_id_patch_request)
        print("The response of AdminsApi->v1_admins_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->v1_admins_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **v1_admins_id_patch_request** | [**V1AdminsIdPatchRequest**](V1AdminsIdPatchRequest.md)|  | 

### Return type

[**AdminFull**](AdminFull.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated admin. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |
**409** | Self-disable on session bearer, or last-admin safeguard. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_admins_post**
> AdminFull v1_admins_post(v1_admins_post_request)

Invite a new admin

Creates a new tenant admin. If `password` is omitted, lockally
generates a 16-char password and returns it ONCE in the response.
Email is case-insensitive and unique per tenant.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.admin_full import AdminFull
from lockally.models.v1_admins_post_request import V1AdminsPostRequest
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
    api_instance = lockally.AdminsApi(api_client)
    v1_admins_post_request = lockally.V1AdminsPostRequest() # V1AdminsPostRequest | 

    try:
        # Invite a new admin
        api_response = api_instance.v1_admins_post(v1_admins_post_request)
        print("The response of AdminsApi->v1_admins_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->v1_admins_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_admins_post_request** | [**V1AdminsPostRequest**](V1AdminsPostRequest.md)|  | 

### Return type

[**AdminFull**](AdminFull.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. &#x60;password&#x60; populated ONLY if generated. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**409** | Email already an admin on this tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

