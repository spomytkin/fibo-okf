---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual element
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: element, such as an arrangement, provision, requirement, rule, specification, and standard that forms an integral
      part of an agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasLegalDescription
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Constituent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: contractual element
type: Ontology Class
---

# contractual element

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement>

## Definition

element, such as an arrangement, provision, requirement, rule, specification, and standard that forms an integral part of an agreement

## Relationships

- **Subclass of**: [Constituent](<https://www.omg.org/spec/Commons/Collections/Constituent>)

## Constraints

- **[hasLegalDescription](/concepts/fibo/FND/Agreements/Contracts/hasLegalDescription.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: contractual element
- **definition**: element, such as an arrangement, provision, requirement, rule, specification, and standard that forms an integral part of an agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
