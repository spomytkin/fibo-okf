---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that owns some stake in some organization by way of investment
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: This is regardless of whether or not the investor is also a constitutional owner (e.g. shareholder) in the entity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwner
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: investor
type: Ontology Class
---

# investor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor>

## Definition

party that owns some stake in some organization by way of investment

## Relationships

- **Subclass of**: [EntityOwner](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)
- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)

## Constraints

- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: some values from of type [InvestmentEquity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md)

## Annotations

- **label**: investor
- **definition**: party that owns some stake in some organization by way of investment
- **editorialNote**: This is regardless of whether or not the investor is also a constitutional owner (e.g. shareholder) in the entity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
