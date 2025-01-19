# Generated by cloudcoil-model-codegen v0.0.31
# DO NOT EDIT

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Dict, List, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseModel
from cloudcoil.resources import Resource


class NamespaceSelector(BaseModel):
    match_labels: Annotated[
        Optional[Dict[str, str]],
        Field(
            alias="matchLabels",
            description='MatchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels\nmap is equivalent to an element of matchExpressions, whose key field is "key", the\noperator is "In", and the values array contains only "value". The requirements are ANDed.',
        ),
    ] = None


class AccessFrom(BaseModel):
    namespace_selectors: Annotated[
        List[NamespaceSelector],
        Field(
            alias="namespaceSelectors",
            description="NamespaceSelectors is the list of namespace selectors to which this ACL applies.\nItems in this list are evaluated using a logical OR operation.",
        ),
    ]


class SecretRef(BaseModel):
    name: Annotated[str, Field(description="Name of the referent.")]


class BucketSpec(BaseModel):
    access_from: Annotated[
        Optional[AccessFrom],
        Field(
            alias="accessFrom",
            description="AccessFrom defines an Access Control List for allowing cross-namespace references to this object.",
        ),
    ] = None
    bucket_name: Annotated[str, Field(alias="bucketName", description="The bucket name.")]
    endpoint: Annotated[str, Field(description="The bucket endpoint address.")]
    ignore: Annotated[
        Optional[str],
        Field(
            description="Ignore overrides the set of excluded patterns in the .sourceignore format\n(which is the same as .gitignore). If not provided, a default will be used,\nconsult the documentation for your version to find out what those are."
        ),
    ] = None
    insecure: Annotated[
        Optional[bool],
        Field(description="Insecure allows connecting to a non-TLS S3 HTTP endpoint."),
    ] = None
    interval: Annotated[
        str, Field(description="The interval at which to check for bucket updates.")
    ]
    provider: Annotated[
        Optional[Literal["generic", "aws", "gcp"]],
        Field(description="The S3 compatible storage provider name, default ('generic')."),
    ] = "generic"
    region: Annotated[Optional[str], Field(description="The bucket region.")] = None
    secret_ref: Annotated[
        Optional[SecretRef],
        Field(
            alias="secretRef",
            description="The name of the secret containing authentication credentials\nfor the Bucket.",
        ),
    ] = None
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend the reconciliation of this source."
        ),
    ] = None
    timeout: Annotated[
        Optional[str],
        Field(description="The timeout for download operations, defaults to 60s."),
    ] = "60s"


class Artifact(BaseModel):
    checksum: Annotated[
        Optional[str],
        Field(description="Checksum is the SHA256 checksum of the artifact."),
    ] = None
    last_update_time: Annotated[
        datetime,
        Field(
            alias="lastUpdateTime",
            description="LastUpdateTime is the timestamp corresponding to the last update of this\nartifact.",
        ),
    ]
    path: Annotated[str, Field(description="Path is the relative file path of this artifact.")]
    revision: Annotated[
        Optional[str],
        Field(
            description="Revision is a human readable identifier traceable in the origin source\nsystem. It can be a Git commit SHA, Git tag, a Helm index timestamp, a Helm\nchart version, etc."
        ),
    ] = None
    url: Annotated[str, Field(description="URL is the HTTP address of this artifact.")]


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


class BucketStatus(BaseModel):
    artifact: Annotated[
        Optional[Artifact],
        Field(description="Artifact represents the output of the last successful Bucket sync."),
    ] = None
    conditions: Annotated[
        Optional[List[Condition]],
        Field(description="Conditions holds the conditions for the Bucket."),
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
            description="ObservedGeneration is the last observed generation.",
        ),
    ] = None
    url: Annotated[
        Optional[str],
        Field(
            description="URL is the download link for the artifact output of the last Bucket sync."
        ),
    ] = None


class Repository(BaseModel):
    name: Annotated[str, Field(description="Name of the referent.")]


