---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: insurance service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service in which the insurer promises to provide compensation for specific potential future losses in
      exchange for a periodic payment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Insurance providers invest the compensation they receive in order to make a profit. In general, insurance transfers
      risk from individuals or organizations to a larger pool of individuals or organizations that are better able to mitigate
      that risk.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InsuranceService
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: insurance service
type: Ontology Class
---

# insurance service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InsuranceService>

## Definition

financial service in which the insurer promises to provide compensation for specific potential future losses in exchange for a periodic payment

## Relationships

- **Subclass of**: [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)

## Annotations

- **label**: insurance service
- **definition**: financial service in which the insurer promises to provide compensation for specific potential future losses in exchange for a periodic payment
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
- **explanatoryNote**: Insurance providers invest the compensation they receive in order to make a profit. In general, insurance transfers risk from individuals or organizations to a larger pool of individuals or organizations that are better able to mitigate that risk.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
