# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmdexec/api/proto/sql_cmd_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from databricks.sql.api import messages_pb2 as cmdexec_dot_api_dot_proto_dot_messages__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='cmdexec/api/proto/sql_cmd_service.proto',
    package='databricks.sql',
    syntax='proto2',
    serialized_options=b'\n\022com.databricks.sql\240\001\001',
    create_key=_descriptor._internal_create_key,
    serialized_pb=
    b'\n\'cmdexec/api/proto/sql_cmd_service.proto\x12\x0e\x64\x61tabricks.sql\x1a cmdexec/api/proto/messages.proto2\x98\x06\n\x11SqlCommandService\x12V\n\x0bOpenSession\x12\".databricks.sql.OpenSessionRequest\x1a#.databricks.sql.OpenSessionResponse\x12Y\n\x0c\x43loseSession\x12#.databricks.sql.CloseSessionRequest\x1a$.databricks.sql.CloseSessionResponse\x12_\n\x0eGetSessionInfo\x12%.databricks.sql.GetSessionInfoRequest\x1a&.databricks.sql.GetSessionInfoResponse\x12_\n\x0e\x45xecuteCommand\x12%.databricks.sql.ExecuteCommandRequest\x1a&.databricks.sql.ExecuteCommandResponse\x12\x65\n\x10GetCommandStatus\x12\'.databricks.sql.GetCommandStatusRequest\x1a(.databricks.sql.GetCommandStatusResponse\x12n\n\x13\x46\x65tchCommandResults\x12*.databricks.sql.FetchCommandResultsRequest\x1a+.databricks.sql.FetchCommandResultsResponse\x12\\\n\rCancelCommand\x12$.databricks.sql.CancelCommandRequest\x1a%.databricks.sql.CancelCommandResponse\x12Y\n\x0c\x43loseCommand\x12#.databricks.sql.CloseCommandRequest\x1a$.databricks.sql.CloseCommandResponseB\x17\n\x12\x63om.databricks.sql\xa0\x01\x01',
    dependencies=[
        cmdexec_dot_api_dot_proto_dot_messages__pb2.DESCRIPTOR,
    ])

_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DESCRIPTOR._options = None

_SQLCOMMANDSERVICE = _descriptor.ServiceDescriptor(
    name='SqlCommandService',
    full_name='databricks.sql.SqlCommandService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=94,
    serialized_end=886,
    methods=[
        _descriptor.MethodDescriptor(
            name='OpenSession',
            full_name='databricks.sql.SqlCommandService.OpenSession',
            index=0,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._OPENSESSIONREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._OPENSESSIONRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='CloseSession',
            full_name='databricks.sql.SqlCommandService.CloseSession',
            index=1,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._CLOSESESSIONREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._CLOSESESSIONRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='GetSessionInfo',
            full_name='databricks.sql.SqlCommandService.GetSessionInfo',
            index=2,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._GETSESSIONINFOREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._GETSESSIONINFORESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='ExecuteCommand',
            full_name='databricks.sql.SqlCommandService.ExecuteCommand',
            index=3,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._EXECUTECOMMANDREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._EXECUTECOMMANDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='GetCommandStatus',
            full_name='databricks.sql.SqlCommandService.GetCommandStatus',
            index=4,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._GETCOMMANDSTATUSREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._GETCOMMANDSTATUSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='FetchCommandResults',
            full_name='databricks.sql.SqlCommandService.FetchCommandResults',
            index=5,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._FETCHCOMMANDRESULTSREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._FETCHCOMMANDRESULTSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='CancelCommand',
            full_name='databricks.sql.SqlCommandService.CancelCommand',
            index=6,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._CANCELCOMMANDREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._CANCELCOMMANDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='CloseCommand',
            full_name='databricks.sql.SqlCommandService.CloseCommand',
            index=7,
            containing_service=None,
            input_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._CLOSECOMMANDREQUEST,
            output_type=cmdexec_dot_api_dot_proto_dot_messages__pb2._CLOSECOMMANDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_SQLCOMMANDSERVICE)

DESCRIPTOR.services_by_name['SqlCommandService'] = _SQLCOMMANDSERVICE

# @@protoc_insertion_point(module_scope)
