# lockally.TenantApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant**](TenantApi.md#get_tenant) | **GET** /v1/tenant | Get the calling tenant
[**get_tracking_policy**](TenantApi.md#get_tracking_policy) | **GET** /v1/tracking | Get the engagement tracking policy
[**get_usage**](TenantApi.md#get_usage) | **GET** /v1/usage | Usage snapshot
[**update_tracking_policy**](TenantApi.md#update_tracking_policy) | **PUT** /v1/tracking | Update the engagement tracking policy


# **get_tenant**
> Tenant get_tenant()

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
        api_response = api_instance.get_tenant()
        print("The response of TenantApi->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant: %s\n" % e)
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

# **get_tracking_policy**
> TrackingPolicy get_tracking_policy()

Get the engagement tracking policy

Whether open and click tracking are enabled for this account. **Both
are off until switched on**, and an account that has never set a policy
reads as off rather than as an error.

`configured` reports whether this deployment holds a signing secret.
Without one no tracking token can be minted or verified, so tracking
cannot work however the flags are set, and a caller seeing
`track_opens: true` with nothing arriving deserves to know why.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.tracking_policy import TrackingPolicy
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
        # Get the engagement tracking policy
        api_response = api_instance.get_tracking_policy()
        print("The response of TenantApi->get_tracking_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tracking_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TrackingPolicy**](TrackingPolicy.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The policy. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage**
> GetUsage200Response get_usage()

Usage snapshot

Returns the tenant's current usage + cap consumption. Designed for
poll-based alerting on the integrator side (e.g. "warn when daily
quota is 80% used"). Computed live on request, so there is no
cache, so callers should poll at most once per minute.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_usage200_response import GetUsage200Response
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
        api_response = api_instance.get_usage()
        print("The response of TenantApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUsage200Response**](GetUsage200Response.md)

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

# **update_tracking_policy**
> TrackingPolicy update_tracking_policy(update_tracking_policy_request)

Update the engagement tracking policy

Enables or disables tracking for the account. Send either flag or both;
an omitted flag is left unchanged rather than reset.

**Enabling this changes what Lockally collects about your recipients**,
who have no relationship with us. You are the controller for them. What
is collected is a user-agent string, a timestamp, and for a click the
destination URL: **no IP address**, ever. The change is written to your
audit log.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.tracking_policy import TrackingPolicy
from lockally.models.update_tracking_policy_request import UpdateTrackingPolicyRequest
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
    update_tracking_policy_request = lockally.UpdateTrackingPolicyRequest() # UpdateTrackingPolicyRequest | 

    try:
        # Update the engagement tracking policy
        api_response = api_instance.update_tracking_policy(update_tracking_policy_request)
        print("The response of TenantApi->update_tracking_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_tracking_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tracking_policy_request** | [**UpdateTrackingPolicyRequest**](UpdateTrackingPolicyRequest.md)|  | 

### Return type

[**TrackingPolicy**](TrackingPolicy.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated policy. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

