# lockally.AdminApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_login**](AdminApi.md#admin_login) | **POST** /v1/admin/login | Tenant-admin email+password login
[**admin_logout**](AdminApi.md#admin_logout) | **POST** /v1/admin/logout | Invalidate the current admin session
[**get_current_admin**](AdminApi.md#get_current_admin) | **GET** /v1/admin/me | Get the current admin + tenant


# **admin_login**
> AdminLogin200Response admin_login(admin_login_request)

Tenant-admin email+password login

Exchanges an admin's email + password for a session token. The web
console at `app.lockally.com` posts this on form submission and
stores the returned token in an httpOnly cookie.

**No enumeration leak.** Wrong-email and wrong-password both return
the same 401 with title "Invalid credentials". The argon2id verify
runs even on lookup miss (well, structurally, the lookup fails fast
but the response shape is constant) so timing leaks are bounded.

Tokens are prefixed `adm_sess_` and valid for 7 days. Use as the
`Authorization: Bearer` value on all subsequent calls.


### Example


```python
import lockally
from lockally.models.admin_login200_response import AdminLogin200Response
from lockally.models.admin_login_request import AdminLoginRequest
from lockally.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lockally.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lockally.Configuration(
    host = "https://api.lockally.com"
)


# Enter a context with an instance of the API client
with lockally.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lockally.AdminApi(api_client)
    admin_login_request = lockally.AdminLoginRequest() # AdminLoginRequest | 

    try:
        # Tenant-admin email+password login
        api_response = api_instance.admin_login(admin_login_request)
        print("The response of AdminApi->admin_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_login_request** | [**AdminLoginRequest**](AdminLoginRequest.md)|  | 

### Return type

[**AdminLogin200Response**](AdminLogin200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authenticated. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_logout**
> admin_logout()

Invalidate the current admin session

Deletes the session row from the database. Idempotent, calling
logout on an already-invalid token returns 204 anyway.


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
    api_instance = lockally.AdminApi(api_client)

    try:
        # Invalidate the current admin session
        api_instance.admin_logout()
    except Exception as e:
        print("Exception when calling AdminApi->admin_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Logged out. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_admin**
> GetCurrentAdmin200Response get_current_admin()

Get the current admin + tenant

Returns the admin profile + tenant for the session token presented
in `Authorization: Bearer`. Used by the web console's layout load
function to populate the sidebar.

Returns 403 if called with an API key (lk_live_*) bearer, admin
context only exists for session tokens.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_current_admin200_response import GetCurrentAdmin200Response
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
    api_instance = lockally.AdminApi(api_client)

    try:
        # Get the current admin + tenant
        api_response = api_instance.get_current_admin()
        print("The response of AdminApi->get_current_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_current_admin: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCurrentAdmin200Response**](GetCurrentAdmin200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Admin + tenant. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

