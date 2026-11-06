# lockally.ApiKeysApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeysApi.md#create_api_key) | **POST** /v1/api-keys | Create an API key
[**list_api_keys**](ApiKeysApi.md#list_api_keys) | **GET** /v1/api-keys | List API keys
[**revoke_api_key**](ApiKeysApi.md#revoke_api_key) | **DELETE** /v1/api-keys/{id} | Revoke an API key
[**rotate_api_key**](ApiKeysApi.md#rotate_api_key) | **POST** /v1/api-keys/{id}/rotate | Rotate an API key
[**update_api_key**](ApiKeysApi.md#update_api_key) | **PATCH** /v1/api-keys/{id} | Update an API key


# **create_api_key**
> CreateApiKey201Response create_api_key(create_api_key_request)

Create an API key

Provisions a fresh API key for the calling tenant.

**The full `secret` is included in this response ONLY**, store it
immediately. The cleartext secret is not recoverable from the
argon2id hash kept server-side; rotate by creating a new key and
revoking the old one.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.create_api_key201_response import CreateApiKey201Response
from lockally.models.create_api_key_request import CreateApiKeyRequest
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
    api_instance = lockally.ApiKeysApi(api_client)
    create_api_key_request = lockally.CreateApiKeyRequest() # CreateApiKeyRequest | 

    try:
        # Create an API key
        api_response = api_instance.create_api_key(create_api_key_request)
        print("The response of ApiKeysApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | 

### Return type

[**CreateApiKey201Response**](CreateApiKey201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Key created, &#x60;secret&#x60; is in the response and shown only here. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ListApiKeys200Response list_api_keys(sort=sort, order=order)

List API keys

Returns all API keys (active and revoked) belonging to the calling
tenant. The `secret` is **never** returned, only prefix + metadata.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_api_keys200_response import ListApiKeys200Response
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
    api_instance = lockally.ApiKeysApi(api_client)
    sort = created_at # str | Field to order by. This list holds tens of rows per account, so every column is offered and none needs an index. (optional) (default to created_at)
    order = 'order_example' # str | Defaults to desc for the default field and asc for any other. Always tie-broken on id, so the order is total. (optional)

    try:
        # List API keys
        api_response = api_instance.list_api_keys(sort=sort, order=order)
        print("The response of ApiKeysApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->list_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Field to order by. This list holds tens of rows per account, so every column is offered and none needs an index. | [optional] [default to created_at]
 **order** | **str**| Defaults to desc for the default field and asc for any other. Always tie-broken on id, so the order is total. | [optional] 

### Return type

[**ListApiKeys200Response**](ListApiKeys200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key list |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key**
> revoke_api_key(id)

Revoke an API key

Soft-deletes (sets `revoked_at`) on the named key. The row stays for
audit purposes; the key no longer authenticates.

You **cannot revoke the key currently being used** to make this
call, that would lock you out. Use a different `tenant:admin` key.


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
    api_instance = lockally.ApiKeysApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Revoke an API key
        api_instance.revoke_api_key(id)
    except Exception as e:
        print("Exception when calling ApiKeysApi->revoke_api_key: %s\n" % e)
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
**204** | Revoked. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |
**409** | Refused, key is the one in use for this request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_api_key**
> CreateApiKey201Response rotate_api_key(id, rotate_api_key_request=rotate_api_key_request)

Rotate an API key

Issues a successor key and puts a short expiry on this one, so **both
work until the overlap ends**. That window is the point: without it,
rotation is revocation with extra steps and every caller has to swap
credentials in the same instant.

The successor inherits this key's scopes, its label (the label names
the integration, and the integration has not changed) and its test
flag. Its full `secret` is in this response and nowhere else.

The response's `expires_at` is the **predecessor's** deadline, so you
can see from the rotation itself how long you have to cut over.

A key that has already been rotated cannot be rotated again: chaining
overlaps would leave several live keys for one integration, which is
the opposite of the intent. Rotate the successor instead.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.create_api_key201_response import CreateApiKey201Response
from lockally.models.rotate_api_key_request import RotateApiKeyRequest
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
    api_instance = lockally.ApiKeysApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    rotate_api_key_request = lockally.RotateApiKeyRequest() # RotateApiKeyRequest |  (optional)

    try:
        # Rotate an API key
        api_response = api_instance.rotate_api_key(id, rotate_api_key_request=rotate_api_key_request)
        print("The response of ApiKeysApi->rotate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->rotate_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **rotate_api_key_request** | [**RotateApiKeyRequest**](RotateApiKeyRequest.md)|  | [optional] 

### Return type

[**CreateApiKey201Response**](CreateApiKey201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successor key. Its &#x60;secret&#x60; is shown only here; &#x60;expires_at&#x60; is the predecessor&#39;s deadline. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |
**409** | The key is revoked, or was already rotated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> APIKey update_api_key(id, update_api_key_request)

Update an API key

Changes a key's label, scopes or expiry in place, without reissuing the
secret.

**Every field is optional and absent means unchanged.** Renaming a key
does not clear its expiry. For `expires_at` there are three distinct
requests: omit the field to leave the expiry alone, send a timestamp to
set one, and send an explicit `null` to remove one.

Scopes are replaced wholesale, not merged. This endpoint does not
restrict which scopes you may grant, because `POST /v1/api-keys` never
has either: a key with `tenant:admin` can already mint a key with any
scope, so `tenant:admin` is root-equivalent for key management.

A revoked key cannot be updated.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.api_key import APIKey
from lockally.models.update_api_key_request import UpdateApiKeyRequest
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
    api_instance = lockally.ApiKeysApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_api_key_request = lockally.UpdateApiKeyRequest() # UpdateApiKeyRequest | 

    try:
        # Update an API key
        api_response = api_instance.update_api_key(id, update_api_key_request)
        print("The response of ApiKeysApi->update_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->update_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **update_api_key_request** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)|  | 

### Return type

[**APIKey**](APIKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated key. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |
**409** | The key is revoked and cannot be changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

