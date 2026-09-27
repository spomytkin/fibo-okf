---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is licensed by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party that has issued a particular license to some other party
  inverse_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/licenses.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/licenses
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isLicensedBy
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: is licensed by
type: Ontology Property
---

# is licensed by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isLicensedBy>

## Definition

indicates the party that has issued a particular license to some other party

## Relationships

- **Inverse of**: [licenses](/concepts/fibo/FND/Law/LegalCapacity/licenses.md)
- **Range**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **Subproperty of**: [isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)

## Annotations

- **label**: is licensed by
- **definition**: indicates the party that has issued a particular license to some other party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
