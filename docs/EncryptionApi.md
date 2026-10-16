# lockally.EncryptionApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_lookup_public_keys**](EncryptionApi.md#batch_lookup_public_keys) | **GET** /v1/encryption/keys/lookup | Batch-lookup public keys by email
[**create_encryption_key**](EncryptionApi.md#create_encryption_key) | **POST** /v1/encryption/keys | Upload an encryption key pair
[**create_encryption_recovery**](EncryptionApi.md#create_encryption_recovery) | **POST** /v1/encryption/recovery | Store an encryption recovery blob
[**get_encryption_key**](EncryptionApi.md#get_encryption_key) | **GET** /v1/encryption/keys/{email} | Get encryption key for a mailbox
[**rotate_encryption_key**](EncryptionApi.md#rotate_encryption_key) | **POST** /v1/encryption/keys/rotate | Rotate an encryption key


# **batch_lookup_public_keys**
> BatchLookupPublicKeys200Response batch_lookup_public_keys(emails)

Batch-lookup public keys by email

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.batch_lookup_public_keys200_response import BatchLookupPublicKeys200Response
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
    api_instance = lockally.EncryptionApi(api_client)
    emails = 'emails_example' # str | Comma-separated list of email addresses

    try:
        # Batch-lookup public keys by email
        api_response = api_instance.batch_lookup_public_keys(emails)
        print("The response of EncryptionApi->batch_lookup_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->batch_lookup_public_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emails** | **str**| Comma-separated list of email addresses | 

### Return type

[**BatchLookupPublicKeys200Response**](BatchLookupPublicKeys200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public keys for requested emails |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_encryption_key**
> CreateEncryptionKey201Response create_encryption_key(create_encryption_key_request)

Upload an encryption key pair

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.create_encryption_key201_response import CreateEncryptionKey201Response
from lockally.models.create_encryption_key_request import CreateEncryptionKeyRequest
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
    api_instance = lockally.EncryptionApi(api_client)
    create_encryption_key_request = lockally.CreateEncryptionKeyRequest() # CreateEncryptionKeyRequest | 

    try:
        # Upload an encryption key pair
        api_response = api_instance.create_encryption_key(create_encryption_key_request)
        print("The response of EncryptionApi->create_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->create_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_encryption_key_request** | [**CreateEncryptionKeyRequest**](CreateEncryptionKeyRequest.md)|  | 

### Return type

[**CreateEncryptionKey201Response**](CreateEncryptionKey201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Key pair stored |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_encryption_recovery**
> create_encryption_recovery(create_encryption_recovery_request)

Store an encryption recovery blob

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.create_encryption_recovery_request import CreateEncryptionRecoveryRequest
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
    api_instance = lockally.EncryptionApi(api_client)
    create_encryption_recovery_request = lockally.CreateEncryptionRecoveryRequest() # CreateEncryptionRecoveryRequest | 

    try:
        # Store an encryption recovery blob
        api_instance.create_encryption_recovery(create_encryption_recovery_request)
    except Exception as e:
        print("Exception when calling EncryptionApi->create_encryption_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_encryption_recovery_request** | [**CreateEncryptionRecoveryRequest**](CreateEncryptionRecoveryRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Recovery blob stored |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_encryption_key**
> GetEncryptionKey200Response get_encryption_key(email)

Get encryption key for a mailbox

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_encryption_key200_response import GetEncryptionKey200Response
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
    api_instance = lockally.EncryptionApi(api_client)
    email = 'email_example' # str | 

    try:
        # Get encryption key for a mailbox
        api_response = api_instance.get_encryption_key(email)
        print("The response of EncryptionApi->get_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->get_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**GetEncryptionKey200Response**](GetEncryptionKey200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Encryption key details |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_encryption_key**
> rotate_encryption_key(rotate_encryption_key_request)

Rotate an encryption key

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.rotate_encryption_key_request import RotateEncryptionKeyRequest
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
    api_instance = lockally.EncryptionApi(api_client)
    rotate_encryption_key_request = lockally.RotateEncryptionKeyRequest() # RotateEncryptionKeyRequest | 

    try:
        # Rotate an encryption key
        api_instance.rotate_encryption_key(rotate_encryption_key_request)
    except Exception as e:
        print("Exception when calling EncryptionApi->rotate_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rotate_encryption_key_request** | [**RotateEncryptionKeyRequest**](RotateEncryptionKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Key rotated |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

