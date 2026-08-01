# lockally.HealthApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthz_get**](HealthApi.md#healthz_get) | **GET** /healthz | Liveness check


# **healthz_get**
> HealthzGet200Response healthz_get()

Liveness check

Returns 200 if the process is up and the database pings cleanly. No authentication required.

### Example


```python
import lockally
from lockally.models.healthz_get200_response import HealthzGet200Response
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
    api_instance = lockally.HealthApi(api_client)

    try:
        # Liveness check
        api_response = api_instance.healthz_get()
        print("The response of HealthApi->healthz_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->healthz_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthzGet200Response**](HealthzGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Healthy |  -  |
**503** | Service is temporarily unable to handle the request (e.g. database unreachable). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

