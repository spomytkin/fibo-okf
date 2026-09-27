---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: LIQUIDATION
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: GLEIF classifier for corporate actions consisting of distribution of cash, assets, or both
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: Debt may be paid in order of priority based on preferred claims to assets specified by the security (event completed).
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: LIQUIDATION
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/BusinessStrategyClassifier
  - https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Liquidation
  - https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent
  related_to:
  - concept: /concepts/fibo/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals/GLEIF-CorporateActionClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals/GLEIF-CorporateActionClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals/LIQUIDATION
sources:
- id: fibo-source-7606bb41f7
  resource: references/fibo/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals.rdf
  sha256: 7606bb41f72dc98e8e5f1d4b5c970686f1a3473c0e6baee42ec320289773c087
  title: FIBO source CAE/CorporateEvents/GLEIF-CorporateActionIndividuals.rdf
title: LIQUIDATION
type: Ontology Individual
---

# LIQUIDATION

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals/LIQUIDATION>

## Definition

GLEIF classifier for corporate actions consisting of distribution of cash, assets, or both

## Relationships

- **Related to**: [GLEIF-CorporateActionClassificationScheme](/concepts/fibo/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals/GLEIF-CorporateActionClassificationScheme.md)

## Annotations

- **label** (en): LIQUIDATION
- **definition** (en): GLEIF classifier for corporate actions consisting of distribution of cash, assets, or both
- **note** (en): Debt may be paid in order of priority based on preferred claims to assets specified by the security (event completed).
- **hasTag**: LIQUIDATION

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
