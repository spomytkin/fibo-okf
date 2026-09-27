---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract third party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is indirectly involved in, but not a counterparty to, an agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: contract third party
type: Ontology Class
---

# contract third party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty>

## Definition

party that is indirectly involved in, but not a counterparty to, an agreement

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label**: contract third party
- **definition**: party that is indirectly involved in, but not a counterparty to, an agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
