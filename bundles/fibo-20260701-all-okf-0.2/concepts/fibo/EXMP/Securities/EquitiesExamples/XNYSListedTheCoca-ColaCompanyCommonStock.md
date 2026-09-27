---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: XNYS-listed The Coca-Cola Company common stock
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The Coca-Cola Company common share listed in the New York Stock Exchange (NYSE)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasListingDate
    value: '1919-09-05'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isTradedOn
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/TheCoca-ColaCompanyCommonStock.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/lists
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/TheCoca-ColaCompanyCommonStock
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNYSListedTheCoca-ColaCompanyCommonStock
sources:
- id: fibo-source-67472951ed
  resource: references/fibo/EXMP/Securities/EquitiesExamples.rdf
  sha256: 67472951eda4ab333ca860aff880574f4629454478bbf8d10154cde935dfb619
  title: FIBO source EXMP/Securities/EquitiesExamples.rdf
title: XNYS-listed The Coca-Cola Company common stock
type: Ontology Individual
---

# XNYS-listed The Coca-Cola Company common stock

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNYSListedTheCoca-ColaCompanyCommonStock>

## Definition

The Coca-Cola Company common share listed in the New York Stock Exchange (NYSE)

## Relationships

- **Related to**: [USDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md)
- **Related to**: [NewYorkStockExchange](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md)
- **Related to**: [TheCoca-ColaCompanyCommonStock](/concepts/fibo/EXMP/Securities/EquitiesExamples/TheCoca-ColaCompanyCommonStock.md)

## Annotations

- **label**: XNYS-listed The Coca-Cola Company common stock
- **definition**: The Coca-Cola Company common share listed in the New York Stock Exchange (NYSE)
- **hasListingDate**: 1919-09-05

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
