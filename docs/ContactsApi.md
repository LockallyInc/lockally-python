# lockally.ContactsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /v1/contacts | Create a contact
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /v1/contacts/{id} | Delete a contact
[**get_contact**](ContactsApi.md#get_contact) | **GET** /v1/contacts/{id} | Get a contact
[**get_contact_lists**](ContactsApi.md#get_contact_lists) | **GET** /v1/contacts/{id}/lists | Get lists a contact belongs to
[**list_contacts**](ContactsApi.md#list_contacts) | **GET** /v1/contacts | List contacts
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /v1/contacts/{id} | Update a contact


# **create_contact**
> Contact create_contact(create_contact_request)

Create a contact

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.contact import Contact
from lockally.models.create_contact_request import CreateContactRequest
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
    api_instance = lockally.ContactsApi(api_client)
    create_contact_request = lockally.CreateContactRequest() # CreateContactRequest | 

    try:
        # Create a contact
        api_response = api_instance.create_contact(create_contact_request)
        print("The response of ContactsApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_request** | [**CreateContactRequest**](CreateContactRequest.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contact created |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete a contact

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
    api_instance = lockally.ContactsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a contact
        api_instance.delete_contact(id)
    except Exception as e:
        print("Exception when calling ContactsApi->delete_contact: %s\n" % e)
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
**204** | Contact deleted |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> Contact get_contact(id)

Get a contact

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.contact import Contact
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
    api_instance = lockally.ContactsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a contact
        api_response = api_instance.get_contact(id)
        print("The response of ContactsApi->get_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact details |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_lists**
> GetContactLists200Response get_contact_lists(id)

Get lists a contact belongs to

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.get_contact_lists200_response import GetContactLists200Response
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
    api_instance = lockally.ContactsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get lists a contact belongs to
        api_response = api_instance.get_contact_lists(id)
        print("The response of ContactsApi->get_contact_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contact_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**GetContactLists200Response**](GetContactLists200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lists containing this contact |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> ListContacts200Response list_contacts(q=q, type=type, department=department, status=status, source=source)

List contacts

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_contacts200_response import ListContacts200Response
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
    api_instance = lockally.ContactsApi(api_client)
    q = 'q_example' # str | Free-text search across name, email, company (optional)
    type = 'type_example' # str | Filter by contact_type (optional)
    department = 'department_example' # str | Filter by department (optional)
    status = 'status_example' # str | Filter by status (optional)
    source = 'source_example' # str | Filter by source (optional)

    try:
        # List contacts
        api_response = api_instance.list_contacts(q=q, type=type, department=department, status=status, source=source)
        print("The response of ContactsApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->list_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free-text search across name, email, company | [optional] 
 **type** | **str**| Filter by contact_type | [optional] 
 **department** | **str**| Filter by department | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **source** | **str**| Filter by source | [optional] 

### Return type

[**ListContacts200Response**](ListContacts200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of contacts |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> Contact update_contact(id, update_contact_request)

Update a contact

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.contact import Contact
from lockally.models.update_contact_request import UpdateContactRequest
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
    api_instance = lockally.ContactsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_contact_request = lockally.UpdateContactRequest() # UpdateContactRequest | 

    try:
        # Update a contact
        api_response = api_instance.update_contact(id, update_contact_request)
        print("The response of ContactsApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **update_contact_request** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact updated |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

