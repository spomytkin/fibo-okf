---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: physical address identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unique identifier for a physical address
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Physical address identifiers may include bar codes, QCR codes, and +codes in a number of countries.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddressingScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddressIdentifier
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: physical address identifier
type: Ontology Class
---

# physical address identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddressIdentifier>

## Definition

unique identifier for a physical address

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)
- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [PhysicalAddressingScheme](/concepts/fibo/FND/Places/Addresses/PhysicalAddressingScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Annotations

- **label**: physical address identifier
- **definition**: unique identifier for a physical address
- **example**: Physical address identifiers may include bar codes, QCR codes, and +codes in a number of countries.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
