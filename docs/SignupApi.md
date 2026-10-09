# lockally.SignupApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signup**](SignupApi.md#signup) | **POST** /v1/signup | Sign up a new tenant


# **signup**
> V1AdminLoginPost200Response signup(signup_request)

Sign up a new tenant

### Example


```python
import lockally
from lockally.models.signup_request import SignupRequest
from lockally.models.v1_admin_login_post200_response import V1AdminLoginPost200Response
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
    api_instance = lockally.SignupApi(api_client)
    signup_request = lockally.SignupRequest() # SignupRequest | 

    try:
        # Sign up a new tenant
        api_response = api_instance.signup(signup_request)
        print("The response of SignupApi->signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignupApi->signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_request** | [**SignupRequest**](SignupRequest.md)|  | 

### Return type

[**V1AdminLoginPost200Response**](V1AdminLoginPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tenant created with initial admin and API token. |  -  |
**400** | Malformed request. |  -  |
**409** | Slug or email already taken. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

