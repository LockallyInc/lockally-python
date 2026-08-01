# lockally.TenantApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_tenant_get**](TenantApi.md#v1_tenant_get) | **GET** /v1/tenant | Get the calling tenant
[**v1_usage_get**](TenantApi.md#v1_usage_get) | **GET** /v1/usage | Usage snapshot


# **v1_tenant_get**
> Tenant v1_tenant_get()

Get the calling tenant

Returns the tenant the presented API key belongs to.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.tenant import Tenant
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
    api_instance = lockally.TenantApi(api_client)

    try:
        # Get the calling tenant
        api_response = api_instance.v1_tenant_get()
        print("The response of TenantApi->v1_tenant_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->v1_tenant_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Tenant**](Tenant.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant info |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_usage_get**
> V1UsageGet200Response v1_usage_get()

Usage snapshot

Returns the tenant's current usage + cap consumption. Designed for
poll-based alerting on the integrator side (e.g. "warn when daily
quota is 80% used"). Refreshed live from Postgres — there is no
cache, so callers should poll at most once per minute.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_usage_get200_response import V1UsageGet200Response
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
    api_instance = lockally.TenantApi(api_client)

    try:
        # Usage snapshot
        api_response = api_instance.v1_usage_get()
        print("The response of TenantApi->v1_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->v1_usage_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UsageGet200Response**](V1UsageGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage snapshot |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

