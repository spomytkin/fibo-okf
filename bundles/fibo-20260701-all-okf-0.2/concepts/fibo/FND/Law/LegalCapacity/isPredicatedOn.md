---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is predicated on
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depends on an assumption or requirement stated in
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ConditionPrecedent
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/isSpecifiedIn
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/refersTo
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isPredicatedOn
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: is predicated on
type: Ontology Property
---

# is predicated on

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isPredicatedOn>

## Definition

depends on an assumption or requirement stated in

## Relationships

- **Domain**: [ConditionPrecedent](/concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md)
- **Subproperty of**: [isSpecifiedIn](<https://www.omg.org/spec/Commons/Documents/isSpecifiedIn>)
- **Subproperty of**: [refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)

## Annotations

- **label** (en): is predicated on
- **definition**: depends on an assumption or requirement stated in

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
