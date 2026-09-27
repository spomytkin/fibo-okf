---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial intermediation service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any financial service in which a third party (the intermediary) matches lenders and investors with entrepreneurs
      and other borrowers in need of capital
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Office of Financial Research (OFR) Annual Report, 2012, Glossary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Often investors and borrowers do not have precisely matching needs, and the intermediary's capital is put at risk
      to transform the credit risk and maturity of the liabilities to meet the needs of investors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialIntermediationService
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: financial intermediation service
type: Ontology Class
---

# financial intermediation service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialIntermediationService>

## Definition

any financial service in which a third party (the intermediary) matches lenders and investors with entrepreneurs and other borrowers in need of capital

## Relationships

- **Subclass of**: [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)

## Annotations

- **label**: financial intermediation service
- **definition**: any financial service in which a third party (the intermediary) matches lenders and investors with entrepreneurs and other borrowers in need of capital
- **definitionOrigin**: Office of Financial Research (OFR) Annual Report, 2012, Glossary
- **explanatoryNote**: Often investors and borrowers do not have precisely matching needs, and the intermediary's capital is put at risk to transform the credit risk and maturity of the liabilities to meet the needs of investors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
