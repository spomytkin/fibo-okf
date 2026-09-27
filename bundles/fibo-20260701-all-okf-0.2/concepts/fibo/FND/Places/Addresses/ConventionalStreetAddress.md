---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: conventional street address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical address that identifies a location on a street to which communications may be delivered
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Other unconventional addresses may include rural and highway route addresses, general delivery addresses, post
      office box addresses, private mail center addresses, and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
  - cardinality: 1
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine2
  - cardinality: 1
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine3
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStreetAddress
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: conventional street address
type: Ontology Class
---

# conventional street address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress>

## Definition

physical address that identifies a location on a street to which communications may be delivered

## Relationships

- **Subclass of**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Constraints

- **[hasAddressLine1](/concepts/fibo/FND/Places/Addresses/hasAddressLine1.md)**: max qualified cardinality 1 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[hasAddressLine2](/concepts/fibo/FND/Places/Addresses/hasAddressLine2.md)**: max qualified cardinality 1 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[hasAddressLine3](/concepts/fibo/FND/Places/Addresses/hasAddressLine3.md)**: max qualified cardinality 1 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[hasStreetAddress](/concepts/fibo/FND/Places/Addresses/hasStreetAddress.md)**: max qualified cardinality 1 of type [StreetAddress](/concepts/fibo/FND/Places/Addresses/StreetAddress.md)

## Annotations

- **label**: conventional street address
- **definition**: physical address that identifies a location on a street to which communications may be delivered
- **explanatoryNote**: Other unconventional addresses may include rural and highway route addresses, general delivery addresses, post office box addresses, private mail center addresses, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
