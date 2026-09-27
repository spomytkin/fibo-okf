---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has mailing address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a physical address where an independent party can receive communications, including letters and packages
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Places/Addresses/hasAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/hasMailingAddress
sources:
- id: fibo-source-2c7ef9cc41
  resource: references/fibo/FND/Parties/Parties.rdf
  sha256: 2c7ef9cc4107e85b5bba3894094e496bcf4e8fe3ef9d6ce3b7d0830fb284f61d
  title: FIBO source FND/Parties/Parties.rdf
title: has mailing address
type: Ontology Property
---

# has mailing address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/hasMailingAddress>

## Definition

identifies a physical address where an independent party can receive communications, including letters and packages

## Relationships

- **Domain**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Range**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)
- **Subproperty of**: [hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)

## Annotations

- **label**: has mailing address
- **definition**: identifies a physical address where an independent party can receive communications, including letters and packages

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
