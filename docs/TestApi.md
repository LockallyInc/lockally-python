# lockally.TestApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simulate_inbound_email**](TestApi.md#simulate_inbound_email) | **POST** /v1/test/inbound | Simulate an inbound email (test keys only)


# **simulate_inbound_email**
> SimulatedInbound simulate_inbound_email()

Simulate an inbound email (test keys only)

Runs a synthetic message through the REAL indexing pipeline — thread adoption, deterministic extraction (incl. injection_risk), and the message.received webhook — so the whole agent loop is testable without a real domain or MTA. Requires an lk_test_* key (create with {"test": true} on POST /v1/api-keys). Body: {mailbox, from, subject, text, in_reply_to?, references?}.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.simulated_inbound import SimulatedInbound
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
    api_instance = lockally.TestApi(api_client)

    try:
        # Simulate an inbound email (test keys only)
        api_response = api_instance.simulate_inbound_email()
        print("The response of TestApi->simulate_inbound_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->simulate_inbound_email: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SimulatedInbound**](SimulatedInbound.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Simulated message indexed (thread_id, annotations) |  -  |
**403** | Live key used — test keys only |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

