---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: complete address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: delivery address that has all the address elements necessary to allow an exact match with the current Postal Service
      ZIP+4 and City State files to obtain the finest level of ZIP+4 and delivery point codes for the delivery address
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A complete address may be required on mail at some automation rates.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/StandardizedAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/StandardizedAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/CompleteAddress
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: complete address
type: Ontology Class
---

# complete address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/CompleteAddress>

## Definition

delivery address that has all the address elements necessary to allow an exact match with the current Postal Service ZIP+4 and City State files to obtain the finest level of ZIP+4 and delivery point codes for the delivery address

## Relationships

- **Subclass of**: [StandardizedAddress](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/StandardizedAddress.md)

## Annotations

- **label**: complete address
- **definition**: delivery address that has all the address elements necessary to allow an exact match with the current Postal Service ZIP+4 and City State files to obtain the finest level of ZIP+4 and delivery point codes for the delivery address
- **explanatoryNote**: A complete address may be required on mail at some automation rates.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
