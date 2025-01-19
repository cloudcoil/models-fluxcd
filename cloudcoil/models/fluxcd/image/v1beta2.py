# Generated by cloudcoil-model-codegen v0.0.31
# DO NOT EDIT

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Dict, List, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseModel
from cloudcoil.resources import Resource


class FilterTags(BaseModel):
    extract: Annotated[
        Optional[str],
        Field(
            description="Extract allows a capture group to be extracted from the specified regular\nexpression pattern, useful before tag evaluation."
        ),
    ] = None
    pattern: Annotated[
        Optional[str],
        Field(
            description="Pattern specifies a regular expression pattern used to filter for image\ntags."
        ),
    ] = None


class ImageRepositoryRef(BaseModel):
    name: Annotated[str, Field(description="Name of the referent.")]
    namespace: Annotated[
        Optional[str],
        Field(
            description="Namespace of the referent, when not specified it acts as LocalObjectReference."
        ),
    ] = None


class Alphabetical(BaseModel):
    order: Annotated[
        Optional[Literal["asc", "desc"]],
        Field(
            description="Order specifies the sorting order of the tags. Given the letters of the\nalphabet as tags, ascending order would select Z, and descending order\nwould select A."
        ),
    ] = "asc"


class Numerical(BaseModel):
    order: Annotated[
        Optional[Literal["asc", "desc"]],
        Field(
            description="Order specifies the sorting order of the tags. Given the integer values\nfrom 0 to 9 as tags, ascending order would select 9, and descending order\nwould select 0."
        ),
    ] = "asc"


class Semver(BaseModel):
    range: Annotated[
        str,
        Field(
            description="Range gives a semver range for the image tag; the highest\nversion within the range that's a tag yields the latest image."
        ),
    ]


class Policy(BaseModel):
    alphabetical: Annotated[
        Optional[Alphabetical],
        Field(
            description="Alphabetical set of rules to use for alphabetical ordering of the tags."
        ),
    ] = None
    numerical: Annotated[
        Optional[Numerical],
        Field(description="Numerical set of rules to use for numerical ordering of the tags."),
    ] = None
    semver: Annotated[
        Optional[Semver],
        Field(
            description="SemVer gives a semantic version range to check against the tags\navailable."
        ),
    ] = None


class ImagePolicySpec(BaseModel):
    filter_tags: Annotated[
        Optional[FilterTags],
        Field(
            alias="filterTags",
            description="FilterTags enables filtering for only a subset of tags based on a set of\nrules. If no rules are provided, all the tags from the repository will be\nordered and compared.",
        ),
    ] = None
    image_repository_ref: Annotated[
        ImageRepositoryRef,
        Field(
            alias="imageRepositoryRef",
            description="ImageRepositoryRef points at the object specifying the image\nbeing scanned",
        ),
    ]
    policy: Annotated[
        Policy,
        Field(
            description="Policy gives the particulars of the policy to be followed in\nselecting the most recent image"
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


class ImagePolicyStatus(BaseModel):
    conditions: Optional[List[Condition]] = None
    latest_image: Annotated[
        Optional[str],
        Field(
            alias="latestImage",
            description="LatestImage gives the first in the list of images scanned by\nthe image repository, when filtered and ordered according to\nthe policy.",
        ),
    ] = None
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration")] = None
    observed_previous_image: Annotated[
        Optional[str],
        Field(
            alias="observedPreviousImage",
            description="ObservedPreviousImage is the observed previous LatestImage. It is used\nto keep track of the previous and current images.",
        ),
    ] = None


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


class CertSecretRef(BaseModel):
    name: Annotated[str, Field(description="Name of the referent.")]


class ProxySecretRef(BaseModel):
    name: Annotated[str, Field(description="Name of the referent.")]


class SecretRef(BaseModel):
    name: Annotated[str, Field(description="Name of the referent.")]


class ImageRepositorySpec(BaseModel):
    access_from: Annotated[
        Optional[AccessFrom],
        Field(
            alias="accessFrom",
            description="AccessFrom defines an ACL for allowing cross-namespace references\nto the ImageRepository object based on the caller's namespace labels.",
        ),
    ] = None
    cert_secret_ref: Annotated[
        Optional[CertSecretRef],
        Field(
            alias="certSecretRef",
            description="CertSecretRef can be given the name of a Secret containing\neither or both of\n\n- a PEM-encoded client certificate (`tls.crt`) and private\nkey (`tls.key`);\n- a PEM-encoded CA certificate (`ca.crt`)\n\nand whichever are supplied, will be used for connecting to the\nregistry. The client cert and key are useful if you are\nauthenticating with a certificate; the CA cert is useful if\nyou are using a self-signed server certificate. The Secret must\nbe of type `Opaque` or `kubernetes.io/tls`.\n\nNote: Support for the `caFile`, `certFile` and `keyFile` keys has\nbeen deprecated.",
        ),
    ] = None
    exclusion_list: Annotated[
        Optional[List[str]],
        Field(
            alias="exclusionList",
            description="ExclusionList is a list of regex strings used to exclude certain tags\nfrom being stored in the database.",
            max_length=25,
        ),
    ] = ["^.*\\.sig$"]
    image: Annotated[str, Field(description="Image is the name of the image repository")]
    insecure: Annotated[
        Optional[bool],
        Field(description="Insecure allows connecting to a non-TLS HTTP container registry."),
    ] = None
    interval: Annotated[
        str,
        Field(
            description="Interval is the length of time to wait between\nscans of the image repository.",
            pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m|h))+$",
        ),
    ]
    provider: Annotated[
        Optional[Literal["generic", "aws", "azure", "gcp"]],
        Field(
            description="The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.\nWhen not specified, defaults to 'generic'."
        ),
    ] = "generic"
    proxy_secret_ref: Annotated[
        Optional[ProxySecretRef],
        Field(
            alias="proxySecretRef",
            description="ProxySecretRef specifies the Secret containing the proxy configuration\nto use while communicating with the container registry.",
        ),
    ] = None
    secret_ref: Annotated[
        Optional[SecretRef],
        Field(
            alias="secretRef",
            description="SecretRef can be given the name of a secret containing\ncredentials to use for the image registry. The secret should be\ncreated with `kubectl create secret docker-registry`, or the\nequivalent.",
        ),
    ] = None
    service_account_name: Annotated[
        Optional[str],
        Field(
            alias="serviceAccountName",
            description="ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate\nthe image pull if the service account has attached pull secrets.",
            max_length=253,
        ),
    ] = None
    suspend: Annotated[
        Optional[bool],
        Field(
            description="This flag tells the controller to suspend subsequent image scans.\nIt does not apply to already started scans. Defaults to false."
        ),
    ] = None
    timeout: Annotated[
        Optional[str],
        Field(
            description="Timeout for image scanning.\nDefaults to 'Interval' duration.",
            pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m))+$",
        ),
    ] = None


