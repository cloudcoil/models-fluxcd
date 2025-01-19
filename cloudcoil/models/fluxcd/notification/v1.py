# Generated by cloudcoil-model-codegen v0.0.32
# DO NOT EDIT

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Dict, List, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseModel
from cloudcoil.resources import Resource


class ResourceModel(BaseModel):
    api_version: Annotated[
        Optional[str],
        Field(alias="apiVersion", description="API version of the referent"),
    ] = None
    kind: Annotated[
        Literal[
            "Bucket",
            "GitRepository",
            "Kustomization",
            "HelmRelease",
            "HelmChart",
            "HelmRepository",
            "ImageRepository",
            "ImagePolicy",
            "ImageUpdateAutomation",
            "OCIRepository",
        ],
        Field(description="Kind of the referent"),
    ]
    match_labels: Annotated[
        Optional[Dict[str, str]],
        Field(
            alias="matchLabels",
            description='MatchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels\nmap is equivalent to an element of matchExpressions, whose key field is "key", the\noperator is "In", and the values array contains only "value". The requirements are ANDed.\nMatchLabels requires the name to be set to `*`.',
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="Name of the referent\nIf multiple resources are targeted `*` may be set.",
            max_length=53,
            min_length=1,
        ),
    ]
    namespace: Annotated[
        Optional[str],
        Field(description="Namespace of the referent", max_length=53, min_length=1),
    ] = None


class SecretRef(BaseModel):
    name: Annotated[str, Field(description="Name of the referent.")]


class ReceiverSpec(BaseModel):
    events: Annotated[
        Optional[List[str]],
        Field(
            description="Events specifies the list of event types to handle,\ne.g. 'push' for GitHub or 'Push Hook' for GitLab."
        ),
    ] = None
    interval: Annotated[
        Optional[str],
        Field(
            description="Interval at which to reconcile the Receiver with its Secret references.",
            pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m|h))+$",
        ),
    ] = "10m"
    resources: Annotated[
        List[ResourceModel],
        Field(description="A list of resources to be notified about changes."),
    ]
    secret_ref: Annotated[
        SecretRef,
        Field(
            alias="secretRef",
            description="SecretRef specifies the Secret containing the token used\nto validate the payload authenticity.",
        ),
    ]
    suspend: Annotated[
        Optional[bool],
        Field(
            description="Suspend tells the controller to suspend subsequent\nevents handling for this receiver."
        ),
    ] = None
    type: Annotated[
        Literal[
            "generic",
            "generic-hmac",
            "github",
            "gitlab",
            "bitbucket",
            "harbor",
            "dockerhub",
            "quay",
            "gcr",
            "nexus",
            "acr",
            "cdevents",
        ],
        Field(
            description="Type of webhook sender, used to determine\nthe validation procedure and payload deserialization."
        ),
    ]


class Condition(BaseModel):
    last_transition_time: Annotated[
        datetime,
        Field(
            alias="lastTransitionTime",
            description="lastTransitionTime is the last time the condition transitioned from one status to another.\nThis should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.",
        ),
    ]
    message: Annotated[
        str,
        Field(
            description="message is a human readable message indicating details about the transition.\nThis may be an empty string.",
            max_length=32768,
        ),
    ]
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="observedGeneration represents the .metadata.generation that the condition was set based upon.\nFor instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date\nwith respect to the current state of the instance.",
            ge=0,
        ),
    ] = None
    reason: Annotated[
        str,
        Field(
            description="reason contains a programmatic identifier indicating the reason for the condition's last transition.\nProducers of specific condition types may define expected values and meanings for this field,\nand whether the values are considered a guaranteed API.\nThe value should be a CamelCase string.\nThis field may not be empty.",
            max_length=1024,
            min_length=1,
            pattern="^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$",
        ),
    ]
    status: Annotated[
        Literal["True", "False", "Unknown"],
        Field(description="status of the condition, one of True, False, Unknown."),
    ]
    type: Annotated[
        str,
        Field(
            description="type of condition in CamelCase or in foo.example.com/CamelCase.",
            max_length=316,
            pattern="^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$",
        ),
    ]


class ReceiverStatus(BaseModel):
    conditions: Annotated[
        Optional[List[Condition]],
        Field(description="Conditions holds the conditions for the Receiver."),
    ] = None
    last_handled_reconcile_at: Annotated[
        Optional[str],
        Field(
            alias="lastHandledReconcileAt",
            description="LastHandledReconcileAt holds the value of the most recent\nreconcile request value, so a change of the annotation value\ncan be detected.",
        ),
    ] = None
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="ObservedGeneration is the last observed generation of the Receiver object.",
        ),
    ] = None
    webhook_path: Annotated[
        Optional[str],
        Field(
            alias="webhookPath",
            description="WebhookPath is the generated incoming webhook address in the format\nof '/hook/sha256sum(token+name+namespace)'.",
        ),
    ] = None


class Receiver(Resource):
    api_version: Annotated[
        Optional[Literal["notification.toolkit.fluxcd.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "notification.toolkit.fluxcd.io/v1"
    kind: Annotated[
        Optional[Literal["Receiver"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Receiver"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ReceiverSpec] = None
    status: Optional[ReceiverStatus] = None
