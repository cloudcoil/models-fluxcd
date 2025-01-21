# cloudcoil-models-fluxcd

Versioned FluxCD models for cloudcoil.

## 🔧 Installation

Using [uv](https://github.com/astral-sh/uv) (recommended):

```bash
# Install with FluxCD support
uv add cloudcoil.models.fluxcd
```

Using pip:

```bash
pip install cloudcoil.models.fluxcd
```

## 💡 Examples

### Using FluxCD Models

```python
from cloudcoil import apimachinery
import cloudcoil.models.fluxcd.source.v1 as fluxsource
import cloudcoil.models.fluxcd.kustomize.v1 as fluxkustomize

# Create a GitRepository
repo = fluxsource.GitRepository(
    metadata=apimachinery.ObjectMeta(name="my-app"),
    spec=fluxsource.GitRepositorySpec(
        url="https://github.com/org/repo",
        ref=fluxsource.Ref(
            branch="main"
        ),
        interval="1m"
    )
).create()

# Create a Kustomization
kustomization = fluxkustomize.Kustomization(
    metadata=apimachinery.ObjectMeta(name="my-app"),
    spec=fluxkustomize.KustomizationSpec(
        interval="5m",
        path="./kustomize",
        source_ref=fluxkustomize.SourceRef(
            kind="GitRepository",
            name="my-app"
        ),
        prune=True
    )
).create()

# List GitRepositories
for repo in fluxsource.GitRepository.list():
    print(f"Found repository: {repo.metadata.name}")

# Update a GitRepository
repo.spec.interval = "5m"
repo.save()

# Delete resources
fluxkustomize.Kustomization.delete("my-app")
fluxsource.GitRepository.delete("my-app")
```

## 📚 Documentation

For complete documentation, visit [cloudcoil.github.io/cloudcoil](https://cloudcoil.github.io/cloudcoil)

## 📜 License

Apache License, Version 2.0 - see [LICENSE](LICENSE)