class Include(BaseModel):
    from_path: Annotated[
        Optional[str],
        Field(
            alias="fromPath",
            description="The path to copy contents from, defaults to the root directory.",
        ),
    ] = None
    repository: Annotated[Repository, Field(description="Reference to a GitRepository to include.")]
    to_path: Annotated[
        Optional[str],
        Field(
            alias="toPath",
            description="The path to copy contents to, defaults to the name of the source ref.",
        ),
    ] = None


class Ref(BaseModel):
    branch: Annotated[
        Optional[str],
        Field(description="The Git branch to checkout, defaults to master."),
    ] = None
    commit: Annotated[
        Optional[str],
        Field(
            description="The Git commit SHA to checkout, if specified Tag filters will be ignored."
        ),
    ] = None
    semver: Annotated[
        Optional[str],
        Field(description="The Git tag semver expression, takes precedence over Tag."),
    ] = None
    tag: Annotated[
        Optional[str],
        Field(description="The Git tag to checkout, takes precedence over Branch."),
    ] = None


class Verify(BaseModel):
    mode: Annotated[
        Literal["head"],
        Field(description="Mode describes what git object should be verified, currently ('head')."),
    ]
    secret_ref: Annotated[
        Optional[SecretRef],
        Field(
            alias="secretRef",
            description="The secret name containing the public keys of all trusted Git authors.",
        ),
    ] = None


class GitRepositorySpec(BaseModel):
    access_from: Annotated[
        Optional[AccessFrom],
        Field(
            alias="accessFrom",
            description="AccessFrom defines an Access Control List for allowing cross-namespace references to this object.",
        ),
    ] = None
    git_implementation: Annotated[
        Optional[Literal["go-git", "libgit2"]],
        Field(
            alias="gitImplementation",
            description="Determines which git client library to use.\nDefaults to go-git, valid values are ('go-git', 'libgit2').",
        ),
    ] = "go-git"
    ignore: Annotated[
        Optional[str],
        Field(
            description="Ignore overrides the set of excluded patterns in the .sourceignore format\n(which is the same as .gitignore). If not provided, a default will be used,\nconsult the documentation for your version to find out what those are."
        ),
    ] = None
    include: Annotated[
        Optional[List[Include]],
        Field(description="Extra git repositories to map into the repository"),
    ] = None
    interval: Annotated[
        str, Field(description="The interval at which to check for repository updates.")
    ]
    recurse_submodules: Annotated[
        Optional[bool],
        Field(
            alias="recurseSubmodules",
            description="When enabled, after the clone is created, initializes all submodules within,\nusing their default settings.\nThis option is available only when using the 'go-git' GitImplementation.",
        ),
    ] = None
    ref: Annotated[
        Optional[Ref],
        Field(
            description="The Git reference to checkout and monitor for changes, defaults to\nmaster branch."
        ),
    ] = None
    secret_ref: Annotated[
        Optional[SecretRef],
        Field(
            alias="secretRef",
            description="The secret name containing the Git credentials.\nFor HTTPS repositories the secret must contain username and password\nfields.\nFor SSH repositories the secret must contain identity and known_hosts\nfields.",
        ),
    ] = None
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend the reconciliation of this source."
        ),
    ] = None
    timeout: Annotated[
        Optional[str],
        Field(description="The timeout for remote Git operations like cloning, defaults to 60s."),
    ] = "60s"
    url: Annotated[
        str,
        Field(
            description="The repository URL, can be a HTTP/S or SSH address.",
            pattern="^(http|https|ssh)://.*$",
        ),
    ]
    verify: Annotated[
        Optional[Verify],
        Field(description="Verify OpenPGP signature for the Git commit HEAD points to."),
    ] = None