class LastScanResult(BaseModel):
    latest_tags: Annotated[Optional[List[str]], Field(alias="latestTags")] = None
    scan_time: Annotated[Optional[datetime], Field(alias="scanTime")] = None
    tag_count: Annotated[int, Field(alias="tagCount")]


class ImageRepositoryStatus(BaseModel):
    canonical_image_name: Annotated[
        Optional[str],
        Field(
            alias="canonicalImageName",
            description="CanonicalName is the name of the image repository with all the\nimplied bits made explicit; e.g., `docker.io/library/alpine`\nrather than `alpine`.",
        ),
    ] = None
    conditions: Optional[List[Condition]] = None
    last_handled_reconcile_at: Annotated[
        Optional[str],
        Field(
            alias="lastHandledReconcileAt",
            description="LastHandledReconcileAt holds the value of the most recent\nreconcile request value, so a change of the annotation value\ncan be detected.",
        ),
    ] = None
    last_scan_result: Annotated[
        Optional[LastScanResult],
        Field(
            alias="lastScanResult",
            description="LastScanResult contains the number of fetched tags.",
        ),
    ] = None
    observed_exclusion_list: Annotated[
        Optional[List[str]],
        Field(
            alias="observedExclusionList",
            description="ObservedExclusionList is a list of observed exclusion list. It reflects\nthe exclusion rules used for the observed scan result in\nspec.lastScanResult.",
        ),
    ] = None
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="ObservedGeneration is the last reconciled generation.",
        ),
    ] = None


class Ref(BaseModel):
    branch: Annotated[
        Optional[str],
        Field(
            description="Branch to check out, defaults to 'master' if no other field is defined."
        ),
    ] = None
    commit: Annotated[
        Optional[str],
        Field(
            description="Commit SHA to check out, takes precedence over all reference fields.\n\nThis can be combined with Branch to shallow clone the branch, in which\nthe commit is expected to exist."
        ),
    ] = None
    name: Annotated[
        Optional[str],
        Field(
            description='Name of the reference to check out; takes precedence over Branch, Tag and SemVer.\n\nIt must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description\nExamples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"'
        ),
    ] = None
    semver: Annotated[
        Optional[str],
        Field(description="SemVer tag expression to check out, takes precedence over Tag."),
    ] = None
    tag: Annotated[
        Optional[str],
        Field(description="Tag to check out, takes precedence over Branch."),
    ] = None


class Checkout(BaseModel):
    ref: Annotated[
        Ref,
        Field(
            description="Reference gives a branch, tag or commit to clone from the Git\nrepository."
        ),
    ]


