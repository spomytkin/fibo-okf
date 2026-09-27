---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has beneficiary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that receives some benefit or advantage or profits from something as specified in the agreement
  range:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Beneficiary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Beneficiary
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasCounterparty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasBeneficiary
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has beneficiary
type: Ontology Property
---

# has beneficiary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasBeneficiary>

## Definition

party that receives some benefit or advantage or profits from something as specified in the agreement

## Relationships

- **Range**: [Beneficiary](/concepts/fibo/FND/Agreements/Agreements/Beneficiary.md)
- **Subproperty of**: [hasCounterparty](/concepts/fibo/FND/Agreements/Contracts/hasCounterparty.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label** (en): has beneficiary
- **definition**: party that receives some benefit or advantage or profits from something as specified in the agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
