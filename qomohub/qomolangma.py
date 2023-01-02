# coding=utf-8
"""Qomolangma signals"""

import json
import textwrap

import datalabs
from datalabs.features import Features, Sequence, Value

_Qomolangma_CITATION = """\
"""

_Qomolangma_DESCRIPTION = """\
Signal data of Qomolangma, the largest Geoscience Language Model.
"""


class QomolangmaConfig(datalabs.BuilderConfig):
    def __init__(
            self,
            data_url,
            data_dir,
            citation,
            url,
            features,
            process_label=lambda x: x,
            task_templates=None,
            **kwargs
    ):
        """BuilderConfig for RST.

        Args:
          data_url: `string`, url to download the zip file from
          data_dir: `string`, the path to the folder containing the tsv files in the
            downloaded zip
          citation: `string`, citation for the data set
          url: `string`, url for information about the data set
          process_label: `Function[string, any]`, function  taking in the raw value
            of the label and processing it to the form required by the label feature
          **kwargs: keyword arguments forwarded to super.
        """
        super(QomolangmaConfig, self).__init__(version=datalabs.Version("1.0.0", ""), **kwargs)

        self.features = features
        self.data_url = data_url
        self.citation = citation
        self.url = url
        self.process_label = process_label
        self.task_templates = task_templates


class Qomolangma(datalabs.GeneratorBasedBuilder):
    """ RST signals """
    BUILDER_CONFIGS = [
        # Wikidata
        QomolangmaConfig(
            name="wikidata_entity",
            description=textwrap.dedent(
                """\
            Entity signals from Wikidata"""
            ),
            data_url="https://dataset.acemap.info/qomolangma-datahub/qomolangma-data-mini/wikidata_entity.jsonl",
            data_dir=None,
            citation=textwrap.dedent(
                """\
                TBC
            }"""
            ),
            url="TBC",
            features=datalabs.Features(
                {
                    "entity": Value("string"),
                    "entity_type": Value("string"),
                    "text": Value("string"),
                }
            )
        ),
        QomolangmaConfig(
            name="wikidata_relation",
            description=textwrap.dedent(
                """\
            Relation signals from Wikidata"""
            ),
            data_url="https://dataset.acemap.info/qomolangma-datahub/qomolangma-data-mini/wikidata_relation.jsonl",
            data_dir=None,
            citation=textwrap.dedent(
                """\
                TBC
            }"""
            ),
            url="TBC",
            features=datalabs.Features(
                {
                    "subject": Value("string"),
                    "object": Value("string"),
                    "relation": Value("string"),
                    "text": Value("string"),
                }
            )
        ),
        QomolangmaConfig(
            name="wikidata_relation",
            description=textwrap.dedent(
                """\
            Summary signals from DDEScholar"""
            ),
            data_url="https://dataset.acemap.info/qomolangma-datahub/qomolangma-data-mini/ddescholar_title_abstract.jsonl",
            data_dir=None,
            citation=textwrap.dedent(
                """\
                TBC
            }"""
            ),
            url="TBC",
            features=datalabs.Features(
                {
                    "title": Value("string"),
                    "abstract": Value("string"),
                }
            )
        ),
    ]

    def _info(self):
        return datalabs.DatasetInfo(
            description=_Qomolangma_DESCRIPTION,
            features=self.config.features,
            homepage=self.config.url,
            citation=self.config.citation + "\n" + _Qomolangma_CITATION,
            task_templates=self.config.task_templates,
        )

    def _split_generators(self, dl_manager):
        data_file = dl_manager.download(self.config.data_url)
        return [
            datalabs.SplitGenerator(
                name=datalabs.Split.TRAIN,
                gen_kwargs={
                    "filepath": data_file,
                    "split": "train",
                },
            )
        ]

    def _generate_examples(self, filepath, split):
        if self.config.name == "wikidata_entity":
            with open(filepath, encoding="utf-8") as f:
                for id_, row in enumerate(f):
                    data = json.loads(row.strip())
                    entity, entity_type, text = data["entity"], data["entity_type"], data["text"]
                    yield id_, {
                        "entity": entity,
                        "entity_type": entity_type,
                        "text": text
                    }

        elif self.config.name == "wikidata_relation":
            with open(filepath, encoding="utf-8") as f:
                for id_, row in enumerate(f):
                    data = json.loads(row.strip())
                    subject, object, relation, text = data["subject"], data["object"], data["relation"], data["text"]
                    yield id_, {
                        "subject": subject,
                        "object": object,
                        "relation": relation,
                        "text": text
                    }

        elif self.config.name == "ddescholar_title_abstract":
            with open(filepath, encoding="utf-8") as f:
                for id_, row in enumerate(f):
                    data = json.loads(row.strip())
                    title, abstract = data["title"], data["abstract"]
                    yield id_, {
                        "title": title,
                        "abstract": abstract,
                    }
