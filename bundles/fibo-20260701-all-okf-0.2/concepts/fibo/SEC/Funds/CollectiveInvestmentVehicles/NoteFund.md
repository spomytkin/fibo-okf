---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: note fund
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pooled investment vehicle that issues debt instruments (notes) to investors rather than (or in addition to) traditional
      equity interests
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The notes issued by a note fund are typically privately rated by agencies like KBRA, DBRS, or Moody's, tranched
      into senior and junior classes, and linked to underlying assets such as private loans, credit instruments, or structured
      products. Note funds are designed to optimize regulatory capital treatment, especially for insurance companies, by offering
      rated debt instead of equity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NoteFund
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: note fund
type: Ontology Class
---

# note fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/NoteFund>

## Definition

pooled investment vehicle that issues debt instruments (notes) to investors rather than (or in addition to) traditional equity interests

## Relationships

- **Subclass of**: [ManagedInvestment](/concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md)

## Annotations

- **label**: note fund
- **definition**: pooled investment vehicle that issues debt instruments (notes) to investors rather than (or in addition to) traditional equity interests
- **explanatoryNote**: The notes issued by a note fund are typically privately rated by agencies like KBRA, DBRS, or Moody's, tranched into senior and junior classes, and linked to underlying assets such as private loans, credit instruments, or structured products. Note funds are designed to optimize regulatory capital treatment, especially for insurance companies, by offering rated debt instead of equity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
