---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment-based de facto controlling interest party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that holds investment-based control over some other party
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControllingPartyIn
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControllingInterestParty
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: investment-based de facto controlling interest party
type: Ontology Class
---

# investment-based de facto controlling interest party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControllingInterestParty>

## Definition

party that holds investment-based control over some other party

## Relationships

- **Subclass of**: [DeFactoControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty.md)
- **Subclass of**: [Investor](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md)

## Constraints

- **[isControllingPartyIn](/concepts/fibo/FND/OwnershipAndControl/Control/isControllingPartyIn.md)**: all values from of type [InvestmentBasedDeFactoControl](/concepts/fibo/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl.md)

## Annotations

- **label**: investment-based de facto controlling interest party
- **definition**: party that holds investment-based control over some other party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
