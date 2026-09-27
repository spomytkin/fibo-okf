---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: clearing bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commercial bank that facilitates payment and settlement of financial transactions, such as check clearing or facilitating
      trades between the sellers and buyers of securities or other financial instruments or contracts
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Office of Financial Research (OFR) Annual Report, 2012, Glossary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingBank
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: clearing bank
type: Ontology Class
---

# clearing bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingBank>

## Definition

commercial bank that facilitates payment and settlement of financial transactions, such as check clearing or facilitating trades between the sellers and buyers of securities or other financial instruments or contracts

## Relationships

- **Subclass of**: [ClearingHouse](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse.md)
- **Subclass of**: [CommercialBank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md)

## Annotations

- **label**: clearing bank
- **definition**: commercial bank that facilitates payment and settlement of financial transactions, such as check clearing or facilitating trades between the sellers and buyers of securities or other financial instruments or contracts
- **definitionOrigin**: Office of Financial Research (OFR) Annual Report, 2012, Glossary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
