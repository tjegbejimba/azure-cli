# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from ..action import AddSku


def load_arguments(self, _):

    with self.argument_context('databoxedge device list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('expand', type=str, help='Specify $expand=details to populate additional fields related to the '
                   'resource or Specify $skipToken=<token> to populate the next page in the list.')

    with self.argument_context('databoxedge device show') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device create') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('sku', action=AddSku, nargs='+', help='The SKU type.')
        c.argument('etag', type=str, help='The etag for the devices.')
        c.argument('data_box_edge_device_status', options_list=['--status'], arg_type=get_enum_type(['ReadyToSetup',
                                                                                                     'Online',
                                                                                                     'Offline',
                                                                                                     'NeedsAttention',
                                                                                                     'Disconnected',
                                                                                                     'PartiallyDisconnected',
                                                                                                     'Maintenance']),
                   help='The status of the Data Box Edge/Gateway device.')
        c.argument('description', type=str, help='The Description of the Data Box Edge/Gateway device.')
        c.argument('model_description', type=str, help='The description of the Data Box Edge/Gateway device model.')
        c.argument('friendly_name', type=str, help='The Data Box Edge/Gateway device name.')

    with self.argument_context('databoxedge device update') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('tags', tags_type)

    with self.argument_context('databoxedge device delete') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device download-update') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device install-update') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device scan-for-update') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device show-update-summary') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device wait') as c:
        c.argument('device_name', options_list=['--name', '-n', '--device-name'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge alert list') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge alert show') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The alert name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule list') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule show') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The bandwidth schedule name.',
                   id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule create') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The bandwidth schedule name which needs to '
                   'be added/updated.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('start', type=str, help='The start time of the schedule in UTC.')
        c.argument('stop', type=str, help='The stop time of the schedule in UTC.')
        c.argument('rate_in_mbps', type=int, help='The bandwidth rate in Mbps.')
        c.argument('days', nargs='+', help='The days of the week when this schedule is applicable.')

    with self.argument_context('databoxedge bandwidth-schedule update') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The bandwidth schedule name which needs to '
                   'be added/updated.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('start', type=str, help='The start time of the schedule in UTC.')
        c.argument('stop', type=str, help='The stop time of the schedule in UTC.')
        c.argument('rate_in_mbps', type=int, help='The bandwidth rate in Mbps.')
        c.argument('days', nargs='+', help='The days of the week when this schedule is applicable.')
        c.ignore('parameters')

    with self.argument_context('databoxedge bandwidth-schedule delete') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The bandwidth schedule name.',
                   id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule wait') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The bandwidth schedule name.',
                   id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge show-job') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The job name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge list-node') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order list') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order show') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order create') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str,
                   help='The order details of a device.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('status', arg_type=get_enum_type(['Untracked', 'AwaitingFulfilment', 'AwaitingPreparation',
                                                     'AwaitingShipment', 'Shipped', 'Arriving', 'Delivered',
                                                     'ReplacementRequested', 'LostDevice', 'Declined',
                                                     'ReturnInitiated', 'AwaitingReturnShipment', 'ShippedBack',
                                                     'CollectedAtMicrosoft']), help='Status of the order as per the '
                   'allowed status types.', arg_group='Current Status')
        c.argument('comments', type=str, help='Comments related to this status change.', arg_group='Current Status')
        c.argument('address_line1', type=str, help='The address line1.', arg_group='Shipping Address')
        c.argument('address_line2', type=str, help='The address line2.', arg_group='Shipping Address')
        c.argument('address_line3', type=str, help='The address line3.', arg_group='Shipping Address')
        c.argument('postal_code', type=str, help='The postal code.', arg_group='Shipping Address')
        c.argument('city', type=str, help='The city name.', arg_group='Shipping Address')
        c.argument('state', type=str, help='The state name.', arg_group='Shipping Address')
        c.argument('country', type=str, help='The country name.', arg_group='Shipping Address')
        c.argument('contact_person', type=str, help='The contact person name.', arg_group='Contact Information')
        c.argument('company_name', type=str, help='The name of the company.', arg_group='Contact Information')
        c.argument('phone', type=str, help='The phone number.', arg_group='Contact Information')
        c.argument('email_list', nargs='+', help='The email list.', arg_group='Contact Information')

    with self.argument_context('databoxedge order update') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str,
                   help='The order details of a device.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('status', arg_type=get_enum_type(['Untracked', 'AwaitingFulfilment', 'AwaitingPreparation',
                                                     'AwaitingShipment', 'Shipped', 'Arriving', 'Delivered',
                                                     'ReplacementRequested', 'LostDevice', 'Declined',
                                                     'ReturnInitiated', 'AwaitingReturnShipment', 'ShippedBack',
                                                     'CollectedAtMicrosoft']), help='Status of the order as per the '
                   'allowed status types.', arg_group='Current Status')
        c.argument('comments', type=str, help='Comments related to this status change.', arg_group='Current Status')
        c.argument('address_line1', type=str, help='The address line1.', arg_group='Shipping Address')
        c.argument('address_line2', type=str, help='The address line2.', arg_group='Shipping Address')
        c.argument('address_line3', type=str, help='The address line3.', arg_group='Shipping Address')
        c.argument('postal_code', type=str, help='The postal code.', arg_group='Shipping Address')
        c.argument('city', type=str, help='The city name.', arg_group='Shipping Address')
        c.argument('state', type=str, help='The state name.', arg_group='Shipping Address')
        c.argument('country', type=str, help='The country name.', arg_group='Shipping Address')
        c.argument('contact_person', type=str, help='The contact person name.', arg_group='Contact Information')
        c.argument('company_name', type=str, help='The name of the company.', arg_group='Contact Information')
        c.argument('phone', type=str, help='The phone number.', arg_group='Contact Information')
        c.argument('email_list', nargs='+', help='The email list.', arg_group='Contact Information')
        c.ignore('order')

    with self.argument_context('databoxedge order delete') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order wait') as c:
        c.argument('device_name', options_list=['--device-name', '-d'], type=str, help='The device name.',
                   id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge list-sku') as c:
        c.argument('filter_', options_list=['--filter'], type=str, help='Specify $filter=\'location eq <location>\' to '
                   'filter on location.')