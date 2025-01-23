# Generated by cloudcoil-model-codegen v0.2.1
# DO NOT EDIT

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Callable, Dict, List, Literal, Optional, Type, Union

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseBuilder, BaseModel, GenericListBuilder, Self
from cloudcoil.resources import Resource


class EventSource(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["EventSource"]:
            return EventSource

        def build(self) -> "EventSource":
            return EventSource(**self._attrs)

        def api_version(self, value: Optional[str]) -> Self:
            return self._set("api_version", value)

        def kind(
            self,
            value: Literal[
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
        ) -> Self:
            return self._set("kind", value)

        def match_labels(self, value: Optional[Dict[str, str]]) -> Self:
            return self._set("match_labels", value)

        def name(self, value: str) -> Self:
            return self._set("name", value)

        def namespace(self, value: Optional[str]) -> Self:
            return self._set("namespace", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["EventSource", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EventSource.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
            description='MatchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels\nmap is equivalent to an element of matchExpressions, whose key field is "key", the\noperator is "In", and the values array contains only "value". The requirements are ANDed.',
        ),
    ] = None
    name: Annotated[str, Field(description="Name of the referent", max_length=53, min_length=1)]
    namespace: Annotated[
        Optional[str],
        Field(description="Namespace of the referent", max_length=53, min_length=1),
    ] = None


class ProviderRef(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["ProviderRef"]:
            return ProviderRef

        def build(self) -> "ProviderRef":
            return ProviderRef(**self._attrs)

        def name(self, value: str) -> Self:
            return self._set("name", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["ProviderRef", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ProviderRef.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    name: Annotated[str, Field(description="Name of the referent.")]


class AlertSpec(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["AlertSpec"]:
            return AlertSpec

        def build(self) -> "AlertSpec":
            return AlertSpec(**self._attrs)

        def event_severity(self, value: Optional[Literal["info", "error"]]) -> Self:
            return self._set("event_severity", value)

        def event_sources(
            self,
            value_or_callback: Union[
                List[EventSource],
                Callable[
                    [GenericListBuilder[EventSource, EventSource.Builder]],
                    GenericListBuilder[EventSource, EventSource.Builder],
                ],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(EventSource.list_builder()).build()
            return self._set("event_sources", value)

        def exclusion_list(self, value: Optional[List[str]]) -> Self:
            return self._set("exclusion_list", value)

        def provider_ref(
            self,
            value_or_callback: Union[
                ProviderRef, Callable[[ProviderRef.Builder], ProviderRef.Builder]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ProviderRef.builder()).build()
            return self._set("provider_ref", value)

        def summary(self, value: Optional[str]) -> Self:
            return self._set("summary", value)

        def suspend(self, value: Optional[bool]) -> Self:
            return self._set("suspend", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["AlertSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use AlertSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    event_severity: Annotated[
        Optional[Literal["info", "error"]],
        Field(
            alias="eventSeverity",
            description="Filter events based on severity, defaults to ('info').\nIf set to 'info' no events will be filtered.",
        ),
    ] = "info"
    event_sources: Annotated[
        List[EventSource],
        Field(
            alias="eventSources",
            description="Filter events based on the involved objects.",
        ),
    ]
    exclusion_list: Annotated[
        Optional[List[str]],
        Field(
            alias="exclusionList",
            description="A list of Golang regular expressions to be used for excluding messages.",
        ),
    ] = None
    provider_ref: Annotated[
        ProviderRef,
        Field(alias="providerRef", description="Send events using this provider."),
    ]
    summary: Annotated[
        Optional[str],
        Field(description="Short description of the impact and affected cluster."),
    ] = None
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend subsequent events dispatching.\nDefaults to false."
        ),
    ] = None


class Condition(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["Condition"]:
            return Condition

        def build(self) -> "Condition":
            return Condition(**self._attrs)

        def last_transition_time(self, value: datetime) -> Self:
            return self._set("last_transition_time", value)

        def message(self, value: str) -> Self:
            return self._set("message", value)

        def observed_generation(self, value: Optional[int]) -> Self:
            return self._set("observed_generation", value)

        def reason(self, value: str) -> Self:
            return self._set("reason", value)

        def status(self, value: Literal["True", "False", "Unknown"]) -> Self:
            return self._set("status", value)

        def type(self, value: str) -> Self:
            return self._set("type", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["Condition", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Condition.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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


class AlertStatus(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["AlertStatus"]:
            return AlertStatus

        def build(self) -> "AlertStatus":
            return AlertStatus(**self._attrs)

        def conditions(
            self,
            value_or_callback: Union[
                Optional[List[Condition]],
                Callable[
                    [GenericListBuilder[Condition, Condition.Builder]],
                    GenericListBuilder[Condition, Condition.Builder],
                ],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(Condition.list_builder()).build()
            return self._set("conditions", value)

        def observed_generation(self, value: Optional[int]) -> Self:
            return self._set("observed_generation", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["AlertStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use AlertStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[Condition]] = None
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="ObservedGeneration is the last observed generation.",
        ),
    ] = None


class CertSecretRef(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["CertSecretRef"]:
            return CertSecretRef

        def build(self) -> "CertSecretRef":
            return CertSecretRef(**self._attrs)

        def name(self, value: str) -> Self:
            return self._set("name", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["CertSecretRef", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use CertSecretRef.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    name: Annotated[str, Field(description="Name of the referent.")]


class SecretRef(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["SecretRef"]:
            return SecretRef

        def build(self) -> "SecretRef":
            return SecretRef(**self._attrs)

        def name(self, value: str) -> Self:
            return self._set("name", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["SecretRef", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use SecretRef.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    name: Annotated[str, Field(description="Name of the referent.")]


class ProviderSpec(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["ProviderSpec"]:
            return ProviderSpec

        def build(self) -> "ProviderSpec":
            return ProviderSpec(**self._attrs)

        def address(self, value: Optional[str]) -> Self:
            return self._set("address", value)

        def cert_secret_ref(
            self,
            value_or_callback: Union[
                Optional[CertSecretRef],
                Callable[[CertSecretRef.Builder], CertSecretRef.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(CertSecretRef.builder()).build()
            return self._set("cert_secret_ref", value)

        def channel(self, value: Optional[str]) -> Self:
            return self._set("channel", value)

        def proxy(self, value: Optional[str]) -> Self:
            return self._set("proxy", value)

        def secret_ref(
            self,
            value_or_callback: Union[
                Optional[SecretRef], Callable[[SecretRef.Builder], SecretRef.Builder]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(SecretRef.builder()).build()
            return self._set("secret_ref", value)

        def suspend(self, value: Optional[bool]) -> Self:
            return self._set("suspend", value)

        def timeout(self, value: Optional[str]) -> Self:
            return self._set("timeout", value)

        def type(
            self,
            value: Literal[
                "slack",
                "discord",
                "msteams",
                "rocket",
                "generic",
                "generic-hmac",
                "github",
                "gitlab",
                "bitbucket",
                "azuredevops",
                "googlechat",
                "webex",
                "sentry",
                "azureeventhub",
                "telegram",
                "lark",
                "matrix",
                "opsgenie",
                "alertmanager",
                "grafana",
                "githubdispatch",
            ],
        ) -> Self:
            return self._set("type", value)

        def username(self, value: Optional[str]) -> Self:
            return self._set("username", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["ProviderSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ProviderSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    address: Annotated[
        Optional[str],
        Field(
            description="HTTP/S webhook address of this provider",
            pattern="^(http|https)://",
        ),
    ] = None
    cert_secret_ref: Annotated[
        Optional[CertSecretRef],
        Field(
            alias="certSecretRef",
            description="CertSecretRef can be given the name of a secret containing\na PEM-encoded CA certificate (`caFile`)",
        ),
    ] = None
    channel: Annotated[Optional[str], Field(description="Alert channel for this provider")] = None
    proxy: Annotated[
        Optional[str],
        Field(description="HTTP/S address of the proxy", pattern="^(http|https)://"),
    ] = None
    secret_ref: Annotated[
        Optional[SecretRef],
        Field(
            alias="secretRef",
            description='Secret reference containing the provider webhook URL\nusing "address" as data key',
        ),
    ] = None
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend subsequent events handling.\nDefaults to false."
        ),
    ] = None
    timeout: Annotated[
        Optional[str],
        Field(
            description="Timeout for sending alerts to the provider.",
            pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m))+$",
        ),
    ] = None
    type: Annotated[
        Literal[
            "slack",
            "discord",
            "msteams",
            "rocket",
            "generic",
            "generic-hmac",
            "github",
            "gitlab",
            "bitbucket",
            "azuredevops",
            "googlechat",
            "webex",
            "sentry",
            "azureeventhub",
            "telegram",
            "lark",
            "matrix",
            "opsgenie",
            "alertmanager",
            "grafana",
            "githubdispatch",
        ],
        Field(description="Type of provider"),
    ]
    username: Annotated[Optional[str], Field(description="Bot username for this provider")] = None


class ProviderStatus(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["ProviderStatus"]:
            return ProviderStatus

        def build(self) -> "ProviderStatus":
            return ProviderStatus(**self._attrs)

        def conditions(
            self,
            value_or_callback: Union[
                Optional[List[Condition]],
                Callable[
                    [GenericListBuilder[Condition, Condition.Builder]],
                    GenericListBuilder[Condition, Condition.Builder],
                ],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(Condition.list_builder()).build()
            return self._set("conditions", value)

        def observed_generation(self, value: Optional[int]) -> Self:
            return self._set("observed_generation", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["ProviderStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ProviderStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[Condition]] = None
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="ObservedGeneration is the last reconciled generation.",
        ),
    ] = None


class ResourceModel(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["ResourceModel"]:
            return ResourceModel

        def build(self) -> "ResourceModel":
            return ResourceModel(**self._attrs)

        def api_version(self, value: Optional[str]) -> Self:
            return self._set("api_version", value)

        def kind(
            self,
            value: Literal[
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
        ) -> Self:
            return self._set("kind", value)

        def match_labels(self, value: Optional[Dict[str, str]]) -> Self:
            return self._set("match_labels", value)

        def name(self, value: str) -> Self:
            return self._set("name", value)

        def namespace(self, value: Optional[str]) -> Self:
            return self._set("namespace", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["ResourceModel", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ResourceModel.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
            description='MatchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels\nmap is equivalent to an element of matchExpressions, whose key field is "key", the\noperator is "In", and the values array contains only "value". The requirements are ANDed.',
        ),
    ] = None
    name: Annotated[str, Field(description="Name of the referent", max_length=53, min_length=1)]
    namespace: Annotated[
        Optional[str],
        Field(description="Namespace of the referent", max_length=53, min_length=1),
    ] = None


class ReceiverSpec(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["ReceiverSpec"]:
            return ReceiverSpec

        def build(self) -> "ReceiverSpec":
            return ReceiverSpec(**self._attrs)

        def events(self, value: Optional[List[str]]) -> Self:
            return self._set("events", value)

        def resources(
            self,
            value_or_callback: Union[
                List[ResourceModel],
                Callable[
                    [GenericListBuilder[ResourceModel, ResourceModel.Builder]],
                    GenericListBuilder[ResourceModel, ResourceModel.Builder],
                ],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ResourceModel.list_builder()).build()
            return self._set("resources", value)

        def secret_ref(
            self,
            value_or_callback: Union[SecretRef, Callable[[SecretRef.Builder], SecretRef.Builder]],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(SecretRef.builder()).build()
            return self._set("secret_ref", value)

        def suspend(self, value: Optional[bool]) -> Self:
            return self._set("suspend", value)

        def type(
            self,
            value: Literal[
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
            ],
        ) -> Self:
            return self._set("type", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["ReceiverSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ReceiverSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    events: Annotated[
        Optional[List[str]],
        Field(
            description="A list of events to handle,\ne.g. 'push' for GitHub or 'Push Hook' for GitLab."
        ),
    ] = None
    resources: Annotated[
        List[ResourceModel],
        Field(description="A list of resources to be notified about changes."),
    ]
    secret_ref: Annotated[
        SecretRef,
        Field(
            alias="secretRef",
            description="Secret reference containing the token used\nto validate the payload authenticity",
        ),
    ]
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend subsequent events handling.\nDefaults to false."
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
        ],
        Field(
            description="Type of webhook sender, used to determine\nthe validation procedure and payload deserialization."
        ),
    ]


class ReceiverStatus(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["ReceiverStatus"]:
            return ReceiverStatus

        def build(self) -> "ReceiverStatus":
            return ReceiverStatus(**self._attrs)

        def conditions(
            self,
            value_or_callback: Union[
                Optional[List[Condition]],
                Callable[
                    [GenericListBuilder[Condition, Condition.Builder]],
                    GenericListBuilder[Condition, Condition.Builder],
                ],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(Condition.list_builder()).build()
            return self._set("conditions", value)

        def observed_generation(self, value: Optional[int]) -> Self:
            return self._set("observed_generation", value)

        def url(self, value: Optional[str]) -> Self:
            return self._set("url", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["ReceiverStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ReceiverStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[Condition]] = None
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="ObservedGeneration is the last observed generation.",
        ),
    ] = None
    url: Annotated[
        Optional[str],
        Field(
            description="Generated webhook URL in the format\nof '/hook/sha256sum(token+name+namespace)'."
        ),
    ] = None


class Alert(Resource):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["Alert"]:
            return Alert

        def build(self) -> "Alert":
            return Alert(**self._attrs)

        def api_version(
            self, value: Optional[Literal["notification.toolkit.fluxcd.io/v1beta1"]]
        ) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Alert"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[apimachinery.ObjectMeta.Builder], apimachinery.ObjectMeta.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta.builder()).build()
            return self._set("metadata", value)

        def spec(
            self,
            value_or_callback: Union[
                Optional[AlertSpec], Callable[[AlertSpec.Builder], AlertSpec.Builder]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(AlertSpec.builder()).build()
            return self._set("spec", value)

        def status(
            self,
            value_or_callback: Union[
                Optional[AlertStatus],
                Callable[[AlertStatus.Builder], AlertStatus.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(AlertStatus.builder()).build()
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["Alert", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Alert.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["notification.toolkit.fluxcd.io/v1beta1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "notification.toolkit.fluxcd.io/v1beta1"
    kind: Annotated[
        Optional[Literal["Alert"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Alert"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[AlertSpec] = None
    status: Optional[AlertStatus] = None


class Provider(Resource):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["Provider"]:
            return Provider

        def build(self) -> "Provider":
            return Provider(**self._attrs)

        def api_version(
            self, value: Optional[Literal["notification.toolkit.fluxcd.io/v1beta1"]]
        ) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Provider"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[apimachinery.ObjectMeta.Builder], apimachinery.ObjectMeta.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta.builder()).build()
            return self._set("metadata", value)

        def spec(
            self,
            value_or_callback: Union[
                Optional[ProviderSpec],
                Callable[[ProviderSpec.Builder], ProviderSpec.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ProviderSpec.builder()).build()
            return self._set("spec", value)

        def status(
            self,
            value_or_callback: Union[
                Optional[ProviderStatus],
                Callable[[ProviderStatus.Builder], ProviderStatus.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ProviderStatus.builder()).build()
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["Provider", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Provider.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["notification.toolkit.fluxcd.io/v1beta1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "notification.toolkit.fluxcd.io/v1beta1"
    kind: Annotated[
        Optional[Literal["Provider"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Provider"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ProviderSpec] = None
    status: Optional[ProviderStatus] = None


class Receiver(Resource):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["Receiver"]:
            return Receiver

        def build(self) -> "Receiver":
            return Receiver(**self._attrs)

        def api_version(
            self, value: Optional[Literal["notification.toolkit.fluxcd.io/v1beta1"]]
        ) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Receiver"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[apimachinery.ObjectMeta.Builder], apimachinery.ObjectMeta.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta.builder()).build()
            return self._set("metadata", value)

        def spec(
            self,
            value_or_callback: Union[
                Optional[ReceiverSpec],
                Callable[[ReceiverSpec.Builder], ReceiverSpec.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ReceiverSpec.builder()).build()
            return self._set("spec", value)

        def status(
            self,
            value_or_callback: Union[
                Optional[ReceiverStatus],
                Callable[[ReceiverStatus.Builder], ReceiverStatus.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ReceiverStatus.builder()).build()
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["Receiver", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Receiver.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["notification.toolkit.fluxcd.io/v1beta1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "notification.toolkit.fluxcd.io/v1beta1"
    kind: Annotated[
        Optional[Literal["Receiver"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Receiver"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ReceiverSpec] = None
    status: Optional[ReceiverStatus] = None
