---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private mail box address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: delivery address provided by a commercial mail receiving company that includes a supplementary address line containing
      the abbreviation 'PMB' or the pound "#" symbol followed by the mailbox number; alternatively, 'PMB' or '#" and the mailbox
      number can be appended to the street address
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/PrivateMailBoxAddress
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: private mail box address
type: Ontology Class
---

# private mail box address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/PrivateMailBoxAddress>

## Definition

delivery address provided by a commercial mail receiving company that includes a supplementary address line containing the abbreviation 'PMB' or the pound "#" symbol followed by the mailbox number; alternatively, 'PMB' or '#" and the mailbox number can be appended to the street address

## Relationships

- **Subclass of**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)

## Annotations

- **label**: private mail box address
- **definition**: delivery address provided by a commercial mail receiving company that includes a supplementary address line containing the abbreviation 'PMB' or the pound "#" symbol followed by the mailbox number; alternatively, 'PMB' or '#" and the mailbox number can be appended to the street address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
