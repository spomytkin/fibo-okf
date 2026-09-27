---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: XNAS-listed Alphabet Inc. class A common stock
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Alphabet Inc. class A common share listed in the Nasdaq (NASDAQ-NGS)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasListingDate
    value: '2004-08-01'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/AlphabetIncClassACommonStock.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/lists
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/AlphabetIncClassACommonStock
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isTradedOn
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNASListedAlphabetIncClassACommonStock
sources:
- id: fibo-source-67472951ed
  resource: references/fibo/EXMP/Securities/EquitiesExamples.rdf
  sha256: 67472951eda4ab333ca860aff880574f4629454478bbf8d10154cde935dfb619
  title: FIBO source EXMP/Securities/EquitiesExamples.rdf
title: XNAS-listed Alphabet Inc. class A common stock
type: Ontology Individual
---

# XNAS-listed Alphabet Inc. class A common stock

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNASListedAlphabetIncClassACommonStock>

## Definition

Alphabet Inc. class A common share listed in the Nasdaq (NASDAQ-NGS)

## Relationships

- **Related to**: [USDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md)
- **Related to**: [Facility-XNAS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md)
- **Related to**: [AlphabetIncClassACommonStock](/concepts/fibo/EXMP/Securities/EquitiesExamples/AlphabetIncClassACommonStock.md)

## Annotations

- **label**: XNAS-listed Alphabet Inc. class A common stock
- **definition**: Alphabet Inc. class A common share listed in the Nasdaq (NASDAQ-NGS)
- **hasListingDate**: 2004-08-01

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
