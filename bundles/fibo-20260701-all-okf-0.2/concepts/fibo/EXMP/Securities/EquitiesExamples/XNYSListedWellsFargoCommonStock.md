---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: XNYS-listed Wells Fargo common stock
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Wells Fargo & Company common share listed in the New York Stock Exchange (NYSE)
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isTradedOn
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/WellsFargoCommonStock.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/lists
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/WellsFargoCommonStock
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNYSListedWellsFargoCommonStock
sources:
- id: fibo-source-67472951ed
  resource: references/fibo/EXMP/Securities/EquitiesExamples.rdf
  sha256: 67472951eda4ab333ca860aff880574f4629454478bbf8d10154cde935dfb619
  title: FIBO source EXMP/Securities/EquitiesExamples.rdf
title: XNYS-listed Wells Fargo common stock
type: Ontology Individual
---

# XNYS-listed Wells Fargo common stock

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNYSListedWellsFargoCommonStock>

## Definition

Wells Fargo & Company common share listed in the New York Stock Exchange (NYSE)

## Relationships

- **Related to**: [USDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md)
- **Related to**: [NewYorkStockExchange](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md)
- **Related to**: [WellsFargoCommonStock](/concepts/fibo/EXMP/Securities/EquitiesExamples/WellsFargoCommonStock.md)

## Annotations

- **label**: XNYS-listed Wells Fargo common stock
- **definition**: Wells Fargo & Company common share listed in the New York Stock Exchange (NYSE)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
