---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has legal description
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provides the text, or a summary thereof, expressed in legal terms, of the contract provision, clause, or other
      element
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Designators/hasDescription
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasLegalDescription
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has legal description
type: Ontology Property
---

# has legal description

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasLegalDescription>

## Definition

provides the text, or a summary thereof, expressed in legal terms, of the contract provision, clause, or other element

## Relationships

- **Domain**: [ContractualElement](/concepts/fibo/FND/Agreements/Contracts/ContractualElement.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)
- **Subproperty of**: [hasDescription](<https://www.omg.org/spec/Commons/Designators/hasDescription>)

## Annotations

- **label**: has legal description
- **definition**: provides the text, or a summary thereof, expressed in legal terms, of the contract provision, clause, or other element

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
