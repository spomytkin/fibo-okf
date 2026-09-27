---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has mail routing
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an optional, free text address line containing explicit routing information (this elements's presence indicates
      that this address is a routing / 'care of' address)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  domain:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasMailRouting
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has mail routing
type: Ontology Property
---

# has mail routing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasMailRouting>

## Definition

an optional, free text address line containing explicit routing information (this elements's presence indicates that this address is a routing / 'care of' address)

## Relationships

- **Domain**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)
- **Subproperty of**: [hasTextValue](<https://www.omg.org/spec/Commons/TextDatatype/hasTextValue>)

## Annotations

- **label**: has mail routing
- **definition**: an optional, free text address line containing explicit routing information (this elements's presence indicates that this address is a routing / 'care of' address)
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
