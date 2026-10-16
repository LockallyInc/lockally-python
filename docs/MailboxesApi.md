# lockally.MailboxesApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shared_member**](MailboxesApi.md#add_shared_member) | **POST** /v1/mailboxes/{email}/members | Add a shared mailbox member
[**create_mailbox**](MailboxesApi.md#create_mailbox) | **POST** /v1/mailboxes | Create a mailbox
[**delete_mailbox**](MailboxesApi.md#delete_mailbox) | **DELETE** /v1/mailboxes/{email} | Soft-delete a mailbox
[**delete_vacation_responder**](MailboxesApi.md#delete_vacation_responder) | **DELETE** /v1/mailboxes/{email}/vacation | Remove the vacation responder
[**download_mailbox_export**](MailboxesApi.md#download_mailbox_export) | **GET** /v1/mailboxes/{email}/export/download | Download a previously-issued mailbox export
[**export_mailbox**](MailboxesApi.md#export_mailbox) | **POST** /v1/mailboxes/{email}/export | Request a mailbox export
[**get_mailbox**](MailboxesApi.md#get_mailbox) | **GET** /v1/mailboxes/{email} | Get a mailbox
[**get_vacation_responder**](MailboxesApi.md#get_vacation_responder) | **GET** /v1/mailboxes/{email}/vacation | Get the vacation responder
[**list_mailboxes**](MailboxesApi.md#list_mailboxes) | **GET** /v1/mailboxes | List mailboxes
[**list_shared_members**](MailboxesApi.md#list_shared_members) | **GET** /v1/mailboxes/{email}/members | List shared mailbox members
[**list_vacation_responders**](MailboxesApi.md#list_vacation_responders) | **GET** /v1/vacation | List all vacation responders
[**remove_shared_member**](MailboxesApi.md#remove_shared_member) | **DELETE** /v1/mailboxes/{email}/members/{memberEmail} | Remove a shared mailbox member
[**set_vacation_responder**](MailboxesApi.md#set_vacation_responder) | **PUT** /v1/mailboxes/{email}/vacation | Set the vacation responder
[**update_mailbox**](MailboxesApi.md#update_mailbox) | **PATCH** /v1/mailboxes/{email} | Update a mailbox


# **add_shared_member**
> SharedMember add_shared_member(email, add_shared_member_request)

Add a shared mailbox member

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.add_shared_member_request import AddSharedMemberRequest
from lockally.models.shared_member import SharedMember
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 
    add_shared_member_request = lockally.AddSharedMemberRequest() # AddSharedMemberRequest | 

    try:
        # Add a shared mailbox member
        api_response = api_instance.add_shared_member(email, add_shared_member_request)
        print("The response of MailboxesApi->add_shared_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->add_shared_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **add_shared_member_request** | [**AddSharedMemberRequest**](AddSharedMemberRequest.md)|  | 

### Return type

[**SharedMember**](SharedMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Member added. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |
**409** | Already a member of this mailbox. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mailbox**
> Mailbox create_mailbox(create_mailbox_request)

Create a mailbox

Creates a mailbox on a tenant-verified domain. If `password` is
omitted, lockally generates a 16-char password and returns it in the
response, shown once.

**Gate.** The mailbox's domain must already be registered AND
verified for this tenant (via `/v1/domains` + `/v1/domains/{domain}/verify`).

**Idempotent.** Re-posting the same email returns the existing
mailbox UNTOUCHED, password is NOT regenerated. To change a
password, use PATCH instead.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.create_mailbox_request import CreateMailboxRequest
from lockally.models.mailbox import Mailbox
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
    api_instance = lockally.MailboxesApi(api_client)
    create_mailbox_request = lockally.CreateMailboxRequest() # CreateMailboxRequest | 

    try:
        # Create a mailbox
        api_response = api_instance.create_mailbox(create_mailbox_request)
        print("The response of MailboxesApi->create_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->create_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mailbox_request** | [**CreateMailboxRequest**](CreateMailboxRequest.md)|  | 

### Return type

[**Mailbox**](Mailbox.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mailbox already existed for this tenant (idempotent). |  -  |
**201** | Mailbox created. &#x60;password&#x60; is in the response ONLY if generated. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**409** | Email claimed by another tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mailbox**
> delete_mailbox(email)

Soft-delete a mailbox

Sets `soft_deleted_at = now()` and `hard_delete_after = now() + 90d`
per design D25. A background sweep (planned) will hard-delete after
the window. The mailbox is also disabled immediately.


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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 

    try:
        # Soft-delete a mailbox
        api_instance.delete_mailbox(email)
    except Exception as e:
        print("Exception when calling MailboxesApi->delete_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

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
**204** | Soft-deleted. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vacation_responder**
> delete_vacation_responder(email)

Remove the vacation responder

Idempotent, 204 whether or not a row existed.

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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 

    try:
        # Remove the vacation responder
        api_instance.delete_vacation_responder(email)
    except Exception as e:
        print("Exception when calling MailboxesApi->delete_vacation_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_mailbox_export**
> bytes download_mailbox_export(email, token)

Download a previously-issued mailbox export

Public endpoint (no Authorization header). Validates the one-shot
token from the URL, marks it used, and streams an mbox file. Second
GET with the same token returns 404, tokens are single-use.


### Example


```python
import lockally
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 
    token = 'token_example' # str | 

    try:
        # Download a previously-issued mailbox export
        api_response = api_instance.download_mailbox_export(email, token)
        print("The response of MailboxesApi->download_mailbox_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->download_mailbox_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **token** | **str**|  | 

### Return type

**bytes**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/mbox, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | mbox stream. |  -  |
**400** | Malformed request. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Token not found, already used, or expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_mailbox**
> ExportMailbox201Response export_mailbox(email)

Request a mailbox export

Issues a one-shot "presigned" download URL for the mailbox's content
in mbox format. The URL works without an Authorization header, the
token in the query string is the authz. TTL is 5 minutes; the token
is consumed on first GET.

**v1 caveat:** the synthesized mbox only contains outbound mail
(sent mail only). A later version will cover received mail
for full inbox + folder structure + flags. The endpoint contract
stays unchanged.

**Scope changed:** this used to accept `mailboxes:read`. It takes any
mailbox in the tenant and returns that mailbox's mail, so it now
requires `tenant:admin`, matching `POST /v1/ediscovery/export`. A key
scoped `mailboxes:read` gets 403 and has to be reissued; admin console
sessions are unaffected.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.export_mailbox201_response import ExportMailbox201Response
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 

    try:
        # Request a mailbox export
        api_response = api_instance.export_mailbox(email)
        print("The response of MailboxesApi->export_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->export_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**ExportMailbox201Response**](ExportMailbox201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Export token issued. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mailbox**
> Mailbox get_mailbox(email)

Get a mailbox

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.mailbox import Mailbox
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 

    try:
        # Get a mailbox
        api_response = api_instance.get_mailbox(email)
        print("The response of MailboxesApi->get_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->get_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**Mailbox**](Mailbox.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mailbox info. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vacation_responder**
> VacationResponder get_vacation_responder(email)

Get the vacation responder

Returns the stored vacation rule or 404 if none is set.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.vacation_responder import VacationResponder
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 

    try:
        # Get the vacation responder
        api_response = api_instance.get_vacation_responder(email)
        print("The response of MailboxesApi->get_vacation_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->get_vacation_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**VacationResponder**](VacationResponder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vacation responder. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mailboxes**
> ListMailboxes200Response list_mailboxes(limit=limit)

List mailboxes

Returns mailboxes under the calling tenant, active and soft-deleted.
`?limit=N` between 1 and 200 (default 50).


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_mailboxes200_response import ListMailboxes200Response
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
    api_instance = lockally.MailboxesApi(api_client)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List mailboxes
        api_response = api_instance.list_mailboxes(limit=limit)
        print("The response of MailboxesApi->list_mailboxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->list_mailboxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**ListMailboxes200Response**](ListMailboxes200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mailbox list. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_members**
> ListSharedMembers200Response list_shared_members(email)

List shared mailbox members

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_shared_members200_response import ListSharedMembers200Response
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 

    try:
        # List shared mailbox members
        api_response = api_instance.list_shared_members(email)
        print("The response of MailboxesApi->list_shared_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->list_shared_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**ListSharedMembers200Response**](ListSharedMembers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Members of the shared mailbox. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vacation_responders**
> ListVacationResponders200Response list_vacation_responders()

List all vacation responders

Returns every vacation responder for the calling tenant.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.list_vacation_responders200_response import ListVacationResponders200Response
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
    api_instance = lockally.MailboxesApi(api_client)

    try:
        # List all vacation responders
        api_response = api_instance.list_vacation_responders()
        print("The response of MailboxesApi->list_vacation_responders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->list_vacation_responders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListVacationResponders200Response**](ListVacationResponders200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shared_member**
> remove_shared_member(email, member_email)

Remove a shared mailbox member

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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 
    member_email = 'member_email_example' # str | 

    try:
        # Remove a shared mailbox member
        api_instance.remove_shared_member(email, member_email)
    except Exception as e:
        print("Exception when calling MailboxesApi->remove_shared_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **member_email** | **str**|  | 

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
**204** | No content |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vacation_responder**
> VacationResponder set_vacation_responder(email, set_vacation_responder_request)

Set the vacation responder

Upsert, same endpoint creates or replaces the rule. Clears
`synced_at`; the rule is staged until a later sync
pushes it to the mail server.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.set_vacation_responder_request import SetVacationResponderRequest
from lockally.models.vacation_responder import VacationResponder
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 
    set_vacation_responder_request = lockally.SetVacationResponderRequest() # SetVacationResponderRequest | 

    try:
        # Set the vacation responder
        api_response = api_instance.set_vacation_responder(email, set_vacation_responder_request)
        print("The response of MailboxesApi->set_vacation_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->set_vacation_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **set_vacation_responder_request** | [**SetVacationResponderRequest**](SetVacationResponderRequest.md)|  | 

### Return type

[**VacationResponder**](VacationResponder.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saved. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mailbox**
> Mailbox update_mailbox(email, update_mailbox_request)

Update a mailbox

Supply at least one of `password`, `quota_bytes`, `disabled`.
Returns the updated mailbox.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.mailbox import Mailbox
from lockally.models.update_mailbox_request import UpdateMailboxRequest
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
    api_instance = lockally.MailboxesApi(api_client)
    email = 'email_example' # str | 
    update_mailbox_request = lockally.UpdateMailboxRequest() # UpdateMailboxRequest | 

    try:
        # Update a mailbox
        api_response = api_instance.update_mailbox(email, update_mailbox_request)
        print("The response of MailboxesApi->update_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->update_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **update_mailbox_request** | [**UpdateMailboxRequest**](UpdateMailboxRequest.md)|  | 

### Return type

[**Mailbox**](Mailbox.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated mailbox. |  -  |
**400** | Malformed request. |  -  |
**401** | Missing, malformed, or invalid API key. |  -  |
**403** | API key lacks the required scope. |  -  |
**404** | Resource not found under the calling tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

