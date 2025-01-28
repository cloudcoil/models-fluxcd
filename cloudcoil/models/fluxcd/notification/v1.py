# Generated by cloudcoil-model-codegen v0.4.0
# DO NOT EDIT

from __future__ import annotations

from datetime import datetime
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


class ResourceModel(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ResourceModel"]:
            return ResourceModel

        def build(self) -> "ResourceModel":
            return ResourceModel(**self._attrs)

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

    class BuilderContext(BuilderContextBase["ResourceModel.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ResourceModel.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ResourceModel."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ResourceModel", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ResourceModel.list_builder() instead."
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


class ReceiverSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ReceiverSpec"]:
            return ReceiverSpec

        def build(self) -> "ReceiverSpec":
            return ReceiverSpec(**self._attrs)

        def events(self, value: Optional[List[str]], /) -> Self:
            """
            Events specifies the list of event types to handle,
            e.g. 'push' for GitHub or 'Push Hook' for GitLab.
            """
            return self._set("events", value)

        def interval(self, value: Optional[str], /) -> Self:
            """
            Interval at which to reconcile the Receiver with its Secret references.
            """
            return self._set("interval", value)

        @overload
        def resources(
            self, value_or_callback: List[ResourceModel], /
        ) -> "ReceiverSpec.Builder": ...

        @overload
        def resources(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[ResourceModel, ResourceModel.Builder]],
                GenericListBuilder[ResourceModel, ResourceModel.Builder] | List[ResourceModel],
            ],
            /,
        ) -> "ReceiverSpec.Builder": ...

        @overload
        def resources(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[ResourceModel.Builder]: ...

        def resources(self, value_or_callback=None, /):
            """
            A list of resources to be notified about changes.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[ResourceModel.Builder]()
                context._parent_builder = self
                context._field_name = "resources"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ResourceModel.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("resources", value)

        @overload
        def secret_ref(self, value_or_callback: SecretRef, /) -> "ReceiverSpec.Builder": ...

        @overload
        def secret_ref(
            self,
            value_or_callback: Callable[[SecretRef.Builder], SecretRef.Builder | SecretRef],
            /,
        ) -> "ReceiverSpec.Builder": ...

        @overload
        def secret_ref(self, value_or_callback: Never = ...) -> "SecretRef.BuilderContext": ...

        def secret_ref(self, value_or_callback=None, /):
            """
            SecretRef specifies the Secret containing the token used
            to validate the payload authenticity.
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
            events handling for this receiver.
            """
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
                "cdevents",
            ],
            /,
        ) -> Self:
            """
            Type of webhook sender, used to determine
            the validation procedure and payload deserialization.
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["ReceiverSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ReceiverSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ReceiverSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ReceiverSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ReceiverSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    events: Optional[List[str]] = None
    """
    Events specifies the list of event types to handle,
    e.g. 'push' for GitHub or 'Push Hook' for GitLab.
    """
    interval: Annotated[Optional[str], Field(pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m|h))+$")] = "10m"
    """
    Interval at which to reconcile the Receiver with its Secret references.
    """
    resources: List[ResourceModel]
    """
    A list of resources to be notified about changes.
    """
    secret_ref: Annotated[SecretRef, Field(alias="secretRef")]
    """
    SecretRef specifies the Secret containing the token used
    to validate the payload authenticity.
    """
    suspend: Optional[bool] = None
    """
    Suspend tells the controller to suspend subsequent
    events handling for this receiver.
    """
    type: Literal[
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
    ]
    """
    Type of webhook sender, used to determine
    the validation procedure and payload deserialization.
    """


class Condition(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Condition"]:
            return Condition

        def build(self) -> "Condition":
            return Condition(**self._attrs)

        def last_transition_time(self, value: datetime, /) -> Self:
            """
            lastTransitionTime is the last time the condition transitioned from one status to another.
            This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
            """
            return self._set("last_transition_time", value)

        def message(self, value: str, /) -> Self:
            """
            message is a human readable message indicating details about the transition.
            This may be an empty string.
            """
            return self._set("message", value)

        def observed_generation(self, value: Optional[int], /) -> Self:
            """
            observedGeneration represents the .metadata.generation that the condition was set based upon.
            For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
            with respect to the current state of the instance.
            """
            return self._set("observed_generation", value)

        def reason(self, value: str, /) -> Self:
            """
            reason contains a programmatic identifier indicating the reason for the condition's last transition.
            Producers of specific condition types may define expected values and meanings for this field,
            and whether the values are considered a guaranteed API.
            The value should be a CamelCase string.
            This field may not be empty.
            """
            return self._set("reason", value)

        def status(self, value: Literal["True", "False", "Unknown"], /) -> Self:
            """
            status of the condition, one of True, False, Unknown.
            """
            return self._set("status", value)

        def type(self, value: str, /) -> Self:
            """
            type of condition in CamelCase or in foo.example.com/CamelCase.
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["Condition.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Condition.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Condition."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Condition", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Condition.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    last_transition_time: Annotated[datetime, Field(alias="lastTransitionTime")]
    """
    lastTransitionTime is the last time the condition transitioned from one status to another.
    This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
    """
    message: Annotated[str, Field(max_length=32768)]
    """
    message is a human readable message indicating details about the transition.
    This may be an empty string.
    """
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration", ge=0)] = None
    """
    observedGeneration represents the .metadata.generation that the condition was set based upon.
    For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
    with respect to the current state of the instance.
    """
    reason: Annotated[
        str,
        Field(
            max_length=1024,
            min_length=1,
            pattern="^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$",
        ),
    ]
    """
    reason contains a programmatic identifier indicating the reason for the condition's last transition.
    Producers of specific condition types may define expected values and meanings for this field,
    and whether the values are considered a guaranteed API.
    The value should be a CamelCase string.
    This field may not be empty.
    """
    status: Literal["True", "False", "Unknown"]
    """
    status of the condition, one of True, False, Unknown.
    """
    type: Annotated[
        str,
        Field(
            max_length=316,
            pattern="^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$",
        ),
    ]
    """
    type of condition in CamelCase or in foo.example.com/CamelCase.
    """


class ReceiverStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ReceiverStatus"]:
            return ReceiverStatus

        def build(self) -> "ReceiverStatus":
            return ReceiverStatus(**self._attrs)

        @overload
        def conditions(self, value_or_callback: List[Condition], /) -> "ReceiverStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[Condition, Condition.Builder]],
                GenericListBuilder[Condition, Condition.Builder] | List[Condition],
            ],
            /,
        ) -> "ReceiverStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[Condition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            """
            Conditions holds the conditions for the Receiver.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[Condition.Builder]()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Condition.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

        def last_handled_reconcile_at(self, value: Optional[str], /) -> Self:
            """
            LastHandledReconcileAt holds the value of the most recent
            reconcile request value, so a change of the annotation value
            can be detected.
            """
            return self._set("last_handled_reconcile_at", value)

        def observed_generation(self, value: Optional[int], /) -> Self:
            """
            ObservedGeneration is the last observed generation of the Receiver object.
            """
            return self._set("observed_generation", value)

        def webhook_path(self, value: Optional[str], /) -> Self:
            """
            WebhookPath is the generated incoming webhook address in the format
            of '/hook/sha256sum(token+name+namespace)'.
            """
            return self._set("webhook_path", value)

    class BuilderContext(BuilderContextBase["ReceiverStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ReceiverStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ReceiverStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ReceiverStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ReceiverStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[Condition]] = None
    """
    Conditions holds the conditions for the Receiver.
    """
    last_handled_reconcile_at: Annotated[Optional[str], Field(alias="lastHandledReconcileAt")] = (
        None
    )
    """
    LastHandledReconcileAt holds the value of the most recent
    reconcile request value, so a change of the annotation value
    can be detected.
    """
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration")] = None
    """
    ObservedGeneration is the last observed generation of the Receiver object.
    """
    webhook_path: Annotated[Optional[str], Field(alias="webhookPath")] = None
    """
    WebhookPath is the generated incoming webhook address in the format
    of '/hook/sha256sum(token+name+namespace)'.
    """


class Receiver(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Receiver"]:
            return Receiver

        def build(self) -> "Receiver":
            return Receiver(**self._attrs)

        def api_version(
            self, value: Optional[Literal["notification.toolkit.fluxcd.io/v1"]], /
        ) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object.
            Servers should convert recognized schemas to the latest internal value, and
            may reject unrecognized values.
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Receiver"]], /) -> Self:
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
        ) -> "Receiver.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "Receiver.Builder": ...

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
        def spec(self, value_or_callback: Optional[ReceiverSpec], /) -> "Receiver.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [ReceiverSpec.Builder], ReceiverSpec.Builder | ReceiverSpec
            ],
            /,
        ) -> "Receiver.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "ReceiverSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = ReceiverSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ReceiverSpec.builder())
                if isinstance(output, ReceiverSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(self, value_or_callback: Optional[ReceiverStatus], /) -> "Receiver.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [ReceiverStatus.Builder], ReceiverStatus.Builder | ReceiverStatus
            ],
            /,
        ) -> "Receiver.Builder": ...

        @overload
        def status(self, value_or_callback: Never = ...) -> "ReceiverStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = ReceiverStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ReceiverStatus.builder())
                if isinstance(output, ReceiverStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["Receiver.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Receiver.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Receiver."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Receiver", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Receiver.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["notification.toolkit.fluxcd.io/v1"]],
        Field(alias="apiVersion"),
    ] = "notification.toolkit.fluxcd.io/v1"
    """
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["Receiver"]] = "Receiver"
    """
    Kind is a string value representing the REST resource this object represents.
    Servers may infer this from the endpoint the client submits requests to.
    Cannot be updated.
    In CamelCase.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ReceiverSpec] = None
    status: Optional[ReceiverStatus] = None
