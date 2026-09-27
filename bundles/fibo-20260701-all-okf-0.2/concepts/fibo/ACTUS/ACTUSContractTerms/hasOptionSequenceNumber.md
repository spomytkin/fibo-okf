---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has option sequence number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the order of occurance of an optional element in an enumerated list
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: has option sequence number
type: Ontology Property
---

# has option sequence number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber>

## Definition

specifies the order of occurance of an optional element in an enumerated list

## Relationships

- **Range**: [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **Subproperty of**: [hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)

## Annotations

- **label**: has option sequence number
- **definition**: specifies the order of occurance of an optional element in an enumerated list

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
