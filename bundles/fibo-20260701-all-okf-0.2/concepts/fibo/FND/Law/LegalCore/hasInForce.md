---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has in force
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a jurisdiction or situation to a rule, regulation or law (collectively "law") that is currently in force
      in that situation or jurisdiction
  inverse_of:
  - concept: /concepts/fibo/FND/Law/LegalCore/isInForceIn.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/isInForceIn
  range:
  - concept: /concepts/fibo/FND/Law/LegalCore/Law.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Law
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/hasInForce
sources:
- id: fibo-source-31fe191c06
  resource: references/fibo/FND/Law/LegalCore.rdf
  sha256: 31fe191c06f11a104ba752303784bfd17673c9e515a6e3d3ed538b19a5da37e9
  title: FIBO source FND/Law/LegalCore.rdf
title: has in force
type: Ontology Property
---

# has in force

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/hasInForce>

## Definition

relates a jurisdiction or situation to a rule, regulation or law (collectively "law") that is currently in force in that situation or jurisdiction

## Relationships

- **Inverse of**: [isInForceIn](/concepts/fibo/FND/Law/LegalCore/isInForceIn.md)
- **Range**: [Law](/concepts/fibo/FND/Law/LegalCore/Law.md)

## Annotations

- **label**: has in force
- **definition**: relates a jurisdiction or situation to a rule, regulation or law (collectively "law") that is currently in force in that situation or jurisdiction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
