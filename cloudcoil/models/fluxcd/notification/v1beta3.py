# Generated by cloudcoil-model-codegen v0.4.7
# DO NOT EDIT

from __future__ import annotations

from typing import (
    Annotated,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    overload,
)

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import (
    BaseModel,
    BaseModelBuilder,
    BuilderContextBase,
    GenericListBuilder,
    ListBuilderContext,
    Never,
    Self,
)
from cloudcoil.resources import Resource


class EventSource(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EventSource"]:
            return EventSource

        def build(self) -> "EventSource":
            return EventSource(**self._attrs)

        def api_version(self, value: Optional[str], /) -> Self:
            """
            API version of the referent
            """
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
            /,
        ) -> Self:
            """
            Kind of the referent
            """
            return self._set("kind", value)

        def match_labels(self, value: Optional[Dict[str, str]], /) -> Self:
            """
            MatchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
            map is equivalent to an element of matchExpressions, whose key field is "key", the
            operator is "In", and the values array contains only "value". The requirements are ANDed.
            MatchLabels requires the name to be set to `*`.
            """
            return self._set("match_labels", value)

        def name(self, value: str, /) -> Self:
            """
            Name of the referent
            If multiple resources are targeted `*` may be set.
            """
            return self._set("name", value)

        def namespace(self, value: Optional[str], /) -> Self:
            """
            Namespace of the referent
            """
            return self._set("namespace", value)

    class BuilderContext(BuilderContextBase["EventSource.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EventSource.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EventSource."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EventSource", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EventSource.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[str], Field(alias="apiVersion")] = None
    """
    API version of the referent
    """
    kind: Literal[
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
    ]
    """
    Kind of the referent
    """
    match_labels: Annotated[Optional[Dict[str, str]], Field(alias="matchLabels")] = None
    """
    MatchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
    map is equivalent to an element of matchExpressions, whose key field is "key", the
    operator is "In", and the values array contains only "value". The requirements are ANDed.
    MatchLabels requires the name to be set to `*`.
    """
    name: Annotated[str, Field(max_length=53, min_length=1)]
    """
    Name of the referent
    If multiple resources are targeted `*` may be set.
    """
    namespace: Annotated[Optional[str], Field(max_length=53, min_length=1)] = None
    """
    Namespace of the referent
    """


class ProviderRef(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ProviderRef"]:
            return ProviderRef

        def build(self) -> "ProviderRef":
            return ProviderRef(**self._attrs)

        def name(self, value: str, /) -> Self:
            """
            Name of the referent.
            """
            return self._set("name", value)

    class BuilderContext(BuilderContextBase["ProviderRef.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ProviderRef.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ProviderRef."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ProviderRef", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ProviderRef.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    name: str
    """
    Name of the referent.
    """


class AlertSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["AlertSpec"]:
            return AlertSpec

        def build(self) -> "AlertSpec":
            return AlertSpec(**self._attrs)

        def event_metadata(self, value: Optional[Dict[str, str]], /) -> Self:
            """
            EventMetadata is an optional field for adding metadata to events dispatched by the
            controller. This can be used for enhancing the context of the event. If a field
            would override one already present on the original event as generated by the emitter,
            then the override doesn't happen, i.e. the original value is preserved, and an info
            log is printed.
            """
            return self._set("event_metadata", value)

        def event_severity(self, value: Optional[Literal["info", "error"]], /) -> Self:
            """
            EventSeverity specifies how to filter events based on severity.
            If set to 'info' no events will be filtered.
            """
            return self._set("event_severity", value)

        @overload
        def event_sources(self, value_or_callback: List[EventSource], /) -> "AlertSpec.Builder": ...

        @overload
        def event_sources(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[EventSource, EventSource.Builder]],
                GenericListBuilder[EventSource, EventSource.Builder] | List[EventSource],
            ],
            /,
        ) -> "AlertSpec.Builder": ...

        @overload
        def event_sources(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[EventSource.Builder]: ...

        def event_sources(self, value_or_callback=None, /):
            """
            EventSources specifies how to filter events based
            on the involved object kind, name and namespace.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[EventSource.Builder]()
                context._parent_builder = self
                context._field_name = "event_sources"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(EventSource.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("event_sources", value)

        def exclusion_list(self, value: Optional[List[str]], /) -> Self:
            """
            ExclusionList specifies a list of Golang regular expressions
            to be used for excluding messages.
            """
            return self._set("exclusion_list", value)

        def inclusion_list(self, value: Optional[List[str]], /) -> Self:
            """
            InclusionList specifies a list of Golang regular expressions
            to be used for including messages.
            """
            return self._set("inclusion_list", value)

        @overload
        def provider_ref(self, value_or_callback: ProviderRef, /) -> "AlertSpec.Builder": ...

        @overload
        def provider_ref(
            self,
            value_or_callback: Callable[[ProviderRef.Builder], ProviderRef.Builder | ProviderRef],
            /,
        ) -> "AlertSpec.Builder": ...

        @overload
        def provider_ref(self, value_or_callback: Never = ...) -> "ProviderRef.BuilderContext": ...

        def provider_ref(self, value_or_callback=None, /):
            """
            ProviderRef specifies which Provider this Alert should use.
            """
            if self._in_context and value_or_callback is None:
                context = ProviderRef.BuilderContext()
                context._parent_builder = self
                context._field_name = "provider_ref"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ProviderRef.builder())
                if isinstance(output, ProviderRef.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("provider_ref", value)

        def summary(self, value: Optional[str], /) -> Self:
            """
            Summary holds a short description of the impact and affected cluster.
            """
            return self._set("summary", value)

        def suspend(self, value: Optional[bool], /) -> Self:
            """
            Suspend tells the controller to suspend subsequent
            events handling for this Alert.
            """
            return self._set("suspend", value)

    class BuilderContext(BuilderContextBase["AlertSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = AlertSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for AlertSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["AlertSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use AlertSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    event_metadata: Annotated[Optional[Dict[str, str]], Field(alias="eventMetadata")] = None
    """
    EventMetadata is an optional field for adding metadata to events dispatched by the
    controller. This can be used for enhancing the context of the event. If a field
    would override one already present on the original event as generated by the emitter,
    then the override doesn't happen, i.e. the original value is preserved, and an info
    log is printed.
    """
    event_severity: Annotated[Optional[Literal["info", "error"]], Field(alias="eventSeverity")] = (
        "info"
    )
    """
    EventSeverity specifies how to filter events based on severity.
    If set to 'info' no events will be filtered.
    """
    event_sources: Annotated[List[EventSource], Field(alias="eventSources")]
    """
    EventSources specifies how to filter events based
    on the involved object kind, name and namespace.
    """
    exclusion_list: Annotated[Optional[List[str]], Field(alias="exclusionList")] = None
    """
    ExclusionList specifies a list of Golang regular expressions
    to be used for excluding messages.
    """
    inclusion_list: Annotated[Optional[List[str]], Field(alias="inclusionList")] = None
    """
    InclusionList specifies a list of Golang regular expressions
    to be used for including messages.
    """
    provider_ref: Annotated[ProviderRef, Field(alias="providerRef")]
    """
    ProviderRef specifies which Provider this Alert should use.
    """
    summary: Annotated[Optional[str], Field(max_length=255)] = None
    """
    Summary holds a short description of the impact and affected cluster.
    """
    suspend: Optional[bool] = None
    """
    Suspend tells the controller to suspend subsequent
    events handling for this Alert.
    """


class CertSecretRef(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["CertSecretRef"]:
            return CertSecretRef

        def build(self) -> "CertSecretRef":
            return CertSecretRef(**self._attrs)

        def name(self, value: str, /) -> Self:
            """
            Name of the referent.
            """
            return self._set("name", value)

    class BuilderContext(BuilderContextBase["CertSecretRef.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = CertSecretRef.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for CertSecretRef."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["CertSecretRef", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use CertSecretRef.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    name: str
    """
    Name of the referent.
    """


class SecretRef(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["SecretRef"]:
            return SecretRef

        def build(self) -> "SecretRef":
            return SecretRef(**self._attrs)

        def name(self, value: str, /) -> Self:
            """
            Name of the referent.
            """
            return self._set("name", value)

    class BuilderContext(BuilderContextBase["SecretRef.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = SecretRef.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for SecretRef."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["SecretRef", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use SecretRef.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    name: str
    """
    Name of the referent.
    """


class ProviderSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ProviderSpec"]:
            return ProviderSpec

        def build(self) -> "ProviderSpec":
            return ProviderSpec(**self._attrs)

        def address(self, value: Optional[str], /) -> Self:
            """
            Address specifies the endpoint, in a generic sense, to where alerts are sent.
            What kind of endpoint depends on the specific Provider type being used.
            For the generic Provider, for example, this is an HTTP/S address.
            For other Provider types this could be a project ID or a namespace.
            """
            return self._set("address", value)

        @overload
        def cert_secret_ref(
            self, value_or_callback: Optional[CertSecretRef], /
        ) -> "ProviderSpec.Builder": ...

        @overload
        def cert_secret_ref(
            self,
            value_or_callback: Callable[
                [CertSecretRef.Builder], CertSecretRef.Builder | CertSecretRef
            ],
            /,
        ) -> "ProviderSpec.Builder": ...

        @overload
        def cert_secret_ref(
            self, value_or_callback: Never = ...
        ) -> "CertSecretRef.BuilderContext": ...

        def cert_secret_ref(self, value_or_callback=None, /):
            """
            CertSecretRef specifies the Secret containing
            a PEM-encoded CA certificate (in the `ca.crt` key).

            Note: Support for the `caFile` key has
            been deprecated.
            """
            if self._in_context and value_or_callback is None:
                context = CertSecretRef.BuilderContext()
                context._parent_builder = self
                context._field_name = "cert_secret_ref"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(CertSecretRef.builder())
                if isinstance(output, CertSecretRef.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("cert_secret_ref", value)

        def channel(self, value: Optional[str], /) -> Self:
            """
            Channel specifies the destination channel where events should be posted.
            """
            return self._set("channel", value)

        def interval(self, value: Optional[str], /) -> Self:
            """
            Interval at which to reconcile the Provider with its Secret references.
            Deprecated and not used in v1beta3.
            """
            return self._set("interval", value)

        def proxy(self, value: Optional[str], /) -> Self:
            """
            Proxy the HTTP/S address of the proxy server.
            """
            return self._set("proxy", value)

        @overload
        def secret_ref(
            self, value_or_callback: Optional[SecretRef], /
        ) -> "ProviderSpec.Builder": ...

        @overload
        def secret_ref(
            self,
            value_or_callback: Callable[[SecretRef.Builder], SecretRef.Builder | SecretRef],
            /,
        ) -> "ProviderSpec.Builder": ...

        @overload
        def secret_ref(self, value_or_callback: Never = ...) -> "SecretRef.BuilderContext": ...

        def secret_ref(self, value_or_callback=None, /):
            """
            SecretRef specifies the Secret containing the authentication
            credentials for this Provider.
            """
            if self._in_context and value_or_callback is None:
                context = SecretRef.BuilderContext()
                context._parent_builder = self
                context._field_name = "secret_ref"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(SecretRef.builder())
                if isinstance(output, SecretRef.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("secret_ref", value)

        def suspend(self, value: Optional[bool], /) -> Self:
            """
            Suspend tells the controller to suspend subsequent
            events handling for this Provider.
            """
            return self._set("suspend", value)

        def timeout(self, value: Optional[str], /) -> Self:
            """
            Timeout for sending alerts to the Provider.
            """
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
                "gitea",
                "bitbucketserver",
                "bitbucket",
                "azuredevops",
                "googlechat",
                "googlepubsub",
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
                "pagerduty",
                "datadog",
                "nats",
            ],
            /,
        ) -> Self:
            """
            Type specifies which Provider implementation to use.
            """
            return self._set("type", value)

        def username(self, value: Optional[str], /) -> Self:
            """
            Username specifies the name under which events are posted.
            """
            return self._set("username", value)

    class BuilderContext(BuilderContextBase["ProviderSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ProviderSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ProviderSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ProviderSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ProviderSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    address: Annotated[Optional[str], Field(max_length=2048)] = None
    """
    Address specifies the endpoint, in a generic sense, to where alerts are sent.
    What kind of endpoint depends on the specific Provider type being used.
    For the generic Provider, for example, this is an HTTP/S address.
    For other Provider types this could be a project ID or a namespace.
    """
    cert_secret_ref: Annotated[Optional[CertSecretRef], Field(alias="certSecretRef")] = None
    """
    CertSecretRef specifies the Secret containing
    a PEM-encoded CA certificate (in the `ca.crt` key).

    Note: Support for the `caFile` key has
    been deprecated.
    """
    channel: Annotated[Optional[str], Field(max_length=2048)] = None
    """
    Channel specifies the destination channel where events should be posted.
    """
    interval: Annotated[Optional[str], Field(pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m|h))+$")] = None
    """
    Interval at which to reconcile the Provider with its Secret references.
    Deprecated and not used in v1beta3.
    """
    proxy: Annotated[Optional[str], Field(max_length=2048, pattern="^(http|https)://.*$")] = None
    """
    Proxy the HTTP/S address of the proxy server.
    """
    secret_ref: Annotated[Optional[SecretRef], Field(alias="secretRef")] = None
    """
    SecretRef specifies the Secret containing the authentication
    credentials for this Provider.
    """
    suspend: Optional[bool] = None
    """
    Suspend tells the controller to suspend subsequent
    events handling for this Provider.
    """
    timeout: Annotated[Optional[str], Field(pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m))+$")] = None
    """
    Timeout for sending alerts to the Provider.
    """
    type: Literal[
        "slack",
        "discord",
        "msteams",
        "rocket",
        "generic",
        "generic-hmac",
        "github",
        "gitlab",
        "gitea",
        "bitbucketserver",
        "bitbucket",
        "azuredevops",
        "googlechat",
        "googlepubsub",
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
        "pagerduty",
        "datadog",
        "nats",
    ]
    """
    Type specifies which Provider implementation to use.
    """
    username: Annotated[Optional[str], Field(max_length=2048)] = None
    """
    Username specifies the name under which events are posted.
    """


class Alert(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Alert"]:
            return Alert

        def build(self) -> "Alert":
            return Alert(**self._attrs)

        def api_version(
            self, value: Optional[Literal["notification.toolkit.fluxcd.io/v1beta3"]], /
        ) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object.
            Servers should convert recognized schemas to the latest internal value, and
            may reject unrecognized values.
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Alert"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents.
            Servers may infer this from the endpoint the client submits requests to.
            Cannot be updated.
            In CamelCase.
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "Alert.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "Alert.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = apimachinery.ObjectMeta.BuilderContext()
                context._parent_builder = self
                context._field_name = "metadata"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.ObjectMeta.builder())
                if isinstance(output, apimachinery.ObjectMeta.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("metadata", value)

        @overload
        def spec(self, value_or_callback: Optional[AlertSpec], /) -> "Alert.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[[AlertSpec.Builder], AlertSpec.Builder | AlertSpec],
            /,
        ) -> "Alert.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "AlertSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = AlertSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(AlertSpec.builder())
                if isinstance(output, AlertSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

    class BuilderContext(BuilderContextBase["Alert.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Alert.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Alert."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Alert", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Alert.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["notification.toolkit.fluxcd.io/v1beta3"]],
        Field(alias="apiVersion"),
    ] = "notification.toolkit.fluxcd.io/v1beta3"
    """
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["Alert"]] = "Alert"
    """
    Kind is a string value representing the REST resource this object represents.
    Servers may infer this from the endpoint the client submits requests to.
    Cannot be updated.
    In CamelCase.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[AlertSpec] = None


class Provider(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Provider"]:
            return Provider

        def build(self) -> "Provider":
            return Provider(**self._attrs)

        def api_version(
            self, value: Optional[Literal["notification.toolkit.fluxcd.io/v1beta3"]], /
        ) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object.
            Servers should convert recognized schemas to the latest internal value, and
            may reject unrecognized values.
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Provider"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents.
            Servers may infer this from the endpoint the client submits requests to.
            Cannot be updated.
            In CamelCase.
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "Provider.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "Provider.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = apimachinery.ObjectMeta.BuilderContext()
                context._parent_builder = self
                context._field_name = "metadata"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.ObjectMeta.builder())
                if isinstance(output, apimachinery.ObjectMeta.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("metadata", value)

        @overload
        def spec(self, value_or_callback: Optional[ProviderSpec], /) -> "Provider.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [ProviderSpec.Builder], ProviderSpec.Builder | ProviderSpec
            ],
            /,
        ) -> "Provider.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "ProviderSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = ProviderSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ProviderSpec.builder())
                if isinstance(output, ProviderSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

    class BuilderContext(BuilderContextBase["Provider.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Provider.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Provider."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Provider", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Provider.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["notification.toolkit.fluxcd.io/v1beta3"]],
        Field(alias="apiVersion"),
    ] = "notification.toolkit.fluxcd.io/v1beta3"
    """
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["Provider"]] = "Provider"
    """
    Kind is a string value representing the REST resource this object represents.
    Servers may infer this from the endpoint the client submits requests to.
    Cannot be updated.
    In CamelCase.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ProviderSpec] = None
