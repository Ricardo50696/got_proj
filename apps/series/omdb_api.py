# import requests
#
# # from got_proj.settings import EVENTBRITE_TOKEN, EVENTBRITE_ORGANIZATION_ID, EVENTBRITE_API_BASE_URL
#
#
# class OMDBAPI:
#     headers = {
#         'Content-Type': 'application/json',
#         # 'Authorization': 'Bearer {}'.format(EVENTBRITE_TOKEN)
#     }
#
#     def __init__(self):
#         # self.base_url = EVENTBRITE_API_BASE_URL
#         # self.api_communicator = ApiCommunicatorRequestsAdapter(api_url=self.base_url)
#         # self.organization_id = EVENTBRITE_ORGANIZATION_ID
#
#     def _set_request_kwargs(self, url, data=None, params=None, files=None, headers=None, auth=None):
#         """
#         Generic method that sets up kwargs for any http request.
#         """
#         kwargs = dict(
#             url=url,
#             headers=self.headers.copy()
#         )
#         if data:
#             kwargs.update(dict(
#                 data=data
#             ))
#         if params:
#             kwargs.update(dict(
#                 params=params
#             ))
#         if files:
#             kwargs.update(dict(
#                 files=files
#             ))
#         if headers:
#             kwargs.update(dict(
#                 headers=headers
#             ))
#         if auth:
#             kwargs.update(dict(
#                 auth=auth
#             ))
#
#         return kwargs
#
#     def _get(self, url, data=None, params=None, headers=None, auth=None):
#         """
#         Generic HTTP GET method.
#         """
#         kwargs = self._set_request_kwargs(url=url, data=data, params=params, headers=headers, auth=auth)
#         return self.api_communicator.get(**kwargs)
#
#     def set_url(self, relative_url):
#         """
#         Sets the full url for an API method.
#         """
#         full_url = "{}{}".format(self.api_communicator.api_url, relative_url)
#         return full_url
#
#     # def get_all_paginated_objects(self, url):  # you cannot query with page_size, api default is 50 objects per request
#     #     object_list = []
#     #     pagination = self._get(url=url).json()['pagination']
#     #     page_number = pagination['page_number']
#     #
#     #     while page_number != pagination['page_count'] + 1:
#     #         object_list.append(self._get(url=url + '&page=%s' % str(page_number)).json())
#     #         page_number += 1
#     #     return object_list
#
#     def list_events(self, **kwargs):
#         """
#         Returns a list of all events from Eventbrite.
#         """
#         url = self.set_url('organizations/{}/events/'.format(self.organization_id))
#         return self._get(url=url)
#
#
#
#
#     def get_event(self, event_id):
#         """
#         Returns a specific event from Eventbrite with category and subcategory class expanded.
#         """
#         url = self.set_url(
#             'events/{}/?expand=category,subcategory'.format(event_id))
#         return self._get(url=url)
#
#
# class ApiCommunicator(object):
#
#     def __init__(self, api_url, package=None):
#         """
#         Constructor of the ApiCommunicator class.
#         """
#         self.api_url = api_url
#         self.package = package
#
#     def get(self, **kwargs):
#         """
#         Calls the GET.
#         """
#         return self.package.get(**kwargs)
#
#     def post(self, **kwargs):
#         """
#         Calls the POST.
#         """
#         return self.package.post(**kwargs)
#
#     def put(self, **kwargs):
#         """
#         Calls the PUT methods.
#         """
#         return self.package.put(**kwargs)
#
#     def delete(self, **kwargs):
#         """
#         Calls the DELETE methods.
#         """
#         return self.package.delete(**kwargs)
#
#     def patch(self):
#         """
#         Calls the PATCH methods.
#         """
#         raise NotImplementedError
#
#
# class ApiCommunicatorRequestsAdapter(ApiCommunicator):
#
#     def __init__(self, api_url):
#         super(ApiCommunicatorRequestsAdapter, self).__init__(api_url, package=requests)
