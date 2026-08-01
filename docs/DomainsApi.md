# lockally.DomainsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_domains_domain_delete**](DomainsApi.md#v1_domains_domain_delete) | **DELETE** /v1/domains/{domain} | Delete a domain
[**v1_domains_domain_get**](DomainsApi.md#v1_domains_domain_get) | **GET** /v1/domains/{domain} | Get a domain
[**v1_domains_domain_verify_post**](DomainsApi.md#v1_domains_domain_verify_post) | **POST** /v1/domains/{domain}/verify | Force-poll DNS verification
[**v1_domains_get**](DomainsApi.md#v1_domains_get) | **GET** /v1/domains | List domains
[**v1_domains_post**](DomainsApi.md#v1_domains_post) | **POST** /v1/domains | Register a domain


# **v1_domains_domain_delete**
> v1_domains_domain_delete(domain)

Delete a domain

Removes the domain registration. Refuses with 409 if any mailbox is
still attached — delete the mailboxes first.


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
    api_instance = lockally.DomainsApi(api_client)
    domain = 'domain_example' # str | 

    try:
        # Delete a domain
        api_instance.v1_domains_domain_delete(domain)
    except Exception as e:
        print("Exception when calling DomainsApi->v1_domains_domain_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

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
**409** | Domain still has mailboxes attached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domains_domain_get**
> Domain v1_domains_domain_get(domain)

Get a domain

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.domain import Domain
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
    api_instance = lockally.DomainsApi(api_client)
    domain = 'domain_example' # str | 

    try:
        # Get a domain
        api_response = api_instance.v1_domains_domain_get(domain)
        print("The response of DomainsApi->v1_domains_domain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->v1_domains_domain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain record including the DNS instructions to publish. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domains_domain_verify_post**
> Domain v1_domains_domain_verify_post(domain)

Force-poll DNS verification

Synchronously checks the `_lockally-verify.<domain>` TXT record
against the stored verification token. Returns 200 either way:
the returned `verified` boolean tells you whether DNS now confirms.
Caller polls until `verified: true`. In v2 a background worker
auto-polls and fires a `domain.verified` webhook.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.domain import Domain
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
    api_instance = lockally.DomainsApi(api_client)
    domain = 'domain_example' # str | 

    try:
        # Force-poll DNS verification
        api_response = api_instance.v1_domains_domain_verify_post(domain)
        print("The response of DomainsApi->v1_domains_domain_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->v1_domains_domain_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current domain state (possibly newly verified). |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |
**502** | Upstream DNS error (timeout, server unreachable). Retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domains_get**
> V1DomainsGet200Response v1_domains_get()

List domains

Returns every domain registered under the calling tenant.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_domains_get200_response import V1DomainsGet200Response
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
    api_instance = lockally.DomainsApi(api_client)

    try:
        # List domains
        api_response = api_instance.v1_domains_get()
        print("The response of DomainsApi->v1_domains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->v1_domains_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1DomainsGet200Response**](V1DomainsGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain list |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_domains_post**
> Domain v1_domains_post(v1_domains_post_request)

Register a domain

Registers a new domain for the calling tenant. Generates a DKIM
keypair and verification token. Returns DNS instructions the tenant
must publish under their own DNS (verification TXT, SPF include,
DKIM TXT, MX records to `mx1`/`mx2.lockally.com`, DMARC seed).

**Idempotent** — re-posting the same domain returns the existing
record with the same DKIM keys and token (regenerating would break
the tenant's published DNS). Returns 200 on idempotent hit, 201 on
first create.

Returns 409 if the domain is already claimed by a different tenant.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.domain import Domain
from lockally.models.v1_domains_post_request import V1DomainsPostRequest
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
    api_instance = lockally.DomainsApi(api_client)
    v1_domains_post_request = lockally.V1DomainsPostRequest() # V1DomainsPostRequest | 

    try:
        # Register a domain
        api_response = api_instance.v1_domains_post(v1_domains_post_request)
        print("The response of DomainsApi->v1_domains_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->v1_domains_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_domains_post_request** | [**V1DomainsPostRequest**](V1DomainsPostRequest.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain already registered to the calling tenant (idempotent). |  -  |
**201** | Domain created. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**409** | Domain claimed by another tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

