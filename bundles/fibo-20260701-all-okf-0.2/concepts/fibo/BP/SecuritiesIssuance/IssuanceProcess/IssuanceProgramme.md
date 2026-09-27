---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issuance programme
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A series of issuances over time.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: See for example MTN.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProgramme
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: issuance programme
type: Ontology Class
---

# issuance programme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProgramme>

## Definition

A series of issuances over time.

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)

## Annotations

- **label** (en): issuance programme
- **definition** (en): A series of issuances over time.
- **explanatoryNote** (en): See for example MTN.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
