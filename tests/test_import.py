from cloudcoil.models.fluxcd.kustomize.v1 import Kustomization
from cloudcoil.models.fluxcd.source.v1 import GitRepository


def test_kustomization():
    kust = (
        Kustomization.builder()
        .metadata(lambda m: m.name("app-stack").namespace("default"))
        .spec(
            lambda s: s.path("./kustomize")
            .interval("1m")
            .source_ref(lambda r: r.kind("GitRepository").name("app-source"))
            .prune(True)
        )
        .build()
    )
    assert kust.spec.path == "./kustomize"
    assert kust.metadata.name == "app-stack"
    assert kust.spec.source_ref.kind == "GitRepository"


def test_git_repository():
    repo = (
        GitRepository.builder()
        .metadata(lambda m: m.name("app-source").namespace("default"))
        .spec(
            lambda s: s.url("https://github.com/org/repo")
            .interval("1m")
            .ref(lambda r: r.branch("main"))
        )
        .build()
    )
    assert repo.spec.url == "https://github.com/org/repo"
    assert repo.metadata.name == "app-source"
    assert repo.spec.ref.branch == "main"