class Author(BaseModel):
    email: Annotated[
        str, Field(description="Email gives the email to provide when making a commit.")
    ]
    name: Annotated[
        Optional[str],
        Field(description="Name gives the name to provide when making a commit."),
    ] = None


class SigningKey(BaseModel):
    secret_ref: Annotated[
        SecretRef,
        Field(
            alias="secretRef",
            description="SecretRef holds the name to a secret that contains a 'git.asc' key\ncorresponding to the ASCII Armored file containing the GPG signing\nkeypair as the value. It must be in the same namespace as the\nImageUpdateAutomation.",
        ),
    ]


class Commit(BaseModel):
    author: Annotated[
        Author,
        Field(
            description="Author gives the email and optionally the name to use as the\nauthor of commits."
        ),
    ]
    message_template: Annotated[
        Optional[str],
        Field(
            alias="messageTemplate",
            description="MessageTemplate provides a template for the commit message,\ninto which will be interpolated the details of the change made.",
        ),
    ] = None
    signing_key: Annotated[
        Optional[SigningKey],
        Field(
            alias="signingKey",
            description="SigningKey provides the option to sign commits with a GPG key",
        ),
    ] = None


class Push(BaseModel):
    branch: Annotated[
        Optional[str],
        Field(
            description="Branch specifies that commits should be pushed to the branch\nnamed. The branch is created using `.spec.checkout.branch` as the\nstarting point, if it doesn't already exist."
        ),
    ] = None
    options: Annotated[
        Optional[Dict[str, str]],
        Field(
            description="Options specifies the push options that are sent to the Git\nserver when performing a push operation. For details, see:\nhttps://git-scm.com/docs/git-push#Documentation/git-push.txt---push-optionltoptiongt"
        ),
    ] = None
    refspec: Annotated[
        Optional[str],
        Field(
            description="Refspec specifies the Git Refspec to use for a push operation.\nIf both Branch and Refspec are provided, then the commit is pushed\nto the branch and also using the specified refspec.\nFor more details about Git Refspecs, see:\nhttps://git-scm.com/book/en/v2/Git-Internals-The-Refspec"
        ),
    ] = None


class Git(BaseModel):
    checkout: Annotated[
        Optional[Checkout],
        Field(
            description="Checkout gives the parameters for cloning the git repository,\nready to make changes. If not present, the `spec.ref` field from the\nreferenced `GitRepository` or its default will be used."
        ),
    ] = None
    commit: Annotated[
        Commit,
        Field(description="Commit specifies how to commit to the git repository."),
    ]
    push: Annotated[
        Optional[Push],
        Field(
            description="Push specifies how and where to push commits made by the\nautomation. If missing, commits are pushed (back) to\n`.spec.checkout.branch` or its default."
        ),
    ] = None


class MatchExpression(BaseModel):
    key: Annotated[str, Field(description="key is the label key that the selector applies to.")]
    operator: Annotated[
        str,
        Field(
            description="operator represents a key's relationship to a set of values.\nValid operators are In, NotIn, Exists and DoesNotExist."
        ),
    ]
    values: Annotated[
        Optional[List[str]],
        Field(
            description="values is an array of string values. If the operator is In or NotIn,\nthe values array must be non-empty. If the operator is Exists or DoesNotExist,\nthe values array must be empty. This array is replaced during a strategic\nmerge patch."
        ),
    ] = None


class PolicySelector(BaseModel):
    match_expressions: Annotated[
        Optional[List[MatchExpression]],
        Field(
            alias="matchExpressions",
            description="matchExpressions is a list of label selector requirements. The requirements are ANDed.",
        ),
    ] = None
    match_labels: Annotated[
        Optional[Dict[str, str]],
        Field(
            alias="matchLabels",
            description='matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels\nmap is equivalent to an element of matchExpressions, whose key field is "key", the\noperator is "In", and the values array contains only "value". The requirements are ANDed.',
        ),
    ] = None


class SourceRef(BaseModel):
    api_version: Annotated[
        Optional[str],
        Field(alias="apiVersion", description="API version of the referent."),
    ] = None
    kind: Annotated[
        Optional[Literal["GitRepository"]], Field(description="Kind of the referent.")
    ] = "GitRepository"
    name: Annotated[str, Field(description="Name of the referent.")]
    namespace: Annotated[
        Optional[str],
        Field(
            description="Namespace of the referent, defaults to the namespace of the Kubernetes resource object that contains the reference."
        ),
    ] = None


class Update(BaseModel):
    path: Annotated[
        Optional[str],
        Field(
            description="Path to the directory containing the manifests to be updated.\nDefaults to 'None', which translates to the root path\nof the GitRepositoryRef."
        ),
    ] = None
    strategy: Annotated[
        Optional[Literal["Setters"]],
        Field(description="Strategy names the strategy to be used."),
    ] = "Setters"


