---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security issuance guarantor
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/isIssuanceGuarantor
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecurityIssuanceGuarantor
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: security issuance guarantor
type: Ontology Class
---

# security issuance guarantor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecurityIssuanceGuarantor>

## Relationships

- **Subclass of**: [SecuritiesIssuanceProcessActor](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor.md)

## Constraints

- **[isIssuanceGuarantor](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/isIssuanceGuarantor.md)**: some values from of type [SecuritiesIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md)

## Annotations

- **label** (en): security issuance guarantor

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
