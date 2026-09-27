---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is beneficiary of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the agreement that a beneficiary is named in
  domain:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Beneficiary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Beneficiary
  range:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isBeneficiaryOf
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: is beneficiary of
type: Ontology Property
---

# is beneficiary of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isBeneficiaryOf>

## Definition

specifies the agreement that a beneficiary is named in

## Relationships

- **Domain**: [Beneficiary](/concepts/fibo/FND/Agreements/Agreements/Beneficiary.md)
- **Range**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: is beneficiary of
- **definition**: specifies the agreement that a beneficiary is named in

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
