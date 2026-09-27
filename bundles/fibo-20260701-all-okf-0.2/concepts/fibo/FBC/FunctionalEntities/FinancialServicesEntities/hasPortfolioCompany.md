---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has portfolio company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a party in which a venture capital firm, a buyout firm, or a holding company has invested
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
  inverse_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/isPortfolioCompanyOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/isPortfolioCompanyOf
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/isPartyControlling.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isPartyControlling
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasPortfolioCompany
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: has portfolio company
type: Ontology Property
---

# has portfolio company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasPortfolioCompany>

## Definition

indicates a party in which a venture capital firm, a buyout firm, or a holding company has invested

## Relationships

- **Domain**: [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)
- **Inverse of**: [isPortfolioCompanyOf](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/isPortfolioCompanyOf.md)
- **Range**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Subproperty of**: [isPartyControlling](/concepts/fibo/FND/OwnershipAndControl/Control/isPartyControlling.md)

## Annotations

- **label**: has portfolio company
- **definition**: indicates a party in which a venture capital firm, a buyout firm, or a holding company has invested

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