class ImageUpdateAutomationSpec(BaseModel):
    git: Annotated[
        Optional[Git],
        Field(
            description="GitSpec contains all the git-specific definitions. This is\ntechnically optional, but in practice mandatory until there are\nother kinds of source allowed."
        ),
    ] = None
    interval: Annotated[
        str,
        Field(
            description="Interval gives an lower bound for how often the automation\nrun should be attempted.",
            pattern="^([0-9]+(\\.[0-9]+)?(ms|s|m|h))+$",
        ),
    ]
    policy_selector: Annotated[
        Optional[PolicySelector],
        Field(
            alias="policySelector",
            description="PolicySelector allows to filter applied policies based on labels.\nBy default includes all policies in namespace.",
        ),
    ] = None
    source_ref: Annotated[
        SourceRef,
        Field(
            alias="sourceRef",
            description="SourceRef refers to the resource giving access details\nto a git repository.",
        ),
    ]
    suspend: Annotated[
        Optional[bool],
        Field(
            description="Suspend tells the controller to not run this automation, until\nit is unset (or set to false). Defaults to false."
        ),
    ] = None
    update: Annotated[
        Optional[Update],
        Field(
            description="Update gives the specification for how to update the files in\nthe repository. This can be left empty, to use the default\nvalue."
        ),
    ] = {"strategy": "Setters"}


class ObservedPolicies(BaseModel):
    name: Annotated[str, Field(description="Name is the bare image's name.")]
    tag: Annotated[str, Field(description="Tag is the image's tag.")]


class ImageUpdateAutomationStatus(BaseModel):
    conditions: Optional[List[Condition]] = None
    last_automation_run_time: Annotated[
        Optional[datetime],
        Field(
            alias="lastAutomationRunTime",
            description="LastAutomationRunTime records the last time the controller ran\nthis automation through to completion (even if no updates were\nmade).",
        ),
    ] = None
    last_handled_reconcile_at: Annotated[
        Optional[str],
        Field(
            alias="lastHandledReconcileAt",
            description="LastHandledReconcileAt holds the value of the most recent\nreconcile request value, so a change of the annotation value\ncan be detected.",
        ),
    ] = None
    last_push_commit: Annotated[
        Optional[str],
        Field(
            alias="lastPushCommit",
            description="LastPushCommit records the SHA1 of the last commit made by the\ncontroller, for this automation object",
        ),
    ] = None
    last_push_time: Annotated[
        Optional[datetime],
        Field(
            alias="lastPushTime",
            description="LastPushTime records the time of the last pushed change.",
        ),
    ] = None
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration")] = None
    observed_policies: Annotated[
        Optional[Dict[str, ObservedPolicies]],
        Field(
            alias="observedPolicies",
            description="ObservedPolicies is the list of observed ImagePolicies that were\nconsidered by the ImageUpdateAutomation update process.",
        ),
    ] = None
    observed_source_revision: Annotated[
        Optional[str],
        Field(
            alias="observedSourceRevision",
            description='ObservedPolicies []ObservedPolicy `json:"observedPolicies,omitempty"`\nObservedSourceRevision is the last observed source revision. This can be\nused to determine if the source has been updated since last observation.',
        ),
    ] = None


class ImagePolicy(Resource):
    api_version: Annotated[
        Optional[Literal["image.toolkit.fluxcd.io/v1beta2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "image.toolkit.fluxcd.io/v1beta2"
    kind: Annotated[
        Optional[Literal["ImagePolicy"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ImagePolicy"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ImagePolicySpec] = None
    status: Optional[ImagePolicyStatus] = None


class ImageRepository(Resource):
    api_version: Annotated[
        Optional[Literal["image.toolkit.fluxcd.io/v1beta2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "image.toolkit.fluxcd.io/v1beta2"
    kind: Annotated[
        Optional[Literal["ImageRepository"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ImageRepository"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ImageRepositorySpec] = None
    status: Optional[ImageRepositoryStatus] = None


class ImageUpdateAutomation(Resource):
    api_version: Annotated[
        Optional[Literal["image.toolkit.fluxcd.io/v1beta2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object.\nServers should convert recognized schemas to the latest internal value, and\nmay reject unrecognized values.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "image.toolkit.fluxcd.io/v1beta2"
    kind: Annotated[
        Optional[Literal["ImageUpdateAutomation"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents.\nServers may infer this from the endpoint the client submits requests to.\nCannot be updated.\nIn CamelCase.\nMore info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ImageUpdateAutomation"
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: Optional[ImageUpdateAutomationSpec] = None
    status: Optional[ImageUpdateAutomationStatus] = None
