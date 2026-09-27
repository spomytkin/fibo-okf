---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is capacity of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies an individual or organization on which a given legal capacity has been conferred
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: This includes capacities specific to duties at law (such as those for corporate officers) as well as the ability
      or capacity to incur liability.
  domain:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalCapacity
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/isConferredOn.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isConferredOn
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isCapacityOf
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: is capacity of
type: Ontology Property
---

# is capacity of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isCapacityOf>

## Definition

identifies an individual or organization on which a given legal capacity has been conferred

## Relationships

- **Domain**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md)
- **Range**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Subproperty of**: [isConferredOn](/concepts/fibo/FND/Law/LegalCapacity/isConferredOn.md)

## Annotations

- **label**: is capacity of
- **definition**: identifies an individual or organization on which a given legal capacity has been conferred
- **scopeNote**: This includes capacities specific to duties at law (such as those for corporate officers) as well as the ability or capacity to incur liability.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
