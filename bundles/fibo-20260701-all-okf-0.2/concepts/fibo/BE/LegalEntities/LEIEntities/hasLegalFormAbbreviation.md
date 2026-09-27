---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has legal form abbreviation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the precise abbreviation for the entity legal form as defined in the jurisdiction in which it is registered, for
      example LLC, LLP, Ltd, PLC, Corp.
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: has legal form abbreviation
type: Ontology Property
---

# has legal form abbreviation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation>

## Definition

the precise abbreviation for the entity legal form as defined in the jurisdiction in which it is registered, for example LLC, LLP, Ltd, PLC, Corp.

## Relationships

- **Subproperty of**: [hasTextValue](<https://www.omg.org/spec/Commons/TextDatatype/hasTextValue>)

## Annotations

- **label**: has legal form abbreviation
- **definition**: the precise abbreviation for the entity legal form as defined in the jurisdiction in which it is registered, for example LLC, LLP, Ltd, PLC, Corp.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
