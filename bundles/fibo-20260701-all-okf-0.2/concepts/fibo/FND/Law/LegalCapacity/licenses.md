---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: licenses
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: issues a license required in order to perform some task, provide some service, exercise some privilege, or pursue
      some line of business or occupation to some party
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/licenses
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: licenses
type: Ontology Property
---

# licenses

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/licenses>

## Definition

issues a license required in order to perform some task, provide some service, exercise some privilege, or pursue some line of business or occupation to some party

## Relationships

- **Domain**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **Subproperty of**: [governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)

## Annotations

- **label**: licenses
- **definition**: issues a license required in order to perform some task, provide some service, exercise some privilege, or pursue some line of business or occupation to some party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
