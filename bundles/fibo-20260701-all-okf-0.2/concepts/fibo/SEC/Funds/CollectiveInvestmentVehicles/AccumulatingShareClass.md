---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: accumulating share class
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A share class in which there is no option to reinvest.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This fact would be determined by the fund unit having a specific Fund Distribution Policy of Accumulating.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/DistributingShareClass.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/DistributingShareClass
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/AccumulatingShareClass
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: accumulating share class
type: Ontology Class
---

# accumulating share class

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/AccumulatingShareClass>

## Definition

A share class in which there is no option to reinvest.

## Relationships

- **Subclass of**: [FundShareClassUnit](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit.md)

## Constraints

- **Disjoint with**: [DistributingShareClass](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/DistributingShareClass.md)

## Annotations

- **label** (en): accumulating share class
- **definition** (en): A share class in which there is no option to reinvest.
- **explanatoryNote** (en): This fact would be determined by the fund unit having a specific Fund Distribution Policy of Accumulating.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
