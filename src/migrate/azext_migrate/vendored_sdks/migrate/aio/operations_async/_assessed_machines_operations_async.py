# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6198, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMError

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AssessedMachinesOperations:
    """AssessedMachinesOperations async operations.

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

    def list_by_assessment(
        self,
        resource_group_name: str,
        project_name: str,
        group_name: str,
        assessment_name: str,
        **kwargs
    ) -> "models.AssessedMachineResultList":
        """Get list of machines that assessed as part of the specified assessment. Returns a json array of objects of type 'assessedMachine' as specified in the Models section.

    Whenever an assessment is created or updated, it goes under computation. During this phase, the 'status' field of Assessment object reports 'Computing'.
    During the period when the assessment is under computation, the list of assessed machines is empty and no assessed machines are returned by this call.

        Get assessed machines for assessment.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param group_name: Unique name of a group within a project.
        :type group_name: str
        :param assessment_name: Unique name of an assessment within a project.
        :type assessment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AssessedMachineResultList or the result of cls(response)
        :rtype: ~azure_migrate.models.AssessedMachineResultList
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.AssessedMachineResultList"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_assessment.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'projectName': self._serialize.url("project_name", project_name, 'str'),
                    'groupName': self._serialize.url("group_name", group_name, 'str'),
                    'assessmentName': self._serialize.url("assessment_name", assessment_name, 'str'),
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
            deserialized = self._deserialize('AssessedMachineResultList', pipeline_response)
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
    list_by_assessment.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines'}

    async def get(
        self,
        resource_group_name: str,
        project_name: str,
        group_name: str,
        assessment_name: str,
        assessed_machine_name: str,
        **kwargs
    ) -> "models.AssessedMachine":
        """Get an assessed machine with its size & cost estimate that was evaluated in the specified assessment.

        Get an assessed machine.

        :param resource_group_name: Name of the Azure Resource Group that project is part of.
        :type resource_group_name: str
        :param project_name: Name of the Azure Migrate project.
        :type project_name: str
        :param group_name: Unique name of a group within a project.
        :type group_name: str
        :param assessment_name: Unique name of an assessment within a project.
        :type assessment_name: str
        :param assessed_machine_name: Unique name of an assessed machine evaluated as part of an
         assessment.
        :type assessed_machine_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AssessedMachine or the result of cls(response)
        :rtype: ~azure_migrate.models.AssessedMachine
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.AssessedMachine"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'assessmentName': self._serialize.url("assessment_name", assessment_name, 'str'),
            'assessedMachineName': self._serialize.url("assessed_machine_name", assessed_machine_name, 'str'),
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
        deserialized = self._deserialize('AssessedMachine', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines/{assessedMachineName}'}
