---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: validate conformance
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The mortgage is automatically validated for conformance to the requirements of the pool in which it is to be included.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'From review comment 6 Oct: box called validate conformance automatic eg max loan balance'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PoolConformanceCriteria
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/ValidateConformance
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: validate conformance
type: Ontology Class
---

# validate conformance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/ValidateConformance>

## Definition

The mortgage is automatically validated for conformance to the requirements of the pool in which it is to be included.

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [PoolConformanceCriteria](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/PoolConformanceCriteria.md)

## Annotations

- **label** (en): validate conformance
- **definition** (en): The mortgage is automatically validated for conformance to the requirements of the pool in which it is to be included.
- **editorialNote** (en): From review comment 6 Oct: box called validate conformance automatic eg max loan balance

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
