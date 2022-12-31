# qomohub (qomolangma-datahub)

Signal datahub of Geoscience Language Model Qomolangma

- backend: [DataLab](https://github.com/ExpressAI/DataLab) from ExpressAI
- data source: [GAKG](https://gakg.deep-time.org)

**qomohub** can be installed from PyPi and it is dependent on DataLab

```shell
pip install --upgrade pip
pip install qomohub
python -m nltk.downloader omw-1.4 # to support more feature calculation
```

---

## Usage

```python
from qomohub import load_signal

signal = load_signal("geo_paper")
print(signal['train'][0])
```