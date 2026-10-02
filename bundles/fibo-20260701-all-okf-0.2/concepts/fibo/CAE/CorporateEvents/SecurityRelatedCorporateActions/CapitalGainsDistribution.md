---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capital gains distribution
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that distributes profits resulting from the sale of company assets to shareholders
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Shareholders of Mutual Funds, Unit Trusts, or SICAVs are recipients of capital gains distributions which are often
      reinvested in additional shares of the fund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CapitalGainsDistribution
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: capital gains distribution
type: Ontology Class
---

# capital gains distribution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CapitalGainsDistribution>

## Definition

corporate action that distributes profits resulting from the sale of company assets to shareholders

## Relationships

- **Subclass of**: [VoluntaryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)

## Annotations

- **label** (en): capital gains distribution
- **definition** (en): corporate action that distributes profits resulting from the sale of company assets to shareholders
- **example** (en): Shareholders of Mutual Funds, Unit Trusts, or SICAVs are recipients of capital gains distributions which are often reinvested in additional shares of the fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
