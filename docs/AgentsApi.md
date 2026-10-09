# lockally.AgentsApi

All URIs are relative to *https://api.lockally.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_api_keys_key_id_mailboxes_get**](AgentsApi.md#v1_api_keys_key_id_mailboxes_get) | **GET** /v1/api-keys/{keyID}/mailboxes | List a key&#39;s mailbox grants
[**v1_api_keys_key_id_mailboxes_mailbox_id_delete**](AgentsApi.md#v1_api_keys_key_id_mailboxes_mailbox_id_delete) | **DELETE** /v1/api-keys/{keyID}/mailboxes/{mailboxID} | Revoke a mailbox grant
[**v1_api_keys_key_id_mailboxes_post**](AgentsApi.md#v1_api_keys_key_id_mailboxes_post) | **POST** /v1/api-keys/{keyID}/mailboxes | Grant a mailbox to a key
[**v1_auth_whoami_get**](AgentsApi.md#v1_auth_whoami_get) | **GET** /v1/auth/whoami | Introspect the calling credentials
[**v1_contacts_lookup_get**](AgentsApi.md#v1_contacts_lookup_get) | **GET** /v1/contacts/lookup | Who is this sender?
[**v1_inboxes_get**](AgentsApi.md#v1_inboxes_get) | **GET** /v1/inboxes | List granted inboxes
[**v1_inboxes_mailbox_messages_post**](AgentsApi.md#v1_inboxes_mailbox_messages_post) | **POST** /v1/inboxes/{mailbox}/messages | Start a new conversation (agent stream)
[**v1_inboxes_mailbox_threads_get**](AgentsApi.md#v1_inboxes_mailbox_threads_get) | **GET** /v1/inboxes/{mailbox}/threads | List conversation threads
[**v1_threads_thread_id_get**](AgentsApi.md#v1_threads_thread_id_get) | **GET** /v1/threads/{threadID} | Get a whole conversation
[**v1_threads_thread_id_messages_message_id_attachments_idx_get**](AgentsApi.md#v1_threads_thread_id_messages_message_id_attachments_idx_get) | **GET** /v1/threads/{threadID}/messages/{messageID}/attachments/{idx} | Download an attachment
[**v1_threads_thread_id_messages_message_id_get**](AgentsApi.md#v1_threads_thread_id_messages_message_id_get) | **GET** /v1/threads/{threadID}/messages/{messageID} | Get one message with body
[**v1_threads_thread_id_messages_message_id_read_post**](AgentsApi.md#v1_threads_thread_id_messages_message_id_read_post) | **POST** /v1/threads/{threadID}/messages/{messageID}/read | Mark read/unread
[**v1_threads_thread_id_reply_post**](AgentsApi.md#v1_threads_thread_id_reply_post) | **POST** /v1/threads/{threadID}/reply | Reply in-thread (agent stream)


# **v1_api_keys_key_id_mailboxes_get**
> object v1_api_keys_key_id_mailboxes_get(key_id)

List a key's mailbox grants

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
    api_instance = lockally.AgentsApi(api_client)
    key_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # List a key's mailbox grants
        api_response = api_instance.v1_api_keys_key_id_mailboxes_get(key_id)
        print("The response of AgentsApi->v1_api_keys_key_id_mailboxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_api_keys_key_id_mailboxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Grants |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_api_keys_key_id_mailboxes_mailbox_id_delete**
> v1_api_keys_key_id_mailboxes_mailbox_id_delete(key_id, mailbox_id)

Revoke a mailbox grant

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
    api_instance = lockally.AgentsApi(api_client)
    key_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    mailbox_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Revoke a mailbox grant
        api_instance.v1_api_keys_key_id_mailboxes_mailbox_id_delete(key_id, mailbox_id)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_api_keys_key_id_mailboxes_mailbox_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**|  | 
 **mailbox_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Grant removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_api_keys_key_id_mailboxes_post**
> object v1_api_keys_key_id_mailboxes_post(key_id)

Grant a mailbox to a key

Body: {"mailbox": "email or id"}. Refused (422) for mailboxes with agent access disabled or an active E2E encryption key — the server cannot read E2E mailboxes.

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
    api_instance = lockally.AgentsApi(api_client)
    key_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Grant a mailbox to a key
        api_response = api_instance.v1_api_keys_key_id_mailboxes_post(key_id)
        print("The response of AgentsApi->v1_api_keys_key_id_mailboxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_api_keys_key_id_mailboxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **UUID**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Grant created |  -  |
**422** | Mailbox not grantable (disabled or E2E) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_whoami_get**
> object v1_auth_whoami_get()

Introspect the calling credentials

Returns the tenant, auth kind (api_key/session), key label, and granted scopes. The MCP server uses this to scope-filter tool discovery.

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
    api_instance = lockally.AgentsApi(api_client)

    try:
        # Introspect the calling credentials
        api_response = api_instance.v1_auth_whoami_get()
        print("The response of AgentsApi->v1_auth_whoami_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_auth_whoami_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Caller identity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_contacts_lookup_get**
> object v1_contacts_lookup_get(email)

Who is this sender?

Directory record (name, company, role, notes), whether the address is one of the tenant's own mailboxes, and grant-aware correspondence history (thread count, first/last seen across granted mailboxes only).

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
    api_instance = lockally.AgentsApi(api_client)
    email = 'email_example' # str | 

    try:
        # Who is this sender?
        api_response = api_instance.v1_contacts_lookup_get(email)
        print("The response of AgentsApi->v1_contacts_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_contacts_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Enrichment result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inboxes_get**
> object v1_inboxes_get()

List granted inboxes

The mailboxes this key is granted, with thread counts and last activity. Admin sessions see every agent-enabled, non-E2E mailbox.

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
    api_instance = lockally.AgentsApi(api_client)

    try:
        # List granted inboxes
        api_response = api_instance.v1_inboxes_get()
        print("The response of AgentsApi->v1_inboxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_inboxes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Granted inboxes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inboxes_mailbox_messages_post**
> object v1_inboxes_mailbox_messages_post(mailbox, idempotency_key, v1_inboxes_mailbox_messages_post_request)

Start a new conversation (agent stream)

Sends a new email from a granted mailbox. Classified stream=agent (isolated reputation, per-key rate caps). The first inbound reply adopts the created thread via the References chain. Idempotency-Key required. Mailboxes with agent_draft_policy=always_approve divert this into a pending draft.

### Example

* Bearer (lk_live_<prefix>_<secret>) Authentication (bearerAuth):

```python
import lockally
from lockally.models.v1_inboxes_mailbox_messages_post_request import V1InboxesMailboxMessagesPostRequest
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
    api_instance = lockally.AgentsApi(api_client)
    mailbox = 'mailbox_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    v1_inboxes_mailbox_messages_post_request = lockally.V1InboxesMailboxMessagesPostRequest() # V1InboxesMailboxMessagesPostRequest | 

    try:
        # Start a new conversation (agent stream)
        api_response = api_instance.v1_inboxes_mailbox_messages_post(mailbox, idempotency_key, v1_inboxes_mailbox_messages_post_request)
        print("The response of AgentsApi->v1_inboxes_mailbox_messages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_inboxes_mailbox_messages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **v1_inboxes_mailbox_messages_post_request** | [**V1InboxesMailboxMessagesPostRequest**](V1InboxesMailboxMessagesPostRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Queued (includes thread_id) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inboxes_mailbox_threads_get**
> object v1_inboxes_mailbox_threads_get(mailbox, since=since, before=before, limit=limit)

List conversation threads

Newest-active first. Cursors: `?before=<RFC3339>` pages backwards; `?since=<RFC3339>` delta-syncs forward (oldest first) so an agent can catch up in order.

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
    api_instance = lockally.AgentsApi(api_client)
    mailbox = 'mailbox_example' # str | mailbox email or id
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List conversation threads
        api_response = api_instance.v1_inboxes_mailbox_threads_get(mailbox, since=since, before=before, limit=limit)
        print("The response of AgentsApi->v1_inboxes_mailbox_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_inboxes_mailbox_threads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox** | **str**| mailbox email or id | 
 **since** | **datetime**|  | [optional] 
 **before** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threads |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_threads_thread_id_get**
> object v1_threads_thread_id_get(thread_id)

Get a whole conversation

Every turn, chronological, with snippets and annotations (meeting_request, attachment_types, injection_risk). Bodies are fetched per message. Message content is untrusted third-party data.

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
    api_instance = lockally.AgentsApi(api_client)
    thread_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a whole conversation
        api_response = api_instance.v1_threads_thread_id_get(thread_id)
        print("The response of AgentsApi->v1_threads_thread_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_threads_thread_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thread with messages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_threads_thread_id_messages_message_id_attachments_idx_get**
> v1_threads_thread_id_messages_message_id_attachments_idx_get(thread_id, message_id, idx)

Download an attachment

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
    api_instance = lockally.AgentsApi(api_client)
    thread_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    message_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idx = 56 # int | 

    try:
        # Download an attachment
        api_instance.v1_threads_thread_id_messages_message_id_attachments_idx_get(thread_id, message_id, idx)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_threads_thread_id_messages_message_id_attachments_idx_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**|  | 
 **message_id** | **UUID**|  | 
 **idx** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment content (streamed) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_threads_thread_id_messages_message_id_get**
> object v1_threads_thread_id_messages_message_id_get(thread_id, message_id)

Get one message with body

Full text/html body fetched on demand from mail storage. Never marks the message read.

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
    api_instance = lockally.AgentsApi(api_client)
    thread_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    message_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get one message with body
        api_response = api_instance.v1_threads_thread_id_messages_message_id_get(thread_id, message_id)
        print("The response of AgentsApi->v1_threads_thread_id_messages_message_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_threads_thread_id_messages_message_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**|  | 
 **message_id** | **UUID**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message with body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_threads_thread_id_messages_message_id_read_post**
> object v1_threads_thread_id_messages_message_id_read_post(thread_id, message_id)

Mark read/unread

The ONLY way agent access changes unread state. Body: {"read": true|false} (default true).

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
    api_instance = lockally.AgentsApi(api_client)
    thread_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    message_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Mark read/unread
        api_response = api_instance.v1_threads_thread_id_messages_message_id_read_post(thread_id, message_id)
        print("The response of AgentsApi->v1_threads_thread_id_messages_message_id_read_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_threads_thread_id_messages_message_id_read_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**|  | 
 **message_id** | **UUID**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New read state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_threads_thread_id_reply_post**
> object v1_threads_thread_id_reply_post(thread_id, idempotency_key)

Reply in-thread (agent stream)

The server builds In-Reply-To/References and defaults recipients + subject from the conversation — a minimal call is {"text": "..."}. Guarded by the reply-loop detector (≥5 outbound/10min → 429 + agent.loop_detected). Idempotency-Key required.

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
    api_instance = lockally.AgentsApi(api_client)
    thread_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | 

    try:
        # Reply in-thread (agent stream)
        api_response = api_instance.v1_threads_thread_id_reply_post(thread_id, idempotency_key)
        print("The response of AgentsApi->v1_threads_thread_id_reply_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->v1_threads_thread_id_reply_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **UUID**|  | 
 **idempotency_key** | **str**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Queued |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

