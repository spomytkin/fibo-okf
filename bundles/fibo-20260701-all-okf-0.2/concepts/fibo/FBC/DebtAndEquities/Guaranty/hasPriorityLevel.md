---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has priority level
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a guaranty to some relative ranking that the guaranty has in the context of the contract, for example for
      a credit enhancement priority
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/Guaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guaranty
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/PriorityLevel.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/PriorityLevel
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasPriorityLevel
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: has priority level
type: Ontology Property
---

# has priority level

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasPriorityLevel>

## Definition

relates a guaranty to some relative ranking that the guaranty has in the context of the contract, for example for a credit enhancement priority

## Relationships

- **Defined by**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Domain**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guaranty.md)
- **Range**: [PriorityLevel](/concepts/fibo/FBC/DebtAndEquities/Guaranty/PriorityLevel.md)
- **Subproperty of**: [isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)

## Annotations

- **label**: has priority level
- **definition**: relates a guaranty to some relative ranking that the guaranty has in the context of the contract, for example for a credit enhancement priority

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
