---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investor contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Contract setting out the terms under which some investor invests in the entity and setting out the rights which
      are conferred on that investor.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/definesTermsFor
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/InvestorContract
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: investor contract
type: Ontology Class
---

# investor contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/InvestorContract>

## Definition

Contract setting out the terms under which some investor invests in the entity and setting out the rights which are conferred on that investor.

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[definesTermsFor](/concepts/fibo/FND/Agreements/Contracts/definesTermsFor.md)**: some values from of type [InvestmentEquity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md)

## Annotations

- **label**: investor contract
- **definition**: Contract setting out the terms under which some investor invests in the entity and setting out the rights which are conferred on that investor.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
