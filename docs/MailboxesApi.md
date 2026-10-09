# lockally.MailboxesApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shared_member**](MailboxesApi.md#add_shared_member) | **POST** /v1/mailboxes/{email}/members | Add a shared mailbox member
[**list_shared_members**](MailboxesApi.md#list_shared_members) | **GET** /v1/mailboxes/{email}/members | List shared mailbox members
[**remove_shared_member**](MailboxesApi.md#remove_shared_member) | **DELETE** /v1/mailboxes/{email}/members/{memberEmail} | Remove a shared mailbox member
[**v1_mailboxes_email_delete**](MailboxesApi.md#v1_mailboxes_email_delete) | **DELETE** /v1/mailboxes/{email} | Soft-delete a mailbox
[**v1_mailboxes_email_export_download_get**](MailboxesApi.md#v1_mailboxes_email_export_download_get) | **GET** /v1/mailboxes/{email}/export/download | Download a previously-issued mailbox export
[**v1_mailboxes_email_export_post**](MailboxesApi.md#v1_mailboxes_email_export_post) | **POST** /v1/mailboxes/{email}/export | Request a mailbox export
[**v1_mailboxes_email_get**](MailboxesApi.md#v1_mailboxes_email_get) | **GET** /v1/mailboxes/{email} | Get a mailbox
[**v1_mailboxes_email_patch**](MailboxesApi.md#v1_mailboxes_email_patch) | **PATCH** /v1/mailboxes/{email} | Update a mailbox
[**v1_mailboxes_email_vacation_delete**](MailboxesApi.md#v1_mailboxes_email_vacation_delete) | **DELETE** /v1/mailboxes/{email}/vacation | Remove the vacation responder
[**v1_mailboxes_email_vacation_get**](MailboxesApi.md#v1_mailboxes_email_vacation_get) | **GET** /v1/mailboxes/{email}/vacation | Get the vacation responder
[**v1_mailboxes_email_vacation_put**](MailboxesApi.md#v1_mailboxes_email_vacation_put) | **PUT** /v1/mailboxes/{email}/vacation | Set the vacation responder
[**v1_mailboxes_get**](MailboxesApi.md#v1_mailboxes_get) | **GET** /v1/mailboxes | List mailboxes
[**v1_mailboxes_post**](MailboxesApi.md#v1_mailboxes_post) | **POST** /v1/mailboxes | Create a mailbox
[**v1_vacation_get**](MailboxesApi.md#v1_vacation_get) | **GET** /v1/vacation | List all vacation responders


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

# **v1_mailboxes_email_delete**
> v1_mailboxes_email_delete(email)

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
        api_instance.v1_mailboxes_email_delete(email)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_delete: %s\n" % e)
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

# **v1_mailboxes_email_export_download_get**
> bytes v1_mailboxes_email_export_download_get(email, token)

Download a previously-issued mailbox export

Public endpoint (no Authorization header). Validates the one-shot
token from the URL, marks it used, and streams an mbox file. Second
GET with the same token returns 404 — tokens are single-use.


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
        api_response = api_instance.v1_mailboxes_email_export_download_get(email, token)
        print("The response of MailboxesApi->v1_mailboxes_email_export_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_export_download_get: %s\n" % e)
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

# **v1_mailboxes_email_export_post**
> V1MailboxesEmailExportPost201Response v1_mailboxes_email_export_post(email)

Request a mailbox export

Issues a one-shot "presigned" download URL for the mailbox's content
in mbox format. The URL works without an Authorization header — the
token in the query string is the authz. TTL is 5 minutes; the token
is consumed on first GET.

**v1 caveat:** the synthesized mbox only contains outbound mail
(from `lockally.messages`). v2 swaps in Stalwart's export primitive
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
from lockally.models.v1_mailboxes_email_export_post201_response import V1MailboxesEmailExportPost201Response
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
        api_response = api_instance.v1_mailboxes_email_export_post(email)
        print("The response of MailboxesApi->v1_mailboxes_email_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**V1MailboxesEmailExportPost201Response**](V1MailboxesEmailExportPost201Response.md)

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

# **v1_mailboxes_email_get**
> Mailbox v1_mailboxes_email_get(email)

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
        api_response = api_instance.v1_mailboxes_email_get(email)
        print("The response of MailboxesApi->v1_mailboxes_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_get: %s\n" % e)
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

# **v1_mailboxes_email_patch**
> Mailbox v1_mailboxes_email_patch(email, v1_mailboxes_email_patch_request)

Update a mailbox

Supply at least one of `password`, `quota_bytes`, `disabled`.
Returns the updated mailbox.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.mailbox import Mailbox
from lockally.models.v1_mailboxes_email_patch_request import V1MailboxesEmailPatchRequest
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
    v1_mailboxes_email_patch_request = lockally.V1MailboxesEmailPatchRequest() # V1MailboxesEmailPatchRequest | 

    try:
        # Update a mailbox
        api_response = api_instance.v1_mailboxes_email_patch(email, v1_mailboxes_email_patch_request)
        print("The response of MailboxesApi->v1_mailboxes_email_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **v1_mailboxes_email_patch_request** | [**V1MailboxesEmailPatchRequest**](V1MailboxesEmailPatchRequest.md)|  | 

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

# **v1_mailboxes_email_vacation_delete**
> v1_mailboxes_email_vacation_delete(email)

Remove the vacation responder

Idempotent — 204 whether or not a row existed.

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
        api_instance.v1_mailboxes_email_vacation_delete(email)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_vacation_delete: %s\n" % e)
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

# **v1_mailboxes_email_vacation_get**
> VacationResponder v1_mailboxes_email_vacation_get(email)

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
        api_response = api_instance.v1_mailboxes_email_vacation_get(email)
        print("The response of MailboxesApi->v1_mailboxes_email_vacation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_vacation_get: %s\n" % e)
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

# **v1_mailboxes_email_vacation_put**
> VacationResponder v1_mailboxes_email_vacation_put(email, v1_mailboxes_email_vacation_put_request)

Set the vacation responder

Upsert — same endpoint creates or replaces the rule. Clears
`synced_at`; the rule is staged on lockally until a sync worker
pushes it to the mail server.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_mailboxes_email_vacation_put_request import V1MailboxesEmailVacationPutRequest
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
    v1_mailboxes_email_vacation_put_request = lockally.V1MailboxesEmailVacationPutRequest() # V1MailboxesEmailVacationPutRequest | 

    try:
        # Set the vacation responder
        api_response = api_instance.v1_mailboxes_email_vacation_put(email, v1_mailboxes_email_vacation_put_request)
        print("The response of MailboxesApi->v1_mailboxes_email_vacation_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_email_vacation_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **v1_mailboxes_email_vacation_put_request** | [**V1MailboxesEmailVacationPutRequest**](V1MailboxesEmailVacationPutRequest.md)|  | 

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

# **v1_mailboxes_get**
> V1MailboxesGet200Response v1_mailboxes_get(limit=limit)

List mailboxes

Returns mailboxes under the calling tenant — active and soft-deleted.
`?limit=N` between 1 and 200 (default 50).


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_mailboxes_get200_response import V1MailboxesGet200Response
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
        api_response = api_instance.v1_mailboxes_get(limit=limit)
        print("The response of MailboxesApi->v1_mailboxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**V1MailboxesGet200Response**](V1MailboxesGet200Response.md)

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

# **v1_mailboxes_post**
> Mailbox v1_mailboxes_post(v1_mailboxes_post_request)

Create a mailbox

Creates a mailbox on a tenant-verified domain. If `password` is
omitted, lockally generates a 16-char password and returns it in the
response — shown once.

**Gate.** The mailbox's domain must already be registered AND
verified for this tenant (via `/v1/domains` + `/v1/domains/{domain}/verify`).

**Idempotent.** Re-posting the same email returns the existing
mailbox UNTOUCHED — password is NOT regenerated. To change a
password, use PATCH instead.


### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.mailbox import Mailbox
from lockally.models.v1_mailboxes_post_request import V1MailboxesPostRequest
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
    v1_mailboxes_post_request = lockally.V1MailboxesPostRequest() # V1MailboxesPostRequest | 

    try:
        # Create a mailbox
        api_response = api_instance.v1_mailboxes_post(v1_mailboxes_post_request)
        print("The response of MailboxesApi->v1_mailboxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_mailboxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_mailboxes_post_request** | [**V1MailboxesPostRequest**](V1MailboxesPostRequest.md)|  | 

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

# **v1_vacation_get**
> V1VacationGet200Response v1_vacation_get()

List all vacation responders

Returns every vacation responder for the calling tenant.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_vacation_get200_response import V1VacationGet200Response
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
        api_response = api_instance.v1_vacation_get()
        print("The response of MailboxesApi->v1_vacation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->v1_vacation_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1VacationGet200Response**](V1VacationGet200Response.md)

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

