---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has registered address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies an address that is officially recorded with some government authority and at which legal papers may
      be served
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Places/Addresses/hasAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress
sources:
- id: fibo-source-9758af6c79
  resource: references/fibo/BE/LegalEntities/FormalBusinessOrganizations.rdf
  sha256: 9758af6c796f157eedb21d72cde0822cb7a2ecbd6b5a70ef23be48121c598ede
  title: FIBO source BE/LegalEntities/FormalBusinessOrganizations.rdf
title: has registered address
type: Ontology Property
---

# has registered address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress>

## Definition

identifies an address that is officially recorded with some government authority and at which legal papers may be served

## Relationships

- **Domain**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Range**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **Subproperty of**: [hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)

## Annotations

- **label**: has registered address
- **definition**: identifies an address that is officially recorded with some government authority and at which legal papers may be served

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