class IncludedArtifact(BaseModel):
    checksum: Annotated[
        Optional[str],
        Field(description="Checksum is the SHA256 checksum of the artifact."),
    ] = None
    last_update_time: Annotated[
        datetime,
        Field(
            alias="lastUpdateTime",
            description="LastUpdateTime is the timestamp corresponding to the last update of this\nartifact.",
        ),
    ]
    path: Annotated[str, Field(description="Path is the relative file path of this artifact.")]
    revision: Annotated[
        Optional[str],
        Field(
            description="Revision is a human readable identifier traceable in the origin source\nsystem. It can be a Git commit SHA, Git tag, a Helm index timestamp, a Helm\nchart version, etc."
        ),
    ] = None
    url: Annotated[str, Field(description="URL is the HTTP address of this artifact.")]


class GitRepositoryStatus(BaseModel):
    artifact: Annotated[
        Optional[Artifact],
        Field(description="Artifact represents the output of the last successful repository sync."),
    ] = None
    conditions: Annotated[
        Optional[List[Condition]],
        Field(description="Conditions holds the conditions for the GitRepository."),
    ] = None
    included_artifacts: Annotated[
        Optional[List[IncludedArtifact]],
        Field(
            alias="includedArtifacts",
            description="IncludedArtifacts represents the included artifacts from the last successful repository sync.",
        ),
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
            description="ObservedGeneration is the last observed generation.",
        ),
    ] = None
    url: Annotated[
        Optional[str],
        Field(
            description="URL is the download link for the artifact output of the last repository\nsync."
        ),
    ] = None


class SourceRef(BaseModel):
    api_version: Annotated[
        Optional[str],
        Field(alias="apiVersion", description="APIVersion of the referent."),
    ] = None
    kind: Annotated[
        Literal["HelmRepository", "GitRepository", "Bucket"],
        Field(
            description="Kind of the referent, valid values are ('HelmRepository', 'GitRepository',\n'Bucket')."
        ),
    ]
    name: Annotated[str, Field(description="Name of the referent.")]


class HelmChartSpec(BaseModel):
    access_from: Annotated[
        Optional[AccessFrom],
        Field(
            alias="accessFrom",
            description="AccessFrom defines an Access Control List for allowing cross-namespace references to this object.",
        ),
    ] = None
    chart: Annotated[
        str,
        Field(description="The name or path the Helm chart is available at in the SourceRef."),
    ]
    interval: Annotated[
        str, Field(description="The interval at which to check the Source for updates.")
    ]
    reconcile_strategy: Annotated[
        Optional[Literal["ChartVersion", "Revision"]],
        Field(
            alias="reconcileStrategy",
            description="Determines what enables the creation of a new artifact. Valid values are\n('ChartVersion', 'Revision').\nSee the documentation of the values for an explanation on their behavior.\nDefaults to ChartVersion when omitted.",
        ),
    ] = "ChartVersion"
    source_ref: Annotated[
        SourceRef,
        Field(
            alias="sourceRef",
            description="The reference to the Source the chart is available at.",
        ),
    ]
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend the reconciliation of this source."
        ),
    ] = None
    values_file: Annotated[
        Optional[str],
        Field(
            alias="valuesFile",
            description="Alternative values file to use as the default chart values, expected to\nbe a relative path in the SourceRef. Deprecated in favor of ValuesFiles,\nfor backwards compatibility the file defined here is merged before the\nValuesFiles items. Ignored when omitted.",
        ),
    ] = None
    values_files: Annotated[
        Optional[List[str]],
        Field(
            alias="valuesFiles",
            description="Alternative list of values files to use as the chart values (values.yaml\nis not included by default), expected to be a relative path in the SourceRef.\nValues files are merged in the order of this list with the last file overriding\nthe first. Ignored when omitted.",
        ),
    ] = None
    version: Annotated[
        Optional[str],
        Field(
            description="The chart version semver expression, ignored for charts from GitRepository\nand Bucket sources. Defaults to latest when omitted."
        ),
    ] = "*"


