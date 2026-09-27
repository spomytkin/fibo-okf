---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service provider/publisher responsible for specifying some benchmark interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: This is typically a bank, central bank in the case of the publication of bank interest rates, or the committee
      responsible for publishing interbank rates, such as EURIBOR.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/produces
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateAuthority
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: interest rate authority
type: Ontology Class
---

# interest rate authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateAuthority>

## Definition

financial service provider/publisher responsible for specifying some benchmark interest rate

## Relationships

- **Subclass of**: [Publisher](/concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md)
- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Constraints

- **[produces](/concepts/fibo/FND/Relations/Relations/produces.md)**: some values from of type [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)

## Annotations

- **label**: interest rate authority
- **definition**: financial service provider/publisher responsible for specifying some benchmark interest rate
- **example**: This is typically a bank, central bank in the case of the publication of bank interest rates, or the committee responsible for publishing interbank rates, such as EURIBOR.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
