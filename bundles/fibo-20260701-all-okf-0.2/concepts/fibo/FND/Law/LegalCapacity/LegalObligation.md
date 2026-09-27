---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal obligation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an obligation or duty that is enforceable by a court
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
    value: N38a23822bab94e41a4de626fde3c5027
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
    value: Nd6a44fc7dcbc41f4bf8d8dd40eb99baa
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Duty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Duty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: legal obligation
type: Ontology Class
---

# legal obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation>

## Definition

an obligation or duty that is enforceable by a court

## Relationships

- **Subclass of**: [Duty](/concepts/fibo/FND/Law/LegalCapacity/Duty.md)

## Constraints

- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from value `N38a23822bab94e41a4de626fde3c5027`
- **[isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)**: some values from value `Nd6a44fc7dcbc41f4bf8d8dd40eb99baa`
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: legal obligation
- **definition**: an obligation or duty that is enforceable by a court

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
