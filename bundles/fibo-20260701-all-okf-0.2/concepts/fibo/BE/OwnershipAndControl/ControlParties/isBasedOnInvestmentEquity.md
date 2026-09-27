---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is based on investment equity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates investment-based de facto control, which is is based on the holding of some investment equity by some
      party
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/isConferredBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/isBasedOnInvestmentEquity
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: is based on investment equity
type: Ontology Property
---

# is based on investment equity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/isBasedOnInvestmentEquity>

## Definition

indicates investment-based de facto control, which is is based on the holding of some investment equity by some party

## Relationships

- **Domain**: [InvestmentBasedDeFactoControl](/concepts/fibo/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl.md)
- **Range**: [InvestmentEquity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md)
- **Subproperty of**: [isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)

## Annotations

- **label**: is based on investment equity
- **definition**: indicates investment-based de facto control, which is is based on the holding of some investment equity by some party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