class HelmChartStatus(BaseModel):
    artifact: Annotated[
        Optional[Artifact],
        Field(description="Artifact represents the output of the last successful chart sync."),
    ] = None
    conditions: Annotated[
        Optional[List[Condition]],
        Field(description="Conditions holds the conditions for the HelmChart."),
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
            description="ObservedGeneration is the last observed generation.",
        ),
    ] = None
    url: Annotated[
        Optional[str],
        Field(description="URL is the download link for the last chart pulled."),
    ] = None


class HelmRepositorySpec(BaseModel):
    access_from: Annotated[
        Optional[AccessFrom],
        Field(
            alias="accessFrom",
            description="AccessFrom defines an Access Control List for allowing cross-namespace references to this object.",
        ),
    ] = None
    interval: Annotated[
        str,
        Field(description="The interval at which to check the upstream for updates."),
    ]
    pass_credentials: Annotated[
        Optional[bool],
        Field(
            alias="passCredentials",
            description="PassCredentials allows the credentials from the SecretRef to be passed on to\na host that does not match the host as defined in URL.\nThis may be required if the host of the advertised chart URLs in the index\ndiffer from the defined URL.\nEnabling this should be done with caution, as it can potentially result in\ncredentials getting stolen in a MITM-attack.",
        ),
    ] = None
    secret_ref: Annotated[
        Optional[SecretRef],
        Field(
            alias="secretRef",
            description="The name of the secret containing authentication credentials for the Helm\nrepository.\nFor HTTP/S basic auth the secret must contain username and\npassword fields.\nFor TLS the secret must contain a certFile and keyFile, and/or\ncaFile fields.",
        ),
    ] = None
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend the reconciliation of this source."
        ),
    ] = None
    timeout: Annotated[
        Optional[str],
        Field(description="The timeout of index downloading, defaults to 60s."),
    ] = "60s"
    url: Annotated[
        str,
        Field(
            description="The Helm repository URL, a valid URL contains at least a protocol and host."
        ),
    ]


class HelmRepositoryStatus(BaseModel):
    artifact: Annotated[
        Optional[Artifact],
        Field(description="Artifact represents the output of the last successful repository sync."),
    ] = None
    conditions: Annotated[
        Optional[List[Condition]],
        Field(description="Conditions holds the conditions for the HelmRepository."),
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
            description="ObservedGeneration is the last observed generation.",
        ),
    ] = None
    url: Annotated[
        Optional[str],
        Field(description="URL is the download link for the last index fetched."),
    ] = None


class Bucket(Resource):
    api_version: Annotated[
        Optional[Literal["source.toolkit.fluxcd.io/v1beta1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "source.toolkit.fluxcd.io/v1beta1"
    kind: Annotated[
        Optional[Literal["Bucket"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Bucket"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[BucketSpec] = None
    status: Optional[BucketStatus] = None


class GitRepository(Resource):
    api_version: Annotated[
        Optional[Literal["source.toolkit.fluxcd.io/v1beta1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "source.toolkit.fluxcd.io/v1beta1"
    kind: Annotated[
        Optional[Literal["GitRepository"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "GitRepository"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[GitRepositorySpec] = None
    status: Optional[GitRepositoryStatus] = None


class HelmChart(Resource):
    api_version: Annotated[
        Optional[Literal["source.toolkit.fluxcd.io/v1beta1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "source.toolkit.fluxcd.io/v1beta1"
    kind: Annotated[
        Optional[Literal["HelmChart"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "HelmChart"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[HelmChartSpec] = None
    status: Optional[HelmChartStatus] = None


class HelmRepository(Resource):
    api_version: Annotated[
        Optional[Literal["source.toolkit.fluxcd.io/v1beta1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "source.toolkit.fluxcd.io/v1beta1"
    kind: Annotated[
        Optional[Literal["HelmRepository"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "HelmRepository"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[HelmRepositorySpec] = None
    status: Optional[HelmRepositoryStatus] = None
