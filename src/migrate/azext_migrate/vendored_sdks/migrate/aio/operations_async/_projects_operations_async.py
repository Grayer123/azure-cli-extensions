# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6198, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMError

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ProjectsOperations:
    """ProjectsOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure_migrate.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_subscription(
        self,
        **kwargs
    ) -> "models.ProjectResultList":
        """Get all the projects in the subscription.

        Get all projects.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectResultList or the result of cls(response)
        :rtype: ~azure_migrate.models.ProjectResultList
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.ProjectResultList"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            if self._config.accept_language is not None:
                header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ProjectResultList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Migrate/projects'}

    def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs
    ) -> "models.ProjectResultList":
        """Get all the projects in the resource group.

        Get all projects.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectResultList or the result of cls(response)
        :rtype: ~azure_migrate.models.ProjectResultList
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.ProjectResultList"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            if self._config.accept_language is not None:
                header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ProjectResultList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects'}

    async def get(
        self,
        resource_group_name: str,
        project_name: str,
        **kwargs
    ) -> "models.Project":
        """Get the project with the specified name.

        Get the specified project.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Project or the result of cls(response)
        :rtype: ~azure_migrate.models.Project
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.Project"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('Project', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}'}

    async def create(
        self,
        resource_group_name: str,
        project_name: str,
        project: Optional["models.Project"] = None,
        **kwargs
    ) -> "models.Project":
        """Create a project with specified name. If a project already exists, update it.

        Create or update project.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param project: New or Updated project object.
        :type project: ~azure_migrate.models.Project
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Project or Project or the result of cls(response)
        :rtype: ~azure_migrate.models.Project or ~azure_migrate.models.Project
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.Project"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if project is not None:
            body_content = self._serialize.body(project, 'Project')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            deserialized = self._deserialize('Project', pipeline_response)

        if response.status_code == 201:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            deserialized = self._deserialize('Project', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}'}

    async def update(
        self,
        resource_group_name: str,
        project_name: str,
        project: Optional["models.Project"] = None,
        **kwargs
    ) -> "models.Project":
        """Update a project with specified name. Supports partial updates, for example only tags can be provided.

        Update project.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param project: New or Updated project object.
        :type project: ~azure_migrate.models.Project
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Project or the result of cls(response)
        :rtype: ~azure_migrate.models.Project
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.Project"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if project is not None:
            body_content = self._serialize.body(project, 'Project')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('Project', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}'}

    async def delete(
        self,
        resource_group_name: str,
        project_name: str,
        **kwargs
    ) -> None:
        """Delete the project. Deleting non-existent project is a no-operation.

        Delete the project.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType[None] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}'}

    async def get_keys(
        self,
        resource_group_name: str,
        project_name: str,
        **kwargs
    ) -> "models.ProjectKey":
        """Gets the Log Analytics Workspace ID and Primary Key for the specified project.

        Get shared keys for the project.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectKey or the result of cls(response)
        :rtype: ~azure_migrate.models.ProjectKey
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.ProjectKey"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_keys.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('ProjectKey', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/keys'}
