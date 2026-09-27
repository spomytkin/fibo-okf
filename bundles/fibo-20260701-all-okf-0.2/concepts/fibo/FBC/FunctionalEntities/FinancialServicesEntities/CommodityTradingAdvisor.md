---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity trading advisor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that directly or indirectly advises others as to the value or advisability of buying or selling futures contracts
      or options
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CTA
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Indirect advice includes exercising trading authority over a customer's account. In the U.S., registered CTAs are
      registered with the Commodities Futures Trading Commission (CFTC) and are generally required to be members of the National
      Futures Association (NFA).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CommodityTradingAdvisor
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: commodity trading advisor
type: Ontology Class
---

# commodity trading advisor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CommodityTradingAdvisor>

## Definition

party that directly or indirectly advises others as to the value or advisability of buying or selling futures contracts or options

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)

## Annotations

- **label**: commodity trading advisor
- **definition**: party that directly or indirectly advises others as to the value or advisability of buying or selling futures contracts or options
- **abbreviation**: CTA
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
- **explanatoryNote**: Indirect advice includes exercising trading authority over a customer's account. In the U.S., registered CTAs are registered with the Commodities Futures Trading Commission (CFTC) and are generally required to be members of the National Futures Association (NFA).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
