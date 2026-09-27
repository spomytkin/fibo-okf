---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has individual postcode
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the local or international postcode element of a delivery address as specified by the local postal service
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  domain:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/Postcode.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Postcode
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasIndividualPostcode
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has individual postcode
type: Ontology Property
---

# has individual postcode

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasIndividualPostcode>

## Definition

indicates the local or international postcode element of a delivery address as specified by the local postal service

## Relationships

- **Domain**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)
- **Range**: [Postcode](/concepts/fibo/FND/Places/Addresses/Postcode.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has individual postcode
- **definition**: indicates the local or international postcode element of a delivery address as specified by the local postal service
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
